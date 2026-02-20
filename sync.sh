#!/bin/bash

# Sync all digests to GitHub
# 从 Obsidian Vault 获取摘要并同步到 GitHub 仓库

set -e

REPO_DIR="$HOME/digest"
OBSIDIAN_VAULT="$HOME/Documents/Obsidian Vault"
DATE=$(date +%Y-%m-%d)

echo "========================================"
echo "📤 同步 Digests 到 GitHub"
echo "日期: $DATE"
echo "========================================"

cd "$REPO_DIR"

# 从 Obsidian 复制 GitHub Digest
if [ -f "$OBSIDIAN_VAULT/GitHub Digest/github-digest-$DATE.md" ]; then
    cp "$OBSIDIAN_VAULT/GitHub Digest/github-digest-$DATE.md" github/
    echo "✅ GitHub Digest 已复制 (from Obsidian)"
else
    echo "⚠️ GitHub Digest 不存在"
fi

# 从 Obsidian 复制 Blog Digest
if [ -f "$OBSIDIAN_VAULT/Blog Digest/blog-digest-$DATE.md" ]; then
    cp "$OBSIDIAN_VAULT/Blog Digest/blog-digest-$DATE.md" blog/
    echo "✅ Blog Digest 已复制 (from Obsidian)"
else
    echo "⚠️ Blog Digest 不存在"
fi

# 从 Obsidian 复制 YouTube Digest
if [ -f "$OBSIDIAN_VAULT/YouTube Digest/digest-$DATE.md" ]; then
    cp "$OBSIDIAN_VAULT/YouTube Digest/digest-$DATE.md" youtube/
    echo "✅ YouTube Digest 已复制 (from Obsidian)"
else
    echo "⚠️ YouTube Digest 不存在"
fi

# 检查是否有变更
if [ -z "$(git status --porcelain)" ]; then
    echo "ℹ️ 没有新的变更需要提交"
    exit 0
fi

# 提交并推送
git add -A
git commit -m "docs: add digest for $DATE

- GitHub Digest: Issues and PRs from Apache projects
- Blog Digest: Databricks, Anthropic, OpenAI news
- YouTube Digest: Latest videos from subscribed channels

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"

git push origin main

echo ""
echo "✅ 已推送到 GitHub: https://github.com/zhaomin1423/digest"
echo "========================================"
