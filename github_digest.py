#!/usr/bin/env python3
"""
GitHub Daily Digest Generator
每天抓取指定 GitHub 仓库的 Issues 和 Pull Requests，生成中文日报
"""

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

import requests

# 配置
CONFIG_DIR = Path(__file__).parent
REPOS_FILE = CONFIG_DIR / "repos.json"
DIGEST_DIR = CONFIG_DIR / "digests"


def get_ai_api_config() -> Optional[dict]:
    """获取 AI API 配置（豆包 API）"""
    openclaw_config = Path.home() / ".openclaw" / "openclaw.json"
    if openclaw_config.exists():
        with open(openclaw_config) as f:
            config = json.load(f)
            models = config.get("models", {}).get("providers", {})
            if "doubao" in models:
                return {
                    "provider": "doubao",
                    "base_url": models["doubao"].get("baseUrl"),
                    "api_key": models["doubao"].get("apiKey"),
                    "model": models["doubao"].get("models", [{}])[0].get("id", "ark-code-latest")
                }
    return None


def call_ai(prompt: str, ai_config: Optional[dict], max_tokens: int = 1000) -> str:
    """调用 AI API"""
    if not ai_config:
        return ""

    try:
        response = requests.post(
            f"{ai_config['base_url']}/chat/completions",
            headers={
                "Authorization": f"Bearer {ai_config['api_key']}",
                "Content-Type": "application/json"
            },
            json={
                "model": ai_config["model"],
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": max_tokens,
                "temperature": 0.7
            },
            timeout=60
        )

        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"]
        else:
            print(f"    ⚠️ AI 调用失败: {response.status_code}")
            return ""

    except Exception as e:
        print(f"    ⚠️ AI 调用出错: {e}")
        return ""


def summarize_issue(title: str, body: str, ai_config: Optional[dict]) -> str:
    """使用 AI 生成 Issue 中文摘要"""
    if not ai_config:
        # 无 AI 时返回原文预览
        preview = body[:500] if body else "无描述内容"
        return f"**描述预览**: {preview}"

    # 截取文本避免太长
    max_chars = 3000
    content = body if body else "无详细描述"

    prompt = f"""请将以下 GitHub Issue 内容翻译成流畅的中文，并用 2-3 句话总结核心内容。

Issue 标题：{title}

Issue 内容：
{content[:max_chars]}

请按以下格式输出：
**核心内容**: [用中文简洁描述这个 Issue 的主要问题或需求，2-3 句话]

只输出中文内容，不要添加任何解释。"""

    result = call_ai(prompt, ai_config, max_tokens=800)
    return result if result else f"**描述预览**: {content[:500]}"


def summarize_pr(title: str, body: str, ai_config: Optional[dict]) -> str:
    """使用 AI 生成 PR 中文摘要"""
    if not ai_config:
        preview = body[:500] if body else "无描述内容"
        return f"**描述预览**: {preview}"

    max_chars = 3000
    content = body if body else "无详细描述"

    prompt = f"""请将以下 GitHub Pull Request 内容翻译成流畅的中文，并用 2-3 句话总结核心内容。

PR 标题：{title}

PR 内容：
{content[:max_chars]}

请按以下格式输出：
**核心内容**: [用中文简洁描述这个 PR 的主要变更或功能，2-3 句话]

只输出中文内容，不要添加任何解释。"""

    result = call_ai(prompt, ai_config, max_tokens=800)
    return result if result else f"**描述预览**: {content[:500]}"


def run_gh_command(args: list) -> Optional[list]:
    """运行 gh CLI 命令并返回 JSON 结果"""
    try:
        result = subprocess.run(
            ["gh"] + args,
            capture_output=True,
            text=True,
            timeout=60
        )
        if result.returncode == 0 and result.stdout.strip():
            return json.loads(result.stdout)
        else:
            print(f"    ⚠️ gh 命令失败: {result.stderr}")
            return None
    except FileNotFoundError:
        print("    ❌ 未找到 gh CLI，请确保已安装 GitHub CLI")
        return None
    except json.JSONDecodeError as e:
        print(f"    ⚠️ JSON 解析失败: {e}")
        return None
    except Exception as e:
        print(f"    ⚠️ 执行 gh 命令出错: {e}")
        return None


