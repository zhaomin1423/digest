# Daily Digests

自动生成的每日摘要，包含 GitHub、博客和 YouTube 内容。

## 目录结构

```
├── github/          # GitHub Issues/PRs 摘要
├── blog/            # 博客文章摘要
├── youtube/         # YouTube 视频摘要
├── run-all.sh       # 统一生成和推送脚本
└── sync.sh          # (已弃用)
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

每天 22:00 执行 `run-all.sh`：
1. 生成 GitHub Digest → 推送到 GitHub
2. 生成 Blog Digest → 推送到 GitHub
3. 生成 YouTube Digest → 推送到 GitHub

每个摘要生成后立即单独推送，确保及时同步。
