# GitHub 每日摘要

📅 **生成时间**: 2026-02-23 22:16:27
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

**核心内容**: 该Issue旨在优化Spark中`DESC TABLE`命令的输出格式，提升可读性。作者提供了当前格式的截图示例，并表示愿意提交PR进行改进。

#### 🔴 [[[Docs] Add documentation for C++ Client]](https://github.com/apache/fluss/issues/2448)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 31天前 |
| 👤 作者 | leekeiabstraction |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 提出 Apache Fluss 项目应为其 C++ 客户端添加文档，参考现有的 Java 客户端文档风格，以完善 API 指南。

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

**核心内容**: 该 Issue 请求为 Vortex 格式实现 Java File Format API。主要任务包括完成 Java 集成、确保通过 TCK 测试 (#15415) 并展示性能结果。

#### 🔴 [[Implement File Format API Technology Compatibility Kit]](https://github.com/apache/iceberg/issues/15415)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2小时前 |
| 👤 作者 | pvary |
| 🏷️ 状态 | OPEN

**核心内容**: 该请求建议为新的 File Format API 实现技术兼容性套件（TCK）。测试需覆盖多种数据格式（Generic、Spark、Flink、Arrow等）的读写互操作性，可基于 `TestGenericFormatModels` 扩展，并确保新测试套件易于为未来的文件格式进行扩展。

#### 🔴 [[GCSAuthManager does not seem to support credentials refresh - jobs crash mid]](https://github.com/apache/iceberg/issues/15414)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2小时前 |
| 👤 作者 | astronautas |
| 🏷️ 状态 | OPEN

**核心内容**: Apache Iceberg 1.10.1 中 GCSAuthManager 不支持凭证刷新，导致 Spark 作业运行数小时后崩溃，报错提示 OAuth2Credentials 实例无法刷新访问令牌。

#### 🔴 [[Clarify contract of `TableOperations#current()`]](https://github.com/apache/iceberg/issues/15413)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 4小时前 |
| 👤 作者 | piotrrzysko |
| 🏷️ 状态 | OPEN

**核心内容**: 该请求澄清了 `TableOperations#current()` 方法的契约。指出元数据加载发生在初始化、`refresh()` 和 `commit()` 时。核心结论是：仅 `refresh()` 和 `commit()` 能保证元数据的新鲜度；调用它们后，`current()` 返回的元数据至少与操作时一样新。在此之前，`current()` 返回的元数据新鲜度取决于初始加载时机，由实现定义。

#### 🔴 [[GCSFileIO - how to connection pooling - exploding number of TCP connections]](https://github.com/apache/iceberg/issues/15411)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 5小时前 |
| 👤 作者 | astronautas |
| 🏷️ 状态 | OPEN

**核心内容**: GCSFileIO 缺少 TCP 连接池支持，导致连接数激增（如每 15 分钟生成数千个 TCP 连接），影响性能。用户请求添加连接池功能，当前使用 Spark 4 引擎。

#### 🔴 [[Expose rollbackTransaction API for clean up ]](https://github.com/apache/iceberg/issues/15377)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 3天前 |
| 👤 作者 | deniskuzZ |
| 🏷️ 状态 | OPEN

**核心内容**: 该请求建议公开 `rollbackTransaction` API 以支持多表事务处理，旨在重用 `BaseTransaction`。请求针对 Hive 查询引擎，并附有相关代码链接。提交者表示可独立贡献此改进。

#### 🔴 [[bump roaringbitmap for spark 4.2 integration]](https://github.com/apache/iceberg/issues/15370)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 3天前 |
| 👤 作者 | kevinjqliu |
| 🏷️ 状态 | OPEN

**核心内容**: 此 Issue 追踪 roaringbitmap 版本升级（从 1.3.0 到 1.6.0）以适配 Spark 4.2 的集成。此前因担心使用 jitpack 仓库产生下游影响，该升级在 PR #15358 中被临时回退，仅为了 1.11 版本发布。现需商讨后续最佳推进方案。

#### 🟢 [[write.metadata.previous-versions-max has no effect]](https://github.com/apache/iceberg/issues/15307)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 10天前 |
| 👤 作者 | astronautas |
| 🏷️ 状态 | CLOSED

**核心内容**: 用户报告 Apache Iceberg 1.10.1 中配置项 `write.metadata.previous-versions-max`（默认值 100）似乎无效，`metadata-log` 的条目数超过了该限制，请求确认预期行为。

#### 🔴 [[Metadata is not committed after Kafka cluster recreation (parquiet files are written successfully)]](https://github.com/apache/iceberg/issues/15293)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 12天前 |
| 👤 作者 | rolxdaytona |
| 🏷️ 状态 | OPEN

**核心内容**: 在 Iceberg 1.9.2 和 Kafka Connect 环境中，完全重建 Kafka 集群后，Sink 连接器停止提交元数据。Parquet 文件写入成功，但日志显示“Nothing to commit”及恢复相关警告。唯一变更是更新了 Bootstrap Servers 配置，其他设置未变。

#### 🔴 [[In Iceberg catalog, JdbcTableOperations should catch and handle PostgresSQL's exception for duplicated keys]](https://github.com/apache/iceberg/issues/13924)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 180天前 |
| 👤 作者 | sqd |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 指出 Apache Iceberg 1.9.2 在 JDBC Catalog 中创建表时，`JdbcTableOperations` 仅捕获部分唯一键冲突异常，未能处理 PostgreSQL 抛出的特定异常（`PSQLException`）。这导致在表已存在时无法正确处理，而是抛出错误。建议增加对 PostgreSQL 异常的捕获和处理。

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

**核心内容**: 该 Issue 指出 Lance 的 LabelListIndex 在处理 NOT 过滤器时存在错误。当列表字段包含 NULL 值时，使用 `NOT array_has_any`、`NOT array_has_all` 或 `NOT array_contains` 进行过滤，实际结果错误地包含了 NULL 行，而预期结果应排除这些行。

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

**核心内容**: 引入 LocalWriter 后，`file://` 协议直接写入文件系统，绕过了 MirroringObjectStoreWrapper，导致 wrapper 无法接收写入操作，测试失败。目前已临时禁用该测试，后续将寻找最佳方案修复并重新启用。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## Daft

> 仓库: https://github.com/Eventual-Inc/Daft

### 📋 Issues (1)
#### 🔴 [[Connection errors when reading multiple parquet files from Azure]](https://github.com/Eventual-Inc/Daft/issues/6279)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 23分钟前 |
| 👤 作者 | gsmit |
| 🏷️ 状态 | OPEN

**核心内容**: 从 Azure 读取多个 Parquet 文件时，Daft 因同时打开过多连接导致网络层过载，引发套接字错误和崩溃。通过设置 `scantask_max_parallel=1` 限制并行度可解决该问题。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

