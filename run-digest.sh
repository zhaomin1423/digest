#!/bin/bash

# GitHub Digest Cron 包装脚本
# 每天定时抓取 GitHub Issues 和 PRs 并导入到 Obsidian

# 设置环境变量
export PATH="/usr/local/bin:/usr/bin:/bin:$PATH"

# Obsidian vault 路径
OBSIDIAN_VAULT="$HOME/Documents/Obsidian Vault"
OBSIDIAN_FOLDER="$OBSIDIAN_VAULT/GitHub Digest"

# 确保目录存在
mkdir -p "$OBSIDIAN_FOLDER"

# 日志文件
LOG_FILE="$HOME/github-digest/digest.log"

# 记录开始时间
echo "========================================" >> "$LOG_FILE"
echo "GitHub Digest started at $(date)" >> "$LOG_FILE"

# 运行 Python 脚本
cd ~/github-digest
/usr/bin/python3 ~/github-digest/github_digest.py >> "$LOG_FILE" 2>&1

# 检查执行结果
if [ $? -eq 0 ]; then
    echo "✅ GitHub Digest completed successfully" >> "$LOG_FILE"
else
    echo "❌ GitHub Digest failed with exit code $?" >> "$LOG_FILE"
fi

echo "Completed at $(date)" >> "$LOG_FILE"