def fetch_issues(owner: str, repo: str, hours_back: int, reference_date: datetime = None) -> list:
    """获取最近 N 小时内的 Issues"""
    if reference_date is None:
        reference_date = datetime.now(timezone.utc)
    # 使用 search 查询来获取最近的 issues
    since_date = (reference_date - timedelta(hours=hours_back)).strftime("%Y-%m-%dT%H:%M:%SZ")
    search_query = f"created:>={since_date}"

    issues = run_gh_command([
        "issue", "list",
        "--repo", f"{owner}/{repo}",
        "--state", "all",
        "--search", search_query,
        "--limit", "50",
        "--json", "number,title,body,state,createdAt,updatedAt,url,labels,author"
    ])

    if not issues:
        return []

    # 进一步过滤时间范围（确保在范围内）
    cutoff = reference_date - timedelta(hours=hours_back)
    filtered = []
    for issue in issues:
        created_str = issue.get("createdAt", "")
        if created_str:
            try:
                created = datetime.fromisoformat(created_str.replace("Z", "+00:00"))
                if created >= cutoff:
                    filtered.append(issue)
            except:
                filtered.append(issue)  # 解析失败则保留

    return filtered


def fetch_prs(owner: str, repo: str, hours_back: int, reference_date: datetime = None) -> list:
    """获取最近 N 小时内的 Pull Requests"""
    if reference_date is None:
        reference_date = datetime.now(timezone.utc)
    # 使用 search 查询来获取最近的 PRs
    since_date = (reference_date - timedelta(hours=hours_back)).strftime("%Y-%m-%dT%H:%M:%SZ")
    search_query = f"created:>={since_date}"

    prs = run_gh_command([
        "pr", "list",
        "--repo", f"{owner}/{repo}",
        "--state", "all",
        "--search", search_query,
        "--limit", "50",
        "--json", "number,title,body,state,createdAt,updatedAt,url,labels,author,additions,deletions,changedFiles"
    ])

    if not prs:
        return []

    # 进一步过滤时间范围
    cutoff = reference_date - timedelta(hours=hours_back)
    filtered = []
    for pr in prs:
        created_str = pr.get("createdAt", "")
        if created_str:
            try:
                created = datetime.fromisoformat(created_str.replace("Z", "+00:00"))
                if created >= cutoff:
                    filtered.append(pr)
            except:
                filtered.append(pr)  # 解析失败则保留

    return filtered


def format_time_ago(dt_str: str) -> str:
    """格式化时间为中文相对时间"""
    try:
        dt = datetime.fromisoformat(dt_str.replace("Z", "+00:00"))
        now = datetime.now(timezone.utc)
        diff = now - dt

        if diff.days > 0:
            return f"{diff.days}天前"
        hours = diff.seconds // 3600
        if hours > 0:
            return f"{hours}小时前"
        minutes = diff.seconds // 60
        return f"{minutes}分钟前"
    except:
        return dt_str[:10] if dt_str else "未知"


def format_labels(labels: list) -> str:
    """格式化标签"""
    if not labels:
        return ""
    label_names = [l.get("name", "") for l in labels]
    return " ".join([f"`{n}`" for n in label_names[:5]])  # 最多显示5个


