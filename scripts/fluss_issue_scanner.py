#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每日扫描 Apache Fluss 仓库 Issue 的脚本

功能:
- 从 GitHub API 获取 apache/fluss 仓库的 Issue 列表
- 支持全量或按日期过滤
- 生成 Markdown 格式的摘要报告
- 具备日志输出和错误重试机制
- 可通过 crontab 定时执行

用法:
    python3 fluss_issue_scanner.py [--date YYYY-MM-DD] [--output-dir DIR] [--token TOKEN]

示例:
    # 扫描过去 24 小时内的 Issue
    python3 fluss_issue_scanner.py

    # 指定日期
    python3 fluss_issue_scanner.py --date 2026-03-19

    # 指定输出目录和 GitHub Token
    python3 fluss_issue_scanner.py --output-dir /path/to/output --token ghp_xxx

Crontab 配置示例 (每天 22:00 执行):
    0 22 * * * /usr/bin/python3 /path/to/fluss_issue_scanner.py --token YOUR_TOKEN >> /var/log/fluss_scanner.log 2>&1
"""

import argparse
import json
import logging
import os
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

# ─── 常量配置 ─────────────────────────────────────────────────────────────────

REPO_OWNER = "apache"
REPO_NAME = "fluss"
REPO_URL = f"https://github.com/{REPO_OWNER}/{REPO_NAME}"
API_BASE = "https://api.github.com"

# 重试配置
MAX_RETRIES = 3
RETRY_BACKOFF_BASE = 2  # 指数退避基数（秒）

# 分页配置
PER_PAGE = 100

# ─── 日志配置 ──────────────────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


# ─── GitHub API 客户端 ─────────────────────────────────────────────────────────

class GitHubClient:
    """封装 GitHub REST API 调用，支持重试和限流处理。"""

    def __init__(self, token: str | None = None):
        self.token = token
        self.headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if token:
            self.headers["Authorization"] = f"Bearer {token}"

    def _request(self, url: str, attempt: int = 1) -> dict | list:
        """发送 GET 请求，处理限流和网络错误，失败时自动重试。"""
        req = Request(url, headers=self.headers)
        try:
            with urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except HTTPError as exc:
            if exc.code == 403:
                # 检查是否触发限流
                reset_ts = exc.headers.get("X-RateLimit-Reset")
                if reset_ts:
                    wait = max(int(reset_ts) - int(time.time()), 1)
                    logger.warning("GitHub API 限流，等待 %d 秒后重试...", wait)
                    time.sleep(wait)
                    return self._request(url, attempt)
            if attempt >= MAX_RETRIES:
                logger.error("请求失败 (HTTP %d): %s", exc.code, url)
                raise
            wait = RETRY_BACKOFF_BASE ** attempt
            logger.warning(
                "HTTP %d 错误，%d 秒后进行第 %d 次重试: %s",
                exc.code, wait, attempt + 1, url,
            )
            time.sleep(wait)
            return self._request(url, attempt + 1)
        except URLError as exc:
            if attempt >= MAX_RETRIES:
                logger.error("网络请求失败: %s — %s", url, exc.reason)
                raise
            wait = RETRY_BACKOFF_BASE ** attempt
            logger.warning(
                "网络错误，%d 秒后进行第 %d 次重试: %s",
                wait, attempt + 1, url,
            )
            time.sleep(wait)
            return self._request(url, attempt + 1)

    def get_issues(
        self,
        owner: str,
        repo: str,
        state: str = "all",
        since: str | None = None,
    ) -> list[dict]:
        """
        获取指定仓库的 Issue 列表（排除 Pull Request）。

        Args:
            owner: 仓库所有者
            repo: 仓库名称
            state: Issue 状态，"open" / "closed" / "all"
            since: ISO 8601 时间字符串，只返回该时间之后更新的 Issue

        Returns:
            Issue 字典列表
        """
        issues: list[dict] = []
        page = 1

        while True:
            params = f"state={state}&per_page={PER_PAGE}&page={page}&filter=all"
            if since:
                params += f"&since={since}"

            url = f"{API_BASE}/repos/{owner}/{repo}/issues?{params}"
            logger.info("正在获取第 %d 页 Issue...", page)

            data = self._request(url)
            if not isinstance(data, list):
                break

            # GitHub Issues API 会返回 PR，通过 pull_request 字段区分
            page_issues = [item for item in data if "pull_request" not in item]
            issues.extend(page_issues)

            if len(data) < PER_PAGE:
                break
            page += 1

        logger.info("共获取到 %d 个 Issue", len(issues))
        return issues


# ─── Markdown 报告生成 ─────────────────────────────────────────────────────────

def _relative_time(dt: datetime) -> str:
    """将 datetime 转换为中文相对时间描述。"""
    now = datetime.now(timezone.utc)
    diff = now - dt

    seconds = int(diff.total_seconds())
    if seconds < 60:
        return f"{seconds}秒前"
    minutes = seconds // 60
    if minutes < 60:
        return f"{minutes}分钟前"
    hours = minutes // 60
    if hours < 24:
        return f"{hours}小时前"
    days = hours // 24
    return f"{days}天前"


def _issue_state_icon(state: str) -> str:
    return "🔴" if state == "open" else "🟢"


def _format_labels(labels: list[dict]) -> str:
    if not labels:
        return "—"
    return ", ".join(f"`{lb['name']}`" for lb in labels)


def generate_markdown(
    issues: list[dict],
    scan_date: str,
    since: datetime | None,
    generated_at: str,
) -> str:
    """生成 Markdown 格式的 Issue 摘要报告。"""

    open_issues = [i for i in issues if i.get("state") == "open"]
    closed_issues = [i for i in issues if i.get("state") == "closed"]

    time_range = (
        f"自 {since.strftime('%Y-%m-%d %H:%M:%S UTC')}"
        if since
        else "全量"
    )

    lines: list[str] = [
        f"# Apache Fluss Issue 每日扫描报告",
        f"",
        f"📅 **生成时间**: {generated_at}",
        f"⏰ **时间范围**: {time_range}",
        f"📊 **仓库**: [{REPO_OWNER}/{REPO_NAME}]({REPO_URL})",
        f"📋 **总计**: {len(issues)} 个 Issue "
        f"（🔴 Open: {len(open_issues)}，🟢 Closed: {len(closed_issues)}）",
        f"",
        f"---",
        f"",
    ]

    # ── Open Issues ──────────────────────────────────────────────────────────
    lines.append(f"## 🔴 Open Issues ({len(open_issues)})")
    lines.append("")

    if open_issues:
        for issue in open_issues:
            created_at = datetime.fromisoformat(
                issue["created_at"].replace("Z", "+00:00")
            )
            updated_at = datetime.fromisoformat(
                issue["updated_at"].replace("Z", "+00:00")
            )
            lines += [
                f"### [{issue['title']}]({issue['html_url']})",
                f"",
                f"| 属性 | 值 |",
                f"|------|----|",
                f"| 🔢 Issue # | #{issue['number']} |",
                f"| 👤 作者 | {issue['user']['login']} |",
                f"| 📅 创建时间 | {created_at.strftime('%Y-%m-%d %H:%M UTC')} ({_relative_time(created_at)}) |",
                f"| 🔄 最后更新 | {updated_at.strftime('%Y-%m-%d %H:%M UTC')} ({_relative_time(updated_at)}) |",
                f"| 💬 评论数 | {issue.get('comments', 0)} |",
                f"| 🏷️ 标签 | {_format_labels(issue.get('labels', []))} |",
                f"",
            ]
            if issue.get("body"):
                # 截取前 300 字符作为摘要
                body = issue["body"].strip().replace("\r\n", "\n")
                preview = body[:300] + ("..." if len(body) > 300 else "")
                lines += [
                    f"**摘要**:",
                    f"",
                    f"> {preview.replace('\n', '\n> ')}",
                    f"",
                ]
            lines.append("---")
            lines.append("")
    else:
        lines += ["_该时间范围内没有 Open Issue_", "", "---", ""]

    # ── Closed Issues ────────────────────────────────────────────────────────
    lines.append(f"## 🟢 Closed Issues ({len(closed_issues)})")
    lines.append("")

    if closed_issues:
        for issue in closed_issues:
            created_at = datetime.fromisoformat(
                issue["created_at"].replace("Z", "+00:00")
            )
            closed_at_raw = issue.get("closed_at")
            closed_at_str = (
                datetime.fromisoformat(
                    closed_at_raw.replace("Z", "+00:00")
                ).strftime("%Y-%m-%d %H:%M UTC")
                if closed_at_raw
                else "—"
            )
            lines += [
                f"### [{issue['title']}]({issue['html_url']})",
                f"",
                f"| 属性 | 值 |",
                f"|------|----|",
                f"| 🔢 Issue # | #{issue['number']} |",
                f"| 👤 作者 | {issue['user']['login']} |",
                f"| 📅 创建时间 | {created_at.strftime('%Y-%m-%d %H:%M UTC')} ({_relative_time(created_at)}) |",
                f"| ✅ 关闭时间 | {closed_at_str} |",
                f"| 💬 评论数 | {issue.get('comments', 0)} |",
                f"| 🏷️ 标签 | {_format_labels(issue.get('labels', []))} |",
                f"",
            ]
            lines.append("---")
            lines.append("")
    else:
        lines += ["_该时间范围内没有 Closed Issue_", "", "---", ""]

    lines += [
        f"",
        f"*报告生成时间: {generated_at}*",
    ]
    return "\n".join(lines)


# ─── 主流程 ────────────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="每日扫描 Apache Fluss 仓库 Issue 并生成 Markdown 报告",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--date",
        default=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        help="扫描日期 YYYY-MM-DD（默认为今天），用于过滤当天 00:00 UTC 之后更新的 Issue",
    )
    parser.add_argument(
        "--full-scan",
        action="store_true",
        help="全量扫描所有 Issue，不按日期过滤",
    )
    parser.add_argument(
        "--state",
        choices=["open", "closed", "all"],
        default="all",
        help="Issue 状态过滤（默认: all）",
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="输出目录（默认: 脚本所在目录的上一级 github/ 目录）",
    )
    parser.add_argument(
        "--token",
        default=os.environ.get("GITHUB_TOKEN"),
        help="GitHub Personal Access Token（也可通过环境变量 GITHUB_TOKEN 提供）",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    # ── 确定输出目录 ──────────────────────────────────────────────────────────
    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        output_dir = Path(__file__).resolve().parent.parent / "github"
    output_dir.mkdir(parents=True, exist_ok=True)

    # ── 确定时间过滤 ──────────────────────────────────────────────────────────
    scan_date = args.date
    since: datetime | None = None
    since_iso: str | None = None

    if not args.full_scan:
        since = datetime.strptime(scan_date, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        since_iso = since.isoformat()
        logger.info("扫描日期: %s（过滤 %s 之后更新的 Issue）", scan_date, since_iso)
    else:
        logger.info("全量扫描模式")

    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    # ── 获取 Issue ────────────────────────────────────────────────────────────
    client = GitHubClient(token=args.token)
    if not args.token:
        logger.warning(
            "未提供 GitHub Token，API 请求速率限制为 60 次/小时。"
            "请通过 --token 或 GITHUB_TOKEN 环境变量提供 Token 以获得更高限额。"
        )

    try:
        issues = client.get_issues(
            owner=REPO_OWNER,
            repo=REPO_NAME,
            state=args.state,
            since=since_iso,
        )
    except Exception as exc:
        logger.error("获取 Issue 失败: %s", exc)
        return 1

    # ── 生成报告 ──────────────────────────────────────────────────────────────
    markdown = generate_markdown(
        issues=issues,
        scan_date=scan_date,
        since=since,
        generated_at=generated_at,
    )

    output_file = output_dir / f"fluss-issue-digest-{scan_date}.md"
    output_file.write_text(markdown, encoding="utf-8")
    logger.info("报告已生成: %s", output_file)

    # ── 统计摘要 ──────────────────────────────────────────────────────────────
    open_count = sum(1 for i in issues if i.get("state") == "open")
    closed_count = sum(1 for i in issues if i.get("state") == "closed")
    logger.info(
        "扫描完成 — 总计 %d 个 Issue（Open: %d，Closed: %d）",
        len(issues), open_count, closed_count,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
