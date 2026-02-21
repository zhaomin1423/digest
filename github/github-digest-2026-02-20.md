# GitHub 每日摘要

📅 **生成时间**: 2026-02-20 23:34:54
⏰ **时间范围**: 过去 24 小时
📊 **监控仓库数**: 5
📋 **总计**: 4 Issues, 33 Pull Requests

## 📑 目录

- [Apache Fluss](#apache-fluss) - 0 Issues, 1 PRs
- [Apache Flink](#apache-flink) - 0 Issues, 2 PRs
- [Apache Spark](#apache-spark) - 1 Issues, 16 PRs
- [Apache Iceberg](#apache-iceberg) - 3 Issues, 10 PRs
- [Apache Paimon](#apache-paimon) - 0 Issues, 4 PRs

---

## Apache Fluss

> 仓库: https://github.com/apache/fluss

### 📋 Issues

_过去 24 小时内没有新的 Issue_

### 🔀 Pull Requests (1)

#### 🔴 [[helm] Enable SASL authenticated connection to Zookeeper nodes](https://github.com/apache/fluss/pull/2700)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 23小时前 |
| 👤 作者 | morazow |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +798/-8 (10 文件) |

**核心内容**: 这个 PR 为 Helm 添加了通过 SASL 认证连接 Zookeeper 节点的选项，并更新了相关文档。它解决了 #2636 问题，使得 Zookeeper 连接支持更安全的认证方式。

---


## Apache Flink

> 仓库: https://github.com/apache/flink

### 📋 Issues

_过去 24 小时内没有新的 Issue_

### 🔀 Pull Requests (2)

#### 🔴 [[FLINK-39088][table] Support injective casts from VARCHAR to BINARY](https://github.com/apache/flink/pull/27640)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2小时前 |
| 👤 作者 | gustavodemorais |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +50/-1 (3 文件) |

**核心内容**: 该 PR 修复了 VARCHAR 到 VARBINARY 类型转换未被识别为单射的问题，确保在满足特定条件（如目标容量足够）时转换保持键的唯一性。通过标记 UTF-8 编码为单射，优化了 upsert 键的处理逻辑。

---

#### 🔴 [[WIP] FLIP-547: Support checkpoint during recovery](https://github.com/apache/flink/pull/27639)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 6小时前 |
| 👤 作者 | 1996fanrui |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +5268/-359 (246 文件) |

**核心内容**: 这个 PR 旨在实现 FLIP-547 功能，支持在恢复过程中进行检查点操作。目前该 PR 尚未完成，需要忽略。

---


## Apache Spark

> 仓库: https://github.com/apache/spark

### 📋 Issues (1)

#### 🔴 [[BUILD] Add coding agent build instructions](https://github.com/apache/spark/issues/54386)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 15小时前 |
| 👤 作者 | szehon-ho |
| 🏷️ 状态 | CLOSED |

**核心内容**: 该 Issue 建议为 Claude Code 和 Cursor 等 AI 编程工具添加 Spark 项目的构建和测试说明。当前默认使用 Maven 构建，但 SBT 更快，因此需要优化构建指令以提升开发效率。

---

### 🔀 Pull Requests (16)

#### 🔴 [[SPARK-54835][SQL][FOLLOWUP] Drain listener bus before registering listener in test](https://github.com/apache/spark/pull/54397)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 0分钟前 |
| 👤 作者 | cloud-fan |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +2/-0 (1 文件) |

**核心内容**: 这个 PR 是对先前修改的跟进，在测试中注册 `QueryExecutionListener` 之前先清空监听总线，以避免之前测试的残留事件导致测试结果不稳定。该变更仅影响测试逻辑，不会引入面向用户的修改。

---

#### 🔴 [[SPARK-55619][SQL] Fix custom metrics in case of coalesced partitions](https://github.com/apache/spark/pull/54396)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 4小时前 |
| 👤 作者 | peter-toth |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +63/-41 (2 文件) |

**核心内容**: 该 PR 修复了在合并分区时自定义指标计算错误的问题，通过回退之前的方案并采用新的方式跟踪最近创建的读取器，在任务完成监听器中更新指标。此变更确保了 `DataSourceRDD.compute()` 在多次调用时仍能正确计算自定义指标。

---

#### 🔴 [[SPARK-55618][BUILD] Upgrade sbt to `1.12.3`](https://github.com/apache/spark/pull/54395)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 5小时前 |
| 👤 作者 | LuciferYang |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +1/-1 (1 文件) |

**核心内容**: 该 PR 提议将 sbt 构建工具升级到版本 `1.12.3`，以引入该版本中的错误修复。此变更不涉及用户可见的功能，并通过 GitHub Actions 测试验证。

---

#### 🔴 [[SPARK-55617] Add VariantGet to V2ExpressionBuilder for DSv2 filter pushdown](https://github.com/apache/spark/pull/54394)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 11小时前 |
| 👤 作者 | qlong |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +70/-2 (2 文件) |

**核心内容**: 该 PR 在 V2ExpressionBuilder 中添加了 VariantGet 支持，使 variant_get 和 try_variant_get 谓词能转换为 V2 UserDefinedScalarFunc 并下推到连接器。这旨在为 Iceberg 的碎片化变体列提供文件级跳过功能，目前仅支持可折叠路径和直接表列引用。

---

#### 🔴 [[SPARK-55616][BUILD] Bump RoaringBitmap 1.6.10 which backs to Maven Central](https://github.com/apache/spark/pull/54393)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 12小时前 |
| 👤 作者 | pan3793 |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +10/-22 (6 文件) |

**核心内容**: 该 PR 将 Spark 中的 RoaringBitmap 依赖从 1.6.0 升级到 1.6.10，以保持第三方依赖的更新。此次升级还移除了有时速度较慢的第三方 Maven 仓库 JitPack，改回使用 Maven Central。

---

#### 🔴 [[SPARK-55296][PS][FOLLOW-UP] Fix CoW mode not to break groupby](https://github.com/apache/spark/pull/54392)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 13小时前 |
| 👤 作者 | ueshin |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +16/-5 (2 文件) |

**核心内容**: 该 PR 修复了 CoW（Copy-on-Write）模式下过早断开锚点导致 `groupby` 功能异常的问题，通过延迟断开锚点的时间至实际更新时。这一变更使 Spark 的行为更接近 pandas 3，确保了 `groupby` 操作的正确性。

---

#### 🔴 [[SPARK-54975][SQL][TESTS][FOLLOW-UP] Split MergeIntoSchemaEvolutionTests](https://github.com/apache/spark/pull/54391)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 13小时前 |
| 👤 作者 | szehon-ho |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +3167/-2889 (7 文件) |

**核心内容**: 这个 PR 将 `MergeIntoSchemaEvolutionTests` 测试类拆分为多个子 trait，以解决测试覆盖率工具在编译时因字节码超过 64k 限制而失败的问题。该变更仅涉及测试代码，不影响用户功能，通过运行现有测试验证。

---

#### 🔴 [[SPARK-55615][PYTHON][CONNECT] Move SparkContext import into class branch](https://github.com/apache/spark/pull/54390)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 14小时前 |
| 👤 作者 | gaogaotiantian |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +2/-2 (1 文件) |

**核心内容**: 该 PR 将 `SparkContext` 的导入语句移至 classic 分支中，以避免在仅使用 Connect 客户端时出现导入错误。此变更确保了代码兼容性，不会影响用户行为。

---

#### 🔴 [[SPARK-55610][PYTHON] Add getExecutorInfos to StatusTracker in Python](https://github.com/apache/spark/pull/54389)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 14小时前 |
| 👤 作者 | WweiL |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +65/-3 (4 文件) |

**核心内容**: 这个 PR 在 PySpark 的 StatusTracker 中添加了 getExecutorInfos 方法，补全了 Python 端缺失但 Scala 端已存在的 API。现在用户可以通过 PySpark 访问执行器的详细信息，如主机名、端口、缓存大小等。

---

#### 🔴 [[SPARK-55613][PYTHON][TESTS] Add main block for tests that are missing it](https://github.com/apache/spark/pull/54388)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 15小时前 |
| 👤 作者 | gaogaotiantian |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +12/-0 (2 文件) |

**核心内容**: 这个 PR 为缺失主块的测试文件添加了主块，以确保这些测试能够被 CI 系统正确执行。变更原因是当前 CI 直接将脚本作为模块运行，导致这些测试未被执行。PR 不涉及任何面向用户的变更。

---

#### 🔴 [[SPARK-55614][BUILD] Add AGENTS.MD](https://github.com/apache/spark/pull/54387)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 15小时前 |
| 👤 作者 | szehon-ho |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +14/-0 (1 文件) |

**核心内容**: 这个 PR 添加了一个 AGENTS.MD 文件，旨在帮助 Claude Code 和 Cursor 等 AI 工具更好地理解如何构建 Spark 和运行测试。该文件默认推荐使用更快的 SBT 而非 Maven 来提升开发效率。

---

#### 🔴 [[SPARK-54599][PYTHON][FOLLOWUP][4.0] Remove another error message check to make CI happy](https://github.com/apache/spark/pull/54385)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 16小时前 |
| 👤 作者 | gaogaotiantian |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +0/-2 (1 文件) |

**核心内容**: 该 PR 移除了 branch-4.0 分支中客户端测试的一项错误信息检查，目的是让 CI 测试通过。变更原因与之前的 PR #54353 相同，不涉及用户可见的功能修改。

---

#### 🔴 [[SPARK-55612][PYTHON][TESTS] Add test_dataframe_query_context to modules](https://github.com/apache/spark/pull/54384)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 16小时前 |
| 👤 作者 | gaogaotiantian |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +24/-0 (2 文件) |

**核心内容**: 这个 PR 将 `test_dataframe_query_context` 和 `test_parity_dataframe_query_context` 测试添加到 `modules.py` 中，确保 CI 能够运行这些测试。同时修复了这些测试当前的失败问题。由于之前未添加测试，CI 无法执行它们，此次变更解决了这一问题。

---

#### 🔴 [[SPARK-55607][PYTHON][TESTS] Skip test_session if we should not test connect](https://github.com/apache/spark/pull/54383)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 19小时前 |
| 👤 作者 | gaogaotiantian |
| 🏷️ 状态 | CLOSED |
| 📊 变更 | +9/-2 (1 文件) |

**核心内容**: 该 PR 提出在不应测试连接时跳过 `test_session` 测试，以修复仅经典模式的 CI 失败问题。所有连接测试都应受到保护，确保测试环境的一致性。

---

#### 🔴 [[SPARK-55600][PYTHON] Fix pandas to arrow loses row count when schema has 0 columns on classic](https://github.com/apache/spark/pull/54382)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 20小时前 |
| 👤 作者 | Yicong-Huang |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +67/-17 (2 文件) |

**核心内容**: 此 PR 修复了在 Classic Spark 中从 Pandas DataFrame 创建 Spark DataFrame 时，若 Schema 为 0 列会导致行数丢失的问题。修复后，即使没有列，也能正确保留行数信息。

---

#### 🔴 [[SPARK-55493] [SS] Do not mkdirs in streaming checkpoint offset/commit log directory in StateDataSource](https://github.com/apache/spark/pull/54381)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 20小时前 |
| 👤 作者 | liviazhu |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +137/-15 (8 文件) |

**核心内容**: 该 PR 修改了 StateDataSource，使其在流处理检查点的偏移量和提交日志目录中不再尝试创建目录。通过引入只读模式的工具函数，允许 StateDataSource 在只读检查点上使用。

---


## Apache Iceberg

> 仓库: https://github.com/apache/iceberg

### 📋 Issues (3)

#### 🔴 [Kafka Connect: CVE-2025-67721 in io.airlift:aircompressor 2.0.2](https://github.com/apache/iceberg/issues/15378)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 4小时前 |
| 👤 作者 | rmoff |
| 🏷️ 状态 | OPEN |

**核心内容**: Kafka Connect 运行时依赖的 io.airlift:aircompressor 2.0.2 版本存在高危漏洞 CVE-2025-67721，可能导致解压缩时缓冲区内容泄露。目前上游修复补丁尚未合并，需等待 2.0.3 版本发布后通过强制依赖升级解决。

---

#### 🔴 [Make BaseTransaction#cleanUpOnCommitFailure package-private](https://github.com/apache/iceberg/issues/15377)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 4小时前 |
| 👤 作者 | deniskuzZ |
| 🏷️ 状态 | OPEN |
| 🏷️ 标签 | `improvement` |

**核心内容**: 该 Issue 请求将 `BaseTransaction#cleanUpOnCommitFailure` 方法改为包级私有，以支持多表事务复用 `BaseTransaction` 的功能。这是为了改进 Hive 查询引擎的事务处理能力。提交者表示可以独立贡献此改进。

---

#### 🔴 [bump roaringbitmap for spark 4.2 integration](https://github.com/apache/iceberg/issues/15370)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 22小时前 |
| 👤 作者 | kevinjqliu |
| 🏷️ 状态 | OPEN |

**核心内容**: 这个 Issue 跟踪了将 RoaringBitmap 从 1.3.0 升级到 1.6.0 的任务，该升级曾因对使用 `jipack` 仓库的下游影响的担忧而被临时回退。目的是确定最佳下一步行动，以便为 Spark 4.2 集成重新推进此升级。

---

### 🔀 Pull Requests (10)

#### 🔴 [Spark: Add separate data and metadata file lists to RewriteTablePath](https://github.com/apache/iceberg/pull/15382)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2小时前 |
| 👤 作者 | mxm |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +94/-12 (4 文件) |
| 🏷️ 标签 | `API` `spark` `core` |

**核心内容**: 该 PR 为 Spark 的 RewriteTablePath 功能添加了独立的数据文件和元数据文件列表，以满足下游工具对不同文件类型采用不同复制策略的需求。在拆分文件列表的同时，保留了原有的合并列表以确保向后兼容性。

---

#### 🔴 [Spark: Add ExecutorService support to RewriteTablePath](https://github.com/apache/iceberg/pull/15381)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2小时前 |
| 👤 作者 | mxm |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +83/-9 (3 文件) |
| 🏷️ 标签 | `API` `spark` |

**核心内容**: 该 PR 为 RewriteTablePath 添加了 `executeWith(ExecutorService)` 方法，以支持并行重写版本文件和清单列表的元数据。这旨在提升元数据重写的效率。

---

#### 🔴 [Docs: Add blog post about File Format API](https://github.com/apache/iceberg/pull/15380)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 3小时前 |
| 👤 作者 | pvary |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +136/-0 (4 文件) |
| 🏷️ 标签 | `docs` |

**核心内容**: 该 PR 新增了一篇关于文件格式 API 的博客文章。主要目的是通过文档介绍文件格式 API 的功能和使用方法。

---

#### 🔴 [Fix s3 IO unclosed instance ](https://github.com/apache/iceberg/pull/15379)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 4小时前 |
| 👤 作者 | donPain |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +395/-1 (4 文件) |
| 🏷️ 标签 | `spark` `core` `flink` |

**核心内容**: 这个 PR 修复了 S3 IO 中未关闭实例的问题，确保资源正确释放。变更涉及相关代码的优化，以避免潜在的内存泄漏或资源浪费。

---

#### 🔴 [Spark 4.1: Refactor metadata column references to use asRef() method](https://github.com/apache/iceberg/pull/15376)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 9小时前 |
| 👤 作者 | aokolnychyi |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +24/-24 (4 文件) |
| 🏷️ 标签 | `spark` |

**核心内容**: 这个 PR 重构了 Spark 4.1 中元数据列引用的实现，改为使用 `asRef()` 方法。目的是优化代码结构，提升列引用的处理效率和一致性。

---

#### 🔴 [Spark 4.1: Simplify time travel option extraction in IcebergSource](https://github.com/apache/iceberg/pull/15375)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 10小时前 |
| 👤 作者 | aokolnychyi |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +2/-5 (1 文件) |
| 🏷️ 标签 | `spark` |

**核心内容**: 这个 PR 优化了 IcebergSource 中提取时间旅行选项的逻辑，移除了不必要的 PropertyUtil 使用，以简化代码实现。

---

#### 🔴 [Spark 4.1: Introduce modes in SparkWriteBuilder](https://github.com/apache/iceberg/pull/15374)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 10小时前 |
| 👤 作者 | aokolnychyi |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +111/-108 (1 文件) |
| 🏷️ 标签 | `spark` |

**核心内容**: 这个 PR 在 Spark 4.1 的 `SparkWriteBuilder` 中引入了模式（modes），目的是让代码更易于理解和维护。主要变更包括通过模式机制优化代码结构，提升可读性。

---

#### 🔴 [Spark, Arrow, Parquet: Add vectorized read support for parquet BYTE_STREAM_SPLIT encoding](https://github.com/apache/iceberg/pull/15373)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 11小时前 |
| 👤 作者 | jbewing |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +441/-90 (31 文件) |
| 🏷️ 标签 | `spark` `parquet` `arrow` |

**核心内容**: 该 PR 为 Apache Iceberg 添加了对 Parquet v2 规范中 BYTE_STREAM_SPLIT 编码的向量化读取支持，解决了 Spark 默认启用向量化读取时无法兼容其他引擎使用 Parquet v2 编写的数据的问题。这一改进提升了与其他计算引擎的互操作性，并避免了因禁用向量化读取或强制使用 Parquet v1 格式带来的性能和存储开销。

---

#### 🔴 [Core, Spark: Adds a Table Property for Relying on Identifier Fields](https://github.com/apache/iceberg/pull/15372)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 13小时前 |
| 👤 作者 | RussellSpitzer |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +164/-7 (5 文件) |
| 🏷️ 标签 | `spark` `core` |

**核心内容**: 该 PR 为 Core 和 Spark 模添加了表属性，允许用户告知引擎可以依赖标识符字段的唯一性进行优化。这一功能作为优化器的提示，与真正的约束验证和执行机制无关，适用于所有具有标识符列的表版本。

---

#### 🔴 [API: Support timestamp types in Conversions.fromPartitionString](https://github.com/apache/iceberg/pull/15371)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 13小时前 |
| 👤 作者 | ebyhr |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +155/-0 (2 文件) |
| 🏷️ 标签 | `API` |

**核心内容**: 这个 PR 为 Conversions.fromPartitionString 方法添加了对时间戳类型的支持。该方法主要用于从 Hive 分区路径推断分区值，而 Hive 支持时间戳类型。尽管时间戳类型在分区中可能较少使用，但该功能确保了兼容性。

---


## Apache Paimon

> 仓库: https://github.com/apache/paimon

### 📋 Issues

_过去 24 小时内没有新的 Issue_

### 🔀 Pull Requests (4)

#### 🔴 [[BUILD] Add `AGENTS.md`](https://github.com/apache/paimon/pull/7297)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 27分钟前 |
| 👤 作者 | Zouxxyy |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +36/-2 (2 文件) |

**核心内容**: 该 PR 新增了 `AGENTS.md` 文件，旨在为 AI 代理提供开发指南，部分参考了 Apache Spark 的同类文件。作者通过实际测试展示了在跳过部分检查项时，测试时间可从约 15 秒缩短至约 5 秒。

---

#### 🔴 [[test] Fix test HiveLocationTest.testExternTableLocation](https://github.com/apache/paimon/pull/7296)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 6小时前 |
| 👤 作者 | Zouxxyy |
| 🏷️ 状态 | MERGED |
| 📊 变更 | +4/-1 (1 文件) |

**核心内容**: 这个 PR 修复了测试用例 `HiveLocationTest.testExternTableLocation` 中的问题，确保测试能够正确验证外部表位置的功能。修复内容未影响 API 或存储格式，仅涉及测试代码的调整。

---

#### 🔴 [[core] Support empty dirs cleaning without bucket sub dir in orphan files cleanup](https://github.com/apache/paimon/pull/7295)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 9小时前 |
| 👤 作者 | XiaoHongbo-Hope |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +315/-4 (6 文件) |

**核心内容**: 该 PR 修复了 OrphanFilesClean 在清理孤立文件时无法删除不包含桶子目录的空分区目录的问题。变更后，所有空目录（包括无桶子目录的分区目录）都将被正确清理，避免残留大量空目录。

---

#### 🔴 [[hotfix] Reorganize .gitignore for better readability and add AI assistant entries](https://github.com/apache/paimon/pull/7294)

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 11小时前 |
| 👤 作者 | Zouxxyy |
| 🏷️ 状态 | OPEN |
| 📊 变更 | +32/-19 (1 文件) |

**核心内容**: 该 PR 重新组织了 .gitignore 文件，将条目按类别分组并按字母排序，以提高可读性。同时新增了对 AI 助手配置目录（如 .claude、.cursor、.qoder）的忽略规则。

---



---
*生成时间: 2026-02-20 23:34:54*