def process_repo(repo_config: dict, hours_back: int, ai_config: Optional[dict], reference_date: datetime = None) -> str:
    """处理单个仓库，返回 Markdown 内容"""
    owner = repo_config.get("owner")
    repo = repo_config.get("repo")
    name = repo_config.get("name", f"{owner}/{repo}")

    print(f"📡 处理仓库: {name} ({owner}/{repo})")

    # 获取 Issues
    print(f"  📋 获取 Issues...")
    issues = fetch_issues(owner, repo, hours_back, reference_date)
    print(f"  📋 找到 {len(issues)} 个 Issue")

    # 获取 PRs
    print(f"  🔀 获取 Pull Requests...")
    prs = fetch_prs(owner, repo, hours_back, reference_date)
    print(f"  🔀 找到 {len(prs)} 个 Pull Request")

    # 生成 Markdown
    md = f"## {name}\n\n"
    md += f"> 仓库: https://github.com/{owner}/{repo}\n\n"

    # Issues 部分
    if issues:
        md += f"### 📋 Issues ({len(issues)})\n\n"
        for issue in issues:
            number = issue.get("number")
            title = issue.get("title", "无标题")
            state = issue.get("state", "unknown")
            html_url = issue.get("url", f"https://github.com/{owner}/{repo}/issues/{number}")
            body = issue.get("body", "")
            created_at = issue.get("createdAt", "")
            labels_str = format_labels(issue.get("labels", []))
            # author 字段可能是 dict 或 string
            author = issue.get("author", {})
            if isinstance(author, dict):
                user = author.get("login", "unknown")
            else:
                user = str(author)

            state_icon = "🟢" if state == "open" else "🔴"
            time_ago = format_time_ago(created_at)

            md += f"#### {state_icon} [{title}]({html_url})\n\n"
            md += f"| 属性 | 值 |\n"
            md += f"|------|----|\n"
            md += f"| 📅 创建时间 | {time_ago} |\n"
            md += f"| 👤 作者 | {user} |\n"
            md += f"| 🏷️ 状态 | {state} |\n"
            if labels_str:
                md += f"| 🏷️ 标签 | {labels_str} |\n"
            md += "\n"

            # 生成中文摘要
            print(f"  🤖 生成 Issue #{number} 摘要...")
            summary = summarize_issue(title, body, ai_config)
            md += f"{summary}\n\n"
            md += "---\n\n"
    else:
        md += "### 📋 Issues\n\n_过去 24 小时内没有新的 Issue_\n\n"

    # PRs 部分
    if prs:
        md += f"### 🔀 Pull Requests ({len(prs)})\n\n"
        for pr in prs:
            number = pr.get("number")
            title = pr.get("title", "无标题")
            state = pr.get("state", "unknown")
            html_url = pr.get("url", f"https://github.com/{owner}/{repo}/pull/{number}")
            body = pr.get("body", "")
            created_at = pr.get("createdAt", "")
            labels_str = format_labels(pr.get("labels", []))
            # author 字段可能是 dict 或 string
            author = pr.get("author", {})
            if isinstance(author, dict):
                user = author.get("login", "unknown")
            else:
                user = str(author)
            additions = pr.get("additions", 0)
            deletions = pr.get("deletions", 0)
            changed_files = pr.get("changedFiles", 0)

            state_icon = "🟢" if state == "open" else ("🟣" if state == "merged" else "🔴")
            time_ago = format_time_ago(created_at)

            md += f"#### {state_icon} [{title}]({html_url})\n\n"
            md += f"| 属性 | 值 |\n"
            md += f"|------|----|\n"
            md += f"| 📅 创建时间 | {time_ago} |\n"
            md += f"| 👤 作者 | {user} |\n"
            md += f"| 🏷️ 状态 | {state} |\n"
            md += f"| 📊 变更 | +{additions}/-{deletions} ({changed_files} 文件) |\n"
            if labels_str:
                md += f"| 🏷️ 标签 | {labels_str} |\n"
            md += "\n"

            # 生成中文摘要
            print(f"  🤖 生成 PR #{number} 摘要...")
            summary = summarize_pr(title, body, ai_config)
            md += f"{summary}\n\n"
            md += "---\n\n"
    else:
        md += "### 🔀 Pull Requests\n\n_过去 24 小时内没有新的 Pull Request_\n\n"

    return md


def save_to_obsidian(content: str, settings: dict, reference_date: datetime = None) -> Path:
    """保存到 Obsidian vault"""
    if reference_date is None:
        reference_date = datetime.now()
    vault_path = Path(settings.get("obsidian_vault", "~/Documents/Obsidian Vault").replace("~", str(Path.home())))
    folder_name = settings.get("output_folder", "GitHub Digest")
    output_dir = vault_path / folder_name

    # 确保目录存在
    output_dir.mkdir(parents=True, exist_ok=True)

    # 生成文件名
    date_stamp = reference_date.strftime("%Y-%m-%d")
    output_file = output_dir / f"github-digest-{date_stamp}.md"

    # 写入文件
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)

    return output_file


