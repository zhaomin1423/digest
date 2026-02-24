# GitHub 每日摘要

📅 **生成时间**: 2026-02-24 22:03:42
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

**核心内容**: 该 Issue 指出 Fluss 默认配置中 ZooKeeper 会话超时（60秒）长于 ISR 收缩时间（约45秒），导致网络故障时 ISR 在 Leader 被判定为失效前就已收缩，造成无可用 Leader。建议参考 Kafka 调整参数顺序，确保 ISR 收缩发生在 Leader 检测之后，以提升可用性。

#### 🔴 [[Lance writer should emit Arrow FixedSizeList for array columns to enable native vector search]](https://github.com/apache/fluss/issues/2706)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2天前 |
| 👤 作者 | leekeiabstraction |
| 🏷️ 状态 | OPEN

**核心内容**: Fluss 在将 ARRAY<FLOAT> 列写入 Lance 时，错误地使用了 Arrow 的变长 List 类型，导致 Lance 的原生向量搜索无法工作，因为 Lance 要求使用 FixedSizeList。问题根源在于 LanceArrowUtils.toArrowType() 中 ArrayType 被无条件映射为 ArrowType.List.INSTANCE。

#### 🔴 [[TableChangeWatcherTest.testTableChanges is not stable]](https://github.com/apache/fluss/issues/1018)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 263天前 |
| 👤 作者 | wuchong |
| 🏷️ 状态 | OPEN

**核心内容**: GitHub Issue 报告 Fluss 项目中 `TableChangeWatcherTest.testTableChanges` 测试不稳定，CI 运行失败。错误显示断言失败，实际输出的 `CreateTableEvent` 列表与预期不符，涉及表路径、ID、分配等信息的差异。

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

**核心内容**: 该 Issue 建议在 Issues 中添加“新贡献者信息”板块，以指导新贡献者。参考了 Pandas 仓库的相关做法。

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

**核心内容**: Apache Iceberg 1.10.1 中，当字符串分区值包含首尾空格时，Spark 过滤会返回空结果，导致与 Athena 行为不一致。这会引发空连接、转换和写入，且难以调试。期望 Iceberg 能规范化或警告空格，或在分区修剪时提示，而非静默返回空数据。

#### 🔴 [[Kafka connect S3tables support]](https://github.com/apache/iceberg/issues/15425)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 14小时前 |
| 👤 作者 | kyrick |
| 🏷️ 状态 | OPEN

**核心内容**: 用户询问 Kafka Connect 的 Iceberg sink connector 是否支持 S3 Tables。虽然支持 REST catalog，但用户尝试配置时遇到 S3 Access Denied 异常，推测未使用 vended credentials。核心问题是确认是否支持 S3 Tables。

#### 🔴 [[Support Newer Delta Protocol Versions in Delta to Iceberg Migration Using Delta Kernel]](https://github.com/apache/iceberg/issues/15420)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 17小时前 |
| 👤 作者 | saitharun15 |
| 🏷️ 状态 | OPEN

**核心内容**: 当前 Delta-to-Iceberg 迁移依赖已弃用的 Delta Standalone，仅支持旧版协议（1,2），导致迁移新版 Delta 表（如 3,7）失败。建议改用 Delta Kernel API 以支持新版协议。

#### 🔴 [[IcebergSource on FlinkJob with Pause/Resume missed data]](https://github.com/apache/iceberg/issues/15418)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 23小时前 |
| 👤 作者 | randomdev2026 |
| 🏷️ 状态 | OPEN

**核心内容**: 使用 Flink 的 IcebergSource 在暂停/恢复作业时，若停机期间生成了多个 Parquet 文件，恢复后仅读取最新的文件，导致中间数据丢失。配置使用 `INCREMENTAL_FROM_LATEST_SNAPSHOT` 策略，怀疑是配置问题。

#### 🔴 [[S3SignerServlet should strip out more request headers for caching]](https://github.com/apache/iceberg/issues/15417)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 23小时前 |
| 👤 作者 | steveloughran |
| 🏷️ 状态 | OPEN

**核心内容**: 建议 S3SignerServlet 在签名时忽略更多请求头（如 User-Agent 和 Referer），以提高缓存复用率并减少签名次数。当前仅排除 range 和部分 SDK 内部头，需扩展排除列表以优化性能。

#### 🔴 [[Implement the Java File Format API  for Vortex]](https://github.com/apache/iceberg/issues/15416)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | pvary |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 请求为 Vortex 格式实现新的 Java File Format API。任务包括完成 Java 集成、确保通过 TCK 测试 (#15415) 并展示性能结果。

#### 🔴 [[GCSAuthManager does not seem to support credentials refresh - jobs crash mid]](https://github.com/apache/iceberg/issues/15414)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | astronautas |
| 🏷️ 状态 | OPEN

