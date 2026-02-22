# GitHub 每日摘要

📅 **生成时间**: 2026-02-22 22:01:45
⏰ **时间范围**: 过去 24 小时
📊 **监控仓库数**: 8
📋 **总计**: 13 Issues, 0 Pull Requests

## 📑 目录

- [Apache Fluss](#apache-fluss) - 2 Issues, 0 PRs
- [Apache Flink](#apache-flink) - 0 Issues, 0 PRs
- [Apache Spark](#apache-spark) - 3 Issues, 0 PRs
- [Apache Iceberg](#apache-iceberg) - 5 Issues, 0 PRs
- [Apache Paimon](#apache-paimon) - 0 Issues, 0 PRs
- [Lance](#lance) - 1 Issues, 0 PRs
- [LanceDB](#lancedb) - 1 Issues, 0 PRs
- [Daft](#daft) - 1 Issues, 0 PRs

---

## Apache Fluss

> 仓库: https://github.com/apache/fluss

### 📋 Issues (2)
#### 🔴 [[Lance writer should emit Arrow FixedSizeList for array columns to enable native vector search]](https://github.com/apache/fluss/issues/2706)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 15小时前 |
| 👤 作者 | leekeiabstraction |
| 🏷️ 状态 | OPEN

**核心内容**: Fluss 在将 ARRAY<FLOAT> 列写入 Lance 时，始终使用 Arrow 的可变长度 List<Float32>，导致 Lance 原生向量搜索无法工作（需 FixedSizeList<Float32>(n)）。问题源于 LanceArrowUtils.toArrowType() 中 ArrayType 无条件映射为 ArrowType.List.INSTANCE。

#### 🔴 [[Lance Quickstart documentation with vector search example]](https://github.com/apache/fluss/issues/2705)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 15小时前 |
| 👤 作者 | leekeiabstraction |
| 🏷️ 状态 | OPEN

**核心内容**: 提议为 Lance 添加 Quickstart 文档，参考现有的 Paimon 和 Iceberg 文档，并提供向量搜索示例。提交者表示愿意提交 PR。

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

### 📋 Issues (3)
#### 🔴 [[Catalyst optimizer non-convergence with iterative withColumn rewrite + filter pushdown in Spark]](https://github.com/apache/spark/issues/54419)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1小时前 |
| 👤 作者 | pravin-thangaraj-13731 |
| 🏷️ 状态 | OPEN

**核心内容**: Spark 4.0.0 在处理大量链式 `withColumn` 操作（如 30+ 次正则替换）时，逻辑计划呈指数级增长，导致 Driver OOM。问题根源在于优化器中的 `PushDownPredicates` 规则，特别是 `PushPredicateThroughNonJoin` 在处理深层嵌套的 Project 节点时，通过 `replaceAlias` 进行转换，触发了非收敛的迭代重写。

#### 🔴 [[[PYTHON] Support path-based table reference in `DataFrame.mergeInto`]](https://github.com/apache/spark/issues/54418)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 4小时前 |
| 👤 作者 | keen85 |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 请求在 PySpark 的 `DataFrame.mergeInto` API 中增加对基于路径（如 S3、本地路径）的表引用支持，而不仅限于已注册在 Catalog 中的表名。此举旨在避免 Catalog 开销并简化数据管道操作。提议通过自动检测字符串格式或增加可选参数来实现。

#### 🔴 [[Suggestion: reference WFGY Problem Map (RAG / LLM debugging checklist) for Spark + LLM workloads]](https://github.com/apache/spark/issues/54415)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 22小时前 |
| 👤 作者 | onestardao |
| 🏷️ 状态 | OPEN

**核心内容**: 建议 Spark 文档引用 WFGY Problem Map（一个 RAG/LLM 调试检查清单）。该项目涵盖 16 种常见故障模式，有助于诊断大规模数据处理（如数据摄取、分块、索引）中 Spark 作业看似正常但检索失败的问题。作者提议在文档或相关资源中添加链接，以辅助结合 Spark 与 LLM 的用户进行调试。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## Apache Iceberg

> 仓库: https://github.com/apache/iceberg

### 📋 Issues (5)
#### 🔴 [[Kafka Connect: Does not evolve schema for nested fields inside struct/list/map of structs]](https://github.com/apache/iceberg/issues/15395)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 19小时前 |
| 👤 作者 | annurahar |
| 🏷️ 状态 | OPEN

**核心内容**: 在 Apache Iceberg Kafka Connect 中，启用 `evolve-schema-enabled` 时，嵌套在 `struct`、`list<struct>` 或 `map<string, struct>` 内的字段无法进行模式演进。新增或更新的嵌套列会被静默忽略，未添加或更新到 Iceberg 表模式中。

#### 🟢 [[Support merge-on-read tables in changelog scans]](https://github.com/apache/iceberg/issues/15394)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 23小时前 |
| 👤 作者 | lawofcycles |
| 🏷️ 状态 | CLOSED

**核心内容**: 该 Issue 提出在 #10935 增加 changelog scan 对 merge-on-read 表的删除支持基础上，针对 v3 表的 row lineage 特性进行优化。通过利用 `_last_updated_sequence_number` 过滤变更行和 `_row_id` 匹配逻辑行，避免全量读取数据文件和合并删除文件，从而提高效率。仍需保留通用删除文件合并作为回退方案。

#### 🔴 [[Massive TIME_WAIT socket exhaustion during metadata (manifest/avro) reads with S3FileIO + Apache HTTP client]](https://github.com/apache/iceberg/issues/14951)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 51天前 |
| 👤 作者 | Sbaia |
| 🏷️ 状态 | OPEN

**核心内容**: 在Iceberg 1.10.0中，使用S3FileIO和Apache HTTP客户端时，执行维护操作（如rewrite_data_files）导致大量TIME_WAIT状态套接字耗尽。问题主要发生在读取元数据（manifest/avro）而非数据文件时，即使启用了连接池。配置中最大连接数为200，但实际连接数达40k-45k，导致内核临时端口耗尽，影响作业稳定性。

#### 🟢 [[Spark's TimeStamp dataType being written as TimeStampMicroTZVector and read as BigIntVector]](https://github.com/apache/iceberg/issues/14046)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 164天前 |
| 👤 作者 | sapienza88 |
| 🏷️ 状态 | CLOSED

**核心内容**: Spark 3.4.2 写入 Iceberg 时间戳列时出现类型转换错误。问题由配置 `spark.sql.parquet.outputTimestampType` 为 `TIMESTAMP_MILLIS` 触发，导致数据被写入为 `TimeStampMicroTZVector`，但读取时尝试转换为 `BigIntVector`，引发 `ClassCastException`。

#### 🔴 [[[Proposal] Add new delete feature: Delete with RowId]](https://github.com/apache/iceberg/issues/13918)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 181天前 |
| 👤 作者 | colinmjj |
| 🏷️ 状态 | OPEN

**核心内容**: 该提案建议在 Iceberg 中新增基于 RowId 的删除功能。动机是支持基于 Spark + Iceberg 的增量物化视图 CDC。目前的位置删除无法直接获取 CDC 信息，需依赖变更日志。RowId 是 V3 格式中每行的唯一键，若能用于标记删除行，将更方便地获取删除的 CDC 信息。

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
#### 🔴 [[Support merges that have null values for some numeric data (int64, float64, etc...)]](https://github.com/lance-format/lance/issues/1214)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 901天前 |
| 👤 作者 | JSpenced |
| 🏷️ 状态 | OPEN

**核心内容**: 用户在合并部分数据时遇到错误，提示 Lance 尚不支持 Int32 等数值类型的 Null 值。Issue 请求 Lance 支持数值类型（如 int64、float64）的 Null 值，以便在合并数据时能正确处理缺失字段。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## LanceDB

> 仓库: https://github.com/lancedb/lancedb

### 📋 Issues (1)
#### 🔴 [[Feature:]](https://github.com/lancedb/lancedb/issues/3004)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 13天前 |
| 👤 作者 | jcbraz |
| 🏷️ 状态 | OPEN

**核心内容**: 用户询问 LanceDB 是否计划支持 SQL 数据转换工具（如 dbt 或 sqlmash），以实现 ELT 类工作负载，特别是元数据转换。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## Daft

> 仓库: https://github.com/Eventual-Inc/Daft

### 📋 Issues (1)
#### 🔴 [[fix(docs): Remove duplicate Voice AI analytics listing in the SUMMARY.md file for examples]](https://github.com/Eventual-Inc/Daft/issues/6273)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 15小时前 |
| 👤 作者 | everettVT |
| 🏷️ 状态 | OPEN

**核心内容**: 修复了 SUMMARY.md 文件中 Voice AI analytics 示例重复列出的问题，确保示例仅显示一次。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

