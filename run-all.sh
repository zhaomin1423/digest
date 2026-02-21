#!/bin/bash

# Daily Digest Runner
# 统一运行所有digest任务（Blog、YouTube、GitHub）并推送到仓库

set -e  # 遇到错误时退出

# 配置
DIGEST_REPO="$HOME/digest"
BLOG_DIGEST_DIR="$HOME/blog-digest"
YOUTUBE_DIGEST_DIR="$HOME/youtube-digest"
GITHUB_DIGEST_DIR="$HOME/github-digest"
LOG_DIR="$DIGEST_REPO/logs"
LOG_FILE="$LOG_DIR/digest-$(date +%Y%m%d).log"

# 确保日志目录存在
mkdir -p "$LOG_DIR"

# 日志函数
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log "========================================="
log "Starting Daily Digest"
log "========================================="

# 函数：运行digest并推送到仓库
run_digest_and_push() {
    local name="$1"
    local dir="$2"
    local script="$3"
    local output_dir="$4"

    log "📌 Running $name Digest..."

    if [ ! -d "$dir" ]; then
        log "❌ Directory not found: $dir"
        return 1
    fi

    if [ ! -f "$script" ]; then
        log "⚠️  Script not found: $script - Skipping $name Digest"
        return 0
    fi

    # 运行脚本
    if bash "$script"; then
        log "✅ $name Digest completed successfully"

        # 如果指定了输出目录，复制文件到digest仓库
        if [ -n "$output_dir" ] && [ -d "$dir/digests" ]; then
            mkdir -p "$DIGEST_REPO/$output_dir"
            TODAY=$(date +%Y-%m-%d)

            # 复制今天的digest文件
            if [ -d "$dir/digests" ]; then
                find "$dir/digests" -name "*${TODAY}*" -type f | while read -r file; do
                    cp "$file" "$DIGEST_REPO/$output_dir/"
                    log "📋 Copied $(basename "$file") to $output_dir/"
                done
            fi
        fi
    else
        log "❌ $name Digest failed"
        return 1
    fi
}

# 运行 Blog Digest
run_digest_and_push "Blog" "$BLOG_DIGEST_DIR" "$BLOG_DIGEST_DIR/run-digest.sh" "blog"

# 运行 YouTube Digest
run_digest_and_push "YouTube" "$YOUTUBE_DIGEST_DIR" "$YOUTUBE_DIGEST_DIR/run-digest.sh" "youtube"

# 运行 GitHub Digest
run_digest_and_push "GitHub" "$GITHUB_DIGEST_DIR" "$GITHUB_DIGEST_DIR/run-digest.sh" "github"

# 推送到git仓库
log "📤 Pushing to git repository..."
cd "$DIGEST_REPO"

if [ -n "$(git status --porcelain)" ]; then
    git add .
    git commit -m "Daily Digest $(date +%Y-%m-%d)"
    git push origin main
    log "✅ Pushed to repository"
else
    log "ℹ️  No changes to commit"
fi

log "========================================="
log "Daily Digest completed"
log "========================================="
