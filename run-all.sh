#!/bin/bash

# 统一的 Digest 生成和推送脚本
# 每天22点执行，每个摘要生成后单独推送到 GitHub

set -e

DATE=$(date +%Y-%m-%d)
REPO_DIR="$HOME/digest"
OBSIDIAN_VAULT="$HOME/Documents/Obsidian Vault"
LOG_FILE="$REPO_DIR/digest.log"

echo "========================================" >> "$LOG_FILE"
echo "Digest Pipeline started at $(date)" >> "$LOG_FILE"
echo "========================================"

cd "$REPO_DIR"

# 函数：推送单个 digest 到 GitHub
push_to_github() {
    local type=$1  # github, blog, youtube
    local source_file=$2
    local target_dir=$3

    if [ -f "$source_file" ]; then
        cp "$source_file" "$target_dir/"
        git add "$target_dir/"
        git commit -m "docs: add $type digest for $DATE

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>" --allow-empty 2>/dev/null || true
        git push origin main
        echo "✅ $type Digest 已推送到 GitHub" >> "$LOG_FILE"
    else
        echo "⚠️ $type Digest 文件不存在" >> "$LOG_FILE"
    fi
}

# 1. 生成 GitHub Digest
echo "" >> "$LOG_FILE"
echo "📋 生成 GitHub Digest..." >> "$LOG_FILE"
cd ~/github-digest
/usr/bin/python3 ~/github-digest/github_digest.py >> "$LOG_FILE" 2>&1
push_to_github "github" "$OBSIDIAN_VAULT/GitHub Digest/github-digest-$DATE.md" "$REPO_DIR/github"

# 2. 生成 Blog Digest
echo "" >> "$LOG_FILE"
echo "📰 生成 Blog Digest..." >> "$LOG_FILE"
cd ~/blog-digest
/usr/bin/python3 ~/blog-digest/blog_digest.py >> "$LOG_FILE" 2>&1
push_to_github "blog" "$OBSIDIAN_VAULT/Blog Digest/blog-digest-$DATE.md" "$REPO_DIR/blog"

# 3. 生成 YouTube Digest
echo "" >> "$LOG_FILE"
echo "📺 生成 YouTube Digest..." >> "$LOG_FILE"
cd ~/youtube-digest
/usr/bin/python3 ~/youtube-digest/youtube_digest.py >> "$LOG_FILE" 2>&1
push_to_github "youtube" "$OBSIDIAN_VAULT/YouTube Digest/digest-$DATE.md" "$REPO_DIR/youtube"

echo "" >> "$LOG_FILE"
echo "✅ All digests completed at $(date)" >> "$LOG_FILE"
echo "========================================" >> "$LOG_FILE"
