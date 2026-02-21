GitHub Digest - Daily Issue/PR Reporter
========================================
Automatically fetches GitHub Issues and Pull Requests from monitored repositories, generates Chinese summaries using AI, and saves to Obsidian vault.

Setup
-----
**Prerequisites:**
1. GitHub CLI (`gh`) installed and authenticated:
   ```bash
   brew install gh
   gh auth login
   ```

2. AI API configured in `~/.openclaw/openclaw.json` (Doubao API):
   ```json
   {
     "models": {
       "providers": {
         "doubao": {
           "baseUrl": "https://api.doubao.com/v1",
           "apiKey": "your-api-key",
           "models": [{"id": "model-id"}]
         }
       }
     }
   }
   ```

3. Obsidian vault path configured in `repos.json`

**Installation:**
```bash
cd ~
git clone <repo> github-digest
cd github-digest
pip3 install -r requirements.txt
```

Configuration
-------------
Edit `~/github-digest/repos.json`:

```json
{
  "repos": [
    {
      "name": "Apache Fluss",
      "owner": "apache",
      "repo": "fluss",
      "enabled": true
    },
    {
      "name": "Apache Flink",
      "owner": "apache",
      "repo": "flink",
      "enabled": true
    },
    {
      "name": "Apache Spark",
      "owner": "apache",
      "repo": "spark",
      "enabled": true
    }
  ],
  "settings": {
    "hours_back": 24,
    "obsidian_vault": "/Users/yourname/Documents/Obsidian Vault",
    "output_folder": "GitHub Digest"
  }
}
```

| Field | Description | Default |
| --- | --- | --- |
| `name` | Display name in report | — |
| `owner` | GitHub org/owner | — |
| `repo` | Repository name | — |
| `enabled` | Include in reports | `true` |
| `hours_back` | Time range to fetch | `24` |
| `obsidian_vault` | Path to Obsidian vault | — |
| `output_folder` | Subfolder in vault | `GitHub Digest` |

Commands
--------
### Run manually
```bash
cd ~/github-digest
python3 github_digest.py
```

### Setup cron job (daily at 22:00)
```bash
crontab -e
# Add:
0 22 * * * /bin/bash /Users/yourname/github-digest/run-digest.sh
```

### View logs
```bash
tail -f ~/github-digest/digest.log
```

Output Format
-------------
Generated files: `github-digest-YYYY-MM-DD.md`

```markdown
# GitHub 每日摘要

📅 **生成时间**: 2026-02-20 22:00:00
⏰ **时间范围**: 过去 24 小时
📊 **监控仓库数**: 3

---

## Apache Fluss

> 仓库: https://github.com/apache/fluss

### 📋 Issues (2)

#### 🟢 [BUG] Issue title #123

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 2小时前 |
| 👤 作者 | username |
| 🏷️ 状态 | open |

**核心内容**: AI 生成的中文摘要...

---

### 🔀 Pull Requests (1)

#### 🟢 feat: New feature #456

| 属性 | 值 |
|------|----|
| 📅 创建时间 | 5小时前 |
| 👤 作者 | devname |
| 🏷️ 状态 | open |
| 📊 变更 | +500/-100 (15 文件) |

**核心内容**: AI 生成的中文摘要...
```

Workflow
--------
1. **Fetch Issues** - Uses `gh issue list` with search query for time range
2. **Fetch PRs** - Uses `gh pr list` with search query for time range
3. **Generate Summaries** - Calls Doubao AI API for Chinese translation/summarization
4. **Save Output** - Writes to both local `digests/` and Obsidian vault

State Icons
-----------
| Icon | Meaning |
| --- | --- |
| 🟢 | Open |
| 🔴 | Closed |
| 🟣 | Merged |

Files
-----
| File | Purpose |
| --- | --- |
| `github_digest.py` | Main script |
| `repos.json` | Repository configuration |
| `run-digest.sh` | Cron wrapper with logging |
| `digest.log` | Execution logs |
| `digests/` | Local copy of generated reports |

Troubleshooting
---------------
| Issue | Solution |
| --- | --- |
| `gh: command not found` | Install: `brew install gh` |
| `gh auth required` | Run: `gh auth login` |
| No AI summaries | Check `~/.openclaw/openclaw.json` config |
| Empty reports | Verify repo has issues/PRs in time range |
| Permission denied | Ensure scripts are executable: `chmod +x *.sh *.py` |

API Dependencies
----------------
- **GitHub CLI** - Fetch issues and PRs
- **Doubao AI API** - Chinese summarization
- **requests** - HTTP client for AI API
