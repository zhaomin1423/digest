#!/usr/bin/env python3
"""
Apache Fluss 仓库 Issue 每日扫描脚本

功能：
- 定时扫描 apache/fluss 仓库的所有 Issues
- 生成每日摘要报告（Markdown 格式）
- 支持错误重试和日志输出
- 输出报告保存至 github/ 目录

用法：
    python3 fluss_issue_scanner.py [--hours 24] [--output-dir ../github] [--token YOUR_TOKEN]

定时任务（crontab 示例）：
    # 每天 22:00 运行
    0 22 * * * cd /path/to/digest && python3 scripts/fluss_issue_scanner.py >> logs/fluss-scanner.log 2>&1
"""

import argparse
import json
import logging
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path


# ─── 日志配置 ──────────────────────────────────────────────────────────────────

def setup_logging(log_file: str | None = None) -> logging.Logger:
    """配置日志，同时输出到控制台和可选的日志文件。"""
    handlers: list[logging.Handler] = [logging.StreamHandler(sys.stdout)]
    if log_file:
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)
        handlers.append(logging.FileHandler(log_file, encoding="utf-8"))

    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=handlers,
    )


logger = logging.getLogger(__name__)


# ─── GitHub API 工具 ────────────────────────────────────────────────────────────

GITHUB_API_BASE = "https://api.github.com"
REPO = "apache/fluss"
MAX_RETRIES = 3
RETRY_WAIT_SECONDS = 5
SUMMARY_MAX_LENGTH = 200


def _build_headers(token: str | None) -> dict[str, str]:
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers

def _fetch_json(url: str, headers: dict[str, str]) -> list | dict:
    """发送 GET 请求并返回解析后的 JSON，失败时自动重试。"""
    last_exc: Exception | None = None

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            last_exc = exc
            if exc.code == 403:
                # 速率限制：读取重置时间
                reset_ts = exc.headers.get("X-RateLimit-Reset")
                wait = int(reset_ts) - int(time.time()) + 5 if reset_ts else 60
                logger.warning(
                    "⚠️  GitHub API 速率限制，等待 %ds 后重试 (尝试 %d/%d)…",
                    wait,
                    attempt,
                    MAX_RETRIES,
                )
                if attempt < MAX_RETRIES:
                    time.sleep(max(wait, 1))
            elif exc.code in (500, 502, 503, 504):
                logger.warning(
                    "⚠️  服务器错误 %d，等待 %ds 后重试 (尝试 %d/%d)…",
                    exc.code,
                    RETRY_WAIT_SECONDS * attempt,
                    attempt,
                    MAX_RETRIES,
                )
                if attempt < MAX_RETRIES:
                    time.sleep(RETRY_WAIT_SECONDS * attempt)
            else:
                raise
        except (urllib.error.URLError, TimeoutError) as exc:
            last_exc = exc
            logger.warning(
                "⚠️  网络错误 %s，等待 %ds 后重试 (尝试 %d/%d)…",
                exc,
                RETRY_WAIT_SECONDS * attempt,
                attempt,
                MAX_RETRIES,
            )
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_WAIT_SECONDS * attempt)

    raise RuntimeError(f"请求失败，已达最大重试次数: {url}") from last_exc


def fetch_issues(token: str | None, since: datetime | None = None) -> list[dict]:
    """
    获取 apache/fluss 仓库的全部 Issues（分页处理）。

    :param token: GitHub 个人访问令牌（可选，未提供时受速率限制约束）
    :param since: 仅返回此时间之后更新的 Issues（ISO 8601）
    :return: Issue 字典列表
    """
    headers = _build_headers(token)
    issues: list[dict] = []
    page = 1

    since_str = since.strftime("%Y-%m-%dT%H:%M:%SZ") if since else ""
    logger.info("📡 开始获取 %s 仓库 Issues…", REPO)

    while True:
        params = f"state=open&per_page=100&page={page}"
        if since_str:
            params += f"&since={since_str}"
        url = f"{GITHUB_API_BASE}/repos/{REPO}/issues?{params}"

        logger.info("  ↳ 获取第 %d 页…", page)
        data = _fetch_json(url, headers)

        if not isinstance(data, list) or not data:
            break

        # GitHub Issues API 会同时返回 pull_requests，过滤掉
        page_issues = [item for item in data if "pull_request" not in item]
        issues.extend(page_issues)

        if len(data) < 100:
            break
        page += 1

    logger.info("✅ 共获取到 %d 个 Issues", len(issues))
    return issues


# ─── 摘要生成 ──────────────────────────────────────────────────────────────────

