# GitHub 每日摘要

📅 **生成时间**: 2026-02-24 22:12:17
⏰ **时间范围**: 过去 24 小时
📊 **监控仓库数**: 8
📋 **总计**: 28 Issues, 0 Pull Requests

## 📑 目录

- [Apache Fluss](#apache-fluss) - 3 Issues, 0 PRs
- [Apache Flink](#apache-flink) - 0 Issues, 0 PRs
- [Apache Spark](#apache-spark) - 1 Issues, 0 PRs
- [Apache Iceberg](#apache-iceberg) - 17 Issues, 0 PRs
- [Apache Paimon](#apache-paimon) - 0 Issues, 0 PRs
- [Lance](#lance) - 3 Issues, 0 PRs
- [LanceDB](#lancedb) - 1 Issues, 0 PRs
- [Daft](#daft) - 3 Issues, 0 PRs

---

## Apache Fluss

> 仓库: https://github.com/apache/fluss

### 📋 Issues (3)
#### 🔴 [[[server] Adjust ZooKeeper session timeout to prevent ISR shrink before leader failover]](https://github.com/apache/fluss/issues/2708)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 11小时前 |
| 👤 作者 | LiebingYu |
| 🏷️ 状态 | OPEN

**核心内容**: Fluss 默认 ZooKeeper 会话超时（60秒）大于 ISR 收缩时间（约45秒），导致网络故障时 ISR 在 Leader 被判定死亡前已收缩，致使无可用 Leader。该 Issue 建议参考 Kafka 配置，调整相关超时参数以修复此可用性问题。

#### 🔴 [[Lance writer should emit Arrow FixedSizeList for array columns to enable native vector search]](https://github.com/apache/fluss/issues/2706)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2天前 |
| 👤 作者 | leekeiabstraction |
| 🏷️ 状态 | OPEN

**核心内容**: Fluss 在将 ARRAY<FLOAT> 列写入 Lance 时，总是将其转换为 Arrow 的变长 List，导致 Lance 的原生向量搜索无法工作，因为 Lance 要求向量列为 FixedSizeList。问题源于 LanceArrowUtils.toArrowType() 中 ArrayType 无条件映射为 ArrowType.List.INSTANCE。

#### 🔴 [[TableChangeWatcherTest.testTableChanges is not stable]](https://github.com/apache/fluss/issues/1018)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 263天前 |
| 👤 作者 | wuchong |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 报告 Fluss 项目中 `TableChangeWatcherTest.testTableChanges` 测试不稳定，在 CI 运行中出现失败。错误日志显示断言失败，实际生成的 `CreateTableEvent` 列表与预期不符，涉及表信息、分配策略等字段的不匹配。

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

### 📋 Issues (1)
#### 🔴 [[Add `Information for new contributors` in Issues]](https://github.com/apache/spark/issues/54438)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 10小时前 |
| 👤 作者 | zhengruifeng |
| 🏷️ 状态 | OPEN

**核心内容**: 该 PR 建议在 Issues 中添加“新贡献者指南”以帮助新人参与，参考了 Pandas 项目的相关实践。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## Apache Iceberg

> 仓库: https://github.com/apache/iceberg

### 📋 Issues (17)
#### 🔴 [[Whitespace in string partition values causes Spark to return empty DataFrames and inconsistent results across engines]](https://github.com/apache/iceberg/issues/15427)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 8小时前 |
| 👤 作者 | khjoshi94 |
| 🏷️ 状态 | OPEN

**核心内容**: 该问题涉及 Apache Iceberg 1.10.1 版本。当表字符串分区值包含空格（如 "20240201 "）时，Spark 过滤查询返回空结果，导致跨引擎行为不一致及下游数据处理错误。期望 Iceberg 能规范化或校验分区值、提供警告或配置选项，而非当前直接存储原值并静默修剪文件，引发数据正确性问题。

#### 🔴 [[Kafka connect S3tables support]](https://github.com/apache/iceberg/issues/15425)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 14小时前 |
| 👤 作者 | kyrick |
| 🏷️ 状态 | OPEN

**核心内容**: 用户询问 Kafka Connect 的 Iceberg sink connector 是否支持 S3 Tables。尽管支持 REST catalog，但用户尝试配置时遇到 S3 Access Denied 异常，推测未使用 vended credentials。核心问题是确认该 connector 是否支持 S3 Tables。

#### 🔴 [[Support Newer Delta Protocol Versions in Delta to Iceberg Migration Using Delta Kernel]](https://github.com/apache/iceberg/issues/15420)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 17小时前 |
| 👤 作者 | saitharun15 |
| 🏷️ 状态 | OPEN

**核心内容**: 当前 Delta 到 Iceberg 迁移依赖已废弃的 Delta Standalone，仅支持旧协议版本 (1,2)，无法处理新版本 (如 3,7)，导致迁移失败。建议改用 Delta Kernel API 以支持最新协议。

#### 🔴 [[IcebergSource on FlinkJob with Pause/Resume missed data]](https://github.com/apache/iceberg/issues/15418)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 23小时前 |
| 👤 作者 | randomdev2026 |
| 🏷️ 状态 | OPEN

**核心内容**: 使用 Flink IcebergSource 的流式作业在暂停/恢复后，若停机期间产生了多个 Parquet 文件，恢复时仅读取最新文件，导致中间数据丢失。用户使用 Iceberg 1.10.1 和 Flink 2.0，作业配置为增量读取最新快照，怀疑是配置问题，需解决数据遗漏问题。

#### 🔴 [[S3SignerServlet should strip out more request headers for caching]](https://github.com/apache/iceberg/issues/15417)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 23小时前 |
| 👤 作者 | steveloughran |
| 🏷️ 状态 | OPEN

**核心内容**: 请求改进 S3SignerServlet，建议在签名时忽略更多请求头（如 user-agent 和 referrer）。这些头部通常由 JVM 或审计追踪生成，忽略它们可增加请求缓存复用，减少签名次数。当前仅排除 range 和部分 SDK 内部头部。

#### 🔴 [[Implement the Java File Format API  for Vortex]](https://github.com/apache/iceberg/issues/15416)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | pvary |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 请求为 Vortex 格式实现 Java 版本的 File Format API。主要任务包括完成 Java 集成、确保通过 TCK 测试，并展示性能结果。

#### 🔴 [[GCSAuthManager does not seem to support credentials refresh - jobs crash mid]](https://github.com/apache/iceberg/issues/15414)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | astronautas |
| 🏷️ 状态 | OPEN

**核心内容**: 在 Apache Iceberg 1.10.1 中，使用 GCSAuthManager 时，作业运行数小时后因 OAuth2Credentials 不支持刷新访问令牌而崩溃，提示需使用新令牌实例或支持刷新的派生类型。用户期望 GCSAuthManager 能自动刷新凭证。

#### 🟢 [[bump roaringbitmap for spark 4.2 integration]](https://github.com/apache/iceberg/issues/15370)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 4天前 |
| 👤 作者 | kevinjqliu |
| 🏷️ 状态 | CLOSED

**核心内容**: 此 Issue 追踪 Apache Iceberg 将 roaringbitmap 从 1.3.0 升级至 1.6.0 以适配 Spark 4.2 的事宜。此前因使用 jitpack 仓库的下游影响担忧，该升级被回退以支持 1.11 版本发布。现需商定后续最佳推进步骤。

#### 🔴 [[Make Spark readers function asynchronously for many small files.]](https://github.com/apache/iceberg/issues/15287)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 13天前 |
| 👤 作者 | varun-lakhyani |
| 🏷️ 状态 | OPEN

**核心内容**: 该请求建议改进Spark读取器，使其能异步处理大量小文件。当前读取器按顺序处理任务，导致CPU和I/O并行度不足，增加开销。建议允许多个小文件任务并发处理，缓冲行至共享迭代器，同时保留默认顺序行为。

#### 🟢 [[Core: HadoopFileIO to take list of filesystem schemas to enable trash for]](https://github.com/apache/iceberg/issues/15093)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 34天前 |
| 👤 作者 | steveloughran |
| 🏷️ 状态 | CLOSED

**核心内容**: 提议改进 HadoopFileIO，通过新增配置 `iceberg.hadoop.trash.schemas` 指定启用 trash 的文件系统列表（默认为 hdfs 和 viewfs）。解决当前方案依赖类名导致的兼容性问题，减少实例化开销，并支持灵活控制。同时需恢复删除不存在文件不抛出异常的语义，添加测试及文档。

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

### 📋 Issues (3)
#### 🔴 [[[Bug] FileFragment.update_columns does not update last_updated_at_version_meta]](https://github.com/lance-format/lance/issues/6000)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2小时前 |
| 👤 作者 | fangbo |
| 🏷️ 状态 | OPEN

#### 🟢 [[Panic decoding primitive miniblock dictionary page (2.0.1): unreachable in primitive.rs:1305]](https://github.com/lance-format/lance/issues/5994)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 12小时前 |
| 👤 作者 | kszlim |
| 🏷️ 状态 | CLOSED

**核心内容**: lance==2.0.1 在解码时间戳列时触发 panic，当元数据强制使用 `structural-encoding=miniblock` 和 `compression=zstd` 时发生。错误源自 `primitive.rs:1305` 的 `unreachable!` 断言。期望应成功解码或返回优雅的错误，而非后台崩溃。设置 `LANCE_ENCODING_DICT_TOO_SMALL` 环境变量可暂时规避该问题。

#### 🔴 [[Add clickbench results]](https://github.com/lance-format/lance/issues/5992)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 18小时前 |
| 👤 作者 | kszlim |
| 🏷️ 状态 | OPEN

**核心内容**: 提议将 Lance 文件格式加入 Clickbench 基准测试，以评估其性能。参考 Vortex/Parquet 在 Clickbench 上通过 DataFusion/DuckDB 查询的示例，希望添加 Lance 的测试结果。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## LanceDB

> 仓库: https://github.com/lancedb/lancedb

### 📋 Issues (1)
#### 🔴 [[bug(python): Compaction failed with "Row ids did not arrive in sorted order: integers are ordered up to the 0th element, /rustc/9fc6b43126469e3858e2fe86cafb4f0fd5068869/library/core/src/task/poll.rs:290:44"]](https://github.com/lancedb/lancedb/issues/3063)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 14小时前 |
| 👤 作者 | edwin-jsi |
| 🏷️ 状态 | OPEN

**核心内容**: LanceDB 0.18 版本在表达到 250 万行后，执行 `compact_files` 时报错 "Row ids did not arrive in sorted order"。错误指向 Rust poll.rs 文件，疑似与已知 issue #2809 相关。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## Daft

> 仓库: https://github.com/Eventual-Inc/Daft

### 📋 Issues (3)
#### 🟢 [[SQL: DATE_TRUNC function not found]](https://github.com/Eventual-Inc/Daft/issues/6257)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 4天前 |
| 👤 作者 | desmondcheongzx |
| 🏷️ 状态 | CLOSED

**核心内容**: SQL中DATE_TRUNC函数报错未找到，尽管Python API可用。原因：1. 注册时因缺少参数静默失败；2. 内部注册名为"truncate"而非"date_trunc"。解决方案：修复注册逻辑和命名，使其在SQL中正常工作。

#### 🔴 [[Poor CPU utilization with Ray cluster: RaySwordfishActor only uses single core despite multi-core workers available]](https://github.com/Eventual-Inc/Daft/issues/6126)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 19天前 |
| 👤 作者 | haifengwang1987 |
| 🏷️ 状态 | OPEN

**核心内容**: Daft 在 Ray 集群上运行时，尽管有多核 CPU 可用，`RaySwordfishActor` 进程仅占用单核（100% CPU），导致其他核心闲置，造成性能瓶颈。环境为 Daft 0.7.2、Ray 2.47.1、Ubuntu 22.04，集群配置为 1 个 Head 节点（4 核）和 1 个 Worker 节点（36 核）。问题通过修改官方文档嵌入基准测试复现。

#### 🔴 [[SQL: tpc-DS q23 fails with schema mismatch error]](https://github.com/Eventual-Inc/Daft/issues/3561)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 438天前 |
| 👤 作者 | universalmind303 |
| 🏷️ 状态 | OPEN

**核心内容**: TPC-DS 查询 q23 因架构不匹配错误而失败，涉及 Da `to_arrow` 方法中的异常。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