**核心内容**: Apache Iceberg 1.10.1 在 Spark 中使用 GCSAuthManager 时，作业运行数小时后因 OAuth2Credentials 不支持刷新访问令牌而崩溃，报错提示需使用支持刷新的实例或派生类型。

#### 🟢 [[bump roaringbitmap for spark 4.2 integration]](https://github.com/apache/iceberg/issues/15370)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 4天前 |
| 👤 作者 | kevinjqliu |
| 🏷️ 状态 | CLOSED

**核心内容**: 为支持 Spark 4.2 集成，将 roaringbitmap 从 1.3.0 升级至 1.6.0 的 PR 因使用 jitpack 仓库可能影响下游而被回退（针对 1.11 版本）。此 Issue 用于追踪该升级，旨在商讨下一步最佳方案。

#### 🔴 [[Make Spark readers function asynchronously for many small files.]](https://github.com/apache/iceberg/issues/15287)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 13天前 |
| 👤 作者 | varun-lakhyani |
| 🏷️ 状态 | OPEN

**核心内容**: Spark readers目前顺序处理扫描任务，在处理大量小文件时导致CPU和I/O并行度利用率低。请求改进为可选支持并发处理多个小文件任务，通过缓冲行到共享迭代器提升性能，同时默认保持现有顺序行为。

#### 🟢 [[Core: HadoopFileIO to take list of filesystem schemas to enable trash for]](https://github.com/apache/iceberg/issues/15093)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 34天前 |
| 👤 作者 | steveloughran |
| 🏷️ 状态 | CLOSED

**核心内容**: 提议改进 HadoopFileIO，通过配置选项 `iceberg.hadoop.trash.schemas` 指定启用回收站的文件系统列表（默认为 "hdfs" 和 "viewfs"），以解决现有方案对类路径依赖、性能开销及灵活性不足的问题。需添加测试验证功能，更新文档，并恢复删除不存在路径不抛出异常的语义。

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
| 📅 创建时间 | 11小时前 |
| 👤 作者 | kszlim |
| 🏷️ 状态 | CLOSED

**核心内容**: lance==2.0.1 在解码元数据强制 `structural-encoding=miniblock` 且 `compression=zstd` 的原始时间戳列时触发 panic。错误发生在 `primitive.rs:1305`，提示“Mini-block dictionary encoding must use Variable, Flat, or General compression”。环境变量 `LANCE_ENCODING_DICT_TOO_SMALL` 可规避此问题。预期应正常解码或返回验证错误，而非崩溃。

#### 🔴 [[Add clickbench results]](https://github.com/lance-format/lance/issues/5992)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 18小时前 |
| 👤 作者 | kszlim |
| 🏷️ 状态 | OPEN

**核心内容**: 建议将 Lance 文件格式添加到 ClickBench 基准测试中，以评估其性能。参考 Vortex 和 Parquet 在 DataFusion/DuckDB 上的测试示例，希望将 Lance 也纳入其中。

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

**核心内容**: LanceDB 0.18 在 Ceph 上对包含 250 万行和两个标量索引的表执行 `compact_files` 时失败。报错信息显示“Row ids did not arrive in sorted order”，该错误与 lance-format/lance #2809 相关。

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

**核心内容**: SQL 中 `DATE_TRUNC` 函数无法使用，报错未找到。原因有二：1. 注册失败，因函数需非空参数；2. 内部名称为 "truncate" 而非 "date_trunc"。解决方案是修复注册和名称匹配，使其与 Python API 和标准 SQL 一致。

#### 🔴 [[Poor CPU utilization with Ray cluster: RaySwordfishActor only uses single core despite multi-core workers available]](https://github.com/Eventual-Inc/Daft/issues/6126)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 19天前 |
| 👤 作者 | haifengwang1987 |
| 🏷️ 状态 | OPEN

**核心内容**: Ray 集群中 Daft 工作负载 CPU 利用率低，`RaySwordfishActor` 仅使用单核导致瓶颈，其他核心空闲。环境为 Daft 0.7.2、Ray 2.47.1、Ubuntu 22.04，配置 1 头节点（4 核）和 1 工作节点（36 核）。复现步骤基于官方文档嵌入基准测试，修改为本地读取并简化逻辑。

#### 🔴 [[SQL: tpc-DS q23 fails with schema mismatch error]](https://github.com/Eventual-Inc/Daft/issues/3561)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 438天前 |
| 👤 作者 | universalmind303 |
| 🏷️ 状态 | OPEN

**核心内容**: TPC-DS 查询 q23 在执行时因模式不匹配错误（schema mismatch error）失败，抛出 DaftCoreException。错误发生在调用 `daft.sql()` 并转换为 Arrow 表格的过程中，具体在 `to_arrow_iter` 迭分区时触发。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