def main():
    """主函数"""
    # 解析命令行参数
    import argparse
    parser = argparse.ArgumentParser(description="GitHub 每日摘要生成器")
    parser.add_argument("--date", type=str, help="目标日期 (格式: YYYY-MM-DD), 默认为今天")
    args = parser.parse_args()

    print("=" * 50)
    print("📊 GitHub 每日摘要生成器（中文版）")
    print("=" * 50)

    # 获取 AI 配置
    ai_config = get_ai_api_config()
    if ai_config:
        print("✅ AI 翻译/摘要服务已配置（豆包 API）")
    else:
        print("⚠️ 未配置 AI 服务，将使用原文预览")

    # 检查 gh CLI
    try:
        result = subprocess.run(["gh", "--version"], capture_output=True, text=True)
        print(f"✅ GitHub CLI 已安装: {result.stdout.strip().split()[2]}")
    except FileNotFoundError:
        print("❌ 未安装 GitHub CLI，请先安装: brew install gh")
        sys.exit(1)

    # 加载仓库配置
    if not REPOS_FILE.exists():
        print(f"❌ 配置文件不存在: {REPOS_FILE}")
        sys.exit(1)

    with open(REPOS_FILE) as f:
        config = json.load(f)

    repos = config.get("repos", [])
    settings = config.get("settings", {})
    hours_back = settings.get("hours_back", 24)

    if not repos:
        print("❌ 没有配置任何仓库")
        sys.exit(1)

    # 创建临时输出目录
    DIGEST_DIR.mkdir(parents=True, exist_ok=True)

    # 确定参考时间（必须在处理仓库之前）
    reference_date = None
    if args.date:
        try:
            reference_date = datetime.strptime(args.date, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        except ValueError:
            print(f"❌ 日期格式错误，请使用 YYYY-MM-DD 格式")
            sys.exit(1)
    else:
        reference_date = datetime.now(timezone.utc)

    print(f"\n🚀 开始处理 {len(repos)} 个仓库...")
    print(f"📅 时间范围: 过去 {hours_back} 小时\n")

    # 处理每个仓库并收集结果
    repo_contents = []
    toc_items = []

    for repo in repos:
        if repo.get("enabled", True):
            repo_content = process_repo(repo, hours_back, ai_config, reference_date)
            repo_name = repo.get("name", f"{repo.get('owner')}/{repo.get('repo')}")

            # 统计 issues 和 PRs 数量
            issue_count = repo_content.count("#### 🟢") + repo_content.count("#### 🔴")
            pr_count = repo_content.count("#### 🟢") + repo_content.count("#### 🔴") + repo_content.count("#### 🟣")
            # 更精确的统计
            issue_match = re.search(r'### 📋 Issues \((\d+)\)', repo_content)
            pr_match = re.search(r'### 🔀 Pull Requests \((\d+)\)', repo_content)
            issue_count = int(issue_match.group(1)) if issue_match else 0
            pr_count = int(pr_match.group(1)) if pr_match else 0

            repo_contents.append((repo_name, repo_content))

            # 添加到目录
            if issue_count > 0 or pr_count > 0:
                toc_items.append(f"- [{repo_name}](#{repo_name.lower().replace(' ', '-').replace('/', '-')}) - {issue_count} Issues, {pr_count} PRs")
            else:
                toc_items.append(f"- [{repo_name}](#{repo_name.lower().replace(' ', '-').replace('/', '-')}) - 无更新")

    # 生成报告头部
    now = reference_date
    total_issues = sum(int(re.search(r'### 📋 Issues \((\d+)\)', c).group(1)) if re.search(r'### 📋 Issues \((\d+)\)', c) else 0 for _, c in repo_contents)
    total_prs = sum(int(re.search(r'### 🔀 Pull Requests \((\d+)\)', c).group(1)) if re.search(r'### 🔀 Pull Requests \((\d+)\)', c) else 0 for _, c in repo_contents)

    content = f"""# GitHub 每日摘要

📅 **生成时间**: {now.strftime("%Y-%m-%d %H:%M:%S")}
⏰ **时间范围**: 过去 {hours_back} 小时
📊 **监控仓库数**: {len(repos)}
📋 **总计**: {total_issues} Issues, {total_prs} Pull Requests

## 📑 目录

{chr(10).join(toc_items)}

---

"""

    # 添加每个仓库的内容
    for repo_name, repo_content in repo_contents:
        content += repo_content
        content += "\n"

    # 添加页脚
    content += f"\n---\n*生成时间: {now.strftime('%Y-%m-%d %H:%M:%S')}*\n"

    # 保存到临时目录
    date_stamp = now.strftime("%Y-%m-%d")
    temp_file = DIGEST_DIR / f"github-digest-{date_stamp}.md"
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"\n📄 临时文件已保存: {temp_file}")

    # 保存到 Obsidian
    obsidian_file = save_to_obsidian(content, settings, reference_date)
    print(f"✅ 已保存到 Obsidian: {obsidian_file}")

    print("\n" + "=" * 50)

    return obsidian_file


if __name__ == "__main__":
    main()
