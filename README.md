# Daily Digests

自动生成的每日摘要，包含 GitHub、博客和 YouTube 内容。

## 目录结构

```
├── github/          # GitHub Issues/PRs 摘要
├── blog/            # 博客文章摘要
└── youtube/         # YouTube 视频摘要
```

## 数据源

### GitHub
- Apache Fluss
- Apache Flink
- Apache Spark
- Apache Iceberg
- Apache Paimon

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

## 脚本工具

### Fluss Issue 每日扫描 (`scripts/fluss_issue_scanner.py`)

每日自动扫描 [apache/fluss](https://github.com/apache/fluss) 仓库的 Issue，生成 Markdown 格式报告至 `github/` 目录。

**功能特性**:
- 支持按日期过滤或全量扫描
- 自动重试（指数退避）和 API 限流处理
- 带时间戳的结构化日志输出
- 输出 Open / Closed Issue 详情（标题、作者、标签、创建时间、摘要等）

**用法**:
```bash
# 扫描今天更新的 Issue（推荐日常使用）
python3 scripts/fluss_issue_scanner.py --token YOUR_GITHUB_TOKEN

# 指定日期
python3 scripts/fluss_issue_scanner.py --date 2026-03-19 --token YOUR_GITHUB_TOKEN

# 全量扫描所有 Open Issue
python3 scripts/fluss_issue_scanner.py --full-scan --state open --token YOUR_GITHUB_TOKEN

# 指定输出目录
python3 scripts/fluss_issue_scanner.py --output-dir /custom/path --token YOUR_GITHUB_TOKEN
```

**Crontab 定时配置（每天 22:00）**:
```cron
0 22 * * * /usr/bin/python3 /path/to/digest/scripts/fluss_issue_scanner.py --token YOUR_TOKEN >> /var/log/fluss_scanner.log 2>&1
```

> 💡 **提示**: 建议通过环境变量 `GITHUB_TOKEN` 提供 Token，避免在命令行中明文传递。
