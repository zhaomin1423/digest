# Daily Digests

自动生成的每日摘要，包含 GitHub、博客和 YouTube 内容。

## 目录结构

```
├── github/          # GitHub Issues/PRs 摘要（含 Fluss Issue 扫描）
├── blog/            # 博客文章摘要
├── youtube/         # YouTube 视频摘要
└── scripts/         # 辅助脚本
    └── fluss_issue_scanner.py  # Apache Fluss Issue 每日扫描脚本
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

## Fluss Issue 扫描器

`scripts/fluss_issue_scanner.py` 专门用于扫描 [apache/fluss](https://github.com/apache/fluss) 仓库的 Issues，并生成每日摘要报告。

### 用法

```bash
# 扫描过去 24 小时内更新的 Issues（默认）
python3 scripts/fluss_issue_scanner.py

# 使用 GitHub Token 提升 API 速率限制
python3 scripts/fluss_issue_scanner.py --token YOUR_TOKEN

# 扫描全部开放 Issues
python3 scripts/fluss_issue_scanner.py --all

# 自定义时间范围（过去 48 小时）
python3 scripts/fluss_issue_scanner.py --hours 48

# 指定输出目录和日志文件
python3 scripts/fluss_issue_scanner.py --output-dir ./github --log-file ./logs/fluss.log
```

### 定时任务（crontab）

```bash
# 每天 22:00 运行，将结果追加到日志文件
0 22 * * * cd /path/to/digest && GITHUB_TOKEN=your_token python3 scripts/fluss_issue_scanner.py >> logs/fluss-scanner.log 2>&1
```

也可通过 `run-all.sh` 统一调度，该脚本会自动调用 Fluss Issue 扫描器。

## 自动更新

每天 22:00 自动生成并推送到本仓库：
1. GitHub Digest → 推送
2. Blog Digest → 推送
3. YouTube Digest → 推送
4. Fluss Issue Digest → 推送

每个摘要生成后立即单独推送。
