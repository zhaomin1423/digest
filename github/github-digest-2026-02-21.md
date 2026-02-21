# GitHub 每日摘要

📅 **生成时间**: 2026-02-21 23:38:13
⏰ **时间范围**: 过去 24 小时
📊 **监控仓库数**: 5
📋 **总计**: 8 Issues, 0 Pull Requests

## 📑 目录

- [Apache Fluss](#apache-fluss) - 1 Issues, 0 PRs
- [Apache Flink](#apache-flink) - 0 Issues, 0 PRs
- [Apache Spark](#apache-spark) - 2 Issues, 0 PRs
- [Apache Iceberg](#apache-iceberg) - 5 Issues, 0 PRs
- [Apache Paimon](#apache-paimon) - 0 Issues, 0 PRs

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

**核心内容**: 该 Issue 报告 Fluss 项目的测试用例 `FlinkUnionReadLogTableITCase.testReadLogTableInStreamMode` 不稳定。测试失败原因为断言错误：特定 bucket 未同步，导致测试在等待超时后失败。

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
| 📅 创建时间 | 8分钟前 |
| 👤 作者 | onestardao |
| 🏷️ 状态 | OPEN

**核心内容**: 建议在 Spark 文档中引用 WFGY Problem Map（一个 RAG/LLM 调试清单）。该项目包含 16 个常见故障模式，涵盖数据摄取、分块、索引和评估，特别适合 Spark 处理大规模 LLM 工作流时的调试。作者提议添加链接以帮助用户解决“Spark 任务正常但检索系统失败”等问题。

#### 🔴 [[[TEST] `test_session.py` does not work properly]](https://github.com/apache/spark/issues/54405)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 17小时前 |
| 👤 作者 | gaogaotiantian |
| 🏷️ 状态 | OPEN

**核心内容**: `test_session.py` 测试卡顿且失败，原因包括无法在没有服务器时调用 `session.stop()` 以及 `_get_default_session()` 无法正确获取会话。该测试缺少 `main()` 导致未在 CI 中执行。修复不易，需原作者介入确保测试逻辑正确并通过。

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

**核心内容**: 该 Issue 提议优化 v3 表的 changelog 扫描。在 #10935 支持删除文件的基础上，对于启用 row lineage 的 v3 表，建议利用 `_last_updated_sequence_number` 过滤变更行，使用 `_row_id` 匹配逻辑行，从而避免全量读取和删除文件合并，提升效率。

#### 🔴 [[Kafka Connect: `iceberg.tables.schema-case-insensitive` config is ignored when name mapping is present]](https://github.com/apache/iceberg/issues/15392)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 4小时前 |
| 👤 作者 | annurahar |
| 🏷️ 状态 | OPEN

**核心内容**: 在 Kafka Connect 中，当同时配置名称映射（`schema.name-mapping.default`）和不区分大小写模式（`iceberg.tables.schema-case-insensitive=true`）时，不区分大小写的设置被忽略。`RecordConverter.java` 在名称映射存在时字段查找未应用大小写逻辑，导致仅大小写不同的字段名（如 "II" 与 "ii"）无法匹配现有列。修复应在存在名称映射时也应用不区分大小写的逻辑。

#### 🔴 [[Expose Transaction#abortTransaction() API for clean up ]](https://github.com/apache/iceberg/issues/15377)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | deniskuzZ |
| 🏷️ 状态 | OPEN

**核心内容**: 该功能请求建议暴露 Transaction#abortTransaction() API，以便在多表事务支持中进行清理，并旨在重用 BaseTransaction。请求者表示愿意独立贡献此改进。

#### 🔴 [[Core: Static thread pools in ThreadPools.java cause ClassLoader leaks in hot-reload scenarios]](https://github.com/apache/iceberg/issues/15031)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 40天前 |
| 👤 作者 | QiuYucheng2003 |
| 🏷️ 状态 | OPEN

**核心内容**: Apache Iceberg 的 `ThreadPools` 类维护静态 `ExecutorService` 实例，这些线程池通过 JVM 关闭钩子终止，缺乏显式关闭机制。在热重载环境（如 Tomcat、Flink）中，静态线程池保持活跃并持有 `ClassLoader` 引用，导致 `ClassLoader` 无法被垃圾回收，引发内存泄漏和 `OutOfMemoryError: Metaspace`。

#### 🔴 [[Max Inferred columns should consider Sort order columns first]](https://github.com/apache/iceberg/issues/13914)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 181天前 |
| 👤 作者 | manirajv06 |
| 🏷️ 状态 | OPEN

**核心内容**: 当排序列数量超过 `max-inferred-column-defaults` 时，当前逻辑会优先选取 Schema 前几列，导致排序列被额外包含，超出限制。Issue 建议优先为排序列生成指标，再考虑剩余列；若排序列过多则忽略部分。

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

