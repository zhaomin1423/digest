# GitHub Digest

自动从 GitHub 仓库抓取 Issues 和 Pull Requests，生成中文日报并导入到 Obsidian。

## 功能

- 使用 `gh` CLI 获取最近 24 小时内的 Issues 和 PRs
- 使用豆包 API 生成中文摘要
- 自动保存到 Obsidian vault 的 `GitHub Digest` 文件夹
- 支持配置多个仓库

## 项目结构

```
~/github-digest/
├── github_digest.py      # 主脚本
├── repos.json            # 仓库配置
├── run-digest.sh         # Cron 包装脚本
├── requirements.txt      # Python 依赖
├── digests/              # 临时输出目录
└── digest.log            # 执行日志
```

## 安装

1. 确保已安装 GitHub CLI:
   ```bash
   brew install gh
   gh auth login
   ```

2. 安装 Python 依赖:
   ```bash
   pip3 install -r requirements.txt
   ```

3. 配置豆包 API（在 `~/.openclaw/openclaw.json` 中）

## 配置

编辑 `repos.json` 添加要监控的仓库:

```json
{
  "repos": [
    {
      "name": "Apache Fluss",
      "owner": "apache",
      "repo": "fluss",
      "enabled": true
    }
  ],
  "settings": {
    "hours_back": 24,
    "obsidian_vault": "/Users/zhaomin/Documents/Obsidian Vault",
    "output_folder": "GitHub Digest"
  }
}
```

## 手动运行

```bash
cd ~/github-digest
python3 github_digest.py
```

## 设置定时任务

每天 22:00 自动执行:

```bash
crontab -e
```

添加以下行:

```
0 22 * * * /bin/bash /Users/zhaomin/github-digest/run-digest.sh
```

## 输出示例

文件名: `github-digest-2026-02-20.md`

```markdown
# GitHub 每日摘要

📅 **生成时间**: 2026-02-20 22:00:00
⏰ **时间范围**: 过去 24 小时
📊 **监控仓库数**: 1

---

## Apache Fluss

> 仓库: https://github.com/apache/fluss

### 📋 Issues (3)

#### 🟢 [BUG] 数据写入时出现内存溢出 #123

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2小时前 |
| 👤 作者 | user123 |
| 🏷️ 状态 | open |

**核心内容**: 用户报告在大规模数据写入场景下出现 OOM 问题...

---

### 🔀 Pull Requests (2)

#### 🟢 feat: 支持增量检查点 #456

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 5小时前 |
| 👤 作者 | dev456 |
| 🏷️ 状态 | open |
| 📊 变更 | +500/-100 (15 文件) |

**核心内容**: 新增增量检查点功能，可减少状态持久化时间约40%...

---
```
