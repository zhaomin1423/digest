# Daily Digests

自动生成的每日摘要，包含 GitHub、博客和 YouTube 内容。

## 目录结构

```
├── github/          # GitHub Issues/PRs 摘要
├── blog/            # 博客文章摘要
├── youtube/         # YouTube 视频摘要
└── sync.sh          # 同步脚本
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

每天 22:00 自动生成并推送到本仓库。
