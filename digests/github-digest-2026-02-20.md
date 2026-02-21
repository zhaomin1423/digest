# GitHub 每日摘要

📅 **生成时间**: 2026-02-20 00:00:00
⏰ **时间范围**: 过去 24 小时
📊 **监控仓库数**: 9
📋 **总计**: 31 Issues, 166 Pull Requests

## 📑 目录

- [Apache Fluss](#apache-fluss) - 1 Issues, 5 PRs
- [Apache Flink](#apache-flink) - 0 Issues, 7 PRs
- [Apache Spark](#apache-spark) - 4 Issues, 37 PRs
- [Apache Iceberg](#apache-iceberg) - 4 Issues, 27 PRs
- [Apache Paimon](#apache-paimon) - 0 Issues, 4 PRs
- [Ray](#ray) - 12 Issues, 50 PRs
- [Lance](#lance) - 3 Issues, 2 PRs
- [LanceDB](#lancedb) - 6 Issues, 2 PRs
- [Daft](#daft) - 1 Issues, 32 PRs

---

## Apache Fluss

> 仓库: https://github.com/apache/fluss

### 📋 Issues (1)

#### 🔴 [Fix SASL client special characters escaping](https://github.com/apache/fluss/issues/2698)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | morazow |
| 🏷️ 状态 | OPEN |

**核心内容**: 该 Issue 指出在 SASL 认证机制中使用特殊字符（如引号）时，客户端 SASL 解析器会失败。建议修复转义逻辑、引入工具方法处理特殊字符，并检查服务器端是否存在类似问题。

---

### 🔀 Pull Requests (5)

#### 🔴 [Fix the LICENSE and NOTICE files for the binary distribution, including transitive dependencies](https://github.com/apache/fluss/pull/2703)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 7分钟前 |
| 👤 作者 | jbonofre |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +1243/-67 (5 文件) |

**核心内容**: 这个 PR 修复了二进制分发中的 LICENSE 和 NOTICE 文件，明确列出了包括传递依赖在内的所有捆绑依赖代码。它还内联了 BSD/MIT 许可证内容，并正确更新了 NOTICE 文件。

---

#### 🔴 [Fix license and notice issue](https://github.com/apache/fluss/pull/2702)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 4小时前 |
| 👤 作者 | luoyuxia |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +2817/-222 (32 文件) |

**核心内容**: 这个 PR 主要修复了许可证和通知文件的问题，包括移除二进制发布包中的 mvnw、统一重复的 LICENSE-re2j 文件，以及将 BSD 许可证的依赖从 NOTICE 文件移至 LICENSE 文件中，以符合 Apache 许可证指南。

---

#### 🔴 [[rpc][helm] Add support for special characters in SASL username and password](https://github.com/apache/fluss/pull/2701)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 15小时前 |
| 👤 作者 | morazow |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +1161/-63 (16 文件) |

**核心内容**: 这个 PR 修复了客户端 SASL 认证中特殊字符转义的问题，并更新了 Helm Chart 以确保服务器端配置文件正确转义 JAAS 值。此外，还添加了针对特殊字符的测试用例和 Helm 单元测试。

---

#### 🔴 [[helm] Enable SASL authenticated connection to Zookeeper nodes](https://github.com/apache/fluss/pull/2700)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | morazow |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +843/-8 (10 文件) |

**核心内容**: 这个 PR 在 Helm 部署中增加了通过 SASL 认证连接 Zookeeper 节点的选项。它更新了相关的部署文档，并包含相应的单元测试验证。

---

#### 🔴 [  [docs] Reorganize Streaming Lakehouse documentation to higlight deployment and core features ](https://github.com/apache/fluss/pull/2699)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | MehulBatra |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +526/-125 (27 文件) |

**核心内容**: 这个 PR 重新组织了 Streaming Lakehouse 文档，重点突出部署和核心功能，包括新增页面、调整目录结构和优化现有文档内容。同时修复了自动压缩和自动过期快照的默认值设置，并更新了相关交叉引用。

---


## Apache Flink

> 仓库: https://github.com/apache/flink

### 📋 Issues

_过去 24 小时内没有新的 Issue_

### 🔀 Pull Requests (7)

#### 🔴 [[FLINK-39130][metrics] Allow native types in MetricConfig](https://github.com/apache/flink/pull/27642)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 15小时前 |
| 👤 作者 | Izeren |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +244/-31 (2 文件) |

**核心内容**: 这个 PR 允许 MetricConfig 使用原生类型（如数字），以支持更灵活的配置方式。主要变更包括让 MetricConfig 能够识别 Number 值，并添加了相应的单元测试验证。

---

#### 🔴 [[FLINK-39105][rest] Fix RestClientTest.testConnectionTimeout to handle environment-dependent exception types](https://github.com/apache/flink/pull/27641)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 15小时前 |
| 👤 作者 | MartijnVisser |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +6/-2 (1 文件) |

**核心内容**: 该 PR 修复了 `RestClientTest.testConnectionTimeout` 测试，使其能够处理环境相关的异常类型。由于某些 CI 环境会立即返回“网络不可达”异常而非连接超时，测试现在接受 `SocketException` 的所有子类型，以确保在不同环境下都能正确验证连接失败。

---

#### 🔴 [[FLINK-39088][table] Support injective casts from VARCHAR to BINARY](https://github.com/apache/flink/pull/27640)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 18小时前 |
| 👤 作者 | gustavodemorais |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +50/-1 (3 文件) |
| 🏷️ 标签 | `community-reviewed` |

**核心内容**: 该 PR �支持将 VARCHAR 到 BINARY 的类型转换标记为单射（injective），以确保在将 VARCHAR 键列转换为 VARBINARY 时保持键的唯一性。转换仅在目标二进制容量足够时被视为单射，例如无界转换或目标容量至少为源字符串最大 UTF-8 编码长度时。

---

#### 🔴 [[WIP] FLIP-547: Support checkpoint during recovery](https://github.com/apache/flink/pull/27639)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 22小时前 |
| 👤 作者 | 1996fanrui |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +5268/-359 (246 文件) |

**核心内容**: 该 PR 旨在支持在恢复过程中进行检查点操作。目前该变更尚未完成，属于工作进行中的状态。

---

#### 🔴 [[FLINK-39073][runtime] Defer alignment check for idle splits](https://github.com/apache/flink/pull/27638)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | Efrat19 |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +83/-5 (3 文件) |

**核心内容**: 该 PR 修复了当数据分区发出远期水位线后变为空闲状态时，对齐检查错误将其标记为暂停的问题。通过推迟对空闲分区的对齐检查，直到其恢复活跃状态，确保了 Source 操作符的状态转换正确性。

---

#### 🔴 [[FLINK-39107][tests] Run otel container from a prebuilt image](https://github.com/apache/flink/pull/27637)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | Efrat19 |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +17/-19 (1 文件) |

**核心内容**: 该 PR 旨在解决多个测试并行构建 OpenTelemetry Docker 镜像时出现的构建问题。改用预构建的镜像并通过挂载输出目录的方式，替代了从 Dockerfile 构建镜像的做法，以避免写时复制瓶颈。

---

#### 🔴 [[FLINK-38533] SqlClientITCase failed for image confluentinc/cp-kafka:7.2.2 startup](https://github.com/apache/flink/pull/27636)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2天前 |
| 👤 作者 | Samrat002 |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +2/-1 (1 文件) |

**核心内容**: 该 PR 修复了 `SqlClientITCase` 测试因 Kafka 容器启动超时而失败的问题。通过将 `confluentinc/cp-kafka:7.2.2` 容器的启动超时时间调整为 5 分钟，确保在 CI 环境中 Kafka 有足够时间完成启动。这一变更旨在解决测试的不稳定性问题。

---


## Apache Spark

> 仓库: https://github.com/apache/spark

### 📋 Issues (4)

#### 🔴 [[TEST] `test_session.py` does not work properly](https://github.com/apache/spark/issues/54405)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 9小时前 |
| 👤 作者 | gaogaotiantian |
| 🏷️ 状态 | OPEN |

**核心内容**: `test_session.py` 测试文件存在问题，部分测试会卡住或失败，原因是缺少服务器导致 `session.stop()` 无法执行，且 `_get_default_session()` 获取会话不正确。此外，该测试因缺少 `main()` 部分未在 CI 中执行，需要原作者修复并确保测试功能正确。

---

#### 🔴 [[BUILD] Add coding agent build instructions](https://github.com/apache/spark/issues/54386)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | szehon-ho |
| 🏷️ 状态 | CLOSED |

**核心内容**: 这个 Issue 建议为 Spark 项目添加构建说明，以便 Claude Code、Cursor 等 AI 工具能正确理解如何构建 Spark 和运行测试。当前默认使用 Maven 的构建方式较慢，希望能优化为更高效的 SBT 构建。

---

#### 🔴 [Framework](https://github.com/apache/spark/issues/54379)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | salvino080-coder |
| 🏷️ 状态 | CLOSED |

**核心内容**: 该 Issue 展示了一个高性能计算（HPC）框架的核心代码，包括硬件级内存对齐分配器和优化的事件视界内核。代码通过手动 SIMD 向量化、稀疏模式支持和软件预取等技术提升计算效率，适用于大规模数据处理场景。

---

#### 🔴 [[SQL] dropDuplicates and Window dedup produce incorrect results with SPJ partiallyClusteredDistribution](https://github.com/apache/spark/issues/54378)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | paryoja |
| 🏷️ 状态 | OPEN |

**核心内容**: 在启用 SPJ 和部分集群分布时，`dropDuplicates()` 和基于 Window 的去重操作会产生错误结果，导致本应被移除的重复行未被正确处理。根本原因是部分集群将同一分区的数据分散到多个任务中，而去重操作依赖于同一分区键的数据位于同一任务的假设，因此跨任务的重复行未被去除。

---

### 🔀 Pull Requests (37)

#### 🔴 [[SPARK-55625][PS] Fix StringOps to make `str` dtype work properly](https://github.com/apache/spark/pull/54413)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 5小时前 |
| 👤 作者 | ueshin |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +53/-31 (7 文件) |

**核心内容**: 该 PR 修复了 `StringOps` 以使 `str` 数据类型在 pandas 3 中正常工作。这是为了适配 pandas 3 中字符串默认数据类型的变化，确保行为与 pandas 3 一致。修复后，现有的测试用例应能通过。

---

#### 🔴 [[SPARK-55624][PS][TESTS] Ignore ArrowDtype in tests with pandas 3](https://github.com/apache/spark/pull/54412)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 5小时前 |
| 👤 作者 | ueshin |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +32/-4 (1 文件) |

**核心内容**: 该 PR 在 pandas 3 环境下的测试中忽略 `ArrowDtype`，因为 pandas 3 默认对某些数据类型的谓词操作结果使用 `ArrowDtype`，但其值与 `BooleanDtype` 相同。这一调整确保了测试的兼容性，不涉及用户可见的变更。

---

#### 🔴 [[SPARK-55622][SQL][TESTS] Add test for DSV2 Metadata Tables on SessionCatalog](https://github.com/apache/spark/pull/54411)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 6小时前 |
| 👤 作者 | szehon-ho |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +108/-1 (3 文件) |

**核心内容**: 该 PR 为 SessionCatalog 中支持多部分标识符的 DSV2 元数据表添加了单元测试，并在 InMemoryDataSource 中引入了一个模拟元数据表。此举旨在提升 Spark 的测试覆盖率，以捕获类似相关 issue 的问题。

---

#### 🔴 [[SPARK-55621][PYTHON] Fix ambiguous and unnecessary unicode usage](https://github.com/apache/spark/pull/54410)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 9小时前 |
| 👤 作者 | gaogaotiantian |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +113/-108 (22 文件) |

**核心内容**: 这个 PR 修复了代码中不必要且容易混淆的 Unicode 字符使用问题，例如将全角符号替换为标准 ASCII 字符。同时引入了 `ruff` 规则以防止未来再次出现类似问题，旨在提高代码的一致性和可读性。

---

#### 🔴 [[SPARK-55619][SQL][3.5] Fix custom metrics in case of coalesced partitions](https://github.com/apache/spark/pull/54409)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 9小时前 |
| 👤 作者 | viirya |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +68/-41 (2 文件) |

**核心内容**: 该 PR 修复了当 `DataSourceRDD` 被合并时，自定义指标跟踪不正确的问题。通过使用以任务尝试 ID 为键的 `ConcurrentHashMap` 替换 `PartitionMetricCallback`，确保在多次调用 `compute()` 时正确跟踪读取器状态。

---

#### 🔴 [[SPARK-55619][SQL][4.0] Fix custom metrics in case of coalesced partitions](https://github.com/apache/spark/pull/54408)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 9小时前 |
| 👤 作者 | viirya |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +69/-41 (2 文件) |

**核心内容**: 该 PR 修复了在合并分区（如使用 `.coalesce(1)`）时自定义指标不准确的问题。通过将 `PartitionMetricCallback` 替换为以任务尝试 ID 为键的 `ConcurrentHashMap`，确保在多次调用 `compute()` 时正确跟踪读取器状态。

---

#### 🔴 [[SPARK-55619][SQL][4.1] Fix custom metrics in case of coalesced partitions](https://github.com/apache/spark/pull/54407)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 9小时前 |
| 👤 作者 | viirya |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +69/-41 (2 文件) |

**核心内容**: 该 PR 修复了在分区合并（coalesced）情况下自定义指标跟踪错误的问题。通过将 `PartitionMetricCallback` 替换为基于任务尝试 ID 的 `ConcurrentHashMap`，确保在多次调用 `compute()` 时正确跟踪读取器状态并更新指标。

---

#### 🔴 [[SPARK-54657][PS] Refactor pyspark.sql.pandas.serializers for readability/reuse](https://github.com/apache/spark/pull/54406)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 9小时前 |
| 👤 作者 | devin-petersohn |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +1103/-919 (5 文件) |

**核心内容**: 该 PR 对 `pyspark.sql.pandas.serializers` 模块进行了重构，以提高代码可读性和复用性。通过拆分和复用相似逻辑，优化了代码结构，但不影响用户功能。

---

#### 🔴 [[SPARK-51834][SQL][FOLLOW-UP][4.1] Add missing `.withConstraints()` in `AtomicReplaceTableExec`](https://github.com/apache/spark/pull/54404)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 12小时前 |
| 👤 作者 | yyanyy |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +72/-3 (7 文件) |

**核心内容**: 这个 PR 修复了 `AtomicReplaceTableExec` 中遗漏的 `.withConstraints()` 调用，导致使用 `StagingTableCatalog` 时 `REPLACE TABLE` 和 `CREATE OR REPLACE TABLE` 会静默丢失约束。同时修复了 `StagingInMemoryTableCatalog` 的约束转发问题，并添加了四种约束类型的回归测试。

---

#### 🔴 [[SPARK-54666][PS] Leave numeric types unchanged on `to_numeric`](https://github.com/apache/spark/pull/54403)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 12小时前 |
| 👤 作者 | devin-petersohn |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +8/-0 (2 文件) |

**核心内容**: 该 PR 修复了 `to_numeric` 方法中数值类型数据会自动转换为浮点数（可能导致精度丢失）的 Bug。变更后，数值类型将保持不变，以匹配 Pandas 的行为和用户预期。

---

#### 🔴 [[SPARK-55302][SQL][3.5] Fix custom metrics in case of `KeyGroupedPartitioning`](https://github.com/apache/spark/pull/54402)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 13小时前 |
| 👤 作者 | peter-toth |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +97/-23 (6 文件) |

**核心内容**: 该 PR 在 `PartitionReader` 中新增了 `initMetricsValues()` 方法，用于初始化自定义指标。在 `KeyGroupedPartitioning` 场景下，通过继承同一分区组中前一个 `PartitionReader` 的指标，确保了自定义指标计算的正确性。

---

#### 🔴 [[SPARK-55302][SQL][4.1] Fix custom metrics in case of `KeyGroupedPartitioning`](https://github.com/apache/spark/pull/54401)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 13小时前 |
| 👤 作者 | peter-toth |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +95/-28 (6 文件) |

**核心内容**: 这个 PR 为 `PartitionReader` 新增了 `initMetricsValues()` 方法，用于初始化自定义指标，确保在 `KeyGroupedPartitioning` 场景下多个输入分区分组时能正确计算指标。修复了自定义指标的计算问题，并新增了单元测试验证。

---

#### 🔴 [[SPARK-55302][SQL][4.0] Fix custom metrics in case of `KeyGroupedPartitioning`](https://github.com/apache/spark/pull/54400)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 13小时前 |
| 👤 作者 | peter-toth |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +95/-28 (6 文件) |

**核心内容**: 这个 PR 在 `PartitionReader` 中新增了 `initMetricsValues()` 方法，用于初始化自定义指标，确保在 `KeyGroupedPartitioning` 场景下正确计算多个输入分组的指标。变更修复了自定义指标的计算逻辑，并通过新增单元测试验证了修复效果。

---

#### 🔴 [[SPARK-55619][SQL] Fix custom metrics in case of coalesced partitions](https://github.com/apache/spark/pull/54399)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 13小时前 |
| 👤 作者 | viirya |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +69/-41 (2 文件) |

**核心内容**: 该 PR 修复了在合并分区情况下自定义指标不准确的问题，通过使用以任务尝试 ID 为键的 ConcurrentHashMap 替换原有的 PartitionMetricCallback 来正确跟踪读取器状态。这确保了在 DataSourceRDD 合并时，多个 compute() 调用之间的指标能够正确刷新和传递。

---

#### 🔴 [[SPARK-55502][PYTHON] Unify UDF and UDTF Arrow conversion error handling](https://github.com/apache/spark/pull/54398)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 14小时前 |
| 👤 作者 | Yicong-Huang |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +54/-83 (3 文件) |

**核心内容**: 该 PR 移除了 `PandasToArrowConversion.convert()` 方法中的 `is_udtf` 参数，统一了 UDF 和 UDTF 的 Arrow 转换错误处理逻辑。主要变更包括简化异常处理机制，并使用通用的 `PySparkTypeError`/`PySparkValueError` 替代 UDTF 特有的错误类型，以提升代码可维护性和错误消息的一致性。

---

#### 🔴 [[SPARK-54835][SQL][TESTS][FOLLOWUP] Drain listener bus before registering listener in test](https://github.com/apache/spark/pull/54397)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 16小时前 |
| 👤 作者 | cloud-fan |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +2/-0 (1 文件) |

**核心内容**: 该 PR 是对测试用例的修复，在注册 `QueryExecutionListener` 之前先清空监听总线，以避免其他测试的遗留事件导致当前测试出现不稳定的计数错误。这是对先前 PR 的跟进，仅涉及测试逻辑的调整，不影响用户功能。

---

#### 🔴 [[SPARK-55619][SQL] Fix custom metrics in case of coalesced partitions](https://github.com/apache/spark/pull/54396)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 20小时前 |
| 👤 作者 | peter-toth |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +63/-41 (2 文件) |

**核心内容**: 该 PR 修复了在分区合并情况下自定义指标计算错误的问题。它通过回退之前的修改，并采用新的方式在任务完成监听器中更新指标，确保在 `DataSourceRDD.compute()` 多次调用时指标计算正确。新增了单元测试验证修复效果。

---

#### 🔴 [[SPARK-55618][BUILD] Upgrade sbt to `1.12.3`](https://github.com/apache/spark/pull/54395)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 21小时前 |
| 👤 作者 | LuciferYang |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +1/-1 (1 文件) |

**核心内容**: 该 PR 提议将构建工具 sbt 升级到版本 1.12.3，以修复该版本中的若干问题。此次升级不涉及面向用户的变更，且已通过 GitHub Actions 测试验证。

---

#### 🔴 [[SPARK-55617] Add VariantGet to V2ExpressionBuilder for DSv2 filter pushdown](https://github.com/apache/spark/pull/54394)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | qlong |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +70/-2 (2 文件) |

**核心内容**: 该 PR 在 V2ExpressionBuilder 中添加了 VariantGet 支持，使 variant_get 和 try_variant_get 谓词能转换为 V2 UserDefinedScalarFunc 并下推到连接器。这旨在支持 Iceberg 中 shredded variant 列的文件级跳过功能，目前仅支持可折叠路径和直接表列引用。

---

#### 🔴 [[SPARK-55616][BUILD] Bump RoaringBitmap 1.6.10 which backs to Maven Central](https://github.com/apache/spark/pull/54393)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | pan3793 |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +10/-22 (6 文件) |

**核心内容**: 该 PR 将 RoaringBitmap 依赖版本从 1.6.0 升级到 1.6.10，以移除对第三方 Maven 仓库 JitPack 的依赖，因为 JitPack 有时速度较慢。此次更新有助于保持第三方依赖的最新状态，并优化构建过程。

---

#### 🔴 [[SPARK-55296][PS][FOLLOW-UP] Fix CoW mode not to break groupby](https://github.com/apache/spark/pull/54392)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | ueshin |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +16/-5 (2 文件) |

**核心内容**: 这个 PR 修复了 CoW（写时复制）模式下过早断开锚点导致 `groupby` 功能异常的问题，将断开锚点的操作延迟到实际更新时执行。该变更使 Spark 的行为更接近 pandas 3，并通过现有测试验证了修复效果。

---

#### 🔴 [[SPARK-54975][SQL][TESTS][FOLLOW-UP] Split MergeIntoSchemaEvolutionTests](https://github.com/apache/spark/pull/54391)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | szehon-ho |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +3167/-2889 (7 文件) |

**核心内容**: 该 PR 将 `MergeIntoSchemaEvolutionTests` 拆分为多个子特性，以解决测试文件因代码覆盖率工具插桩导致编译字节码超过 64KB 限制的问题。这是一个仅涉及测试的重构，不引入任何用户可见的变更。

---

#### 🔴 [[SPARK-55615][PYTHON][CONNECT] Move SparkContext import into class branch](https://github.com/apache/spark/pull/54390)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | gaogaotiantian |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +2/-2 (1 文件) |

**核心内容**: 该 PR 将 `SparkContext` 的导入语句移至经典模式的分支中，以解决在仅使用 Connect 客户端时因无法导入 `pyspark.core` 而导致的失败问题。此变更确保了代码在 Connect 环境下的兼容性，同时不影响完整 PySpark 环境的功能。

---

#### 🔴 [[SPARK-55610][PYTHON] Add getExecutorInfos to StatusTracker in Python](https://github.com/apache/spark/pull/54389)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | WweiL |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +65/-3 (4 文件) |

**核心内容**: 该 PR 为 PySpark 的 StatusTracker 添加了 getExecutorInfos 方法，补全了 Python 端缺失的 API。现在用户可以通过 PySpark 获取执行器的详细信息，包括主机、端口、缓存大小等。

---

#### 🔴 [[SPARK-55613][PYTHON][TESTS] Add main block for tests that are missing it](https://github.com/apache/spark/pull/54388)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | gaogaotiantian |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +6/-0 (1 文件) |

**核心内容**: 该 PR 为缺少 `main` 块的测试文件添加了 `main` 块，以确保这些测试在 CI 中能够正确执行。原因是这些测试目前无法通过模块直接运行的方式被 CI 执行到。

---

#### 🔴 [[SPARK-55614][BUILD] Add AGENTS.MD](https://github.com/apache/spark/pull/54387)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | szehon-ho |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +14/-0 (1 文件) |

**核心内容**: 这个 PR 添加了 AGENTS.MD 文件，旨在帮助 AI 开发工具（如 Claude Code/Cursor）更好地理解如何构建 Spark 和运行测试。该文件优化了开发流程，默认使用更快的 SBT 替代 Maven。

---

#### 🔴 [[SPARK-54599][PYTHON][FOLLOWUP][4.0] Remove another error message check to make CI happy](https://github.com/apache/spark/pull/54385)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | gaogaotiantian |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +0/-2 (1 文件) |

**核心内容**: 这个 PR 移除了针对 branch-4.0 分支客户端测试中的另一个错误信息检查，目的是为了让 CI 持续集成测试通过。变更原因与之前的 PR #54353 相同，属于后续的维护性调整。

---

#### 🔴 [[SPARK-55612][PYTHON][TESTS] Add test_dataframe_query_context to modules](https://github.com/apache/spark/pull/54384)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | gaogaotiantian |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +24/-0 (2 文件) |

**核心内容**: 该 PR 将 `test_dataframe_query_context` 和 `test_parity_dataframe_query_context` 测试用例添加到 `modules.py` 中，并修复了相关测试失败问题。这些测试此前未包含在 CI 流程中，且因依赖问题导致运行失败。此变更旨在确保测试能正常执行并集成到持续集成系统中。

---

#### 🔴 [[SPARK-55607][PYTHON][TESTS] Skip test_session if we should not test connect](https://github.com/apache/spark/pull/54383)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | gaogaotiantian |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +9/-2 (1 文件) |

**核心内容**: 该 PR 提议在不需要测试 Spark Connect 时跳过 `test_session` 测试，以修复仅使用经典模式的 CI 失败问题。此变更不涉及用户可见的功能调整。

---

#### 🔴 [[SPARK-55600][PYTHON] Fix pandas to arrow loses row count when schema has 0 columns on classic](https://github.com/apache/spark/pull/54382)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | Yicong-Huang |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +67/-17 (2 文件) |

**核心内容**: 这个 PR 修复了在经典 Spark 中从 pandas DataFrame 创建 Spark DataFrame 时，当 schema 包含 0 列时导致行数丢失的问题。修复后，即使 DataFrame 没有列，也能正确保留并返回行数信息。

---

#### 🔴 [[SPARK-55493] [SS] Do not mkdirs in streaming checkpoint offset/commit log directory in StateDataSource](https://github.com/apache/spark/pull/54381)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | liviazhu |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +137/-15 (8 文件) |

**核心内容**: 该 PR 修改了 StateDataSource 的行为，使其在处理流式检查点的偏移量和提交日志目录时不再尝试创建目录。通过引入只读模式的工具函数，允许 StateDataSource 在只读检查点上使用，避免不必要的目录创建操作。

---

#### 🔴 [[SPARK-55605][BUILD][DOCS] Bump dev.ludovic.netlib 3.1.1 and update docs](https://github.com/apache/spark/pull/54380)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | pan3793 |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +7/-6 (3 文件) |

**核心内容**: 该 PR 将 Spark 项目中的 dev.ludovic.netlib 依赖升级到 3.1.1 版本，并同步更新了相关文档。新版本增加了允许原生库的系统属性开关、支持 JDK 25 测试、现代化开发容器以及 macOS Apple Accelerate 框架支持。

---

#### 🔴 [[SPARK-55604][INFRA] Make `actions/*` GitHub Actions jobs up-to-date](https://github.com/apache/spark/pull/54377)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2天前 |
| 👤 作者 | dongjoon-hyun |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +118/-118 (15 文件) |

**核心内容**: 该 PR 旨在更新 GitHub Actions 中 `actions/*` 相关作业的依赖版本，以确保 CI 系统保持最新状态。具体变更包括将 `actions/checkout`、`actions/cache` 等多个核心 Action 从旧版本升级至最新版本（如 v6、v8 等）。

---

#### 🔴 [[SPARK-55603][K8S] Improve `removeExecutorFromK8s` to use `patch` instead of `edit` API](https://github.com/apache/spark/pull/54376)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2天前 |
| 👤 作者 | dongjoon-hyun |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +14/-18 (2 文件) |

**核心内容**: 这个 PR 将 Kubernetes 中的 `removeExecutorFromK8s` 方法从使用 `edit` API 改为使用 `patch` API，以提高网络效率和减少并发冲突风险。通过只传输变更内容而非完整资源，该方法降低了控制平面开销并避免了 409 错误。

---

#### 🔴 [[SPARK-55296][PS] Support CoW mode with pandas 3](https://github.com/apache/spark/pull/54375)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2天前 |
| 👤 作者 | ueshin |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +140/-65 (4 文件) |

**核心内容**: 该 PR 为 Spark 的 pandas API (PS) 增加了对 pandas 3 “写时复制” (CoW) 模式的支持。此举旨在使 Spark 的行为与 pandas 3 的默认行为保持一致，即修改数据时不再影响原始引用。

---

#### 🔴 [[SPARK-55597][INFRA] Add initial issue templates for spark](https://github.com/apache/spark/pull/54374)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2天前 |
| 👤 作者 | gaogaotiantian |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +161/-0 (2 文件) |

**核心内容**: 该 PR 为 Spark 项目添加了初始的 Issue 模板，以帮助社区提交更规范的反馈。模板涵盖 Bug 和功能增强等类型，未来可根据使用情况逐步优化。

---

#### 🔴 [[SPARK-55601][SS] Hook StreamingSourceIdentifyingName into MicrobatchExecution for source naming](https://github.com/apache/spark/pull/54373)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2天前 |
| 👤 作者 | ericm-db |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +758/-220 (15 文件) |

**核心内容**: 该 PR 将 `streamingSourceIdentifyingName` 从显式传递改为通过 `DataSource` 的 `lazy val` 派生，简化了 `StreamingRelation` 的构造。同时，在 `MicroBatchExecution` 中从 `StreamingRelation` 提取源名称，用于在查询执行时为 `OffsetMap` 提供键。这是实现源命名功能的最后一步。

---


## Apache Iceberg

> 仓库: https://github.com/apache/iceberg

### 📋 Issues (4)

#### 🔴 [Kafka Connect: CVE-2025-67721 in io.airlift:aircompressor 2.0.2](https://github.com/apache/iceberg/issues/15378)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 20小时前 |
| 👤 作者 | rmoff |
| 🏷️ 状态 | OPEN |

**核心内容**:这个 Issue 指出 Kafka Connect 运行时依赖的 `io.airlift:aircompressor:2.0.2` 存在 CVE-2025-67721 高危漏洞，可能导致缓冲区内容泄露。目前上游修复 PR 尚未合并，计划等待 2.0.3 版本发布后，通过在构建配置中强制升级依赖来修复该问题。

---

#### 🔴 [Make BaseTransaction#cleanUpOnCommitFailure package-private](https://github.com/apache/iceberg/issues/15377)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 20小时前 |
| 👤 作者 | deniskuzZ |
| 🏷️ 状态 | OPEN |
| 🏷️ 标签 | `improvement` |

**核心内容**: 该 Issue 请求将 BaseTransaction#cleanUpOnCommitFailure 方法改为包私有（package-private），以支持多表事务功能并复用 BaseTransaction。提交者表示愿意独立贡献此改进。

---

#### 🔴 [bump roaringbitmap for spark 4.2 integration](https://github.com/apache/iceberg/issues/15370)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | kevinjqliu |
| 🏷️ 状态 | OPEN |

**核心内容**: 这个 Issue 跟踪了将 roaringbitmap 从 1.3.0 升级到 1.6.0 的进展，该升级此前因担心使用 jitpack 仓库的下游影响而被暂时回退。目的是确定最佳后续步骤以推进该升级，为 Spark 4.2 集成做准备。

---

#### 🔴 [RemoveDanglingDeleteFiles does not support branches and skips unpartitioned tables](https://github.com/apache/iceberg/issues/15369)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | pratikpandey21 |
| 🏷️ 状态 | OPEN |
| 🏷️ 标签 | `improvement` |

**核心内容**: RemoveDanglingDeleteFiles 操作目前存在两个问题：一是会跳过未分区的表，二是仅支持主分支而无法处理其他分支。建议通过添加 toBranch 方法来支持指定分支，以便在合并到主分支前清理分支上的悬挂删除文件。

---

### 🔀 Pull Requests (27)

#### 🔴 [[Spec] Add Spark MERGE INTO fields in snapshot summary](https://github.com/apache/iceberg/pull/15390)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 6小时前 |
| 👤 作者 | szehon-ho |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +15/-0 (1 文件) |
| 🏷️ 标签 | `Specification` |

**核心内容**: 这个 PR 在快照摘要中添加了 Spark MERGE INTO 相关字段。它实现了 Apache Iceberg #15014 中新增的快照属性。

---

#### 🔴 [API: Introduce an abortTransaction() API](https://github.com/apache/iceberg/pull/15389)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 9小时前 |
| 👤 作者 | deniskuzZ |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +134/-4 (4 文件) |
| 🏷️ 标签 | `API` `parquet` `core` |

**核心内容**: 这个 PR 引入了一个新的 `abortTransaction()` API，用于中止事务操作。该功能旨在提供更灵活的事务管理能力，允许用户在需要时取消正在进行的操作。

---

#### 🔴 [Data: Support listing files from hive partitions with subdirectories](https://github.com/apache/iceberg/pull/15388)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 10小时前 |
| 👤 作者 | edgarRd |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +57/-5 (2 文件) |
| 🏷️ 标签 | `data` |

**核心内容**: 该 PR 为 `TableMigrationUtil` 增加了对 Hive 分区子目录中数据文件的支持，当启用 `hive.mapred.supports.subdirectories` 配置时，能够正确列出并迁移这些文件，避免遗漏数据。

---

#### 🔴 [Core: Avoid exceptions for selecting schema for metadata tables in SnapshotUtil](https://github.com/apache/iceberg/pull/15387)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 10小时前 |
| 👤 作者 | aokolnychyi |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +77/-0 (2 文件) |
| 🏷️ 标签 | `core` |

**核心内容**: 这个 PR 修复了 `SnapshotUtil` 中为元数据表选择 schema 时可能引发的异常问题。主要目的是避免在选择过程中抛出异常，从而提升代码的健壮性。

---

#### 🔴 [Revert "Move deleted files to Hadoop trash if configured (#14501)"](https://github.com/apache/iceberg/pull/15386)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 11小时前 |
| 👤 作者 | danielcweeks |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +2/-77 (2 文件) |
| 🏷️ 标签 | `core` |

**核心内容**: 这个 PR 撤销了之前将删除文件移至 Hadoop 垃圾桶的功能，原因是该功能在删除和恢复支持上不一致，且在不同环境配置下行为令人困惑。由于 Iceberg 内置了历史记录和恢复功能，因此该功能被视为不必要而被移除。

---

#### 🔴 [Spark: Support variant_get predicate pushdown for file skipping](https://github.com/apache/iceberg/pull/15385)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 13小时前 |
| 👤 作者 | qlong |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +116/-2 (4 文件) |
| 🏷️ 标签 | `spark` |

**核心内容**: 该 PR 为 Spark 增加了对 variant 列的基于清单的文件跳过功能，支持将 variant_get 和 try_variant_get 谓词下推到 Iceberg 进行文件过滤。主要变更包括在 SparkV2Filters 中将 variant_get 转换为 Expressions.extract，并添加了相应的单元测试和端到端验证。

---

#### 🔴 [Api: Support variant extract and fix manifest bounds byte order](https://github.com/apache/iceberg/pull/15384)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 13小时前 |
| 👤 作者 | qlong |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +188/-1 (6 文件) |
| 🏷️ 标签 | `API` `core` |

**核心内容**: 这个 PR 增加了对变体列提取功能的支持，修复了清单边界字节顺序问题。通过改进 ExpressionUtil 和 PathUtil 来处理变体提取项的描述和解绑，同时修正了变体边界的字节序处理以支持基于清单的文件跳过。

---

#### 🔴 [Fix typos in contribute.md documentation](https://github.com/apache/iceberg/pull/15383)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 15小时前 |
| 👤 作者 | MosheBlumbergX |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +3/-3 (1 文件) |
| 🏷️ 标签 | `docs` |

**核心内容**: 这个 PR 修复了 contribute.md 文档中的拼写错误。变更内容较小，主要是对文档中的错别字进行了修正。

---

#### 🔴 [Spark: Add separate data and metadata file lists to RewriteTablePath](https://github.com/apache/iceberg/pull/15382)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 18小时前 |
| 👤 作者 | mxm |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +94/-12 (4 文件) |
| 🏷️ 标签 | `API` `spark` `core` |

**核心内容**: 该 PR 为 RewriteTablePath 添加了独立的数据文件和元数据文件列表，以满足下游工具对这两类文件的不同处理需求（如不同存储位置或额外检查）。同时保留了原有的合并列表以确保向后兼容性。

---

#### 🔴 [Spark: Add ExecutorService support to RewriteTablePath](https://github.com/apache/iceberg/pull/15381)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 19小时前 |
| 👤 作者 | mxm |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +83/-9 (3 文件) |
| 🏷️ 标签 | `API` `spark` |

**核心内容**: 这个 PR 为 RewriteTablePath 添加了 `executeWith(ExecutorService)` 支持，以实现对版本文件和清单列表的并行元数据重写。当前版本是单线程处理，在处理大量版本文件和清单列表时可能成为性能瓶颈，并行化可以提升效率。

---

#### 🔴 [Docs: Add blog post about File Format API](https://github.com/apache/iceberg/pull/15380)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 19小时前 |
| 👤 作者 | pvary |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +136/-0 (4 文件) |
| 🏷️ 标签 | `docs` |

**核心内容**: 这个 PR 添加了一篇关于文件格式 API 的博客文章。文档更新旨在帮助开发者更好地理解和使用该 API。

---

#### 🔴 [[FLINK] Fix s3 IO unclosed instance ](https://github.com/apache/iceberg/pull/15379)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 20小时前 |
| 👤 作者 | donPain |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +649/-3 (11 文件) |
| 🏷️ 标签 | `spark` `core` `flink` `MR` `build` |

**核心内容**: 这个 PR 修复了 Flink 项目中 S3 IO 操作未关闭实例的问题，确保资源被正确释放，避免潜在的内存泄漏。

---

#### 🔴 [Spark 4.1: Refactor metadata column references to use asRef() method](https://github.com/apache/iceberg/pull/15376)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | aokolnychyi |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +24/-24 (4 文件) |
| 🏷️ 标签 | `spark` |

**核心内容**: 这个 PR 重构了 Spark 4.1 中元数据列的引用方式，改用 `asRef()` 方法。主要目的是优化代码结构，提高引用处理的规范性。

---

#### 🔴 [Spark 4.1: Simplify time travel option extraction in IcebergSource](https://github.com/apache/iceberg/pull/15375)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | aokolnychyi |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +2/-5 (1 文件) |
| 🏷️ 标签 | `spark` |

**核心内容**: 该 PR 优化了 Spark 4.1 中 IcebergSource 的时间旅行选项提取逻辑，移除了不必要的 PropertyUtil 调用，以简化代码实现。

---

#### 🔴 [Spark 4.1: Introduce modes in SparkWriteBuilder](https://github.com/apache/iceberg/pull/15374)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | aokolnychyi |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +111/-108 (1 文件) |
| 🏷️ 标签 | `spark` |

**核心内容**: 这个 PR 在 SparkWriteBuilder 中引入了模式（modes），旨在让代码更易于理解和维护。这是针对 Spark 4.1 版本的代码改进。

---

#### 🔴 [Spark, Arrow, Parquet: Add vectorized read support for parquet BYTE_STREAM_SPLIT encoding](https://github.com/apache/iceberg/pull/15373)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | jbewing |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +439/-90 (31 文件) |
| 🏷️ 标签 | `spark` `parquet` `arrow` |

**核心内容**: 该 PR 为 Apache Iceberg 添加了对 Parquet BYTE_STREAM_SPLIT 编码的向量化读取支持，解决了 Spark 在默认向量化设置下无法读取其他计算引擎写入的 Parquet v2 文件的兼容性问题。这一改进旨在提升性能并减少存储开销，避免因禁用向量化读取或强制使用 Parquet v1 规范导致的性能损失。

---

#### 🔴 [Core, Spark: Adds a Table Property for Relying on Identifier Fields](https://github.com/apache/iceberg/pull/15372)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | RussellSpitzer |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +158/-7 (5 文件) |
| 🏷️ 标签 | `spark` `core` |

**核心内容**: 这个 PR 为 Core 和 Spark 模块添加了一个表属性，允许用户向引擎表明其标识符字段具有唯一性，从而便于引擎进行优化。该功能仅作为优化提示，不强制进行约束验证，适用于所有带有标识符列的表版本。

---

#### 🔴 [API: Support timestamp types in Conversions.fromPartitionString](https://github.com/apache/iceberg/pull/15371)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | ebyhr |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +155/-0 (2 文件) |
| 🏷️ 标签 | `API` |

**核心内容**: 这个 PR 为 Conversions.fromPartitionString 方法增加了对时间戳类型的支持。该方法主要用于从 Hive 分区路径推断分区值，而 Hive 支持时间戳类型。尽管时间戳类型在分区中可能很少使用，但此功能确保了兼容性。

---

#### 🔴 [Core: Properly propagate FileIO for remote scan planning](https://github.com/apache/iceberg/pull/15368)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | nastra |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +128/-10 (5 文件) |
| 🏷️ 标签 | `core` |

**核心内容**: 这个 PR 修复了远程扫描计划中 FileIO 实例未正确传递的问题，确保从服务器获取的 PlanID 和自定义存储凭证能够被正确使用。变更解决了在从底层存储加载表时因凭证缺失导致的错误。

---

#### 🔴 [Docs: Add informational properties section for table comment](https://github.com/apache/iceberg/pull/15367)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | yguy-ryft |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +9/-0 (1 文件) |
| 🏷️ 标签 | `docs` |

**核心内容**: 该 PR 在表属性文档中新增了“信息属性”部分，专门记录 `comment` 属性的用法。此属性由 Spark 和 Flink 等引擎通过 CREATE TABLE DDL 中的 COMMENT 设置，用于提供表的语义上下文。变更基于开发邮件列表的讨论，旨在标准化相关属性的文档说明。

---

#### 🔴 [Spark 4.1: Rename expectedSchema to projection for clarity](https://github.com/apache/iceberg/pull/15366)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2天前 |
| 👤 作者 | aokolnychyi |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +69/-70 (13 文件) |
| 🏷️ 标签 | `spark` |

**核心内容**: 这个 PR 在 Spark 4.1 中将变量名 `expectedSchema` 重命名为 `projection`，以提高代码清晰度。新命名与核心模块保持一致，有助于避免在这些类中引入和固定 `schema` 时的混淆。

---

#### 🔴 [Spark 4.1: Use scan filter for conflict detection](https://github.com/apache/iceberg/pull/15365)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2天前 |
| 👤 作者 | aokolnychyi |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +15/-35 (4 文件) |
| 🏷️ 标签 | `spark` |

**核心内容**: 这个 PR 将冲突检测过滤器的推导逻辑移到了扫描操作中，以避免重复代码。主要目的是通过复用扫描过滤器来简化 Spark 4.1 中的冲突检测逻辑。

---

#### 🔴 [Spark 4.1: Remove unnecessary stats reporting from scan builder](https://github.com/apache/iceberg/pull/15364)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2天前 |
| 👤 作者 | aokolnychyi |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +0/-13 (1 文件) |
| 🏷️ 标签 | `spark` |

**核心内容**: 这个 PR 移除了 Spark 4.1 中扫描构建器不必要的统计信息报告功能。该变更基于 `SupportsReportStatistics` 应定义在 `Scan` 而非 `ScanBuilder` 上的设计原则，且早期相关的统计信息检查漏洞已于 2022 年修复。

---

#### 🔴 [Spark 4.1: Use table IDs in scan equals/hashCode](https://github.com/apache/iceberg/pull/15363)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2天前 |
| 👤 作者 | aokolnychyi |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +20/-3 (4 文件) |
| 🏷️ 标签 | `spark` |

**核心内容**: 这个 PR 在 Spark 4.1 中为扫描操作的 equals 和 hashCode 方法添加了表 ID 的支持。这一变更旨在优化扫描对象的比较和哈希计算，确保表 ID 被纳入一致性判断中。

---

#### 🔴 [Spark, Arrow, Parquet: Add vectorized parquet read support for `DELTA_LENGTH_BYTE_ARRAY` & `DELTA_BYTE_ARRAY` encodings](https://github.com/apache/iceberg/pull/15362)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2天前 |
| 👤 作者 | jbewing |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +294/-69 (24 文件) |
| 🏷️ 标签 | `spark` `parquet` `arrow` |

**核心内容**: 该 PR 为 Iceberg 添加了对 Parquet v2 规范中 `DELTA_LENGTH_BYTE_ARRAY` 和 `DELTA_BYTE_ARRAY` 编码的向量化读取支持。这解决了 Spark 默认设置下无法读取其他引擎生成的 Parquet v2 文件的兼容性问题，并提升了读取性能。此外，还优化了内存使用并增强了测试覆盖率。

---

#### 🔴 [Spark 4.1: Use enum conf parser for isolation level](https://github.com/apache/iceberg/pull/15361)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2天前 |
| 👤 作者 | aokolnychyi |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +4/-3 (1 文件) |
| 🏷️ 标签 | `spark` |

**核心内容**: 这个 PR 在 Spark 4.1 中为隔离级别配置引入了枚举解析值，替换了原有的解析方式。这一变更旨在提高配置处理的类型安全性和一致性。

---

#### 🔴 [Spark 4.1: Add BaseSparkScanBuilder](https://github.com/apache/iceberg/pull/15360)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2天前 |
| 👤 作者 | aokolnychyi |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +359/-331 (4 文件) |
| 🏷️ 标签 | `spark` |

**核心内容**: 这个 PR 为 Spark 4.1 新增了 `BaseSparkScanBuilder` 类，用于支持 PR #15240 的相关功能。该类将作为基础组件被其他模块引用。

---


## Apache Paimon

> 仓库: https://github.com/apache/paimon

### 📋 Issues

_过去 24 小时内没有新的 Issue_

### 🔀 Pull Requests (4)

#### 🔴 [[BUILD] Add `AGENTS.md`](https://github.com/apache/paimon/pull/7297)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 16小时前 |
| 👤 作者 | Zouxxyy |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +53/-2 (2 文件) |

**核心内容**: 这个 PR 添加了 `AGENTS.md` 文件，旨在为 AI 智能体提供项目开发指南，部分参考了 Apache Spark 的同类文件。作者通过实际测试展示了 AI 智能体修改代码并运行测试的效果，测试耗时约 5 秒。该变更使用了 Qoder 和 gpt-5.2 等生成式 AI 工具辅助完成。

---

#### 🔴 [[test] Fix test HiveLocationTest.testExternTableLocation](https://github.com/apache/paimon/pull/7296)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 23小时前 |
| 👤 作者 | Zouxxyy |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +4/-1 (1 文件) |

**核心内容**: 这个 PR 修复了测试用例 `HiveLocationTest.testExternTableLocation` 中的问题，确保外部表位置测试的准确性。主要目的是解决相关的测试失败情况。

---

#### 🔴 [[core] Support empty dirs cleaning without bucket sub dir in orphan files cleanup](https://github.com/apache/paimon/pull/7295)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | XiaoHongbo-Hope |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +315/-4 (6 文件) |

**核心内容**: 该 PR 修复了 OrphanFilesClean 在清理孤立文件时无法删除不包含 bucket 子目录的空分区目录的问题。修复后，所有空目录（包括中间层级目录）都会被正确清理，避免残留。

---

#### 🔴 [[hotfix] Reorganize .gitignore for better readability and add AI assistant entries](https://github.com/apache/paimon/pull/7294)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | Zouxxyy |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +32/-19 (1 文件) |

**核心内容**: 这个 PR 重新组织了 `.gitignore` 文件，将条目按类别分组并按字母排序以提高可读性。同时新增了 `.claude`、`.cursor` 和 `.qoder` 等目录，用于忽略 AI 助手的配置文件。

---


## Ray

> 仓库: https://github.com/ray-project/ray

### 📋 Issues (12)

#### 🔴 [[Serve] Disallow model multiplexing on ingress replicas; ensure it works on downstream replicas in direct ingress mode](https://github.com/ray-project/ray/issues/61227)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1小时前 |
| 👤 作者 | abrarsheikh |
| 🏷️ 状态 | OPEN |
| 🏷️ 标签 | `contribution-welcome` |

**核心内容**: 该 Issue 提出应禁止在入口副本上使用模型多路复用功能，并确保在直接入口模式下，下游副本能正确通过 `DeploymentHandle` 使用多路复用。主要任务包括添加验证逻辑、更新文档以及增加测试用例以验证模型 ID 的正确传播。

---

#### 🔴 [[Serve] Turn same event loop flags on by default](https://github.com/ray-project/ray/issues/61226)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1小时前 |
| 👤 作者 | abrarsheikh |
| 🏷️ 状态 | OPEN |
| 🏷️ 标签 | `contribution-welcome` |

**核心内容**: 该 Issue 提议将 `RUN_USER_CODE_IN_SEPARATE_THREAD` 和 `RUN_ROUTER_IN_SEPARATE_LOOP` 两个事件循环标志默认设置为 0，以优化 Serve 的默认行为。这旨在通过调整默认配置来改进事件循环的处理方式。

---

#### 🔴 [[Serve] set RAY_SERVE_RUN_SYNC_IN_THREADPOOL=1](https://github.com/ray-project/ray/issues/61225)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1小时前 |
| 👤 作者 | abrarsheikh |
| 🏷️ 状态 | OPEN |
| 🏷️ 标签 | `contribution-welcome` |

**核心内容**: 该 Issue 涉及将 Ray Serve 的同步方法默认运行方式从主事件循环迁移到线程池，以避免阻塞异步操作。需要将默认环境变量 `RAY_SERVE_RUN_SYNC_IN_THREADPOOL` 从 0 改为 1，并提醒用户确保线程安全或改用异步方法。

---

#### 🔴 [[Data] Refactor test_numpy.py to remove redundant file I/O tests](https://github.com/ray-project/ray/issues/61224)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2小时前 |
| 👤 作者 | yuhuan130 |
| 🏷️ 状态 | OPEN |
| 🏷️ 标签 | `community-backlog` |

**核心内容**: 该 Issue 提议重构 `test_numpy.py`，移除冗余的文件 I/O 测试和重复的往返测试，以简化测试逻辑。主要保留 NumPy 特定的测试（如 `np.load/np.save`）和内存操作相关测试，将通用文件 I/O 行为测试提升至 `FileBasedDatasource` 层级。

---

#### 🔴 [[Data] Refactor test_binary.py to remove redundant file I/O tests](https://github.com/ray-project/ray/issues/61223)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 3小时前 |
| 👤 作者 | yuhuan130 |
| 🏷️ 状态 | OPEN |
| 🏷️ 标签 | `community-backlog` |

**核心内容**: 该 Issue 提议重构 `test_binary.py`，将通用的文件 I/O 测试移至 `test_file_based_datasource.py`，仅保留二进制格式特定的测试。具体将移除已在基类测试过的 `test_read_binary_files_with_fs` 方法，以消除冗余测试。

---

#### 🔴 [[Data] Audit and refactor file based datasource tests](https://github.com/ray-project/ray/issues/61222)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 4小时前 |
| 👤 作者 | yuhuan130 |
| 🏷️ 状态 | OPEN |
| 🏷️ 标签 | `community-backlog` |

**核心内容**: 该 Issue 旨在审计和重构基于文件的数据源测试，通过将通用文件 I/O 测试移至基础层来减少冗余代码。这将提高测试执行速度、优化测试组织结构并降低维护成本。

---

#### 🔴 [[Serve LLM] Excessive per-request traceback spam after vLLM EngineDeadError/replica crash](https://github.com/ray-project/ray/issues/61219)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 7小时前 |
| 👤 作者 | kouroshHakha |
| 🏷️ 状态 | OPEN |
| 🏷️ 标签 | `bug` `triage` `llm` |

**核心内容**: 当 vLLM 引擎副本因资源不足等原因崩溃时，Ray Serve LLM 会对每个失败的请求重复输出冗长的堆栈跟踪，导致日志泛滥，难以定位根本原因。用户希望引入速率限制和熔断机制，避免重复日志，同时保持副本重启功能。

---

#### 🔴 [[Serve] Upcoming Changes in Ray Serve 2.55+](https://github.com/ray-project/ray/issues/61212)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 9小时前 |
| 👤 作者 | abrarsheikh |
| 🏷️ 状态 | OPEN |

**核心内容**: Ray Serve 2.55+ 将移除 Pydantic v1 支持，默认将同步部署方法运行在线程池中，并引入更优化的 HTTP 代理层，同时调整用户代码和请求路由器的默认线程配置。用户需提前升级依赖并根据应用需求调整相关设置。

---

#### 🔴 [Fix spikiness in blocked by min/max limits metric in serve dashboard](https://github.com/ray-project/ray/issues/61204)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 12小时前 |
| 👤 作者 | akyang-anyscale |
| 🏷️ 状态 | OPEN |
| 🏷️ 标签 | `triage` `serve` |

**核心内容**: 该 Issue 指出由于自动扩缩容决策计数器重置，导致 Serve Dashboard 中“受最小/最大限制阻塞”的指标图表出现异常波动。这是因为仅当决策计数器超过连续计数阈值时才会更新期望副本数，从而造成图表显示不平稳。

---

#### 🔴 [Support Python 3.15](https://github.com/ray-project/ray/issues/61200)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 18小时前 |
| 👤 作者 | NeilGirdhar |
| 🏷️ 状态 | OPEN |
| 🏷️ 标签 | `enhancement` `triage` `community-backlog` |

**核心内容**: 该 Issue 提议 Ray 尽早开始测试与 Python 3.15 的兼容性，以避免像过去版本那样出现较长的支持延迟。Python 3.15 带来了 JIT 编译器改进、惰性导入、性能分析器及 `frozendict` 类型等重要新特性，值得提前适配。

---

#### 🔴 [[Data] Ray Data in client mode fails with RuntimeError: Global node is not initialized when creating dataset from pandas refs](https://github.com/ray-project/ray/issues/61162)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | christhorn2 |
| 🏷️ 状态 | OPEN |
| 🏷️ 标签 | `bug` `triage` `community-backlog` |

**核心内容**: 在使用 Ray Client 连接 Kubernetes 集群时，通过 ray.data.from_pandas_refs() 创建数据集并执行操作会报错“RuntimeError: Global node is not initialized”。尽管初始化检查通过，但 Ray Data 统计管理器在客户端模式下因假设本地节点上下文而失败。

---

#### 🔴 [[Data] Support per-partition config of offsets for `read_kafka`](https://github.com/ray-project/ray/issues/61160)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2天前 |
| 👤 作者 | owenowenisme |
| 🏷️ 状态 | OPEN |
| 🏷️ 标签 | `enhancement` `P2` `data` |

**核心内容**: 该 Issue 请求为 `ray.data.read_kafka` 添加支持按分区配置起始偏移量的功能，允许用户通过嵌套字典为不同分区指定精确偏移量。同时需确保向后兼容性，处理未指定分区的默认回退逻辑以及偏移量越界等边界情况。

---

### 🔀 Pull Requests (50)

#### 🔴 [[Data] - Make operator fusion test suite medium](https://github.com/ray-project/ray/pull/61221)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 5小时前 |
| 👤 作者 | goutamvenkat-anyscale |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +1/-1 (1 文件) |
| 🏷️ 标签 | `data` `go` |

**核心内容**: 该 PR 将 operator fusion 测试套件的超时时间从默认值调整为中等时长，以解决测试执行超时的问题。这一变更旨在确保测试有足够的时间完成，避免因超时导致测试失败。

---

#### 🔴 [[1/n] [Data][DatasourceV2] Add datasource_v2 file listing infrastructure](https://github.com/ray-project/ray/pull/61220)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 6小时前 |
| 👤 作者 | goutamvenkat-anyscale |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +549/-0 (7 文件) |
| 🏷️ 标签 | `data` `data:datasources` |

**核心内容**: 这个 PR 为 DataSourceV2 引入了基础文件发现管道，包括文件清单结构、线程化文件列表索引器、可扩展的文件过滤器以及目录扩展工具。同时新增了针对 NonSamplingFileIndexer 的 29 个单元测试，以确保功能稳定性。

---

#### 🔴 [Bump werkzeug from 2.3.8 to 3.1.6 in /python](https://github.com/ray-project/ray/pull/61218)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 8小时前 |
| 👤 作者 | app/dependabot |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +3/-3 (3 文件) |
| 🏷️ 标签 | `dependencies` `python` |

**核心内容**: 该 PR 将 `/python` 目录中的 `werkzeug` 依赖从 2.3.8 升级到 3.1.6，主要包含多个安全修复和 bug 修复。新版本解决了 Windows 平台上的特殊设备名漏洞，并修复了多部分表单解析器的边界处理问题。

---

#### 🔴 [[serve][7/n] Gang scheduling -- STARTING replica cleanup](https://github.com/ray-project/ray/pull/61217)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 9小时前 |
| 👤 作者 | jeffreywang-anyscale |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +211/-0 (2 文件) |
| 🏷️ 标签 | `serve` |

**核心内容**: 该 PR 修复了 Gang 调度中孤儿副本的问题，当某个副本启动失败时，会自动停止同一 Gang 中处于 STARTING/UPDATING/RECOVERING 状态的关联副本，避免部分残留导致 PG 预订永久阻塞。通过追踪失败的 Gang ID 并强制停止相关副本，确保 Gang 调度的完整性和资源释放。

---

#### 🔴 [[serve][6/n] Gang scheduling -- rolling updates and migration](https://github.com/ray-project/ray/pull/61216)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 9小时前 |
| 👤 作者 | jeffreywang-anyscale |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +417/-29 (2 文件) |
| 🏷️ 标签 | `serve` |

**核心内容**: 该 PR 为 gang 调度的部署增加了 gang 感知的滚动更新和节点迁移功能，确保在更新或迁移时 gang 始终作为完整单元操作。滚动更新时按 gang 分组重启，迁移时 gang 成员同步移动或停止，避免部分停机。

---

#### 🔴 [[serve][5/n] Gang scheduling -- downscaling and PG recovery](https://github.com/ray-project/ray/pull/61215)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 9小时前 |
| 👤 作者 | jeffreywang-anyscale |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +330/-54 (6 文件) |
| 🏷️ 标签 | `serve` |

**核心内容**: 这个 PR 为 Gang 调度部署添加了感知 Gang 的缩放功能和 Placement Group 恢复机制。缩放时以整个 Gang 为单位进行原子操作，并优化了 PG 分配时的向下取整逻辑。此外，新增了控制器重启后恢复 PG 引用的功能，以防止部署删除时的 PG 泄漏。

---

#### 🔴 [Bump ajv in /python/ray/dashboard/client](https://github.com/ray-project/ray/pull/61214)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 9小时前 |
| 👤 作者 | app/dependabot |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +21849/-14307 (1 文件) |
| 🏷️ 标签 | `dependencies` `javascript` |

**核心内容**: 该 PR 将 `/python/ray/dashboard/client` 目录下的 `ajv` 依赖从 6.12.6 和 8.11.0 分别升级至 6.14.0 和 8.18.0。此次更新修复了潜在的安全漏洞（如 CVE-2025 相关的正则表达式利用问题），并同步更新了相关依赖。

---

#### 🔴 [[Data] Consolidate Schema Inference](https://github.com/ray-project/ray/pull/61213)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 9小时前 |
| 👤 作者 | kyuds |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +17/-24 (2 文件) |
| 🏷️ 标签 | `go` |

**核心内容**: 该 PR 将原本分散在 `Dataset` 和 `ExecutionPlan` 中的模式推断逻辑进行了整合，减少了两者之间的频繁交互。主要目的是优化代码结构，使模式推断更加集中和高效。

---

#### 🔴 [[RAY] adding cursor sub-agent directory to gitignore](https://github.com/ray-project/ray/pull/61211)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 10小时前 |
| 👤 作者 | HassamSheikh |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +3/-0 (1 文件) |
| 🏷️ 标签 | `community-contribution` |

**核心内容**: 这个 PR 将 `.cursor` 文件夹添加到 `.gitignore` 文件中，以避免将该目录下的文件提交到 Git 仓库。这通常是为了排除 Cursor 编辑器生成的临时文件或配置文件。

---

#### 🔴 [[Core] (Resource Isolation 6/n) Update killing policy interface to support multi-worker killing policy](https://github.com/ray-project/ray/pull/61210)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 10小时前 |
| 👤 作者 | Kunchd |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +273/-181 (11 文件) |
| 🏷️ 标签 | `community-contribution` |

**核心内容**: 该 PR 更新了 Ray 的 Worker 杀死策略接口，以支持未来的多 Worker 杀死策略。这解决了当前策略在内存压力下无法通过一次性杀死多个 Worker 来快速恢复内存限制的问题。

---

#### 🔴 [[train][tests] Test xgboost and lightgbm data parallel training](https://github.com/ray-project/ray/pull/61209)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 10小时前 |
| 👤 作者 | TimothySeah |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +88/-26 (2 文件) |

**核心内容**: 该 PR 改进了 `test_lightgbm_trainer` 和 `test_xgboost_trainer` 测试，通过比较验证损失来验证数据并行训练的正确性。针对 LightGBM 和 XGBoost 在验证数据集分片和指标聚合上的差异，分别采用了不同的测试策略，并在单元测试中进行了详细说明。

---

#### 🔴 [[data] Fix multi-input operator object store memory attribution to upstream operators](https://github.com/ray-project/ray/pull/61208)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 11小时前 |
| 👤 作者 | justinvyu |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +107/-45 (10 文件) |
| 🏷️ 标签 | `data` `go` |

**核心内容**: 该 PR 修复了多输入操作符（如 union、zip）的资源归属问题，解决了之前资源管理器对上游操作符重复计算内存的缺陷。现在通过跟踪每个输入队列的内存使用情况，确保每个上游操作符仅被正确扣除其产生的内存占用。这修复了 `preserve_order=True` 模式下的死锁问题，避免了因错误反压导致的阻塞。

---

#### 🔴 [[serve][4/n] Gang scheduling -- fault tolerance](https://github.com/ray-project/ray/pull/61207)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 12小时前 |
| 👤 作者 | jeffreywang-anyscale |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +374/-14 (4 文件) |
| 🏷️ 标签 | `serve` |

**核心内容**: 该 PR 为 Gang 调度部署增加了容错机制，包括实现 RESTART_GANG 运行时故障策略和控制器恢复后的泄漏 Gang 放置组检测。当副本健康检查失败时，RESTART_GANG 策略会强制停止整个 Gang 以便重新调度，同时扩展了泄漏检测逻辑以支持 Gang 放置组。

---

#### 🔴 [[serve][3/n] Gang scheduling -- core scheduling engine](https://github.com/ray-project/ray/pull/61206)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 12小时前 |
| 👤 作者 | jeffreywang-anyscale |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +1224/-36 (10 文件) |
| 🏷️ 标签 | `serve` |

**核心内容**: 这个 PR 实现了 Gang 调度的核心逻辑，通过原子化地预留放置组并协同启动副本，确保 Gang 中的所有成员要么全部成功调度，要么全部失败。修改涉及调度器、状态机和副本模块，新增了 Gang 上下文处理、预留步骤以及失败回滚机制，以支持严格的协同调度需求。

---

#### 🔴 [[serve][2/n] Gang scheduling -- validation and utilities](https://github.com/ray-project/ray/pull/61205)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 12小时前 |
| 👤 作者 | jeffreywang-anyscale |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +326/-7 (9 文件) |
| 🏷️ 标签 | `serve` `go` |

**核心内容**: 该 PR 为 Ray Serve 的 gang scheduling 奠定基础，通过扩展数据模型、添加了配置验证规则，并引入了从 GCS 查询活跃 placement group ID 的工具。测试覆盖了无效 gang_size、与 max_replicas_per_node 和 placement_group_strategy 的互斥性，以及通过 .options() 覆盖 gang config 的场景。

---

#### 🔴 [[Core] Add root logger handler so user loggers work in spawn'd subprocesses](https://github.com/ray-project/ray/pull/61203)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 13小时前 |
| 👤 作者 | xyuzh |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +20/-1 (3 文件) |
| 🏷️ 标签 | `community-contribution` |

**核心内容**: 这个 PR 修复了在使用 `multiprocessing.get_context('spawn')` 创建子进程时，用户日志记录器的 `INFO` 级别日志被静默丢弃的问题。通过在根日志记录器中添加 `PlainRayHandler`，确保用户日志能够自动传播并正确输出到 Ray 的日志文件中。

---

#### 🔴 [[Serve] increase timeout on test_cli test_status_package_unavailable_…](https://github.com/ray-project/ray/pull/61202)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 13小时前 |
| 👤 作者 | abrarsheikh |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +1/-1 (1 文件) |
| 🏷️ 标签 | `go` |

**核心内容**: 该 PR 将测试 `test_status_package_unavailable` 的超时时间从 20 秒延长至 40 秒，以适应 CI 环境中 pip 安装依赖的延迟。测试需要等待多次副本启动失败才能达到预期状态，原有超时时间不足。

---

#### 🔴 [SGLangServer: Multi-GPU Deployment (TP/PP Support) fix](https://github.com/ray-project/ray/pull/61201)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 14小时前 |
| 👤 作者 | limarkdcunha |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +99/-12 (3 文件) |
| 🏷️ 标签 | `community-contribution` |

**核心内容**: 这个 PR 修复了 sglang_engine.py 中 placement group 的构建问题，以正确支持多 GPU 部署（包括张量并行和流水线并行）。它通过资源合并模式，将 HTTP 前端和主 GPU 工作器部署在同一节点上，以最小化网络延迟。

---

#### 🔴 [[Data] Extract Unity Catalog credential resolution into dedicated function](https://github.com/ray-project/ray/pull/61199)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 19小时前 |
| 👤 作者 | ankur-anyscale |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +154/-58 (3 文件) |
| 🏷️ 标签 | `community-contribution` |

**核心内容**: 这个 PR 将 Unity Catalog 的凭证解析逻辑提取为独立的函数，并重命名了原有的凭证解析函数以明确其用途。它优化了凭证处理逻辑，将分支判断移至凭证模块，提高了代码的关注点分离。同时更新了测试以覆盖新函数和所有分支。

---

#### 🔴 [[Data] Extract Unity Catalog credential resolution into dedicated function.](https://github.com/ray-project/ray/pull/61198)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 20小时前 |
| 👤 作者 | ankur-anyscale |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +154/-58 (3 文件) |

**核心内容**: 这个 PR 将 Unity Catalog 的凭据解析逻辑提取为独立的函数 resolve_credential_provider_for_unity_catalog，并将原有的 resolve_credential_provider 重命名。通过将凭据解析的分支逻辑移至凭据模块，实现了更好的关注点分离，并更新了相关测试。

---

#### 🔴 [[llm][examples] Add manual CI for Ray Serve LLM SGLang engine](https://github.com/ray-project/ray/pull/61197)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 23小时前 |
| 👤 作者 | eicherseiji |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +92/-0 (5 文件) |
| 🏷️ 标签 | `go` `claude-code-assisted` |

**核心内容**: 这个 PR 为 Ray Serve LLM SGLang 引擎添加了手动 CI，用于验证社区开发者的 PR。它还包含必要的 `__init__.py` 文件以确保发布测试能正确识别引擎模块，且该测试不会阻塞发布流程。

---

#### 🔴 [[Data] Separate unit tests from integration-heavy tests - 1](https://github.com/ray-project/ray/pull/61196)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | Hyunoh-Yeo |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +3137/-3112 (2 文件) |
| 🏷️ 标签 | `community-contribution` |

**核心内容**: 这个 PR 将 `test_transform_pyarrow.py` 拆分为两个文件，将约 40 个纯单元测试（无 Ray 依赖）移至 `tests/unit/test_transform_pyarrow.py`，保留 5 个需要 Ray 集群的集成测试在原文件中。此举旨在提高开发迭代速度，允许单元测试无需启动 Ray 集群即可运行，并通过现有配置强制单元测试边界。

---

#### 🔴 [[core] upgrade grpc to 1.58.0 to fix getenv races](https://github.com/ray-project/ray/pull/61195)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | rueian |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +5/-5 (1 文件) |
| 🏷️ 标签 | `core` `go` |

**核心内容**: 该 PR 将 grpc 库升级到 1.58.0 版本，以解决因频繁调用 `GetEnv` 导致的竞态条件问题。升级后移除了对 `GRPC_EXPERIMENTAL_PICKFIRST_LB_CONFIG` 环境变量的依赖，避免了用户任务在任意时间调用 `setenv` 时引发的冲突。

---

#### 🔴 [[Serve] classify test_fastapi as large](https://github.com/ray-project/ray/pull/61194)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | abrarsheikh |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +1/-1 (1 文件) |
| 🏷️ 标签 | `go` `claude-code-assisted` |

**核心内容**: 这个 PR 将 `test_fastapi` 测试分类为“大型”测试，以优化测试资源分配。变更涉及 Buildkite 构建日志中的相关配置调整。

---

#### 🔴 [[docs] [example] Add multi agent example](https://github.com/ray-project/ray/pull/61193)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | Aydin-ab |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +5109/-0 (36 文件) |
| 🏷️ 标签 | `docs` `go` |

**核心内容**: 该 PR 在文档和示例中新增了一个多智能体示例，展示了多智能体协作的实现方式。

---

#### 🔴 [[Data] Added metrics to track task scheduling time, output backpressure](https://github.com/ray-project/ray/pull/61192)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | alexeykudinkin |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +549/-137 (20 文件) |
| 🏷️ 标签 | `go` |

**核心内容**: 这个 PR 新增了两个指标来跟踪任务调度时间和输出背压情况。具体包括累计任务输出背压（记录任务结果因对象存储预算不足而无法被消费的次数）和累计任务调度时间（计算任务从驱动端到工作端完成参数拉取的耗时）。

---

#### 🔴 [Download task num_cpus zero](https://github.com/ray-project/ray/pull/61191)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | kouroshHakha |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +1/-1 (1 文件) |
| 🏷️ 标签 | `go` |

**核心内容**: 该 PR 将 `initialize_node` 函数中下载任务的 `num_cpus` 设置为 0，以避免在 GPU 节点 CPU 资源耗尽时导致 LLMServer 挂起。由于下载任务主要是 I/O 密集型且无需 CPU 资源，但仍需通过 `NodeAffinitySchedulingStrategy` 调度到目标节点，此调整可优化资源使用。

---

#### 🔴 [[Data] Cleaning up `SplitCoordinator`](https://github.com/ray-project/ray/pull/61190)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | alexeykudinkin |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +43/-32 (2 文件) |
| 🏷️ 标签 | `go` |

**核心内容**: 这个 PR 重构了 `SplitCoordinator`，将启动新 epoch 的逻辑抽象到 `_try_start_new_epoch` 方法中，并移除了之前的迭代器语义。此外，它还确保在启动新 epoch 之前先关闭现有的执行器。

---

#### 🔴 [SGLangServer: Fix Sequential Batch Processing fix](https://github.com/ray-project/ray/pull/61189)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | limarkdcunha |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +10/-6 (1 文件) |
| 🏷️ 标签 | `community-contribution` |

**核心内容**: 这个 PR 修复了 SGLangServer 的顺序批处理问题。它将 completions() 函数中的顺序处理改为使用 asyncio.gather 并发处理多个提示词，从而提高了效率。

---

#### 🔴 [[core] fix symbols](https://github.com/ray-project/ray/pull/61188)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | rueian |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +2/-2 (2 文件) |

**核心内容**: 这个 PR 修复了 Ray 核心模块中的关于符号的问题。具体的变更细节和原因需要在 PR 描述中补充。

---

#### 🔴 [Releases 2.53.0 fix symbols](https://github.com/ray-project/ray/pull/61187)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | rueian |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +185/-73 (20 文件) |

**核心内容**: 该 PR 主要针对 Ray 2.53.0 版本进行符号修复，确保相关功能或接口的正确性。具体变更细节和修复原因需进一步查看代码提交记录。

---

#### 🔴 [[serve] include haproxy unit tests](https://github.com/ray-project/ray/pull/61186)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | akyang-anyscale |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +1/-25 (1 文件) |
| 🏷️ 标签 | `go` |

**核心内容**: 这个 PR 在 Ray 的 serve 模块中添加了 HAProxy 的单元测试。主要目的是确保 HAProxy 相关功能的正确性和稳定性。

---

#### 🔴 [[core] Fixing the dashboard node_head api's dead node cache.](https://github.com/ray-project/ray/pull/61185)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | israbbani |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +99/-4 (2 文件) |
| 🏷️ 标签 | `core` `go` |

**核心内容**: 这个 PR 修复了仪表板节点头部 API 中死节点缓存的问题。问题在于死节点缓存驱逐逻辑错误地覆盖了所有者节点 ID。修复旨在确保节点 ID 信息正确被保留。

---

#### 🔴 [[deps][llm] Update CI and release tests to use the updated LLM image (py312 / cu129)](https://github.com/ray-project/ray/pull/61184)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | jeffreywang-anyscale |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +103/-78 (5 文件) |
| 🏷️ 标签 | `go` `community-contribution` |

**核心内容**: 该 PR 更新了使用 Ray LLM 镜像的测试，使其适配新的 LLM 镜像（基于 Python 3.12 和 CUDA 12.9）。这是对之前引入依赖集和新 LLM CI/发布镜像的 PR 的后续跟进。

---

#### 🔴 [[RLlib] Working implementation of pettingzoo_shared_value_function.py](https://github.com/ray-project/ray/pull/61183)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | HassamSheikh |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +1709/-10 (18 文件) |
| 🏷️ 标签 | `rllib` `rllib-algorithms` `go` |

**核心内容**: 这个 PR 修复了 RLlib 中 MAPPO 实现的类继承错误、价值函数损失裁剪顺序问题以及多代理批处理逻辑的脆弱性，并添加了 30 个单元测试以提高代码健壮性。同时，优化了连接器逻辑并减少了 178 行代码，使其符合 RLlib 的现有模式。

---

#### 🔴 [[DNM][DNR] Sphinx collections: pull deployment serve llm ](https://github.com/ray-project/ray/pull/61182)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | elliot-barn |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +104/-6101 (56 文件) |

**核心内容**: 该 PR 使用 Sphinx collections 功能，将已发布的 S3 存储桶中的部署服务 LLM 示例同步到文档构建中。此变更需要在合并前先进行生产环境部署，并通过本地运行 `make local` 进行了测试验证。

---

#### 🔴 [[Tune] Remove deprecated logger_creator parameter from Trainable](https://github.com/ray-project/ray/pull/61181)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | xinyuangui2 |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +53/-71 (5 文件) |

**核心内容**: 该 PR 移除了 `Trainable` 中已弃用的 `logger_creator` 参数，并将相关逻辑迁移到 `Trainable._create_logger` 中。同时，清理了内部调用点，并在 RLlib 的 `Algorithm` 中添加了 `_create_logger` 重写以保持独立模式兼容。

---

#### 🔴 [[serve] Support scale from zero in haproxy](https://github.com/ray-project/ray/pull/61180)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | akyang-anyscale |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +189/-26 (6 文件) |

**核心内容**: 该 PR 在 HAProxy 中支持从零扩容功能，允许服务实例从零开始自动扩展。这解决了 Ray Serve 在 HAProxy 负载均衡场景下的冷启动问题。

---

#### 🔴 [add support for kafka partition config - addresses #61160](https://github.com/ray-project/ray/pull/61179)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | jake-ogle |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +298/-12 (3 文件) |
| 🏷️ 标签 | `community-contribution` |

**核心内容**: 这个 PR 新增了对 Kafka 分区配置的支持，允许用户通过嵌套字典为特定分区设置精确的起始偏移量，同时为未指定的分区保留全局默认值。代码和测试用例已更新，并经过审查修复了边缘情况和文档。

---

#### 🔴 [Bump flask from 2.1.3 to 3.1.3 in /python](https://github.com/ray-project/ray/pull/61178)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | app/dependabot |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +3/-3 (3 文件) |
| 🏷️ 标签 | `dependencies` `python` |

**核心内容**: 该 PR 将 Flask 版本从 2.1.3 升级到 3.1.3，主要修复了会话访问相关的安全问题（GHSA-68rp-wp8r-4726）。此外，升级还包含多个 Bug 修复和改进，如异步视图支持、测试客户端会话状态优化等。

---

#### 🔴 [Bump flask from 2.1.3 to 3.1.3 in /python/requirements](https://github.com/ray-project/ray/pull/61177)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | app/dependabot |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +1/-1 (1 文件) |
| 🏷️ 标签 | `dependencies` `python` |

**核心内容**: 该 PR 将 Flask 版本从 2.1.3 升级到 3.1.3，包含安全修复和多项功能改进。主要修复了会话访问标记问题、异步视图中的流处理错误以及密钥轮换时的签名密钥选择顺序问题。

---

#### 🔴 [[docs] Removing an incorrect warning for placement groups.](https://github.com/ray-project/ray/pull/61176)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | israbbani |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +0/-4 (1 文件) |
| 🏷️ 标签 | `go` |

**核心内容**: 这个 PR 修正了关于放置组（placement group）的文档错误，移除了不正确的警告说明。文档曾错误地要求显式设置 Actor 所有后代的属性以保持行为，但实际上子 Actor 会自动继承父 Actor 的 `placement_group_capture_child_tasks` 属性。

---

#### 🔴 [[ci][docker] Wire TPU images into CI build and publish pipeline](https://github.com/ray-project/ray/pull/61175)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | andrew-anyscale |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +37/-0 (2 文件) |
| 🏷️ 标签 | `ci` |

**核心内容**: 该 PR 在 Buildkite 构建流水线中添加了 TPU 镜像的构建和发布步骤，生成的镜像将标记为 `rayproject/ray:nightly-py310-tpu` 等格式。这一变更旨在将 TPU 镜像集成到 CI 构建和发布流程中，以支持 TPU 相关的持续集成。

---

#### 🔴 [[ci][docker] Generate TPU dependency lock files via raydepsets](https://github.com/ray-project/ray/pull/61174)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | andrew-anyscale |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +12122/-0 (6 文件) |
| 🏷️ 标签 | `ci` |

**核心内容**: 该 PR 在 rayimg.depsets.yaml 中添加了 TPU 依赖配置，并为 Python 3.10-3.13 生成了固定的依赖锁文件。这些 TPU 锁文件基于 CPU 基础依赖，额外包含 jax==0.5.2、jaxlib==0.5.1 和 libtpu==0.0.10.1。

---

#### 🔴 [[ci][docker] Add wanda configs for TPU Docker images](https://github.com/ray-project/ray/pull/61173)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | andrew-anyscale |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +25/-0 (2 文件) |
| 🏷️ 标签 | `ci` |

**核心内容**: 该 PR 为构建 TPU Ray Docker 镜像添加了 Wanda YAML 配置文件。TPU 镜像基于 ubuntu:22.04，并使用包含 jax[tpu] 和 libtpu 依赖的 TPU 专用锁定文件。

---

#### 🔴 [[ci][docker] Add TPU as a recognized platform for Ray Docker images](https://github.com/ray-project/ray/pull/61172)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | andrew-anyscale |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +22/-1 (5 文件) |
| 🏷️ 标签 | `ci` |

**核心内容**: 这个 PR 为 Ray Docker 镜像添加了 TPU 作为受支持的平台，更新了标签格式以支持 `--platform tpu` 参数。使用该参数生成的 Docker 镜像将带有 `-tpu` 后缀（如 `nightly-py310-tpu`）。

---

#### 🔴 [[RLlib] Adding torch gpu test again](https://github.com/ray-project/ray/pull/61171)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | HassamSheikh |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +14/-9 (1 文件) |
| 🏷️ 标签 | `rllib` `go` |

**核心内容**: 这个 PR 重新引入了之前启用的 Torch GPU 测试，该测试之前被 APPO 相关的 PR 覆盖。目的是恢复 GPU 测试功能以确保兼容性。

---

#### 🔴 [[deps] adding --no-upgrade as a default flag](https://github.com/ray-project/ray/pull/61170)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | elliot-barn |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +11/-6 (4 文件) |

**核心内容**: 这个 PR 将 `--no-upgrade` 作为 `raydepsets uv` 的默认标志，以防止依赖项自动升级。这是针对 GitHub issue #61169 的长期修复方案。

---

#### 🔴 [[deps] recompiling depsets](https://github.com/ray-project/ray/pull/61169)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | elliot-barn |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +6/-6 (2 文件) |
| 🏷️ 标签 | `go` |

**核心内容**: 这个 PR 重新编译了依赖集作为临时修复方案。由于 UV 拉取了最新发布的 virtualenv 20.38.0 版本（因 20.37.0 已从 PyPI 移除），需要紧急调整依赖配置。

---

#### 🔴 [[Train] Add exclude_resources and worker_cpus options to training_ingest benchmark](https://github.com/ray-project/ray/pull/61168)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | justinvyu |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +20/-2 (3 文件) |

**核心内容**: 该 PR 为训练摄入基准测试添加了 exclude_resources 和 worker_cpus 选项，以支持异构设置中训练工作节点预留 CPU。目的是评估跨节点传输是否导致额外的数据溢出，以及修复数据对象存储内存预算是否能缓解问题。

---


## Lance

> 仓库: https://github.com/lance-format/lance

### 📋 Issues (3)

#### 🔴 [Java - create fragment with a new schema](https://github.com/lance-format/lance/issues/5972)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 8小时前 |
| 👤 作者 | jackye1995 |
| 🏷️ 状态 | OPEN |

**核心内容**: 这个 Issue 提出需要在 Java 中实现基于新 schema 创建 fragment 的功能，以支持使用不同 schema 的 REPLACE TABLE AS SELECT 操作。该需求与另一个 PR 相关，可能需要协同修复。

---

#### 🔴 [Allow the part files to be skipped when training FTS](https://github.com/lance-format/lance/issues/5970)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 13小时前 |
| 👤 作者 | westonpace |
| 🏷️ 状态 | OPEN |

**核心内容**: 该 Issue 提议优化 FTS 索引构建过程，通过将分词与最终索引构建并行化，跳过中间的磁盘写入步骤。这一改进预计能将索引构建时间缩短约一半，并显著减少临时磁盘空间占用，但可能增加内存使用。

---

#### 🔴 [Java - support commit transaction to create a new table](https://github.com/lance-format/lance/issues/5969)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 13小时前 |
| 👤 作者 | jackye1995 |
| 🏷️ 状态 | OPEN |

**核心内容**: 该 Issue 指出在 Spark 中实现 CTAS（创建表并加载数据）时，受限于 Java SDK 必须先创建表再提交数据片段，导致功能受限。由于 Rust 端已支持该特性，需在 Java SDK 中添加支持事务提交以创建新表的功能。

---

### 🔀 Pull Requests (2)

#### 🔴 [feat: serialize storage options in table identifier proto](https://github.com/lance-format/lance/pull/5973)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 6小时前 |
| 👤 作者 | LuQQiu |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +56/-15 (2 文件) |
| 🏷️ 标签 | `enhancement` |

**核心内容**: 该 PR 在表标识符协议中添加了存储选项序列化功能，以便传递存储凭证或相关信息。同时，它将 `filtered_read_exec` 函数中的 `dataset` 参数设为可选，并在未提供时回退到从协议的表标识符中打开数据。

---

#### 🔴 [chore(deps): bump werkzeug from 3.1.3 to 3.1.6 in /python](https://github.com/lance-format/lance/pull/5971)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 10小时前 |
| 👤 作者 | app/dependabot |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +3/-3 (1 文件) |
| 🏷️ 标签 | `python` `chore` `dependencies` `python:uv` |

**核心内容**: 该 PR 将 Werkzeug 依赖从版本 3.1.3 升级到 3.1.6，修复了多个安全漏洞和错误。主要改进包括增强 Windows 平台上 `safe_join` 对特殊设备名称的限制、修复多部分表单解析器的边界处理问题，以及解决 `DebuggedApplication` 初始化时的属性错误。

---


## LanceDB

> 仓库: https://github.com/lancedb/lancedb

### 📋 Issues (6)

#### 🔴 [Python: Expand test suite for minimal dependency test](https://github.com/lancedb/lancedb/issues/3054)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 12小时前 |
| 👤 作者 | wjones127 |
| 🏷️ 状态 | OPEN |

**核心内容**: 该 Issue 提议扩展 Python 最小依赖测试的范围，以便在缺少 `pylance` 或 `pandas` 的情况下运行大部分测试。同时需确保测试仅在真正需要时才使用 pandas，例如避免因缺少 pandas 而跳过与 pydantic 相关的测试。这有助于捕获潜在问题（如 #3053）。

---

#### 🔴 [Import error in Python when using namespace](https://github.com/lancedb/lancedb/issues/3053)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 12小时前 |
| 👤 作者 | wjones127 |
| 🏷️ 状态 | OPEN |

**核心内容**: 在使用命名空间时，LanceDB 因缺少对 `lance` 模块的显式依赖而引发导入错误，尽管该依赖是可选的以保持包体积小。问题发生在尝试连接或创建命名空间时，提示需要安装 `pylance` 包才能解决。

---

#### 🔴 [Java - creating empty table](https://github.com/lancedb/lancedb/issues/3052)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | jackye1995 |
| 🏷️ 状态 | OPEN |

**核心内容**: 该 Issue 指出在 Java 中创建空表（即通过无数据的 Arrow IPC 流创建表）的操作不够直观，建议添加一些工具函数以改善用户体验。

---

#### 🔴 [Java - setting custom index parameters](https://github.com/lancedb/lancedb/issues/3051)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | jackye1995 |
| 🏷️ 状态 | OPEN |

**核心内容**: 该 Issue 要求提供在 Java 中设置自定义索引参数（如 num_partitions）的示例。部分参数可能需要通过更新命名空间规范和远程实现来支持。

---

#### 🔴 [Java - return Arrow IPC stream instead of raw bytes](https://github.com/lancedb/lancedb/issues/3050)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | jackye1995 |
| 🏷️ 状态 | OPEN |

**核心内容**: 该 Issue 指出当前 Java SDK 要求用户手动解析 Arrow 流字节为 Arrow IPC 流类，体验不够友好。建议将解析逻辑封装为工具函数，方便用户直接使用。

---

#### 🔴 [Java - auto retry throttling error in the SDK](https://github.com/lancedb/lancedb/issues/3049)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | jackye1995 |
| 🏷️ 状态 | OPEN |

**核心内容**: 客户报告 SDK 遇到限流等错误时未自动重试，需要手动添加重试逻辑。该 Issue 要求更新远程连接以返回限流错误类型，并在客户端实现自动重试机制。

---

### 🔀 Pull Requests (2)

#### 🔴 [chore: update lance dependency to v3.0.0-beta.4](https://github.com/lancedb/lancedb/pull/3056)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 8小时前 |
| 👤 作者 | lancedb-robot |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +96/-125 (10 文件) |
| 🏷️ 标签 | `Python` `Rust` `chore` |

**核心内容**: 该 PR 将 Lance Rust 依赖升级到 v3.0.0-beta.4，并同步更新 Java lance-core 版本至 3.0.0-beta.4。同时调整默认配置并升级 Rust 工具链至 1.91.0，以满足新 Lance 的要求。

---

#### 🔴 [fix: update DatasetConsistencyWrapper to accept same-version updates](https://github.com/lancedb/lancedb/pull/3055)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 9小时前 |
| 👤 作者 | wjones127 |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +6/-2 (3 文件) |
| 🏷️ 标签 | `bug` `Rust` |

**核心内容**: 该 PR 修复了 `DatasetConsistencyWrapper::update()` 方法，将其版本检查从严格大于 (`>`) 改为大于等于 (`>=`)，以接受同版本的数据集更新。这解决了 `migrate_manifest_paths_v2` 在重命名文件但不增加版本号时更新被静默丢弃的问题，确保后续调用能获取到最新的缓存数据集。

---


## Daft

> 仓库: https://github.com/Eventual-Inc/Daft

### 📋 Issues (1)

#### 🔴 [SQL: DATE_TRUNC function not found](https://github.com/Eventual-Inc/Daft/issues/6257)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | desmondcheongzx |
| 🏷️ 状态 | OPEN |
| 🏷️ 标签 | `enhancement` `p2 (backlog)` |

**核心内容**: 该 Issue 指出在 Daft 的 SQL 接口中使用 `DATE_TRUNC` 函数会报错，尽管底层内核支持该功能且 Python API 可以正常调用。问题原因包括函数注册时的静默失败和内部命名不匹配，导致 SQL 无法识别 `date_trunc`。期望修复后 SQL 能正确支持 `DATE_TRUNC`，使其行为与 Python API 和标准 SQL 保持一致。

---

### 🔀 Pull Requests (32)

#### 🔴 [refactor(arrow2): misc deprecation warnings](https://github.com/Eventual-Inc/Daft/pull/6270)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 7小时前 |
| 👤 作者 | universalmind303 |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +24/-29 (5 文件) |
| 🏷️ 标签 | `refactor` |

**核心内容**: 这个 PR 对 arrow2 项目进行了重构，主要修复了各种废弃警告。变更旨在清理代码中的废弃提示，提升代码质量和兼容性。

---

#### 🔴 [refactor(swordfish): Streaming flight shuffle read](https://github.com/Eventual-Inc/Daft/pull/6269)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 7小时前 |
| 👤 作者 | colin-ho |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +318/-168 (9 文件) |
| 🏷️ 标签 | `refactor` |

**核心内容**: 这个 PR 将 FlightShuffleRead 从静态配置的源节点重构为通过通道动态接收输入的流式源节点，与其他源类型保持一致。主要改进包括调整枚举顺序、移动结构体定义、添加并发控制机制以及移除冗余字段。

---

#### 🔴 [ci: fix restore-mtime exit code when last file is deleted on macos runners](https://github.com/Eventual-Inc/Daft/pull/6268)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 7小时前 |
| 👤 作者 | desmondcheongzx |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +2/-2 (1 文件) |
| 🏷️ 标签 | `ci` |

**核心内容**: 这个 PR 修复了在 macOS 运行器上执行 restore-mtime 时因最后一个文件被删除导致退出码错误的问题。通过将命令模式改为 `if/then/fi` 结构，确保不存在的文件不会触发错误退出码。该修复已在 ubuntu-latest 和 macos-latest 平台上验证通过，解决了 #6264 中报告的失败问题。

---

#### 🔴 [refactor(arrow2): remove from_arrow2](https://github.com/Eventual-Inc/Daft/pull/6267)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 8小时前 |
| 👤 作者 | universalmind303 |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +97/-478 (14 文件) |
| 🏷️ 标签 | `refactor` |

**核心内容**: 这个 PR 对 arrow2 进行了重构，移除了 from_arrow2 相关代码。变更旨在简化代码结构或优化功能实现。

---

#### 🔴 [fix(flight): Add a check for `flight_shuffle_dirs` arg and change default](https://github.com/Eventual-Inc/Daft/pull/6266)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 8小时前 |
| 👤 作者 | srilman |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +7/-2 (3 文件) |
| 🏷️ 标签 | `fix` |

**核心内容**: 这个 PR 将 `flight_shuffle_dirs` 参数的默认值恢复为 `/tmp`，与旧版 Ray runner 保持一致。同时，增加了对该参数是否为空的检查，以确保其有效性。

---

#### 🔴 [refactor(arrow2): fully remove toarrow2 from arrays & series](https://github.com/Eventual-Inc/Daft/pull/6265)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 8小时前 |
| 👤 作者 | universalmind303 |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +21/-170 (16 文件) |
| 🏷️ 标签 | `refactor` |

**核心PR内容**: 这个PR从arrays和series模块中完全移除了toarrow2功能，进行代码重构。部分IO代码保留了兼容性桥接代码，以支持重构过程的过渡。

---

#### 🔴 [ci: cache workspace crates and share rust caches across all workflows](https://github.com/Eventual-Inc/Daft/pull/6264)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 11小时前 |
| 👤 作者 | desmondcheongzx |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +112/-45 (5 文件) |
| 🏷️ 标签 | `ci` |

**核心内容**: 该 PR 将 Swatinem/rust-cache 配置优化为共享缓存策略，通过统一缓存键和保存工作区构件，将原本分散的约 8 个缓存条目整合为 3 个共享键，显著节省了 10 GB 仓库缓存限制下的空间。在集成测试构建任务中，此优化将热缓存下的构建时间从 36 分钟缩短至 10 秒，预计单元测试和基准测试等任务也将获得类似性能提升。

---

#### 🔴 [refactor(arrow2)!: use arrow-rs casting for strftime function](https://github.com/Eventual-Inc/Daft/pull/6263)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 11小时前 |
| 👤 作者 | universalmind303 |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +190/-9 (2 文件) |
| 🏷️ 标签 | `refactor` `breaking change` |

**核心内容**: 该 PR 将 `strftime` 函数从 arrow2 迁移到 arrow-rs 的实现方式。主要变更是在微秒级时间戳的默认 ISO 格式输出中，当微秒为零时不再显示尾随的 `.000000`，以符合 ISO 8601 标准。依赖固定格式的用户需显式指定 `%Y-%m-%dT%H:%M:%S.%f` 格式字符串。

---

#### 🔴 [refactor(arrow2): use arrow-rs for filtering on python arrays](https://github.com/Eventual-Inc/Daft/pull/6262)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 11小时前 |
| 👤 作者 | universalmind303 |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +8/-16 (1 文件) |
| 🏷️ 标签 | `refactor` |

**核心内容**: 这个 PR 重构了 arrow2 模块，使用 arrow-rs 库在 Python 数组上进行过滤操作。目的是优化过滤功能的实现，提升性能或代码一致性。

---

#### 🔴 [ci: cache workspace crate artifacts in integration build](https://github.com/Eventual-Inc/Daft/pull/6261)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 23小时前 |
| 👤 作者 | desmondcheongzx |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +1/-0 (1 文件) |
| 🏷️ 标签 | `ci` |

**核心内容**: 该 PR 在集成测试构建作业中配置了 Swatinem/rust-cache 的 `cache-workspace-crates: "true"` 选项，以保留工作区成员的构建产物，避免每次运行都重新编译约 70 个本地 crate。这一变更将构建时间从冷缓存时的 36 分钟缩短至热缓存时的 10 秒，显著提升了 CI 效率。

---

#### 🔴 [refactor(arrow2): remove as_arrow2 from ops/get](https://github.com/Eventual-Inc/Daft/pull/6260)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | universalmind303 |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +128/-66 (5 文件) |
| 🏷️ 标签 | `refactor` |

**核心内容**: 这个 PR 重构了 `ops/get` 模块，移除了 `as_arrow2` 方法。由于对实际 `data` 迁移的依赖（特别是处理 `&str` 或 `&[u8]` 引用时），这不是完整的重构。

---

#### 🔴 [[wip] chore: refactor pipeline node ownership in start](https://github.com/Eventual-Inc/Daft/pull/6259)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | srilman |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +26/-17 (7 文件) |

**核心内容**: 这个 PR 重构了启动流程中的管道节点所有权逻辑，旨在优化代码结构和资源管理。具体实现细节和关联问题尚未在描述中详细说明。

---

#### 🔴 [[DRAFT] feat(sql): add DATE_TRUNC function support](https://github.com/Eventual-Inc/Daft/pull/6258)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | desmondcheongzx |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +143/-10 (5 文件) |
| 🏷️ 标签 | `feat` |

**核心内容**: 该 PR 为 SQL 添加了 `DATE_TRUNC` 函数支持，通过自定义 `SQLFunction` 包装器正确处理参数格式，将 SQL 位置参数转换为 `Truncate` UDF 所需的命名参数。它同时注册了 `date_trunc` 和 `truncate` 两个函数名，确保优先级高于通用自动注册逻辑。

---

#### 🔴 [refactor(arrow2): migrate BooleanArray bitmap access to arrow-rs](https://github.com/Eventual-Inc/Daft/pull/6256)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | desmondcheongzx |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +15/-14 (4 文件) |
| 🏷️ 标签 | `refactor` |

**核心内容**: 该 PR 将 `BooleanArray` 的位图访问从 arrow2 迁移到 arrow-rs，移除了对 `daft_arrow::bitmap` 和 `as_arrow2()` 的依赖。主要变更包括将 `as_bitmap()` 重命名为 `to_bitmap()` 以返回所有权的 `BooleanBuffer`，并更新相关迭代器、序列化和过滤逻辑以适配 arrow-rs 的实现。

---

#### 🔴 [refactor(arrow2): migrate concat.rs to arrow-rs](https://github.com/Eventual-Inc/Daft/pull/6255)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | desmondcheongzx |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +17/-87 (2 文件) |
| 🏷️ 标签 | `refactor` |

**核心内容**: 这个 PR 将 `concat.rs` 从 `arrow2` 迁移到 `arrow-rs`，移除了针对 `arrow2` 类型的专用宏和函数，统一使用 `arrow::compute::concat` 处理所有连接操作。同时更新了 `PythonArray::concat` 和 `PythonArray::iter()` 的相关实现，确保 `concat.rs` 完全不再依赖 `arrow2` 或 `daft_arrow`。

---

#### 🔴 [[wip] chore: Move EXPLAIN ANALYZE to Python](https://github.com/Eventual-Inc/Daft/pull/6254)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | srilman |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +312/-239 (26 文件) |

**核心内容**: 这个 PR 将 EXPLAIN ANALYZE 功能从其他位置迁移到 Python 中实现，属于代码重构任务。目的是优化代码结构，提高可维护性。

---

#### 🔴 [feat(metrics): add metrics docs](https://github.com/Eventual-Inc/Daft/pull/6253)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | cckellogg |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +88/-13 (5 文件) |
| 🏷️ 标签 | `feat` |

**核心内容**: 这个 PR 将可观测性相关文档整合到 docs/observability/ 目录下，并新增了进度指示器和 OpenTelemetry 指标文档。同时迁移了日志文档，优化了文档结构和分类。

---

#### 🔴 [feat: Add protocol aliases for IOConfig](https://github.com/Eventual-Inc/Daft/pull/6252)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | universalmind303 |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +327/-72 (5 文件) |
| 🏷️ 标签 | `feat` |

**核心内容**: 该 PR 为 `IOConfig` 新增了协议别名功能，允许用户将自定义协议名称映射到现有协议（如 `"my-s3"` 映射到 `"s3"`），从而支持使用领域特定的协议名称访问标准后端。实现包括 Rust 核心逻辑、Python API 绑定、类型存根更新及测试，设计上采用单层解析、内置协议保护、大小写不敏感等特性，且最小化对现有代码的影响。

---

#### 🔴 [refactor(arrow2): remove daft_arrow from arrow_growable](https://github.com/Eventual-Inc/Daft/pull/6251)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | universalmind303 |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +2/-6 (1 文件) |
| 🏷️ 标签 | `refactor` |

**核心内容**: 这个 PR 对 `arrow_growable` 进行了微小的重构，完全移除了对 `daft_arrow` 的依赖。主要目的是简化代码结构，消除不必要的模块关联。

---

#### 🔴 [ci: bump all timeouts from 30 -> 45](https://github.com/Eventual-Inc/Daft/pull/6250)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | universalmind303 |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +12/-12 (4 文件) |
| 🏷️ 标签 | `ci` |

**核心内容**: 该 PR 将所有超时时间从 30 秒增加到 45 秒，作为临时解决方案以解除 PR 和 CI 的阻塞问题。此举旨在为后续优化缓存和增量编译策略争取时间。

---

#### 🔴 [refactor(arrow2): remove more arrow2 usages in daft-core](https://github.com/Eventual-Inc/Daft/pull/6249)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | universalmind303 |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +71/-146 (3 文件) |
| 🏷️ 标签 | `refactor` |

**核心内容**: 这个 PR 重构了 `add_utf8_arrays` 以使用 arrow-rs，并移除了 `cast.rs` 中部分 arrow2 的引用。需要注意的是，`cast.rs` 尚未完全重构，此次仅处理了容易修改的部分。

---

#### 🔴 [refactor(arrow2): remove misc arrow2 references in csv and json](https://github.com/Eventual-Inc/Daft/pull/6248)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | universalmind303 |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +26/-39 (3 文件) |
| 🏷️ 标签 | `refactor` |

**核心内容**: 这个 PR 重构了 arrow2 相关代码，移除了 CSV 和 JSON 模块中多余的 arrow2 引用。目的是清理代码依赖，提高模块的独立性和可维护性。

---

#### 🔴 [refactor(arrow2): replace arrow2 based buffer with custom impl](https://github.com/Eventual-Inc/Daft/pull/6247)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | universalmind303 |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +94/-19 (3 文件) |
| 🏷️ 标签 | `refactor` |

**核心内容**: 该 PR 将基于 arrow2 的缓冲区替换为自定义的轻量级缓冲区（`PythonBuffer`），以保持相同的行为和性能特征。这一重构旨在优化缓冲区实现，减少对第三方库的依赖。

---

#### 🔴 [ci: share rust cache across branches and restore file mtimes](https://github.com/Eventual-Inc/Daft/pull/6246)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | desmondcheongzx |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +37/-1 (1 文件) |
| 🏷️ 标签 | `ci` |

**核心内容**: 该 PR 通过将 Rust 缓存改为跨分支共享并仅在主分支保存，解决了因缓存重复导致的 GitHub Actions 缓存限制问题。同时，通过恢复文件的修改时间，避免了 `actions/checkout` 导致的 Cargo 指纹失效，减少了不必要的重新编译。

---

#### 🔴 [ci: replace Swatinem/rust-cache with sccache for integration-test-build](https://github.com/Eventual-Inc/Daft/pull/6245)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | desmondcheongzx |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +5/-4 (1 文件) |
| 🏷️ 标签 | `ci` |

**核心内容**: 该 PR 将 `integration-test-build` 任务中的 `Swatinem/rust` 缓存替换为 `mozilla-actions/sccache-action`，以解决因 GitHub Actions 缓存空间不足导致的频繁缓存驱逐和超时问题。sccache 通过缓存单个编译单元而非整个 `target/` 目录，显著减小了缓存占用（约 3-5 倍），并支持跨任务缓存共享和部分缓存驱逐的优雅降级。此变更仅作为实验性应用于 `integration-test-build` 任务，后续可能推广至其他任务。

---

#### 🔴 [ci: increase integration-test-build timeout from 45 to 90 minutes](https://github.com/Eventual-Inc/Daft/pull/6244)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 1天前 |
| 👤 作者 | desmondcheongzx |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +1/-1 (1 文件) |
| 🏷️ 标签 | `ci` |

**核心内容**: 该 PR 将集成测试构建的超时时间从 45 分钟延长至 90 分钟，因为之前的超时设置无法应对 Rust 缓存完全未命中时的冷构建（需编译 676 个 crate）。长期计划是考虑使用 `sccache` 或更大的运行器来提高冷构建的稳定性。

---

#### 🔴 [fix: handle case where join keys are different for sort-merge multi-partition join](https://github.com/Eventual-Inc/Daft/pull/6243)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2天前 |
| 👤 作者 | gweaverbiodev |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +78/-6 (2 文件) |
| 🏷️ 标签 | `fix` |

**核心内容**: 这个 PR 修复了排序合并多分区连接在左右数据框连接键不同时的处理问题。通过在生成边界样本时对右键进行别名处理，并在应用边界创建范围分区任务时重命名物化边界，确保了正确性。此外，还添加了回归测试并临时增加了部分工作流的超时时间。

---

#### 🔴 [fix: NaN-aware comparator for multi-column search_sorted and sort](https://github.com/Eventual-Inc/Daft/pull/6242)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2天前 |
| 👤 作者 | desmondcheongzx |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +175/-43 (2 文件) |
| 🏷️ 标签 | `fix` |

**核心内容**: 这个 PR 修复了分布式排序中的多列搜索和排序函数对 NaN 值的处理问题，确保负 NaN 不会导致错误的数据分区。它引入了新的 NaN 感知比较器 `make_daft_comparator`，替换了 arrow-rs 的默认比较器，解决了排序和合并 join 中的潜在 bug。

---

#### 🔴 [ci: increase integration-test-build timeout from 30 to 45 minutes](https://github.com/Eventual-Inc/Daft/pull/6241)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2天前 |
| 👤 作者 | desmondcheongzx |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +1/-1 (1 文件) |
| 🏷️ 标签 | `ci` |

**核心内容**: 该 PR 将集成测试构建的超时时间从 30 分钟延长至 45 分钟，以解决因 Cargo.lock 更新导致缓存失效后构建超时的问题。这确保首次完整构建能完成并保存缓存，后续构建时间可恢复到约 10 分钟。

---

#### 🔴 [refactor(arrow2): migrate if_else kernel from arrow2 to arrow-rs](https://github.com/Eventual-Inc/Daft/pull/6240)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2天前 |
| 👤 作者 | desmondcheongzx |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +10/-12 (1 文件) |
| 🏷️ 标签 | `refactor` |

**核心内容**: 这个 PR 将 `if_else` 内核从 arrow2 迁移到 arrow-rs，并直接使用 Daft 的 `BooleanArray` API 替代 arrow2 的调用。同时，优化了位图迭代路径，移除了非 null 快速路径中冗余的 `total_len` 累加器。

---

#### 🔴 [refactor(arrow2): migrate cast.rs from arrow2 to arrow-rs](https://github.com/Eventual-Inc/Daft/pull/6239)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2天前 |
| 👤 作者 | desmondcheongzx |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +198/-175 (2 文件) |
| 🏷️ 标签 | `refactor` |

**核心内容**: 该 PR 将 `src/daft-core/src/array/ops/cast.rs` 从 arrow2 迁移到 arrow-rs，替换了相关的 API 调用并调整了类型转换逻辑。迁移过程中增加了兼容性处理，以解决 arrow-rs 在部分类型转换支持上的差异。

---

#### 🔴 [refactor(arrow2): migrate array serdes from arrow2 to arrow-rs](https://github.com/Eventual-Inc/Daft/pull/6238)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2天前 |
| 👤 作者 | desmondcheongzx |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +30/-69 (1 文件) |
| 🏷️ 标签 | `refactor` |

**核心内容**: 该 PR 将数组序列化和反序列化功能从 arrow2 迁移到 arrow-rs。主要目的是通过迁移到更现代的 arrow-rs 库来优化代码库。

---



---
*生成时间: 2026-02-20 00:00:00*
