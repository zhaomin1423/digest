# Daily Digests

自动生成的每日摘要，包含 GitHub、博客和 YouTube 内容。

## 目录结构

```
├── github/          # GitHub Issues/PRs 摘要
├── blog/            # 博客文章摘要
├── youtube/         # YouTube 视频摘要
├── github_digest.py  # GitHub 摘要生成脚本
├── repos.json        # GitHub 仓库配置
└── run-digest.sh    # Cron 包装脚本
```

## GitHub Digest 功能

- 使用 `gh` CLI 获取最近 24 小时内的 Issues 和 PRs
- 使用豆包 API 生成中文摘要
- 自动保存到 Obsidian vault 的 `GitHub Digest` 文件夹
- 支持配置多个仓库
- 支持 `--date` 参数重新生成指定日期的摘要

## 安装

1. 确保已安装 GitHub CLI:
   ```bash
   brew install gh
   gh auth login
   ```

2. 安装 Python 依赖:
   ```bash
   pip3 install -r requirements.txt
   ```

3. 配置豆包 API（在 `~/.openclaw/openclaw.json` 中）

## 配置

编辑 `repos.json` 添加要监控的仓库:

```json
{
  "repos": [
    {
      "name": "Apache Fluss",
      "owner": "apache",
      "repo": "fluss",
      "enabled": true
    }
  ],
  "settings": {
    "hours_back": 24,
    "obsidian_vault": "/Users/zhaomin/Documents/Obsidian Vault",
    "output_folder": "GitHub Digest"
  }
}
```

## 手动运行

```bash
cd ~/github-digest
python3 github_digest.py
```

重新生成指定日期的摘要:
```bash
python3 github_digest.py --date 2026-02-20
```

## 设置定时任务

每天 22:00 自动执行:

```bash
crontab -e
```

添加以下行:

```
0 22 * * * /bin/bash /Users/zhaomin/github-digest/run-digest.sh
```

## 数据源

### GitHub
- Apache Fluss
- Apache Flink
- Apache Spark
- Apache Iceberg
- Apache Paimon
- Ray (ray-project/ray)
- Lance (lance-format/lance)
- LanceDB (lancedb/lancedb)
- Daft (Eventual-Inc/Daft)

### Blog
- Databricks Blog
- Anthropic News
- OpenAI News (RSS)

### YouTube
- Matt Wolfe
- Databricks
- 小Lin说
- Anthropic
- OpenAI

## 自动更新

每天 22:00 自动生成并推送到本仓库：
1. GitHub Digest → 推送
2. Blog Digest → 推送
3. YouTube Digest → 推送

每个摘要生成后立即单独推送。
