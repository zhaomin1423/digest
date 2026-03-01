# GitHub 每日摘要

📅 **生成时间**: 2026-03-01 22:02:02
⏰ **时间范围**: 过去 24 小时
📊 **监控仓库数**: 8
📋 **总计**: 18 Issues, 0 Pull Requests

## 📑 目录

- [Apache Fluss](#apache-fluss) - 9 Issues, 0 PRs
- [Apache Flink](#apache-flink) - 0 Issues, 0 PRs
- [Apache Spark](#apache-spark) - 1 Issues, 0 PRs
- [Apache Iceberg](#apache-iceberg) - 8 Issues, 0 PRs
- [Apache Paimon](#apache-paimon) - 0 Issues, 0 PRs
- [Lance](#lance) - 0 Issues, 0 PRs
- [LanceDB](#lancedb) - 0 Issues, 0 PRs
- [Daft](#daft) - 0 Issues, 0 PRs

---

## Apache Fluss

> 仓库: https://github.com/apache/fluss

### 📋 Issues (9)
#### 🔴 [[[workflow/doc] How to host a community call as a contributor]](https://github.com/apache/fluss/issues/2759)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1小时前 |
| 👤 作者 | MehulBatra |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 提出需要为贡献者添加关于如何主持社区会议的文档，以规范流程并明确角色轮换。目的是确保在负责人缺席时，社区记录和笔记工作不受影响，使任何贡献者都能透明地接手职责。作者表示愿意提交 PR。

#### 🔴 [[[flink] Rewrite waitForCheckpoint, getFileBasedCheckpointsConfig to a shared base class]](https://github.com/apache/fluss/issues/2758)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1小时前 |
| 👤 作者 | MehulBatra |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 提议将 `waitForCheckpoint` 和 `getFileBasedCheckpointsConfig` 方法重构为共享基类，以消除在 changelog 和 binlog 的 scan.startup 配置中的代码重复。作者已表示愿意提交 PR。

#### 🔴 [[[server] Update Tablet Server to use per-table/partition remote data directory]](https://github.com/apache/fluss/issues/2756)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 5小时前 |
| 👤 作者 | LiebingYu |
| 🏷️ 状态 | OPEN

#### 🔴 [[[server] Integrate remote directory selector into table/partition creation]](https://github.com/apache/fluss/issues/2755)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 5小时前 |
| 👤 作者 | LiebingYu |
| 🏷️ 状态 | OPEN

#### 🔴 [[[server] Extend metadata models to support per-table/partition remote data directory]](https://github.com/apache/fluss/issues/2754)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 5小时前 |
| 👤 作者 | LiebingYu |
| 🏷️ 状态 | OPEN

#### 🔴 [[[server] Add configuration options for multiple remote data directories]](https://github.com/apache/fluss/issues/2753)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 5小时前 |
| 👤 作者 | LiebingYu |
| 🏷️ 状态 | OPEN

#### 🔴 [[[test] OutOfMemoryError in Flink IT case]](https://github.com/apache/fluss/issues/2744)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | wuchong |
| 🏷️ 状态 | OPEN

**核心内容**: Fluss 主分支在 Flink 集成测试中发生 OutOfMemoryError，导致 `Flink119MetricsITCase` 执行失败。

#### 🔴 [[Support Multi-Location for Remote Storage]](https://github.com/apache/fluss/issues/2292)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 60天前 |
| 👤 作者 | LiebingYu |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 提议支持远程存储的多位置功能（FIP-25）。旨在让 Fluss 服务器支持多路径远程存储，并包含多个相关子任务（如 #2753 至 #2756），涉及 RemoteStorageCleaner 对多个远程目录的清理支持。目前方案未定，暂无 PR 提交意愿。

#### 🔴 [[[Umbrella][Feature] Support for complex data types]](https://github.com/apache/fluss/issues/816)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 302天前 |
| 👤 作者 | XuQianJin-Stars |
| 🏷️ 状态 | OPEN

**核心内容**: 该 Issue 旨在为 Fluss 增加对复杂数据类型的支持，包括 Array、Map、Struct 和 Variant/JSON。方案涉及实现接口层、通用实现及基于 Arrow 等的具体类型，并集成 Flink/Spark 数据类型及数据湖（如 Paimon）。目前除 Variant/JSON 外，其他类型支持已完成。

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
#### 🔴 [[Any plan to update Derby from 10.16.1.1 to 10.17.1.0?]](https://github.com/apache/spark/issues/54563)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 3小时前 |
| 👤 作者 | stayform |
| 🏷️ 状态 | OPEN

**核心内容**: Issue 询问 Spark 是否有计划将 Derby 从 10.16.1.1 升级至 10.17.1.0 以修复已知 CVE 漏洞，以及是否有计划将内置 Hive 依赖升级至 4.2.0。

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## Apache Iceberg

> 仓库: https://github.com/apache/iceberg

### 📋 Issues (8)
#### 🔴 [[Flink tableMaintenance incorrectly delete manifest files]](https://github.com/apache/iceberg/issues/15487)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 8小时前 |
| 👤 作者 | zncleon |
| 🏷️ 状态 | OPEN

**核心内容**: 该报告指出，在 Flink 中使用 Iceberg 1.10.1 版本进行表维护时，`IncrementalFileCleanup` 错误地删除了 manifest 文件。这导致任务在尝试打开已删除的文件时抛出 `NotFoundException`，并引发重试警告，可能造成孤立数据文件。

#### 🔴 [[Optimise HadoopFileIO for cloud IO]](https://github.com/apache/iceberg/issues/15353)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 10天前 |
| 👤 作者 | steveloughran |
| 🏷️ 状态 | OPEN

**核心内容**: 该提议旨在优化 HadoopFileIO 以提升云存储性能。通过迁移至 Hadoop 3.3.5 的新 API，可减少打开文件时的 head 请求，为已知文件类型设置最优读取策略，并让 S3a 跳过防覆盖目录检查。此改进需兼容 HDFS 和本地文件系统，且无需反射调用。

#### 🔴 [[`CREATE OR REPLACE VIEW` preserves other dialects.]](https://github.com/apache/iceberg/issues/15296)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 18天前 |
| 👤 作者 | Guosmilesmile |
| 🏷️ 状态 | OPEN

**核心内容**: 当视图包含多种方言 SQL 时，直接执行 `CREATE OR REPLACE VIEW` 会删除其他方言的 SQL，仅保留最新的 Spark SQL。请求改进该行为，使其仅更新 Spark 部分，同时保留其他引擎的 SQL。用户表示愿意独立贡献此改进。

#### 🔴 [[MERGE INTO doesn't work when using non-deterministic expressions in Pyspark]](https://github.com/apache/iceberg/issues/14585)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 107天前 |
| 👤 作者 | Diogo20Mata |
| 🏷️ 状态 | OPEN

**核心内容**: 在 Apache Iceberg 1.7.1 中，使用 PySpark 的 MERGE INTO 语句向 Iceberg 表写入数据时，若应用非确定性表达式（如 `uuid`），会报错 `[INVALID_NON_DETERMINISTIC_EXPRESSIONS]`。用户询问该问题是否已在较新版本中修复。

#### 🔴 [[How to handle ValidationException: Cannot determine history during rewrite_data_files with concurrent streaming writes?]](https://github.com/apache/iceberg/issues/13972)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 180天前 |
| 👤 作者 | jordi-crespo |
| 🏷️ 状态 | OPEN

**核心内容**: 用户在Iceberg 1.9.2中使用`rewrite_data_files`压缩高碎片化分区时，因存在并发流式写入，报错`ValidationException: Cannot determine history`。已尝试调整`partial-progress`参数及重试逻辑无效。用户询问如何处理并发写入下的压缩、提高过程韧性、是否需调整隔离级别或暂停写入，以及未来改进计划。

#### 🟢 [[Use SqlApiConf.CASE_SENSITIVE_KEY() instead of hard-coded spark.sql.caseSensitive]](https://github.com/apache/iceberg/issues/13857)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 194天前 |
| 👤 作者 | guixiaowen |
| 🏷️ 状态 | CLOSED

**核心内容**: 该 Issue/PR 建议使用 `SqlApiConf.CASE_SENSITIVE_KEY()` 替代硬编码的 `spark.sql.caseSensitive`，以避免硬编码配置键。

#### 🟢 [[Introducing a New Hive to Iceberg Table Migration Method: In-Place Upgrade]](https://github.com/apache/iceberg/issues/12762)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 325天前 |
| 👤 作者 | slfan1989 |
| 🏷️ 状态 | CLOSED

**核心内容**: 该提案针对Hive表迁移至Iceberg的痛点，提出一种名为“In-Place Upgrade”的新方法。现有Snapshot和Migrate方法分别存在需改表名和迁移期间需中断读写的问题。新方法结合两者优点，允许迁移期间源表可读，升级后表名不变，对用户透明且不影响业务操作。

#### 🔴 [[Variant Data Type Support]](https://github.com/apache/iceberg/issues/10392)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 641天前 |
| 👤 作者 | sfc-gh-aixu |
| 🏷️ 状态 | OPEN

**核心内容**: 提议在 Iceberg 数据类型中增加 Variant 类型，用于高效二进制编码动态半结构化数据（如 JSON、Avro）。该类型支持创建包含 Variant 列的表、插入半结构化数据及查询操作，以提升查询引擎性能。

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

### 📋 Issues (0)
_过去 24 小时内没有新的 Issue_

### 🔀 Pull Requests (0)
_过去 24 小时内没有新的 Pull Requests_

---

## LanceDB

> 仓库: https://github.com/lancedb/lancedb

### 📋 Issues (0)
_过去 24 小时内没有新的 Issue_

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

