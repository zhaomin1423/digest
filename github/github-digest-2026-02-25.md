# GitHub 每日摘要

📅 **生成时间**: 2026-02-25 22:02:50
⏰ **时间范围**: 过去 24 小时
📊 **监控仓库数**: 8
📋 **总计**: 36 Issues, 0 Pull Requests

## 📑 目录

- [Apache Fluss](#apache-fluss) - 8 Issues, 0 PRs
- [Apache Flink](#apache-flink) - 0 Issues, 0 PRs
- [Apache Spark](#apache-spark) - 0 Issues, 0 PRs
- [Apache Iceberg](#apache-iceberg) - 14 Issues, 0 PRs
- [Apache Paimon](#apache-paimon) - 4 Issues, 0 PRs
- [Lance](#lance) - 3 Issues, 0 PRs
- [LanceDB](#lancedb) - 2 Issues, 0 PRs
- [Daft](#daft) - 5 Issues, 0 PRs

---

## Apache Fluss

> 仓库: https://github.com/apache/fluss

### 📋 Issues (8)
#### 🔴 [[Fluss fails to drop underlying paimon tables]](https://github.com/apache/fluss/issues/2717)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 3小时前 |
| 👤 作者 | TakodaS |
| 🏷️ 状态 | OPEN

**核心内容**: Fluss 0.8.0 在删除启用了 datalake 的表后，重建同名表时报错，提示底层 Paimon 表已存在。这是 Fluss 未能正确删除底层 Paimon 表的 Bug。

#### 🔴 [[[lake/lance] Support Batch / Union Read query against Lance table]](https://github.com/apache/fluss/issues/2715)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 4小时前 |
| 👤 作者 | leekeiabstraction |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 请求为 Apache Fluss 中的 Lance 表实现 Batch / Union Read 查询功能。目前相关方法抛出未实现异常，通过实现 `LakeSource` 可支持从 Flink SQL 进行批量或联合读取。提交者表示愿意提交 PR。

#### 🔴 [[When enabled, JMX metrics reporter throws exception on startup]](https://github.com/apache/fluss/issues/2712)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 21小时前 |
| 👤 作者 | morazow |
| 🏷️ 状态 | OPEN

**核心内容**: 启用 JMX 指标报告器时，启动报错 `IllegalAccessError`。原因是 JMXServer$JmxRegistry 无法访问 `sun.rmi.registry.RegistryImpl`，因 `java.rmi` 模块未导出该包至未命名模块。

#### 🔴 [[[lake/lance] Lance writer should emit Arrow FixedSizeList for array columns to enable native vector search]](https://github.com/apache/fluss/issues/2706)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 3天前 |
| 👤 作者 | leekeiabstraction |
| 🏷️ 状态 | OPEN

**核心内容**: Fluss 在将 ARRAY<FLOAT> 列写入 Lance 时使用 Arrow 的变长 List，导致 Lance 原生向量搜索无法工作，因为 Lance 要求使用 FixedSizeSize。问题源于 LanceArrowUtils.toArrowType() 中 ArrayType 无条件映射为 ArrowType.List.INSTANCE。

#### 🔴 [[[docs] Lance Quickstart documentation with vector search example]](https://github.com/apache/fluss/issues/2705)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 3天前 |
| 👤 作者 | leekeiabstraction |
| 🏷️ 状态 | OPEN

**核心内容**: 请求添加 Lance Quickstart 文档，包含向量搜索示例，类似现有的 Paimon 和 Iceberg 文档。提交者表示愿意提交 PR。

#### 🟢 [[[helm] Enable pulling from private Docker registry]](https://github.com/apache/fluss/issues/2691)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 9天前 |
| 👤 作者 | affo |
| 🏷️ 状态 | CLOSED

**核心内容**: 该 Issue 指出 Helm Chart 的 `values.yaml` 中存在 `imagePullSecrets` 和 `image.registry`，但未在模板中实际使用。修复方案为在 StatefulSet 模板中渲染这两个配置，以支持从私有 Docker registry 拉取镜像。

#### 🔴 [[[helm] Enable metrics reporting on helm charts]](https://github.com/apache/fluss/issues/2677)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 12天前 |
| 👤 作者 | morazow |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 提议在 Helm Chart 部署中启用指标报告功能，允许用户开启指标抓取和上报。初步实现将基于 Helm 注解的 Prometheus 抓取方式。提交者表示愿意提交 PR。

#### 🔴 [[bufferAllocator of LogRecordReadContext will leak if oom when decompress data.]](https://github.com/apache/fluss/issues/2646)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 14天前 |
| 👤 作者 | loserwang1024 |
| 🏷️ 状态 | OPEN

**核心内容**: Fluss 0.8.0 中，LogRecordReadContext 的 bufferAllocator 在解压数据时若发生 OOM 会导致内存泄漏。该问题在 Flink connector 中引发 FetchException，影响数据扫描稳定性。

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

### 📋 Issues (14)
#### 🔴 [[AWS: S3SignerServlet should strip out more request headers for caching]](https://github.com/apache/iceberg/issues/15442)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 26分钟前 |
| 👤 作者 | steveloughran |
| 🏷️ 状态 | OPEN

**核心内容**: AWS S3SignerServlet 需要扩展请求头剥离列表（如 user-agent、referrer 等），并在签名时跟踪实际使用的请求头，以便准确判断缓存值是否可复用，避免因猜测错误导致请求被拒绝。

#### 🔴 [[Whitespace in string partition values causes Spark to return empty DataFrames and inconsistent results across engines]](https://github.com/apache/iceberg/issues/15427)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | khjoshi94 |
| 🏷️ 状态 | OPEN

**核心内容**: Apache Iceberg 表字符串分区值含空格时，Spark 过滤返回空结果，与 Athena 行为不一致。导致分区修剪错误、连接空结果及数据写入失败。期望 Iceberg 能标准化或校验分区值、提供警告或修剪选项，或至少在分区修剪消除所有文件时提示。当前无任何警告，影响数据正确性和可用性。

#### 🔴 [[IcebergSource on FlinkJob with Pause/Resume missed data]](https://github.com/apache/iceberg/issues/15418)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | randomdev2026 |
| 🏷️ 状态 | OPEN

**核心内容**: Flink Job 使用 IcebergSource 在暂停/恢复时丢失数据。Job1 写入 Iceberg 表，Job2 读取。当 Job2 停止期间若生成了多个 Parquet 文件，恢复后仅读取最新文件，导致中间数据丢失。配置使用 Iceberg 1.10.1、Flink 2.0.1，起始策略为 INCREMENTAL_FROM_LATEST_SNAPSHOT。

#### 🔴 [[AWS: S3SignerServlet should strip out more request headers for caching]](https://github.com/apache/iceberg/issues/15417)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | steveloughran |
| 🏷️ 状态 | OPEN

**核心内容**: 该请求建议改进 AWS S3SignerServlet，使其在签名时忽略更多请求头（如 user-agent 和 referer）。这些头部通常由 JVM 库或审计追踪生成，不参与签名可提高缓存请求的复用率，从而减少签名次数。目前仅排除 range 等少量头部。

#### 🔴 [[GCSFileIO - how to connection pooling - exploding number of TCP connections]](https://github.com/apache/iceberg/issues/15411)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2天前 |
| 👤 作者 | astronautas |
| 🏷️ 状态 | OPEN

**核心内容**: GCSFileIO 缺乏 TCP 连接池支持，导致连接数激增（如每 15 分钟产生数千个 TCP 连接），影响性能。请求改进连接池功能。

#### 🔴 [[Kafka Connect: CVE-2025-67721 in io.airlift:aircompressor 2.0.2]](https://github.com/apache/iceberg/issues/15378)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 5天前 |
| 👤 作者 | rmoff |
| 🏷️ 状态 | OPEN

**核心内容**: Kafka Connect 运行时包含的 `io.airlift:aircompressor:2.0.2` 存在 CVE-2025-67721 高危漏洞。该漏洞源于 Snappy 和 LZ4 解压器对恶意数据处理不当，可能导致缓冲区内容泄露。上游修复 PR 目前未合并，且无法直接升级至 v3 版本。此漏洞已导致连接器发布受阻。

#### 🔴 [[How Flink TableMaintenance work with the parallelism]](https://github.com/apache/iceberg/issues/15292)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 14天前 |
| 👤 作者 | zncleon |
| 🏷️ 状态 | OPEN

**核心内容**: 用户询问 Flink Table Maintenance 在流模式下，设置并行度为 8 并使用 `maxFileGroupSizeBytes` 分组时，为何文件组是串行处理而非并发执行。用户期望不同文件组在不同 Slot 上并发运行，但实际观察到是按顺序提交。用户质疑这是否为正常行为或存在误解。

#### 🔴 [[Exception when using DELETE FROM Spark query on table using copy-on-write]](https://github.com/apache/iceberg/issues/14239)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 145天前 |
| 👤 作者 | npennequin |
| 🏷️ 状态 | OPEN

**核心内容**: 在 Apache Iceberg 1.10.0 中，使用 Spark 对 `copy-on-write` 模式的表执行 `DELETE FROM` 查询时，会在数据重写阶段抛出 `IllegalStateException` 异常，提示类型错误。而在 `merge-on-read` 模式下该查询正常工作。

#### 🔴 [[In Iceberg catalog, JdbcTableOperations should catch and handle PostgresSQL's exception for duplicated keys]](https://github.com/apache/iceberg/issues/13924)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 182天前 |
| 👤 作者 | sqd |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 指出 Apache Iceberg 1.9.2 在通过 JDBC Catalog 创建表时，`JdbcTableOperations` 仅捕获了标准的唯一键冲突异常，未能处理 PostgreSQL 抛出的特定异常（`PSQLException`）。当表已存在时，这会导致操作失败而非正确处理重复键错误。建议修改代码以捕获并处理 PostgreSQL 的该异常。

#### 🔴 [[ExposeLocality parameter in Flink]](https://github.com/apache/iceberg/issues/13919)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 184天前 |
| 👤 作者 | Guosmilesmile |
| 🏷️ 状态 | OPEN

**核心内容**: 用户询问 Flink Iceberg 源中的 `exposeLocality` 参数是否仍有效，因为在 `FlinkInputSplit` 中未发现调用 `getHostnames()` 的地方，质疑该配置是否起作用。请求开发者确认是否遗漏了相关信息。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## Apache Paimon

> 仓库: https://github.com/apache/paimon

### 📋 Issues (4)
#### 🔴 [[[Bug] [fs] Add missing s3-transfer-manager dependency for AWS SDK]](https://github.com/apache/paimon/issues/7303)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 3小时前 |
| 👤 作者 | juntaozhang |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 报告了 Apache Paimon 在使用 Spark 连接 S3 时出现 `NoClassDefFoundError`，提示缺少 `software/amazon/awssdk/transfer/s3/model/ObjectTransfer` 类。问题原因是 AWS SDK 的 `s3-transfer-manager` 依赖缺失。PR 提议添加该缺失依赖以修复 S3 文件系统初始化错误。

#### 🟢 [[[Bug] Fix ChainSplit NPE after branch table cache invalidation]](https://github.com/apache/paimon/issues/7299)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 11小时前 |
| 👤 作者 | juntaozhang |
| 🏷️ 状态 | CLOSED

**核心内容**: 修复分支表缓存失效后 ChainSplit NPE 问题。在 Paimon 主版本使用 Spark 3.5 时，创建链表分支并设置回退属性后出现空指针异常。该 PR 旨在解决此崩溃。

#### 🔴 [[[Feature] [python] Streaming Read Support in paimon-python]](https://github.com/apache/paimon/issues/7152)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 26天前 |
| 👤 作者 | tub |
| 🏷️ 状态 | OPEN

**核心内容**: 该提议为 paimon-python 添加流式读取支持，引入基于 asyncio 的流式消费者和消费注册功能。方案包括 StreamReadBuilder、AsyncStreamingTableScan 等核心组件，支持增量快照扫描和消费进度管理，旨在简化 Python 流式数据管道构建。

#### 🔴 [[[Bug] In cdc database synchronization, data changes to new tables using the combined mode are not monitored, and the job needs to be restarted]](https://github.com/apache/paimon/issues/3511)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 622天前 |
| 👤 作者 | dsanww |
| 🏷️ 状态 | OPEN

**核心内容**: 在 Paimon 的 CDC 数据库同步中，使用 combined 模式时，新表的数据变更无法被监控，需要重启作业才能生效。用户期望能动态监听新表的 binlog 而无需重启作业。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## Lance

> 仓库: https://github.com/lance-format/lance

### 📋 Issues (3)
#### 🟢 [[Panic decoding primitive miniblock dictionary page (2.0.1): unreachable in primitive.rs:1305]](https://github.com/lance-format/lance/issues/5994)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | kszlim |
| 🏷️ 状态 | CLOSED

**核心内容**: lance==2.0.1 在解码原始时间戳列时可能触发 panic，当元数据强制使用 `structural-encoding=miniblock`` 和 `compression=zstd` 组时。panic 发生在 `primitive.rs:1305`，提示不可达的字典编码压缩类型。预期应成功解码或优雅报错，而非崩溃。设置环境变量 `LANCE_ENCODING_DICT_TOO_SMALL` 可规避该问题。

#### 🔴 [[Epic: from shallow_clone to branch]](https://github.com/lance-format/lance/issues/4853)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 148天前 |
| 👤 作者 | majin1102 |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Epic 记录了 Lance 从 shallow_clone 到 branch 的演进。Branch 是基于 shallow_clone 的机制，增加了分支元数据并实现了全局文件生命周期管理。范围包括在 Java 和 Python 运行时中交付分支功能，确保 shallow_clone 支持片段操作和索引，并实现跨分支文件管理。内容列出了 shallow clone 和 branch 相关的实现及 PR 清单。

#### 🔴 [[Can't use JSON fields with merge_insert]](https://github.com/lance-format/lance/issues/4831)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 150天前 |
| 👤 作者 | ztorchan |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 指出在 `merge_insert` 操作中，`FullSchemaMergeInsertExec::prepare_stream_schema` 未将数据列字段的元数据复制到输出架构，导致元数据丢失。这会在数据集包含 JSON 列时引发错误，提示尝试以不同类型投影字段。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## LanceDB

> 仓库: https://github.com/lancedb/lancedb

### 📋 Issues (2)
#### 🔴 [[bug(python): Compaction failed with "Row ids did not arrive in sorted order: integers are ordered up to the 0th element, /rustc/9fc6b43126469e3858e2fe86cafb4f0fd5068869/library/core/src/task/poll.rs:290:44"]](https://github.com/lancedb/lancedb/issues/3063)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | edwin-jsi |
| 🏷️ 状态 | OPEN

**核心内容**: LanceDB 0.18 版本在包含 250 万行数据的表上执行压缩操作时失败，错误提示“Row ids did not arrive in sorted order”。该表使用 merge_insert 添加记录，并按 compact_files、optimize_indices、cleanup_old_versions 顺序进行优化。错误堆栈指向 Rust 代码，疑似与 lance-format/lance 的已知问题相关。

#### 🟢 [[Rust - support Expr in filter]](https://github.com/lancedb/lancedb/issues/3038)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 7天前 |
| 👤 作者 | wjones127 |
| 🏷️ 状态 | CLOSED

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## Daft

> 仓库: https://github.com/Eventual-Inc/Daft

### 📋 Issues (5)
#### 🔴 [[Support reading and writing LeRobot format datasets]](https://github.com/Eventual-Inc/Daft/issues/6296)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1小时前 |
| 👤 作者 | plotor |
| 🏷️ 状态 | OPEN

**核心内容**: 为支持具身智能行业的用户，请求在 Daft 中添加读取和写入 LeRobot 格式数据集的功能，以方便用户使用 Daft 处理数据。该功能目前处于积极设计阶段，且请求者愿意实现该功能。

#### 🔴 [[Connection errors when reading multiple parquet files from Azure]](https://github.com/Eventual-Inc/Daft/issues/6279)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2天前 |
| 👤 作者 | gsmit |
| 🏷️ 状态 | OPEN

**核心内容**: Daft 从 Azure 读取 7+ 个 Parquet 文件时因同时打开过多连接导致 Socket 错误崩溃。限制并行度（scantask_max_parallel=1）可解决此问题。

#### 🟢 [[fix(docs): Remove duplicate Voice AI analytics listing in the SUMMARY.md file for examples]](https://github.com/Eventual-Inc/Daft/issues/6273)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 3天前 |
| 👤 作者 | everettVT |
| 🏷️ 状态 | CLOSED

**核心内容**: 修复 SUMMARY.md 中 Voice AI analytics 示例的重复列表项，确保示例仅显示一次。

#### 🟢 [[Hash rows of dataframe]](https://github.com/Eventual-Inc/Daft/issues/4390)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 280天前 |
| 👤 作者 | colin-ho |
| 🏷️ 状态 | CLOSED

**核心内容**: 请求为 Daft DataFrame 添加按行生成哈希值的功能，支持类似 Spark 的 `df.with_column('hash', daft.functions.hash("*"))` 语法。当前实现仅支持单列哈希，需先拼接列再哈希，不直观且性能低。底层已有必要内核，需实现 API 并允许 HashFunction 接受多输入。

#### 🔴 [[`read_text` and `read_blob` functions]](https://github.com/Eventual-Inc/Daft/issues/2859)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 523天前 |
| 👤 作者 | universalmind303 |
| 🏷️ 状态 | OPEN

**核心内容**: 请求添加类似 DuckDB 的 `read_text` 和 `read_blob` 函数，用于读取非表格格式文件（如 `.txt` 文件）。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

