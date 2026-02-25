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

# 错误日志函数
log_error() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ❌ ERROR: $1" | tee -a "$LOG_FILE"
}

# 检查 timeout 命令是否可用
if command -v timeout &> /dev/null; then
    HAS_TIMEOUT=1
else
    HAS_TIMEOUT=0
fi

# git push 带超时和重试的函数
git_push_with_retry() {
    local max_retries=3
    local timeout_seconds=60
    local attempt=1
    local branch="${1:-main}"

    while [ $attempt -le $max_retries ]; do
        log "📤 Push attempt $attempt/$max_retries to $branch..."

        # 根据系统是否支持 timeout 选择执行方式
        if [ $HAS_TIMEOUT -eq 1 ]; then
            { timeout $timeout_seconds git push origin "$branch" 2>&1 | tee -a "$LOG_FILE"; } \
                && local push_exit_code=${PIPESTATUS[0]} || local push_exit_code=${PIPESTATUS[0]}
            if [ $push_exit_code -eq 0 ]; then
                log "✅ Pushed to repository successfully"
                return 0
            else
                if [ $push_exit_code -eq 124 ]; then
                    log_error "Git push timed out (timeout: ${timeout_seconds}s)"
                else
                    log_error "Git push failed with exit code: $push_exit_code"
                fi
            fi
        else
            { git push origin "$branch" 2>&1 | tee -a "$LOG_FILE"; } \
                && local push_exit_code=${PIPESTATUS[0]} || local push_exit_code=${PIPESTATUS[0]}
            if [ $push_exit_code -eq 0 ]; then
                log "✅ Pushed to repository successfully"
                return 0
            else
                log_error "Git push failed with exit code: $push_exit_code"
            fi
        fi

        if [ $attempt -lt $max_retries ]; then
            local wait_time=$((attempt * 5))
            log "⏳ Waiting ${wait_time}s before retry..."
            sleep $wait_time
            attempt=$((attempt + 1))
        fi
    done

    log_error "❌ Failed to push after $max_retries attempts"
    return 1
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
    log "📝 Detected changes, committing..."
    git add .
    git commit -m "Daily Digest $(date +%Y-%m-%d)" 2>&1 | tee -a "$LOG_FILE"

    # 使用带重试和超时的push函数
    if git_push_with_retry "main"; then
        log "✅ Repository updated successfully"
    else
        log_error "❌ Failed to push to repository - changes committed locally but not pushed"
        log "⚠️  You may need to push manually: cd $DIGEST_REPO && git push origin main"
    fi
else
    log "ℹ️  No changes to commit"
fi

log "========================================="
log "Daily Digest completed"
log "========================================="