def _relative_time(dt_str: str) -> str:
    """将 ISO 8601 时间字符串转换为可读的相对时间描述。"""
    try:
        dt = datetime.fromisoformat(dt_str.replace("Z", "+00:00"))
        now = datetime.now(timezone.utc)
        delta = now - dt
        seconds = int(delta.total_seconds())
        if seconds < 3600:
            return f"{seconds // 60}分钟前"
        if seconds < 86400:
            return f"{seconds // 3600}小时前"
        return f"{seconds // 86400}天前"
    except ValueError:
        return dt_str


def generate_digest(issues: list[dict], hours: int) -> str:
    """根据 Issues 列表生成 Markdown 格式的每日摘要。"""
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines: list[str] = [
        "# Apache Fluss Issue 每日摘要\n",
        f"📅 **生成时间**: {now_str}",
        f"⏰ **时间范围**: 过去 {hours} 小时",
        f"📋 **开放 Issues 总计**: {len(issues)} 个",
        "",
        "---",
        "",
    ]

    if not issues:
        lines.append(f"_过去 {hours} 小时内没有新的或更新的 Issue_")
        return "\n".join(lines)

    for issue in issues:
        number = issue.get("number", "")
        title = issue.get("title", "（无标题）")
        html_url = issue.get("html_url", "")
        state = issue.get("state", "").upper()
        user = (issue.get("user") or {}).get("login", "未知")
        created_at = issue.get("created_at", "")
        updated_at = issue.get("updated_at", "")
        labels = [lbl.get("name", "") for lbl in (issue.get("labels") or [])]
        body = (issue.get("body") or "").strip()
        summary = body[:SUMMARY_MAX_LENGTH] + "…" if len(body) > SUMMARY_MAX_LENGTH else body

        state_icon = "🔴" if state == "OPEN" else "🟢"
        lines += [
            f"## {state_icon} [#{number} {title}]({html_url})",
            "",
            "| 属性 | 值 |",
            "|------|----|",
            f"| 📅 创建时间 | {_relative_time(created_at)} |",
            f"| 🔄 更新时间 | {_relative_time(updated_at)} |",
            f"| 👤 作者 | {user} |",
            f"| 🏷️ 状态 | {state} |",
        ]
        if labels:
            lines.append(f"| 🔖 标签 | {', '.join(labels)} |")
        if summary:
            lines += ["", f"**摘要**: {summary}"]
        lines += ["", "---", ""]

    return "\n".join(lines)


# ─── 文件输出 ──────────────────────────────────────────────────────────────────

def save_digest(content: str, output_dir: str) -> Path:
    """将摘要写入 <output_dir>/fluss-issue-digest-YYYY-MM-DD.md。"""
    today = datetime.now().strftime("%Y-%m-%d")
    output_path = Path(output_dir) / f"fluss-issue-digest-{today}.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    logger.info("💾 摘要已保存至: %s", output_path)
    return output_path


# ─── 主入口 ────────────────────────────────────────────────────────────────────

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="每日扫描 Apache Fluss 仓库 Issues 并生成摘要报告"
    )
    parser.add_argument(
        "--hours",
        type=int,
        default=24,
        help="扫描过去多少小时内更新的 Issues（默认: 24）",
    )
    parser.add_argument(
        "--output-dir",
        default=str(Path(__file__).parent.parent / "github"),
        help="摘要文件输出目录（默认: ../github）",
    )
    parser.add_argument(
        "--token",
        default=os.environ.get("GITHUB_TOKEN"),
        help="GitHub 个人访问令牌（也可通过 GITHUB_TOKEN 环境变量设置）",
    )
    parser.add_argument(
        "--log-file",
        default=None,
        help="日志文件路径（可选，默认仅输出到控制台）",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="获取全部开放 Issues（忽略 --hours 时间过滤）",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    setup_logging(args.log_file)

    logger.info("=========================================")
    logger.info("Apache Fluss Issue 扫描器启动")
    logger.info("=========================================")

    since: datetime | None = None
    if not args.all:
        since = datetime.now(timezone.utc) - timedelta(hours=args.hours)
        logger.info("📅 扫描范围: 过去 %d 小时（自 %s）", args.hours, since.strftime("%Y-%m-%d %H:%M:%S UTC"))
    else:
        logger.info("📅 扫描范围: 全部开放 Issues")

    try:
        issues = fetch_issues(token=args.token, since=since)
        digest = generate_digest(issues, args.hours)
        save_digest(digest, args.output_dir)
    except Exception as exc:
        logger.error("❌ 扫描失败: %s", exc)
        return 1

    logger.info("=========================================")
    logger.info("Apache Fluss Issue 扫描器完成")
    logger.info("=========================================")
    return 0


if __name__ == "__main__":
    sys.exit(main())
