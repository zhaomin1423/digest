# GitHub 每日摘要

📅 **生成时间**: 2026-03-07 22:02:27
⏰ **时间范围**: 过去 24 小时
📊 **监控仓库数**: 8
📋 **总计**: 24 Issues, 0 Pull Requests

## 📑 目录

- [Apache Fluss](#apache-fluss) - 5 Issues, 0 PRs
- [Apache Flink](#apache-flink) - 0 Issues, 0 PRs
- [Apache Spark](#apache-spark) - 3 Issues, 0 PRs
- [Apache Iceberg](#apache-iceberg) - 3 Issues, 0 PRs
- [Apache Paimon](#apache-paimon) - 3 Issues, 0 PRs
- [Lance](#lance) - 4 Issues, 0 PRs
- [LanceDB](#lancedb) - 1 Issues, 0 PRs
- [Daft](#daft) - 5 Issues, 0 PRs

---

## Apache Fluss

> 仓库: https://github.com/apache/fluss

### 📋 Issues (5)
#### 🔴 [[Add compression for CompactedRow]](https://github.com/apache/fluss/issues/2806)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | polyzos |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 提出为 Fluss 0.9 引入的 CompactedRow 格式添加压缩功能。目前 CompactedRow 相比 Arrow 格式缺少压缩支持，需补充以完善该功能。

#### 🔴 [[Support Complex Data Types on the Java Typed API]](https://github.com/apache/fluss/issues/2805)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | polyzos |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 请求在 Fluss Java Typed API 中增加对复杂数据类型的支持。Fluss 0.9 已引入复杂数据类型，但目前的 Java Typed API 尚未提供相应支持。

#### 🔴 [[[spark] Support streaming read with latest mode]](https://github.com/apache/fluss/issues/2553)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 32天前 |
| 👤 作者 | Yohahaha |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 是 Apache Fluss 项目中关于 Spark 连接器的子任务，旨在支持 Spark 流式读取的“latest”模式。

#### 🔴 [[[spark] Add streaming metrics]](https://github.com/apache/fluss/issues/2552)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 32天前 |
| 👤 作者 | Yohahaha |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 是 #2527 的子任务，旨在为 Spark 集成添加流式指标功能。

#### 🔴 [[[KV]  Support Full KV Scan for Primary Key Tables]](https://github.com/apache/fluss/issues/1600)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 191天前 |
| 👤 作者 | polyzos |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 提出 Fluss KV 目前仅支持点查询，而 RocksDB 支持迭代器、范围和前缀扫描。针对需要定期读取少量数据（如创建仪表盘）的场景，建议通过 API 暴露功能以支持全表扫描（快照一致性），简化此类用例。提交者愿意提交 PR。

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
#### 🔴 [[Spark map lookup is O(n)]](https://github.com/apache/spark/issues/54646)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | DanSkells |
| 🏷️ 状态 | OPEN

**核心内容**: 用户在 Spark 中对包含超过 100 万个元素的 Map 进行查找时遇到性能问题。经分析发现 Map 查询是线性扫描（O(n)），导致效率低下。用户希望优化此操作或寻找替代方案，其场景仅需插入和查找，无需删除。用户提到 Spark 内部的 OpenHashMap 实现，并愿与维护者合作解决。

#### 🔴 [[[FEATURE REQUEST] Add ADBC (Arrow Database Connectivity) Data Source]](https://github.com/apache/spark/issues/54603)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 3天前 |
| 👤 作者 | tokoko |
| 🏷️ 状态 | OPEN

**核心内容**: 该请求为 Spark 添加原生 ADBC (Arrow Database Connectivity) 数据源。ADBC 是基于 Arrow 的列式数据库连接标准，提供比 JDBC 更高效的分析性能。鉴于 Java 对 ADBC 的支持已成熟，且能与 Spark 的列式读取和外部加速器良好集成，提议者已提供概念验证代码，并愿意在社区感兴趣的情况下将其合并至 Spark 上游。

#### 🔴 [[[SQL] dropDuplicates and Window dedup produce incorrect results with SPJ partiallyClusteredDistribution]](https://github.com/apache/spark/issues/54378)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 16天前 |
| 👤 作者 | paryoja |
| 🏷️ 状态 | OPEN

**核心内容**: 在 Spark 4.0.1 中，启用 SPJ 和 `partiallyClusteredDistribution` 时，`dropDuplicates` 和 Window 去重产生错误结果。根本原因是部分聚簇将同一分区拆分到不同任务，而去重操作依赖所有相同键在同一任务中。由于 SPJ 移除了 Exchange，各任务独立去重导致跨任务的重复键未被移除。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## Apache Iceberg

> 仓库: https://github.com/apache/iceberg

### 📋 Issues (3)
#### 🔴 [[AnalysisException: [UNRESOLVED_COLUMN] during MERGE INTO on wide Iceberg tables (400+ columns) in Spark 3.5]](https://github.com/apache/iceberg/issues/15526)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 16小时前 |
| 👤 作者 | NataliaLaurova |
| 🏷️ 状态 | OPEN

**核心内容**: 在 Spark 3.5 中，对包含约 450 列的 Iceberg 表执行 `MERGE INTO` 操作时，分析阶段抛出 `UNRESOLVED_COLUMN` 异常，尽管错误提示中包含该列名。该问题仅在宽表（400+ 列）和 SQL 语法下出现，小表或使用 DataFrame API（Join + Overwrite）可正常工作，推测与 Spark Catalyst 优化器解析逻辑计划有关。

#### 🔴 [[Strict metrics evaluation for `startsWith` predicate]](https://github.com/apache/iceberg/issues/14016)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 180天前 |
| 👤 作者 | smaheshwar-pltr |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 请求为 `startsWith` 谓词实现严格指标评估。当边界范围都匹配前缀（如 `["xa", "xz"]` 匹配 `startsWith("x")`）时，确定所有行均匹配。其语义与 `notStartsWith` 的包含指标评估对称。Issue 跟踪了 PR #14014 中提出的 TODO。

#### 🟢 [[kafka-connect auto-create not setting identifier-field-ids]](https://github.com/apache/iceberg/issues/13623)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 228天前 |
| 👤 作者 | rlokugamage |
| 🏷️ 状态 | CLOSED

**核心内容**: 在 Apache Iceberg 1.9.2 版本中，使用 Kafka Connect 插件自动创建表时，尽管配置了 `iceberg.tables.default-id-columns`，但未在 Schema 中设置 `identifier-field-ids` 属性。这导致连接器无法正确识别标识字段，从而重复写入消息。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## Apache Paimon

> 仓库: https://github.com/apache/paimon

### 📋 Issues (3)
#### 🟢 [[[Bug] Allow "IF NOT EXISTS" check on branches]](https://github.com/apache/paimon/issues/7277)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 22天前 |
| 👤 作者 | emalit |
| 🏷️ 状态 | CLOSED

**核心内容**: Paimon 在 Flink 作业中创建分支时，若分支已存在会导致作业重启失败。建议为分支创建操作添加类似 `IF NOT EXISTS` 的检查机制，以避免重复创建分支引发的错误，支持作业幂等性重跑。

#### 🔴 [[[Feature] [python] Streaming Read Support in paimon-python]](https://github.com/apache/paimon/issues/7152)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 36天前 |
| 👤 作者 | tub |
| 🏷️ 状态 | OPEN

**核心内容**: 该提案为 paimon-python 增加流式读取支持，解决目前仅支持批读取需手动轮询快照的问题。方案引入基于 asyncio 的流式消费者及注册机制，核心包含 StreamReadBuilder、AsyncStreamingTableScan 等组件，通过 ConsumerManager 管理消费进度，旨在简化 Python 流式数据管道构建。

#### 🟢 [[[Bug] Too much connection when using HiveCatalog]](https://github.com/apache/paimon/issues/6719)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 96天前 |
| 👤 作者 | Aitozi |
| 🏷️ 状态 | CLOSED

**核心内容**: Bug报告：使用HiveCatalog时连接过多。SnapshotLoader默认加载并初始化HiveCatalog等catalog，应将初始化改为懒加载以减少连接数。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## Lance

> 仓库: https://github.com/lance-format/lance

### 📋 Issues (4)
#### 🔴 [[Automatic cleanup of transaction files on failure]](https://github.com/lance-format/lance/issues/6125)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 8小时前 |
| 👤 作者 | wjones127 |
| 🏷️ 状态 | OPEN

**核心内容**: 提议在事务失败时自动清理不再需要的事务文件。

#### 🔴 [[Automatic cleanup of data files on failed writes]](https://github.com/lance-format/lance/issues/6124)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 8小时前 |
| 👤 作者 | wjones127 |
| 🏷️ 状态 | OPEN

**核心内容**: 写入失败（如追加操作）时应立即删除已写入的数据文件。虽然垃圾回收最终会清理，但立即进行尽力而为的清理更佳。

#### 🔴 [[Automatic cleanup of indexes on failed builds]](https://github.com/lance-format/lance/issues/6123)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 9小时前 |
| 👤 作者 | wjones127 |
| 🏷️ 状态 | OPEN

**核心内容**: 构建索引时应追踪创建的文件。若构建失败，需清理这些文件以便重试。此需求也关联了 PR #6011。

#### 🔴 [[[bug] `optimize_indices` can drop valid BTree entries when stable row IDs are enabled]](https://github.com/lance-format/lance/issues/6116)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 23小时前 |
| 👤 作者 | acking-you |
| 🏷️ 状态 | OPEN

**核心内容**: 开启 `enable_stable_row_ids` 并使用 BTree 索引时，执行 `compact_files()` 和 `optimize_indices()` 会导致索引丢失有效数据，全扫正常但索引查询无结果。问题在于 `optimize_indices` 合并索引时，错误地使用 `row_id >> 32` 推断 Fragment ID 来过滤旧行，此逻辑仅适用于地址式 Row ID，不兼容稳定 Row ID。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## LanceDB

> 仓库: https://github.com/lancedb/lancedb

### 📋 Issues (1)
#### 🔴 [[Feedback on CRUD patterns with S3+DDB: storage growth vs. "Too many concurrent writers" on delete]](https://github.com/lancedb/lancedb/issues/3086)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 5天前 |
| 👤 作者 | Erry91 |
| 🏷️ 状态 | OPEN

**核心内容**: 用户在 AWS S3+DynamoDB 环境下使用 LanceDB v0.25.1，发现单条记录频繁增删导致存储增长。通过在更新后执行 `cleanup_old_versions` 和 `compact_files` 解决了存储问题，但随即引发 `delete` 操作报错“Too many concurrent writers”。用户寻求关于这种 CRUD 模式的建议，以平衡存储控制与并发写入冲突。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## Daft

> 仓库: https://github.com/Eventual-Inc/Daft

### 📋 Issues (5)
#### 🟢 [[fix(video): Missing pillow dependency causes confusing 'concat' error on Python 3.12]](https://github.com/Eventual-Inc/Daft/issues/6064)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 46天前 |
| 👤 作者 | everettVT |
| 🏷️ 状态 | CLOSED

**核心内容**: 该 Issue 修复了 Python 3.12 中因缺少 Pillow 依赖导致 `video_keyframes()` 报错“Need at least 1 series to perform concat”的问题。根本原因是 `video` extra 未包含 Pillow 依赖，且 `VideoFile.keyframes()` 未检查 PIL 可用性。修复方法是在 `pyproject.toml` 中添加 Pillow 依赖，并在代码中添加依赖检查。

#### 🟢 [[Public interface for custom Catalog implementations]](https://github.com/Eventual-Inc/Daft/issues/6001)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 56天前 |
| 👤 作者 | jakajancar |
| 🏷️ 状态 | CLOSED

**核心内容**: 请求将自定义 Catalog 实现公开为公共 API，以便更高效地通过 SQL 暴露大量目录，避免使用 `from_pydict` 时的性能问题。用户指出实现自定义 Catalog 很容易，但目前不是公共接口，并希望将其正式化。

#### 🔴 [[Maintain fields order in from_pylist function]](https://github.com/Eventual-Inc/Daft/issues/4591)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 256天前 |
| 👤 作者 | rchowell |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 请求在 `from_pylist` 函数中保持字段的顺序，并关联了 PR #2838。用户表示不希望自行实现修复。

#### 🟢 [[Field name use `Arc<str>` instead of `String`]](https://github.com/Eventual-Inc/Daft/issues/2892)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 529天前 |
| 👤 作者 | andrewgazelka |
| 🏷️ 状态 | CLOSED

**核心内容**: 该 Issue 提议将 `Field` 的名称类型从 `String` 改为 `Arc<str>`，以降低克隆开销。考虑到 `Metadata` 已使用 `Arc`，作者认为此举合理但不确定，请求验证。

#### 🟢 [[Create Join Explainer in Docs]](https://github.com/Eventual-Inc/Daft/issues/2690)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 564天前 |
| 👤 作者 | kevinzwang |
| 🏷️ 状态 | CLOSED

**核心内容**: 该 Issue 提议在文档中创建一个 Join 解释页面，以阐述 Join 行为的复杂性。内容需涵盖 Join 类型及其功能、连接键合并与右列重命名行为，以及 Join 策略和性能优化等高级话题。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

