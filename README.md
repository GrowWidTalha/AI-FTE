# 🤖 AI Employee - Autonomous Digital FTE

> A fully autonomous AI employee that manages your business 24/7 using Claude Code, Obsidian, and Python.

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude_Code-4.6-purple.svg)](https://claude.ai/claude-code)

## 🎯 What Is This?

An **AI Employee** that acts as a full-time equivalent (FTE) for your business. It watches your inboxes, processes tasks, communicates with customers, and manages operations - all while following your company handbook.

Built for **Turbo Launch** - helping founders launch MVPs in 15 days.

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         AI Employee                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐      │
│  │  Senses │───►│   Brain │───►│  Hands  │───►│  Memory │      │
│  │Watchers │    │  Claude │    │   MCP   │    │Obsidian │      │
│  └─────────┘    │  Code   │    │ Servers │    │  Vault  │      │
│                 └─────────┘    └─────────┘    └─────────┘      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Senses** | Python Watchers | Monitor email, files, messages |
| **Brain** | Claude Code | Reasoning, decision making |
| **Hands** | MCP Servers | Execute actions (send email, post, etc.) |
| **Memory** | Obsidian Vault | Long-term knowledge, logs, plans |

---

## ✨ Features

### Bronze Tier (Current - ✅ Complete)
- ✅ Obsidian vault with Dashboard & Company Handbook
- ✅ File watcher (drop files → auto-process)
- ✅ 5 Agent Skills (process-inbox, gmail-triage, update-dashboard, create-plan, draft-reply)
- ✅ Claude Code integration with local skills

### Silver Tier (Next)
- 🔄 Gmail watcher with OAuth
- 🔄 MCP servers for email, browser automation
- 🔄 Human-in-the-Loop approval workflow
- 🔄 Orchestrator for automatic triggering

### Gold Tier
- ⏳ Odoo accounting integration
- ⏳ Social media posting (LinkedIn, Twitter, Instagram)
- ⏳ Ralph Wiggum persistence loop

### Platinum Tier
- ⏳ Cloud 24/7 deployment
- ⏳ Work-zone specialization

---

## 🚀 Quick Start

### Prerequisites

- [Python 3.13+](https://www.python.org/downloads/)
- [UV](https://github.com/astral-sh/uv) (Python package manager)
- [Claude Code](https://claude.ai/claude-code)
- [Obsidian](https://obsidian.md) (optional, for GUI)

### Installation

```bash
# Clone the repository
git clone https://github.com/GrowWidTalha/AI-FTE.git
cd AI-FTE

# Install dependencies
uv sync

# Set up environment
cp .env.example .env
# Edit .env with your credentials
```

### Usage

```bash
# Show help
uv run ai-employee

# Start file watcher
uv run ai-watch

# Start orchestrator
uv run ai-orchestrate
```

### With Claude Code

```bash
# Start Claude Code in the project directory
claude --cwd .

# Try skills
/update-dashboard
/process-inbox
/create-plan
```

---

## 📁 Project Structure

```
AI-FTE/
├── .claude/                  # Claude Code config
│   ├── skills/               # Agent skills
│   └── settings/             # MCP & working dir
├── scripts/                  # Python package
│   ├── watchers/             # File, Gmail, WhatsApp watchers
│   ├── mcp_servers/          # MCP implementations
│   └── orchestrator/         # Coordination logic
├── Dashboard.md              # Live overview
├── Company_Handbook.md       # Rules of engagement
├── Business_Goals.md         # Targets & metrics
├── Needs_Action/             # Tasks needing attention
├── In_Progress/              # Active work
├── Done/                     # Completed tasks
└── pyproject.toml            # UV project config
```

---

## 🧪 Testing

```bash
# 1. Start the file watcher
uv run ai-watch

# 2. In another terminal, drop a test file
echo "Task: Review the handbook" > Inbox/test.txt

# 3. Watch it appear in Needs_Action/ automatically!
```

---

## 📚 How It Works

1. **Watchers** detect new activity (files dropped, emails received)
2. They create action files in `/Needs_Action`
3. **Claude Code** reads these files and follows `Company_Handbook.md` rules
4. Claude creates plans in `/Plans` or drafts in `/Pending_Approval`
5. **You** review and approve/reject
6. **MCP Servers** execute approved actions
7. Completed items move to `/Done` with logs

---

## 🛠️ Tech Stack

- **Python 3.13+** with UV package manager
- **Claude Code** for AI reasoning
- **Obsidian** for memory & GUI
- **Google APIs** for Gmail (Silver tier)
- **Watchdog** for file monitoring
- **MCP** for tool integration

---

## 📝 License

MIT License - see [LICENSE](LICENSE) for details.

---

## 🤝 Contributing

Contributions welcome! Feel free to open issues or PRs.

---

## 🌟 Star History

If you find this useful, please star the repo!

---

**Built with ❤️ for Turbo Launch**

*MVPs in 15 days or less*
