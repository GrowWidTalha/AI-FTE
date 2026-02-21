<!--
  SYNC IMPACT REPORT
  ===================
  Version: None → 1.0.0
  Rationale: Initial constitution created from hackathon_tiers.md specification

  Modified Principles: N/A (initial creation)

  Added Sections:
    - Core Principles (7 principles)
    - Security & Privacy Requirements
    - Development Workflow

  Removed Sections: N/A (initial creation)

  Templates Status:
    ✅ plan-template.md - Aligned with Agent Skills, MCP, HITL principles
    ✅ spec-template.md - User stories align with tiered progression
    ✅ tasks-template.md - No TDD requirement noted
    ⚠️ commands/*.md - No changes needed (generic guidance)

  Follow-up TODOs: None
-->

# AI Employee Constitution

## Core Principles

### I. Local-First Architecture

The AI Employee MUST prioritize local data storage and processing. All sensitive data (credentials, personal communications, financial information) resides on the user's machine. Obsidian vault serves as the single source of truth for state, plans, and logs. Cloud services are used only for:
- Reasoning via Claude Code API
- External service integrations via MCP (Gmail, banking, social media)
- Optional 24/7 cloud deployment (Platinum tier) with explicit domain separation

**Rationale**: Privacy is non-negotiable for an autonomous agent handling personal and business affairs. Local-first ensures user control and compliance with data protection regulations.

### II. Human-in-the-Loop (HITL) Safety

All sensitive actions MUST require human approval before execution. The approval workflow uses file-based state transitions:
- `/Pending_Approval/` - AI creates request files
- `/Approved/` - Human moves files to authorize
- `/Rejected/` - Human moves files to deny

Actions ALWAYS requiring approval:
- Payments to new recipients or amounts > $100
- Emails to new contacts
- Social media posts (drafts auto-approved, posting requires approval)
- Any action with financial or legal implications
- Deleting files or data

**Rationale**: Autonomous systems can make mistakes. HITL prevents catastrophic errors while maintaining efficiency for routine tasks.

### III. Agent Skills封装

All AI functionality MUST be implemented as [Claude Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview). Skills provide:
- Single-command invocation for complex workflows
- Consistent input/output interfaces
- Easy testing and iteration
- Shareable capabilities across the community

Required skills for Bronze tier:
- `process-inbox` - Scan and triage Needs_Action folder
- `update-dashboard` - Refresh Dashboard.md with current state
- `create-plan` - Generate Plan.md for tasks
- `draft-reply` - Create response drafts for approval

**Rationale**: Skills transform ad-hoc prompting into repeatable, verifiable automation capabilities.

### IV. MCP-Based Actions

All external actions MUST be implemented via Model Context Protocol (MCP) servers. MCP servers:
- Expose specific capabilities (email, browser, calendar, etc.)
- Maintain isolation from core reasoning
- Support dry-run mode for safe testing
- Enable graceful degradation when unavailable

Common MCP servers for this project:
- `filesystem` - Built-in, for vault operations
- `email-mcp` - Gmail integration (Silver tier)
- `browser-mcp` - Web automation for payments
- `odoo-mcp` - Accounting integration (Gold tier)

**Rationale**: MCP provides a clean interface boundary, enabling independent development and testing of action capabilities.

### V. Security & Credential Management

NEVER store credentials in:
- Plain text files
- Obsidian vault
- Git repository

Credentials MUST be:
- Stored in environment variables (.env file, gitignored)
- Managed via system keychain (macOS Keychain, Windows Credential Manager)
- Rotated monthly and after any suspected breach
- Used only by MCP servers, never directly by watchers or orchestrator

All MCP servers MUST support:
- `--dry-run` flag for development
- `DEV_MODE` environment variable to block real actions
- Rate limiting (max 10 emails/hour, max 3 payments/hour)

**Rationale**: An autonomous agent with your credentials is a powerful weapon. Proper security prevents accidental or malicious use.

### VI. Observability & Audit Logging

Every action the AI takes MUST be logged with:
- Timestamp (ISO 8601 format)
- Action type (email_send, payment_made, etc.)
- Actor (claude_code or human)
- Target (recipient, file path, etc.)
- Approval status
- Result (success/failed)

Logs stored in: `/Vault/Logs/YYYY-MM-DD.json`
Retention: Minimum 90 days

**Rationale**: Audit trails enable debugging, compliance, and trust. When something goes wrong, you need to know exactly what happened.

### VII. Tiered Progression & MVP-First

Features organized into four tiers with clear deliverables:
- **Bronze** (8-12 hours): Foundation - Vault, one watcher, basic skills
- **Silver** (20-30 hours): Functional - Multiple watchers, MCP, HITL, scheduling
- **Gold** (40+ hours): Autonomous - Full integration, Odoo accounting, social media
- **Platinum** (60+ hours): Production - Cloud 24/7, work-zone specialization

Each tier MUST be independently functional. Start with Bronze, validate, then progress.

**Rationale**: Incremental delivery prevents over-engineering and provides working software at each stage.

## Security & Privacy Requirements

### Data Classification

- **HIGH SENSITIVITY**: Banking credentials, WhatsApp sessions, payment tokens - Local only, never synced
- **MEDIUM SENSITIVITY**: Email content, personal messages - Encrypted at rest
- **LOW SENSITIVITY**: Task lists, plans, business goals - Can be synced to cloud (Platinum tier)

### Approval Thresholds

| Action Category | Auto-Approve | Always Require Approval |
|-----------------|--------------|-------------------------|
| Email replies | Known contacts | New contacts, bulk sends |
| Payments | <$50 recurring | New payees, >$100 |
| Social media | Scheduled drafts | Posts, replies, DMs |
| File operations | Create, read | Delete, move outside vault |

### Error Recovery

The system MUST handle failures gracefully:
- **Transient errors** (network timeout): Exponential backoff retry (max 3 attempts)
- **Authentication errors**: Alert human, pause operations
- **Logic errors** (Claude misinterprets): Human review queue
- **System crashes** (orchestrator dies): Watchdog auto-restart

## Development Workflow

### Skill Development Cycle

1. Define skill behavior (input → output)
2. Implement as `.claude/skills/<skill-name>.md`
3. Test manually with Claude Code
4. Add to documentation if reusable

### Feature Development (Spec-Driven)

For each new feature (tier progression):
1. Create spec in `specs/<feature>/spec.md`
2. Generate plan with `/sp.plan`
3. Create tasks with `/sp.tasks`
4. Implement and validate
5. Document lessons learned

### Constitution Compliance

All pull requests and feature implementations MUST:
- Verify alignment with Core Principles
- Include security review for credential handling
- Ensure HITL workflow for sensitive actions
- Add audit logging for new actions

## Governance

### Amendment Process

1. Propose change with rationale
2. Document impact on existing features
3. Update version number (semantic versioning)
4. Migrate dependent artifacts (templates, docs)
5. Communicate changes to contributors

### Versioning

- **MAJOR**: Backward incompatible principle changes or removals
- **MINOR**: New principles added or materially expanded
- **PATCH**: Clarifications, wording fixes, non-semantic changes

### Compliance Review

- Weekly: Review action logs for anomalies
- Monthly: Credential rotation and security audit
- Quarterly: Full constitution review and update

**Version**: 1.0.0 | **Ratified**: 2026-02-21 | **Last Amended**: 2026-02-21
