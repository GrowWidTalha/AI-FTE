# Turbo Launch AI Employee Vault

This Obsidian vault serves as the **Memory and GUI** for your Personal AI Employee.

## Project Location

- **WSL Path:** `/mnt/d/class/AI_EMPLOYEE_FTE`
- **Windows Path:** `D:\class\AI_EMPLOYEE_FTE`
- **Obsidian:** Open this folder as a vault

## Vault Structure

```
AI_EMPLOYEE_FTE/
├── Dashboard.md           # Main overview and status
├── Company_Handbook.md    # Rules of engagement
├── Business_Goals.md      # Targets and metrics
├── .claude/               # Claude Code local configuration
│   ├── skills/            # Agent skills (process-inbox, gmail-triage, etc.)
│   ├── settings/          # Claude Code settings (mcp.json, etc.)
│   └── hooks/             # Stop hooks (Ralph Wiggum loop)
├── Needs_Action/          # Tasks requiring AI attention
├── In_Progress/           # Tasks currently being worked on
├── Plans/                 # AI-generated execution plans
├── Pending_Approval/      # Items awaiting human approval
├── Approved/              # Approved actions ready to execute
├── Rejected/              # Rejected actions
├── Done/                  # Completed tasks
├── Inbox/                 # Raw inputs from watchers
├── Updates/               # Cloud agent updates (Platinum tier)
├── Briefings/             # Weekly CEO briefings
├── Accounting/            # Financial records
├── Invoices/              # Generated invoices
├── Logs/                  # Activity logs (YYYY-MM-DD.json)
├── Skills/                # Skill definitions (legacy)
├── sessions/              # Claude Code session history
└── scripts/               # Watchers, MCP servers, orchestrator
    ├── watchers/          # Python watcher scripts
    ├── mcp_servers/       # MCP server implementations
    └── orchestrator/      # Orchestration logic
```

## How It Works

1. **Watchers** detect new activity (email, WhatsApp, files)
2. They create files in `/Inbox` or `/Needs_Action`
3. **Claude Code** reads these files and follows Company_Handbook.md rules
4. Claude creates plans in `/Plans` and approval requests in `/Pending_Approval`
5. **You** review and move items to `/Approved` or `/Rejected`
6. **MCP Servers** execute approved actions
7. Completed items move to `/Done` with logs

## Getting Started

### In WSL/Linux

```bash
cd /mnt/d/class/AI_EMPLOYEE_FTE
claude --cwd .
```

### In Windows (PowerShell/CMD)

```powershell
cd D:\class\AI_EMPLOYEE_FTE
claude --cwd .
```

Claude Code will now read and write to this vault.

## Tier Progress

- [x] **Bronze:** Vault structure, Dashboard, Handbook, Skills folder
- [ ] **Silver:** Watchers, MCP integration, HITL workflow
- [ ] **Gold:** Full integration, Odoo, Ralph Wiggum loop
- [ ] **Platinum:** Cloud deployment, work-zone specialization

## Important Notes

- **Never commit** sensitive files (.env, credentials.json, token.json)
- **Keep Dashboard.md** open in Obsidian for real-time updates
- **Review Pending_Approval** folder regularly
- **Check Logs/** folder to monitor AI activity
- **Windows Task Scheduler** will be used for automation (Tier 2+)

---

*This is your AI Employee's brain. Keep it organized and secure.*
