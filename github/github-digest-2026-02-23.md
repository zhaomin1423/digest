# GitHub 每日摘要

📅 **生成时间**: 2026-02-23 22:13:38
⏰ **时间范围**: 过去 24 小时
📊 **监控仓库数**: 8
📋 **总计**: 16 Issues, 0 Pull Requests

## 📑 目录

- [Apache Fluss](#apache-fluss) - 2 Issues, 0 PRs
- [Apache Flink](#apache-flink) - 0 Issues, 0 PRs
- [Apache Spark](#apache-spark) - 0 Issues, 0 PRs
- [Apache Iceberg](#apache-iceberg) - 11 Issues, 0 PRs
- [Apache Paimon](#apache-paimon) - 0 Issues, 0 PRs
- [Lance](#lance) - 1 Issues, 0 PRs
- [LanceDB](#lancedb) - 1 Issues, 0 PRs
- [Daft](#daft) - 1 Issues, 0 PRs

---

## Apache Fluss

> 仓库: https://github.com/apache/fluss

### 📋 Issues (2)
#### 🔴 [[[spark] refine the format when desc table]](https://github.com/apache/fluss/issues/2675)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 10天前 |
| 👤 作者 | YannByron |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 旨在优化 Spark 中 `DESC TABLE` 命令的输出格式。提交者提供了当前输出样式的截图，并愿意提交 PR 来改进格式。

#### 🔴 [[[Docs] Add documentation for C++ Client]](https://github.com/apache/fluss/issues/2448)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 31天前 |
| 👤 作者 | leekeiabstraction |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 建议为 Apache Fluss 的 C++ 客户端添加文档，参考现有 Java 客户端文档（https://fluss.apache.org/docs/apis/java-client/），以保持文档一致性。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## Apache Flink

> 仓库: https://github.com/apache/flink

### 📋 Issues (0)
_过去 24 小时内没有新的 Issue_

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## Apache Spark

> 仓库: https://github.com/apache/spark

### 📋 Issues (0)
_过去 24 小时内没有新的 Issue_

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## Apache Iceberg

> 仓库: https://github.com/apache/iceberg

### 📋 Issues (11)
#### 🔴 [[Implement the Java File Format API  for Vortex]](https://github.com/apache/iceberg/issues/15416)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2小时前 |
| 👤 作者 | pvary |
| 🏷️ 状态 | OPEN

**核心内容**: 该请求为 Vortex 格式实现 Java 文件格式 API，包括集成、通过 TCK 测试及展示性能结果。

#### 🔴 [[Implement File Format API Technology Compatibility Kit]](https://github.com/apache/iceberg/issues/15415)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2小时前 |
| 👤 作者 | pvary |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 提出为新的 File Format API 实现技术兼容套件（TCK）。测试需覆盖基于 Generic 数据的写入，以及使用 Generic/Spark/Flink/Arrow 等多种引擎进行读取和写入的互操作性。建议从 `TestGenericFormatModels` 开始，并确保测试套件易于扩展以支持新的文件格式。

#### 🔴 [[GCSAuthManager does not seem to support credentials refresh - jobs crash mid]](https://github.com/apache/iceberg/issues/15414)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2小时前 |
| 👤 作者 | astronautas |
| 🏷️ 状态 | OPEN

**核心内容**: Apache Iceberg 1.10.1 中使用 GCSAuthManager 时，作业运行数小时后因 `OAuth2Credentials` 不支持访问令牌刷新而崩溃。用户期望 GCSAuthManager 能自动刷新凭证，但当前实现不支持，导致作业中断。

#### 🔴 [[Clarify contract of `TableOperations#current()`]](https://github.com/apache/iceberg/issues/15413)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 4小时前 |
| 👤 作者 | piotrrzysko |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 旨在澄清 `TableOperations#current()` 的“加载”契约。通过代码追踪，发现加载发生在初始化、`refresh()` 和 `commit()` 时。核心结论是：只有 `refresh()` 和 `commit()` 能保证元数据的新鲜度，调用它们后 `current()` 返回的数据至少与操作时一样新；在此之前，`current()` 返回的新鲜程度取决于实现定义，无保证。

#### 🔴 [[GCSFileIO - how to connection pooling - exploding number of TCP connections]](https://github.com/apache/iceberg/issues/15411)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 5小时前 |
| 👤 作者 | astronautas |
| 🏷️ 状态 | OPEN

**核心内容**: 用户请求改进 GCSFileIO，指出目前缺乏 TCP 连接池支持导致连接数激增（如每 15 分钟产生数千个 TCP 连接进行合并操作）。该问题发生在 Spark 4 环境下，用户目前无法贡献代码。

#### 🔴 [[Expose rollbackTransaction API for clean up ]](https://github.com/apache/iceberg/issues/15377)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 3天前 |
| 👤 作者 | deniskuzZ |
| 🏷️ 状态 | OPEN

**核心内容**: 该功能请求旨在暴露 `rollbackTransaction` API 以支持多表事务，意图复用 `BaseTransaction`。针对 Hive 查询引擎，提交者表示可独立贡献此改进。相关参考链接指向 Apache Hive 的具体代码变更。

#### 🔴 [[bump roaringbitmap for spark 4.2 integration]](https://github.com/apache/iceberg/issues/15370)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 3天前 |
| 👤 作者 | kevinjqliu |
| 🏷️ 状态 | OPEN

**核心内容**: 为支持 Spark 4.2 集成，此前将 roaringbitmap 从 1.3.0 升级至 1.6.0 的 PR 因使用 `jitpack` 仓库引发下游影响担忧而被回退。此次回退仅针对 1.11 版本。本 Issue 旨在确定后续最佳推进步骤。

#### 🟢 [[write.metadata.previous-versions-max has no effect]](https://github.com/apache/iceberg/issues/15307)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 10天前 |
| 👤 作者 | astronautas |
| 🏷️ 状态 | CLOSED

**核心内容**: 用户报告在 Apache Iceberg 1.10.1 和 Spark 4+ 中，配置项 `write.metadata.previous-versions-max` 似乎无效。尽管默认值为 100，但 `metadata-log` 的条目数仍会超出该限制，不符合文档描述的清理旧元文件的行为。

#### 🔴 [[Metadata is not committed after Kafka cluster recreation (parquiet files are written successfully)]](https://github.com/apache/iceberg/issues/15293)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 12天前 |
| 👤 作者 | rolxdaytona |
| 🏷️ 状态 | OPEN

**核心内容**: Kafka集群重建后，Iceberg Kafka Connect Sink停止提交元数据。数据文件写入成功，但日志显示“Nothing to commit”及恢复警告。环境为Iceberg 1.9.2、JDBC Catalog、Kafka 3.5.1。仅变更了Kafka bootstrap servers配置，其他未变。

#### 🔴 [[In Iceberg catalog, JdbcTableOperations should catch and handle PostgresSQL's exception for duplicated keys]](https://github.com/apache/iceberg/issues/13924)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 180天前 |
| 👤 作者 | sqd |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 指出 Apache Iceberg 1.9.2 在使用 JDBC Catalog 创建表时，未能正确捕获和处理 PostgreSQL 抛出的唯一键冲突异常。当前代码仅处理了通用的重复键异常，导致表已存在时抛出 PSQLException。建议修复 JdbcTableOperations 以兼容 PostgreSQL 的特定异常处理机制。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## Apache Paimon

> 仓库: https://github.com/apache/paimon

### 📋 Issues (0)
_过去 24 小时内没有新的 Issue_

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## Lance

> 仓库: https://github.com/lance-format/lance

### 📋 Issues (1)
#### 🔴 [[LabelListIndex: NOT filters mis-handle NULL lists (list-level NULLs)]](https://github.com/lance-format/lance/issues/5904)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 16天前 |
| 👤 作者 | fenfeng9 |
| 🏷️ 状态 | OPEN

**核心内容**: Lance 的 LabelListIndex 在处理 NOT 过滤器（如 NOT array_has_any）时错误地包含了列表级别的 NULL 值。实际查询结果中包含了 NULL，而预期结果应将其排除。该问题导致带索引的查询与无索引查询结果不一致。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## LanceDB

> 仓库: https://github.com/lancedb/lancedb

### 📋 Issues (1)
#### 🔴 [[Rust - LocalWriter breaks io::object_store::test::test_e2e]](https://github.com/lancedb/lancedb/issues/3059)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 6小时前 |
| 👤 作者 | jackye1995 |
| 🏷️ 状态 | OPEN

**核心内容**: 引入 LocalWriter 后，对于 `file://` 方案，Lance 直接写文件系统绕过 MirroringObjectStoreWrapper，导致包装器未捕获写入操作，无法镜像到次要存储，从而破坏了 `io::object_store::test::test_e2e` 测试。该测试已被暂时禁用，待寻找合适方案修复后重新启用。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## Daft

> 仓库: https://github.com/Eventual-Inc/Daft

### 📋 Issues (1)
#### 🔴 [[Connection errors when reading multiple parquet files from Azure]](https://github.com/Eventual-Inc/Daft/issues/6279)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 20分钟前 |
| 👤 作者 | gsmit |
| 🏷️ 状态 | OPEN

**核心内容**: 从 Azure 读取多个 Parquet 文件时，因连接过多导致网络层崩溃并报错。限制并行度（`scantask_max_parallel=1`）可解决此问题。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

