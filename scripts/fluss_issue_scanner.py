#!/usr/bin/env python3
"""
Fluss Issue Scanner
每天定时扫描 Apache Fluss 仓库的 issue 列表，生成日报并存储到 github/ 目录。

用法:
    python fluss_issue_scanner.py [--all] [--output-dir ../github]

    --all          获取全部 issue（默认仅获取过去 24 小时内更新的 issue）
    --output-dir   输出目录，默认为脚本同级的 ../github

crontab 示例（每日 00:05 执行）:
    5 0 * * * cd /path/to/digest && python scripts/fluss_issue_scanner.py >> logs/fluss-scan.log 2>&1
"""

import argparse
import json
import logging
import os
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

# ---------------------------------------------------------------------------
# 配置
# ---------------------------------------------------------------------------
REPO_OWNER = "apache"
REPO_NAME = "fluss"
GITHUB_API_BASE = "https://api.github.com"
PER_PAGE = 100  # GitHub API 最大单页数量

# 重试配置
MAX_RETRIES = 3
RETRY_BACKOFF_BASE = 2  # 指数退避基数（秒）

# ---------------------------------------------------------------------------
# 日志
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# GitHub API 工具函数
# ---------------------------------------------------------------------------

def _build_request(url: str) -> Request:
    """构建带认证头的 GitHub API 请求。"""
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return Request(url, headers=headers)


def _fetch_json(url: str) -> Any:
    """发送 GET 请求并以 JSON 返回，处理限流和重试。"""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            req = _build_request(url)
            with urlopen(req, timeout=30) as resp:
                body = resp.read()
                return json.loads(body)
        except HTTPError as exc:
            if exc.code == 403:
                # 检查是否为限流
                reset_ts = exc.headers.get("X-RateLimit-Reset")
                if reset_ts:
                    wait = max(int(reset_ts) - int(time.time()), 0) + 1
                    logger.warning(
                        "Rate limited. Waiting %ds before retry %d/%d …",
                        wait, attempt, MAX_RETRIES,
                    )
                    time.sleep(wait)
                    continue
            if exc.code == 429:
                try:
                    wait = int(exc.headers.get("Retry-After", 0)) or RETRY_BACKOFF_BASE ** attempt
                except ValueError:
                    wait = RETRY_BACKOFF_BASE ** attempt
                logger.warning(
                    "HTTP 429 Too Many Requests. Waiting %ds (attempt %d/%d) …",
                    wait, attempt, MAX_RETRIES,
                )
                time.sleep(wait)
                continue
            logger.error("HTTP error %d for URL: %s", exc.code, url)
            raise
        except URLError as exc:
            wait = RETRY_BACKOFF_BASE ** attempt
            logger.warning(
                "Network error (%s). Retrying in %ds (attempt %d/%d) …",
                exc.reason, wait, attempt, MAX_RETRIES,
            )
            if attempt < MAX_RETRIES:
                time.sleep(wait)
            else:
                raise

    raise RuntimeError(f"Failed to fetch {url} after {MAX_RETRIES} attempts")


# ---------------------------------------------------------------------------
# Issue 获取
# ---------------------------------------------------------------------------

def fetch_all_issues(since: datetime | None = None) -> list[dict]:
    """
    获取 apache/fluss 仓库的全部 issue（含所有状态）。

    参数:
        since: 若提供，则只返回该时间点之后更新的 issue（ISO 8601）。
               若为 None，则获取全部 issue。

    返回:
        issue 对象列表（来自 GitHub REST API）。
    """
    issues: list[dict] = []
    page = 1

    since_param = ""
    if since:
        since_param = f"&since={since.strftime('%Y-%m-%dT%H:%M:%SZ')}"

    logger.info(
        "Fetching issues from %s/%s%s …",
        REPO_OWNER, REPO_NAME,
        f" (since {since.strftime('%Y-%m-%d %H:%M:%S UTC')})" if since else " (all)",
    )

    while True:
        url = (
            f"{GITHUB_API_BASE}/repos/{REPO_OWNER}/{REPO_NAME}/issues"
            f"?state=all&per_page={PER_PAGE}&page={page}{since_param}"
        )
        data = _fetch_json(url)

        if not data:
            break

        # GitHub Issues API 也会返回 pull requests；过滤掉
        only_issues = [item for item in data if "pull_request" not in item]
        issues.extend(only_issues)
        logger.info("  Page %d: fetched %d items (%d issues)", page, len(data), len(only_issues))

        if len(data) < PER_PAGE:
            break
        page += 1

    logger.info("Total issues fetched: %d", len(issues))
    return issues


