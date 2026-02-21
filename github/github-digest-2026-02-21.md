# GitHub 每日摘要

📅 **生成时间**: 2026-02-21 23:41:54
⏰ **时间范围**: 过去 24 小时
📊 **监控仓库数**: 8
📋 **总计**: 17 Issues, 0 Pull Requests

## 📑 目录

- [Apache Fluss](#apache-fluss) - 1 Issues, 0 PRs
- [Apache Flink](#apache-flink) - 0 Issues, 0 PRs
- [Apache Spark](#apache-spark) - 2 Issues, 0 PRs
- [Apache Iceberg](#apache-iceberg) - 5 Issues, 0 PRs
- [Apache Paimon](#apache-paimon) - 0 Issues, 0 PRs
- [Lance](#lance) - 6 Issues, 0 PRs
- [LanceDB](#lancedb) - 3 Issues, 0 PRs
- [Daft](#daft) - 0 Issues, 0 PRs

---

## Apache Fluss

> 仓库: https://github.com/apache/fluss

### 📋 Issues (1)
#### 🔴 [[[test] Unstable test FlinkUnionReadLogTableITCase.testReadLogTableInStreamMode]](https://github.com/apache/fluss/issues/2580)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 16天前 |
| 👤 作者 | wuchong |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 报告 Fluss 项目中测试用例 `FlinkUnionReadLogTableITCase.testReadLogTableInStreamMode` 存在不稳定性问题。测试失败原因为 `AssertionError: bucket TableBucket{tableId=8, partitionId=9, bucket=0} not synced`，表明在等待存储桶同步时超时。

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

### 📋 Issues (2)
#### 🔴 [[Suggestion: reference WFGY Problem Map (RAG / LLM debugging checklist) for Spark + LLM workloads]](https://github.com/apache/spark/issues/54415)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 11分钟前 |
| 👤 作者 | onestardao |
| 🏷️ 状态 | OPEN

**核心内容**: 建议在 Spark 文档中引用 WFGY Problem Map（RAG/LLM 调试检查清单）。该项目提供 16 个常见失败模式，帮助用户调试大规模数据摄取、分块和索引问题。Spark 常用于生成嵌入和检索语料库，该清单能发现 Spark 作业看似正常但检索系统失败的问题，适用于 Python/Scala 等多语言场景。

#### 🔴 [[[TEST] `test_session.py` does not work properly]](https://github.com/apache/spark/issues/54405)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 17小时前 |
| 👤 作者 | gaogaotiantian |
| 🏷️ 状态 | OPEN

**核心内容**: `test_session.py` 测试卡住且未在 CI 执行，因 `session.stop()` 无服务器会失败，且 `_get_default_session()` 无法正确获取当前会话。测试整体失败且修复不易，需原作者检查测试逻辑并确保通过。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## Apache Iceberg

> 仓库: https://github.com/apache/iceberg

### 📋 Issues (5)
#### 🟢 [[Support merge-on-read tables in changelog scans]](https://github.com/apache/iceberg/issues/15394)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1小时前 |
| 👤 作者 | lawofcycles |
| 🏷️ 状态 | CLOSED

**核心内容**: 该Issue提议优化v3表的changelog扫描，利用row lineage的`_last_updated_sequence_number`和`_row_id`字段，避免全量数据文件读取和删除文件合并，从而提升效率。此优化建立在#10935删除文件支持的基础上，仅针对v3表，且仍需保留常规删除文件合并路径作为回退。

#### 🔴 [[Kafka Connect: `iceberg.tables.schema-case-insensitive` config is ignored when name mapping is present]](https://github.com/apache/iceberg/issues/15392)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 4小时前 |
| 👤 作者 | annurahar |
| 🏷️ 状态 | OPEN

**核心内容**: Kafka Connect 在同时配置 `schema.name-mapping.default` 和 `iceberg.tables.schema-case-insensitive=true` 时，忽略大小写不敏感设置。导致字段名仅大小写不同的记录无法匹配现有列。根本原因是 `RecordConverter.java` 在存在名称映射时未应用大小写不敏感逻辑。期望无论是否启用名称映射，字段查找都应遵循大小写不敏感配置。

#### 🔴 [[Expose Transaction#abortTransaction() API for clean up ]](https://github.com/apache/iceberg/issues/15377)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | deniskuzZ |
| 🏷️ 状态 | OPEN

**核心内容**: 该请求建议公开 `Transaction#abortTransaction()` API 以支持多表事务并复用 `BaseTransaction`。该功能针对 Hive 查询引擎，旨在改进事务清理机制。提交者表示可独立贡献此改进。

#### 🔴 [[Core: Static thread pools in ThreadPools.java cause ClassLoader leaks in hot-reload scenarios]](https://github.com/apache/iceberg/issues/15031)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 40天前 |
| 👤 作者 | QiuYucheng2003 |
| 🏷️ 状态 | OPEN

**核心内容**: `ThreadPools.java` 中的静态线程池在热重载场景下导致 ClassLoader 泄漏。这些线程池无法在应用卸载时显式关闭，线程保留对 ClassLoader 的引用，阻止垃圾回收，最终引发 Metaspace 内存溢出。

#### 🔴 [[Max Inferred columns should consider Sort order columns first]](https://github.com/apache/iceberg/issues/13914)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 181天前 |
| 👤 作者 | manirajv06 |
| 🏷️ 状态 | OPEN

**核心内容**: 当排序顺序列数超过 `max-inferred-column-defaults` 时，指标生成未优先考虑排序列，导致实际生成的列数超过限制。建议优先选择排序顺序列，若排序列数超过限制，则忽略多余的排序列，以确保指标生成的优先级正确。

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

### 📋 Issues (6)
#### 🔴 [[Java - create fragment with a new schema]](https://github.com/lance-format/lance/issues/5972)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 16小时前 |
| 👤 作者 | jackye1995 |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 提出在 Java 中需要支持使用新 Schema 创建 Fragment，以实现具有不同 Schema 的 REPLACE TABLE AS SELECT 操作。相关工作涉及 lance-spark 和 lance 项目的相关 PR。

#### 🔴 [[Allow the part files to be skipped when training FTS]](https://github.com/lance-format/lance/issues/5970)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 21小时前 |
| 👤 作者 | westonpace |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 提议优化 FTS 索引构建流程。通过将分词与最终索引构建交错进行，利用共享通道将数据直接发送至写入线程，从而跳过中间磁盘写入步骤。此举可显著减少构建时间和临时磁盘空间占用，代价是可能增加内存消耗，但可通过限制通道大小加以控制。

#### 🔴 [[Java - support commit transaction to create a new table]](https://github.com/lance-format/lance/issues/5969)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 21小时前 |
| 👤 作者 | jackye1995 |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 指出在 Spark 中实现 CTAS（创建表并加载数据）时，必须先创建表再提交分片的流程成为了阻碍。这是 Java SDK 的限制，因为该功能已在 Rust 中实现。相关 PR 链接和 TODO 位于 `StagedCommit.java` 中，建议增加支持在提交事务时创建新表的功能。

#### 🔴 [[LabelListIndex: NOT filters mis-handle NULL lists (list-level NULLs)]](https://github.com/lance-format/lance/issues/5904)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 14天前 |
| 👤 作者 | fenfeng9 |
| 🏷️ 状态 | OPEN

**核心内容**: Lance 数据库中 `LabelListIndex` 在处理 `NOT` 过滤器时错误地包含了列表级别的 NULL 值。使用 `NOT array_has_any`、`NOT array_has_all` 或 `NOT array_contains`` 过滤时，实际结果错误地返回了 `None`，而预期结果应排除这些 NULL 值。

#### 🟢 [[Blob Encoding not working with Lance Java SDK]](https://github.com/lance-format/lance/issues/5167)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 107天前 |
| 👤 作者 | rahil-c |
| 🏷️ 状态 | CLOSED

**核心内容**: 用户反馈 Lance Java SDK 的 blob encoding 功能未按预期工作。尽管在写入时设置了 `"lance-encoding:blob": "true"`，但使用 `LanceFileReader` 读取时，二进制内容仍被完全物化，而非返回位置和大小的结构体。用户提供了单元测试复现该问题。

#### 🟢 [[Add docs for branch]](https://github.com/lance-format/lance/issues/5073)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 117天前 |
| 👤 作者 | majin1102 |
| 🏷️ 状态 | CLOSED

**核心内容**: 该请求建议更新文档以覆盖分支功能，具体涉及 README.md、docs/src/quickstart/versioning.md 和 docs/src/guide 三个部分。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## LanceDB

> 仓库: https://github.com/lancedb/lancedb

### 📋 Issues (3)
#### 🔴 [[Python: Expand test suite for minimal dependency test]](https://github.com/lancedb/lancedb/issues/3054)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 20小时前 |
| 👤 作者 | wjones127 |
| 🏷️ 状态 | OPEN

**核心内容**: 该 PR 提议扩展 Python 最小依赖测试的范围，使其运行大部分测试，而非仅限于当前有限的范围。同时，确保仅在真正需要的测试中使用 pandas，例如不应因缺少 pandas 而跳过与 pydantic 相关的测试。此举旨在更早发现类似 #3053 的问题。

#### 🔴 [[Import error in Python when using namespace]](https://github.com/lancedb/lancedb/issues/3053)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 20小时前 |
| 👤 作者 | wjones127 |
| 🏷️ 状态 | OPEN

**核心内容**: 使用命名空间时因缺少 `lance` 模块导致导入错误。LanceDB 和 lance_namespace 未显式依赖 `lance` 以保持包体积小，但当前代码仍需安装 `pylance` 才能运行。

#### 🔴 [[Improving throughput for add]](https://github.com/lancedb/lancedb/issues/3048)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2天前 |
| 👤 作者 | wjones127 |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 跟进 #3029，旨在提升 `add` 操作的吞吐量。核心任务包括：添加进度条、实现本地和远程并行写入、在 DataFusion 中调用嵌入函数、支持 Overwrite 模式下推断表结构、处理坏向量（Fill/Drop）、以及优化 DuckDB 和 `Polars LazyFrame` 的流式读取。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## Daft

> 仓库: https://github.com/Eventual-Inc/Daft

### 📋 Issues (0)
_过去 24 小时内没有新的 Issue_

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

