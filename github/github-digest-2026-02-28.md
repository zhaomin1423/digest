# GitHub 每日摘要

📅 **生成时间**: 2026-02-28 22:03:06
⏰ **时间范围**: 过去 24 小时
📊 **监控仓库数**: 8
📋 **总计**: 24 Issues, 0 Pull Requests

## 📑 目录

- [Apache Fluss](#apache-fluss) - 11 Issues, 0 PRs
- [Apache Flink](#apache-flink) - 0 Issues, 0 PRs
- [Apache Spark](#apache-spark) - 2 Issues, 0 PRs
- [Apache Iceberg](#apache-iceberg) - 2 Issues, 0 PRs
- [Apache Paimon](#apache-paimon) - 1 Issues, 0 PRs
- [Lance](#lance) - 4 Issues, 0 PRs
- [LanceDB](#lancedb) - 2 Issues, 0 PRs
- [Daft](#daft) - 2 Issues, 0 PRs

---

## Apache Fluss

> 仓库: https://github.com/apache/fluss

### 📋 Issues (11)
#### 🔴 [[[lake/lance] Support Flink SQL batch query against Lance table]](https://github.com/apache/fluss/issues/2751)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 55分钟前 |
| 👤 作者 | leekeiabstraction |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 提出目前 Flink SQL 不支持对 Lance 表进行批量查询（如 `SELECT * FROM product$lake`），请求增加对此功能的支持。

#### 🔴 [[KV tablet should not produce log via PRODUCE_LOG]](https://github.com/apache/fluss/issues/2750)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 4小时前 |
| 👤 作者 | loserwang1024 |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 指出 Fluss 当前在执行 PRODUCE_LOG 操作时未区分日志表和 KV 表（PK table），导致 KV tablet 不应通过 PRODUCE_LOG 产生日志。这是一个关于类型检查缺失的 Bug 报告。

#### 🔴 [[Timeout for fetch log request]](https://github.com/apache/fluss/issues/2749)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 5小时前 |
| 👤 作者 | zuston |
| 🏷️ 状态 | OPEN

**核心内容**: Fluss 0.8.0 中，当 Tablet Server 重启时，ReplicaFetcherThread 处理 FetchLogRequest 遭遇 TimeoutException。用户尝试调整 fetcher-number 和 fetch.wait-max-time 配置无效，请求仍持续报错重试。

#### 🔴 [[If table id is changed, sender will send request to wrong bucket.]](https://github.com/apache/fluss/issues/2746)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 7小时前 |
| 👤 作者 | loserwang1024 |
| 🏷️ 状态 | OPEN

**核心内容**: 当表被删除并重建（同名但ID变化）时，RecordAccumulator 基于表名而非表ID分桶，导致旧请求被发送到新表的错误分桶。建议在发送前检查表ID是否变化。

#### 🔴 [[Dedicated tiering service for specified table]](https://github.com/apache/fluss/issues/2745)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 7小时前 |
| 👤 作者 | zuston |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 提出为特定关键表提供专属分层服务的需求，认为这对重要表是良好选项。作者表示愿意提交 PR 实现该功能。

#### 🔴 [[[test] OutOfMemoryError in Flink IT case]](https://github.com/apache/fluss/issues/2744)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 11小时前 |
| 👤 作者 | wuchong |
| 🏷️ 状态 | OPEN

**核心内容**: Flink 集成测试 `Flink119MetricsITCase` 在 `main` 分支运行时发生 `OutOfMemoryError`，导致测试失败。错误日志显示 JUnit 测试引擎执行异常。

#### 🟢 [[[flink] $changelog and $binlog virtual tables fail to complete checkpoint (NullPointerException)]](https://github.com/apache/fluss/issues/2743)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 20小时前 |
| 👤 作者 | wuchong |
| 🏷️ 状态 | CLOSED

**核心内容**: 启用检查点时，读取 `$changelog` 或 `$binlog` 虚拟表的任务会因 NullPointerException 导致检查点失败，报错为 `CheckpointException: Trigger checkpoint failure`。

#### 🔴 [[[lake/lance] Support Union Read query against Lance table]](https://github.com/apache/fluss/issues/2715)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 3天前 |
| 👤 作者 | leekeiabstraction |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 提出为 Fluss 的 Lance 表实现 Union Read 查询支持。目前相关功能未实现，导致无法通过 Flink SQL 进行批量或联合读取。Issue 提议通过实现 `LakeSource` 接口来解决此问题，提交者表示愿意提交 PR。

#### 🟢 [[[lake/lance] Lance writer should emit Arrow FixedSizeList for array columns to enable native vector search]](https://github.com/apache/fluss/issues/2706)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 6天前 |
| 👤 作者 | leekeiabstraction |
| 🏷️ 状态 | CLOSED

**核心内容**: Fluss 将 ARRAY<FLOAT> 列写入 Lance 时使用 Arrow 变长 List，导致 Lance 原生向量搜索（需 FixedSizeList）失效。问题源于 LanceArrowUtils.toArrowType() 中 ArrayType 无条件映射为 ArrowType.List.INSTANCE。

#### 🟢 [[[flink] IT test for latest scan startup mode for changelog virtual table]](https://github.com/apache/fluss/issues/2471)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 34天前 |
| 👤 作者 | MehulBatra |
| 🏷️ 状态 | CLOSED

**核心内容**: 该 Issue 为 Flink 项目添加 IT 测试，旨在验证针对变更日志虚拟表的最新扫描启动模式。具体背景参考相关 PR 讨论链接。

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
#### 🔴 [[Add `Information for new contributors` in Issues]](https://github.com/apache/spark/issues/54438)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 4天前 |
| 👤 作者 | zhengruifeng |
| 🏷️ 状态 | OPEN

**核心内容**: 该 PR 建议在 Issues 中添加“新贡献者指南”以帮助新贡献者，参考了 Pandas 项目的做法。

#### 🔴 [[[PYTHON] Support path-based table reference in `DataFrame.mergeInto`]](https://github.com/apache/spark/issues/54418)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 6天前 |
| 👤 作者 | keen85 |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 请求扩展 PySpark 的 `DataFrame.mergeInto` API，使其支持直接通过路径（如 S3 或 ABFSS URI）引用目标表，而不仅限于已注册的 Catalog 表名。此举旨在减少 Catalog 开销，适应现代数据湖架构，并与其他读写 API 保持一致。提议方案包括自动检测路径字符串或添加显式参数。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## Apache Iceberg

> 仓库: https://github.com/apache/iceberg

### 📋 Issues (2)
#### 🔴 [[Automated Incremental Clustering]](https://github.com/apache/iceberg/issues/15473)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 8小时前 |
| 👤 作者 | PuspenduBanerjee |
| 🏷️ 状态 | OPEN

**核心内容**: 该提案建议在 Apache Iceberg 中引入自动化增量聚类功能。虽然 Iceberg 已支持分区演进，但缺乏细粒度的物理文件聚类以优化数据跳过。提案旨在通过将相关行在文件内共置，提升查询效率，并涉及 Table、View 和 REST 规范的实现。

#### 🔴 [[Rewrite data files can create more small files after partition evolution]](https://github.com/apache/iceberg/issues/15465)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | lirui-apache |
| 🏷️ 状态 | OPEN

**核心内容**: 重写数据文件时，若分区粒度变细，默认使用当前分区规范可能导致生成更多小文件。建议在 bin-pack 策略下默认使用输入文件的分区规范以避免此问题。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## Apache Paimon

> 仓库: https://github.com/apache/paimon

### 📋 Issues (1)
#### 🟢 [[[Bug] Discrepancy in Paimon Procedures documentation]](https://github.com/apache/paimon/issues/7197)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 25天前 |
| 👤 作者 | junmuz |
| 🏷️ 状态 | CLOSED

**核心内容**: Paimon Procedures 文档示例中 parallelism 参数使用字符串类型，但代码实际要求整数类型，导致在 Flink 和 Spark 中执行时报错。用户已确认愿意提交 PR 修复文档。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## Lance

> 仓库: https://github.com/lance-format/lance

### 📋 Issues (4)
#### 🔴 [[lance-linalg build.rs add android target_os]](https://github.com/lance-format/lance/issues/6058)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 8分钟前 |
| 👤 作者 | franklaranja |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 提出 lance-linalg 的 build.rs 中第 40 行的条件判断未包含 Android 目标系统，导致无法在 Android 上构建。建议将条件 `target_os == "linux"` 修改为 `target_os == "linux" || target_os == "android"`，以支持 Android 平台的编译。

#### 🔴 [[Missing file: ./dataset/lineitem.lance in benchmark script]](https://github.com/lance-format/lance/issues/6055)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 3小时前 |
| 👤 作者 | muclover |
| 🏷️ 状态 | OPEN

**核心内容**: 用户在 GitHub Issue 中指出 tpch/benchmark.py 引用的 ./dataset/lineitem.lance 文件缺失，询问如何生成或获取该数据集，并建议在 README 中补充相关说明。

#### 🔴 [[Bounded Compaction Planner To Limit the amount of data processed during a single compaction]](https://github.com/lance-format/lance/issues/6039)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | zhangyue19921010 |
| 🏷️ 状态 | OPEN

**核心内容**: 为针对大规模数据集压缩的瓶颈，提出引入 **BoundedCompactionPlanner**。该规划器通过限制单次压缩的计算负载（如数据吞吐量或分片数量），将大型压缩作业拆分为多个子作业，从而避免生成计划耗时过长或 OOM 错误，并减少因任务失败导致的资源浪费。

#### 🔴 [[Put data and deletion files in subdirectories]](https://github.com/lance-format/lance/issues/6030)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | wjones127 |
| 🏷️ 状态 | OPEN

**核心内容**: 为解决大量文件导致清理时列取慢的问题，提议将数据文件和删除文件放入子目录以实现并行列取。数据文件可通过修改命名方案实现，但删除文件需更新规范。此举可显著提升 S3 等存储上的文件列取效率。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## LanceDB

> 仓库: https://github.com/lancedb/lancedb

### 📋 Issues (2)
#### 🔴 [[Provide optional method to split a Scannable]](https://github.com/lancedb/lancedb/issues/3082)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 16小时前 |
| 👤 作者 | wjones127 |
| 🏷️ 状态 | OPEN

**核心内容**: 当前通过轮询并行插入时，若某分区失败需从头重试。提议在 Scannable 层级添加 split 方法，将其拆分为独立可重扫的子流，从而仅重试失败部分，保留已成功部分的进度。

#### 🔴 [[FileFragment.update_columns does not update last_updated_at_version_meta]](https://github.com/lancedb/lancedb/issues/3079)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 22小时前 |
| 👤 作者 | mackrorysd |
| 🏷️ 状态 | OPEN

**核心内容**: FileFragment.update_columns 方法未更新 last_updated_at_version_meta 字段，这被认为是一个疏漏。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## Daft

> 仓库: https://github.com/Eventual-Inc/Daft

### 📋 Issues (2)
#### 🔴 [[Support reading and writing LeRobot format datasets]](https://github.com/Eventual-Inc/Daft/issues/6296)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 3天前 |
| 👤 作者 | plotor |
| 🏷️ 状态 | OPEN

**核心内容**: 为支持具身智能行业用户，请求在 Daft 中新增读取和写入 LeRobot 格式数据集的功能，以便用户能便捷地处理该格式数据。

#### 🟢 [[`ddof` argument to `stddev`]](https://github.com/Eventual-Inc/Daft/issues/4464)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 271天前 |
| 👤 作者 | MarcoGorelli |
| 🏷️ 状态 | CLOSED

**核心内容**: 请求为 `stddev` 函数添加 `ddof` 参数，以支持自定义自由度计算标准差。用户希望直接使用 `daft.col('a').stddev(ddof=1)`，而非通过手动计算替代方案，因为后者无法在 `over` 上下文中评估。用户表示不打算自行实现该功能。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

