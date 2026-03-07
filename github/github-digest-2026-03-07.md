# GitHub 每日摘要

📅 **生成时间**: 2026-03-07 23:58:19
⏰ **时间范围**: 过去 24 小时
📊 **监控仓库数**: 8
📋 **总计**: 2 Issues, 21 Pull Requests

## 📑 目录

- [Apache Fluss](#apache-fluss) - 0 Issues, 1 PRs
- [Apache Flink](#apache-flink) - 0 Issues, 1 PRs
- [Apache Spark](#apache-spark) - 1 Issues, 16 PRs
- [Apache Iceberg](#apache-iceberg) - 1 Issues, 3 PRs
- [Apache Paimon](#apache-paimon) - 0 Issues, 0 PRs
- [Lance](#lance) - 0 Issues, 0 PRs
- [LanceDB](#lancedb) - 0 Issues, 0 PRs
- [Daft](#daft) - 0 Issues, 0 PRs

---

## Apache Fluss

> 仓库: https://github.com/apache/fluss

### 📋 Issues (0)
_过去 24 小时内没有新的 Issue_

### 🔀 Pull Requests (1)
#### 🔴 [[[KV] Support Full KV Scan ]](https://github.com/apache/fluss/pull/2809)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 7小时前 |
| 👤 作者 | polyzos |
| 🏷️ 状态 | OPEN

---

## Apache Flink

> 仓库: https://github.com/apache/flink

### 📋 Issues (0)
_过去 24 小时内没有新的 Issue_

### 🔀 Pull Requests (1)
#### 🔴 [[[hotfix] [docs] Fix broken flink-training links in hands-on section]](https://github.com/apache/flink/pull/27746)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 22小时前 |
| 👤 作者 | kylerballiet |
| 🏷️ 状态 | OPEN

**核心内容**: 修复 Learn Flink 文档中 "Hands-on" 部分的 flink-training 链接。问题包括：仓库链接指向不存在的分支，练习链接使用了错误的 `blob` 路径。修复方案是将相关短代码统一使用 `master` 分支，并将练习路径从 `blob` 改为 `tree`，确保所有受影响页面的链接正常工作。

---

## Apache Spark

> 仓库: https://github.com/apache/spark

### 📋 Issues (1)
#### 🔴 [[Fix various typo errors in code comments across multiple modules]](https://github.com/apache/spark/issues/54674)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1小时前 |
| 👤 作者 | ycli12 |
| 🏷️ 状态 | OPEN

**核心内容**: 该 PR 修复了多个模块中代码注释的拼写错误，包括将 `neccessary`、`overriden`、`custome` 等更正为正确的拼写。修改旨在提升代码可读性和文档一致性，不涉及用户功能变更。

### 🔀 Pull Requests (16)
#### 🔴 [[[SPARK-54674][CORE][SQL][YARN] Fix various typo errors in comments]](https://github.com/apache/spark/pull/54675)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1小时前 |
| 👤 作者 | ycli12 |
| 🏷️ 状态 | OPEN

**核心内容**: 该 PR 修复了 Spark 多个模块（Core、SQL、YARN）代码注释中的拼写错误，包括将 `neccessary`、`overriden`、`custome`、`commiting`、`curent` 和 `commited` 等单词更正为正确拼写。此举旨在提高代码可读性和文档一致性，不涉及功能变更，无用户影响。

#### 🔴 [[[SPARK-55881][SQL][UI] Add queryId, errorMessage, and rootExecutionId to SQL execution REST API]](https://github.com/apache/spark/pull/54673)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 3小时前 |
| 👤 作者 | yaooqinn |
| 🏷️ 状态 | OPEN

**核心内容**: 该 PR 扩展了 Spark SQL 执行 REST API，新增了 `queryId`、`errorMessage` 和 `rootExecutionId` 三个字段。这些字段原存在于内部数据结构中，现对外暴露以支持客户端 SQL 标签页的渲染功能，确保 REST API 与原服务端页面功能一致。修改向后兼容，现有测试全部通过。

#### 🔴 [[[SPARK-48942][SQL][TESTS] Add regression tests for Array of Structs with UDT fields in Parquet]](https://github.com/apache/spark/pull/54672)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 6小时前 |
| 👤 作者 | james-willis |
| 🏷️ 状态 | OPEN

**核心内容**: 该 PR 为 Parquet 中包含 UDT 字段的 Array of Structs 添加回归测试。此前 SPARK-52651 已修复相关 Bug，但缺乏针对特定嵌套模式的测试。新增测试确保修复持续有效，无功能性变更。

#### 🔴 [[[SPARK-55875][UI] Switch SQL tab query listing to client-side DataTables]](https://github.com/apache/spark/pull/54671)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 9小时前 |
| 👤 作者 | yaooqinn |
| 🏷️ 状态 | OPEN

**核心内容**: 该 PR 将 Spark UI 的 SQL 标签页从服务端渲染的 PagedTable 替换为客户端 DataTables。新实现通过 REST API 获取数据，支持即时搜索、排序和状态过滤，无需页面刷新。此举简化了 Scala 代码（590 行减至 50 行），提升了用户体验，并保持与环境页面的一致性。测试已更新以验证新页面渲染。

#### 🔴 [[[SPARK-55768][UI] Improve responsive layout with table-responsive wrappers and viz overflow]](https://github.com/apache/spark/pull/54670)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 11小时前 |
| 👤 作者 | yaooqinn |
| 🏷️ 状态 | OPEN

**核心内容**: 该 PR 为 Spark Web UI 添加了 Bootstrap 5 响应式布局改进。通过在 `UIUtils.listingTable` 中包装 `table-responsive` 类，使表格在窄屏下支持水平滚动；同时在 DAG 和 SQL 可视化容器中添加 `overflow-x: auto`，防止图形溢出破坏布局。此更改属于 Spark Web UI 现代化的一部分，解决了移动端和分屏视图下的显示问题。

#### 🔴 [[[SPARK-55869][SQL] Extended Predicate Pushdown for DataSource V2]](https://github.com/apache/spark/pull/54669)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 12小时前 |
| 👤 作者 | schenksj |
| 🏷️ 状态 | OPEN

**核心内容**: 该 PR 扩展了 Spark DataSource V2 的谓词下推功能，新增三层能力：1. 支持数据源声明内置谓词（如 LIKE、RLIKE、ARRAY_CONTAINS 等）的下推能力；2. 允许表通过 `SupportsCustomPredicates` 声明自定义谓词函数；3. （内容截断未显示）。所有功能默认开启，通过配置项控制。

#### 🔴 [[[SPARK-55870][SQL] Add docs for Geo types]](https://github.com/apache/spark/pull/54668)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 14小时前 |
| 👤 作者 | szehon-ho |
| 🏷️ 状态 | OPEN

**核心内容**: 该 PR 为 Spark 4.2 新增的 Geometry/Geography 类型添加了文档。这些类型目前受特性标志控制，预计将在下一版本移除标志。PR 未引入面向用户的变更，且使用了生成式 AI 工具辅助编写。

#### 🔴 [[[SQL] Add toV2Stats/toV2ColStat to CatalogStatistics for DSv2 connectors]](https://github.com/apache/spark/pull/54667)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 14小时前 |
| 👤 作者 | huan233usc |
| 🏷️ 状态 | OPEN

**核心内容**: 该 PR 为 DSv2 连接器（如 Delta Kernel）添加了从 V1 到 V2 的目录统计转换方法，包括 `toV2ColStat` 和 `toV2Stats`，避免连接器重复实现转换逻辑。

#### 🔴 [[[SPARK-55868][SQL][Tests] Fix Predicate Pushdown for InMemoryTable for V2Filters]](https://github.com/apache/spark/pull/54666)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 15小时前 |
| 👤 作者 | szehon-ho |
| 🏷️ 状态 | OPEN

**核心内容**: 修复了 InMemoryTable 中 V2Filter 谓词下推的名称匹配问题，解决了测试表无法接受过滤器的问题。此变更仅影响测试，不涉及用户功能。

#### 🔴 [[[SPARK-55453][SQL] Fix LIKE pattern matching for supplementary Unicode characters]](https://github.com/apache/spark/pull/54665)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 16小时前 |
| 👤 作者 | xiaoxuandev |
| 🏷️ 状态 | OPEN

**核心内容**: 该 PR 修复了 Spark SQL 中 LIKE 模式匹配对补充 Unicode 字符（如 emoji）的处理。修复了 `escapeLikeRegex` 迭代字符和 `LikeSimplification` 长度计算时的错误，确保正确处理 UTF-16 代理对。此修复改变了用户行为，使得包含补充字符的模式匹配结果正确。已添加相关测试。

#### 🔴 [[[SPARK-55867][PS] Fix StringMethods with pandas 3]](https://github.com/apache/spark/pull/54664)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 18小时前 |
| 👤 作者 | ueshin |
| 🏷️ 状态 | OPEN

**核心内容**: 该 PR 修复了 `StringMethods` 在 pandas 3 中的兼容性问题，涉及 `findall`、`match`、`rsplit` 和 `split` 方法。更新了相关测试以确保行为与 pandas 3 一致。

#### 🔴 [[[SPARK-55289][SQL][FOLLOWUP] Fix flaky test in-order-by.sql by disabling broadcast join]](https://github.com/apache/spark/pull/54663)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 21小时前 |
| 👤 作者 | yaooqinn |
| 🏷️ 状态 | OPEN

**核心内容**: 该 PR 为修复 `in-order-by.sql` 测试中的内存溢出问题，禁用了广播连接。通过设置 `spark.sql.autoBroadcastJoinThreshold=-1`，防止复杂相关 IN 子查询在内存受限的 CI 环境中因 BroadcastHashJoin 导致 OOM。此为仅测试的修改，不涉及用户变更，并重新生成了 Golden 文件。

#### 🔴 [[[SPARK-55866][SQL] Rename _LEGACY_ERROR_TEMP_2145 to OPTION_VALUE_EXCEEDS_ONE_CHARACTER]](https://github.com/apache/spark/pull/54662)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 22小时前 |
| 👤 作者 | mikhailnik-db |
| 🏷️ 状态 | OPEN

**核心内容**: 该 PR 将 Spark SQL 中的错误类名从临时占位符 `_LEGACY_ERROR_TEMP_2145` 重命名为更具描述性的 `OPTION_VALUE_EXCEEDS_ONE_CHARACTER`，并为其分配了 SQL 状态 `22023`（无效参数值）。此更改旨在改进错误报告并符合 ANSI SQL 标准，错误消息本身保持不变。

#### 🔴 [[[SPARK-55865][SQL] Rename _LEGACY_ERROR_TEMP_1266 to CANNOT_TRUNCATE_EXTERNAL_TABLE]](https://github.com/apache/spark/pull/54661)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 22小时前 |
| 👤 作者 | mikhailnik-db |
| 🏷️ 状态 | OPEN

**核心内容**: 该 PR 将 Spark SQL 中的遗留错误条件 `_LEGACY_ERROR_TEMP_1266` 重命名为正式的错误类 `CANNOT_TRUNCATE_EXTERNAL_TABLE`，并设置 SQL 状态为 `0A000`（不支持的功能）。同时，将消息参数从 `tableIdentWithDB` 重命名为 `tableName` 以保持一致性。

#### 🔴 [[[SPARK-55864][CORE][TESTS] Add more tests for SHS multiple log directories feature]](https://github.com/apache/spark/pull/54660)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 22小时前 |
| 👤 作者 | sarutak |
| 🏷️ 状态 | OPEN

**核心内容**: 该 PR 为 Spark 历史服务器（SHS）的多日志目录功能增加了测试覆盖。新增测试包括运行时移除目录、启动后动态创建目录、目录暂时不可用及恢复、所有目录不可用时的优雅处理、配置中含空逗号项以及名称数量不匹配时的回退机制。旨在提升测试覆盖率，无用户可见变更。

#### 🔴 [[[SPARK-47997][PS] Add errors parameter to DataFrame.drop and Series.drop]](https://github.com/apache/spark/pull/54659)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 23小时前 |
| 👤 作者 | devin-petersohn |
| 🏷️ 状态 | OPEN

**核心内容**: 该 PR 为 `DataFrame.drop` 和 `Series.drop` 添加了 `errors` 参数以匹配 pandas API。默认值 `errors='raise'` 在标签缺失时抛出 `KeyError`，而 `errors='ignore'` 则静默跳过缺失标签。此变更旨在实现 API 兼容性，方便用户迁移。

---

## Apache Iceberg

> 仓库: https://github.com/apache/iceberg

### 📋 Issues (1)
#### 🔴 [[AnalysisException: [UNRESOLVED_COLUMN] during MERGE INTO on wide Iceberg tables (400+ columns) in Spark 3.5]](https://github.com/apache/iceberg/issues/15526)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 18小时前 |
| 👤 作者 | NataliaLaurova |
| 🏷️ 状态 | OPEN

**核心内容**: 在 Spark 3.5 中，对包含 400+ 列的宽 Iceberg 表执行 MERGE INTO 操作时，分析阶段抛出 UNRESOLVED_COLUMN 错误。尽管错误提示包含建议的列名，且相同 SQL 在小表或其他引擎上正常，但解析失败。该问题仅限 SQL 语法，DataFrame API 可作为变通方案，推测与 Catalyst Optimizer 处理极宽表的解析能力有关。

### 🔀 Pull Requests (3)
#### 🔴 [[docs: reformat mailing list]](https://github.com/apache/iceberg/pull/15527)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 12小时前 |
| 👤 作者 | kevinjqliu |
| 🏷️ 状态 | OPEN

**核心内容**: 该 PR 重新格式化了 Apache Iceberg 社区页面的邮件列表部分。它将邮件链接从 `mailto:` 改为普通链接，避免点击时自动打开邮件应用，并调整了顺序，将“Archive”置顶以便更轻松地访问归档。

#### 🔴 [[API, Core: Add overwrite-aware table registration]](https://github.com/apache/iceberg/pull/15525)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 20小时前 |
| 👤 作者 | sririshindra |
| 🏷️ 状态 | OPEN

**核心内容**: 该 PR 在 Catalog API 中新增支持覆盖感知的表注册功能，并连接到 REST 目录实现。新增了带 `overwrite` 参数的 `registerTable` 重载方法，保持向后兼容。默认行为为 `overwrite=false`，`overwrite=true` 时若未覆盖实现则抛出异常。同时更新了 `RESTCatalog` 和 `RESTSessionCatalog` 以传递请求标志，并添加了相关测试验证功能。

#### 🟢 [[OpenAPI: Include storage credentials for PlanTableScanResponse/FetchPlanningResultResponse when include-credentials flag is set]](https://github.com/apache/iceberg/pull/15524)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 23小时前 |
| 👤 作者 | nastra |
| 🏷️ 状态 | CLOSED

**核心内容**: 该 PR 旨在在 OpenAPI 中，当设置 `include-credentials=true` 标志时，为 `PlanTableScanResponse` 和 `FetchPlanningResultResponse` 包含存储凭据。这是从 Apache Iceberg #15461 PR 中提取出来的功能。

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