# ---------------------------------------------------------------------------
# 报告生成
# ---------------------------------------------------------------------------

def _state_emoji(state: str) -> str:
    return "🟢" if state == "open" else "🔴"


def generate_report(issues: list[dict], since: datetime | None) -> str:
    """将 issue 列表渲染为 Markdown 报告。"""
    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    open_issues = [i for i in issues if i["state"] == "open"]
    closed_issues = [i for i in issues if i["state"] == "closed"]

    time_range_desc = (
        f"过去 24 小时内更新（since {since.strftime('%Y-%m-%d %H:%M UTC')}）"
        if since
        else "全量扫描"
    )

    lines = [
        "# Apache Fluss Issue 每日扫描报告",
        "",
        f"📅 **生成时间**: {now_str}",
        f"⏰ **扫描范围**: {time_range_desc}",
        f"📊 **总计**: {len(issues)} Issues（🟢 {len(open_issues)} open / 🔴 {len(closed_issues)} closed）",
        "",
        "---",
        "",
    ]

    if not issues:
        lines.append("_该时间段内没有新增或更新的 Issue。_")
        return "\n".join(lines)

    lines += [
        "## 🟢 Open Issues",
        "",
    ]
    if open_issues:
        for issue in open_issues:
            labels = ", ".join(lbl["name"] for lbl in issue.get("labels", []))
            label_str = f" `{labels}`" if labels else ""
            lines.append(
                f"- [#{issue['number']} {issue['title']}]({issue['html_url']})"
                f"{label_str}"
                f" — updated {issue['updated_at'][:10]}"
            )
    else:
        lines.append("_无 Open Issue_")

    lines += [
        "",
        "## 🔴 Closed Issues",
        "",
    ]
    if closed_issues:
        for issue in closed_issues:
            labels = ", ".join(lbl["name"] for lbl in issue.get("labels", []))
            label_str = f" `{labels}`" if labels else ""
            lines.append(
                f"- [#{issue['number']} {issue['title']}]({issue['html_url']})"
                f"{label_str}"
                f" — closed {issue.get('closed_at', '')[:10]}"
            )
    else:
        lines.append("_无 Closed Issue_")

    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# 主函数
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="每天定时扫描 Apache Fluss 仓库 issue 并生成 Markdown 报告"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        dest="fetch_all",
        help="获取全部 issue（默认仅获取过去 24 小时内更新的 issue）",
    )
    parser.add_argument(
        "--output-dir",
        default=str(Path(__file__).parent.parent / "github"),
        help="报告输出目录（默认: ../github）",
    )
    args = parser.parse_args()

    since: datetime | None = None
    if not args.fetch_all:
        since = datetime.now(timezone.utc) - timedelta(hours=24)

    try:
        issues = fetch_all_issues(since=since)
    except Exception as exc:
        logger.error("Failed to fetch issues: %s", exc)
        return 1

    report = generate_report(issues, since=since)

    # 输出到 stdout（便于 crontab 捕获日志）
    print(report)

    # 写入文件
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    output_file = output_dir / f"fluss-issue-scan-{today}.md"
    output_file.write_text(report, encoding="utf-8")
    logger.info("Report written to %s", output_file)

    return 0


if __name__ == "__main__":
    sys.exit(main())
