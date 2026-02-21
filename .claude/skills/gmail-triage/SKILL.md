# Gmail Triage

Reviews and triages new emails from /Needs_Action that were created by the Gmail Watcher.

## What This Skill Does

1. Finds all EMAIL_*.md files in /Needs_Action
2. For each email:
   - Checks Company_Handbook.md for handling rules
   - Identifies trigger words (legal, financial, deadline)
   - Determines if auto-reply is appropriate
   - Creates draft response if needed
3. Creates approval request for sensitive emails
4. Moves processed emails to /Done

## Usage

```
/gmail-triage
```

## Rules

- NEVER auto-reply to emails with legal keywords
- ALWAYS flag payments over $500 for approval
- Use VIP contacts from handbook to prioritize
- Follow Turbo Launch tone guidelines

## Output

For each processed email, updates the file with:

```yaml
triaged: true
action_taken: [drafted|flagged|approved|skipped]
requires_approval: true/false
```
