# Update Dashboard

Updates the Dashboard.md with current system state.

## What This Skill Does

1. Scans all folders to count items
2. Reads /Logs for today's activity
3. Updates Dashboard.md sections:
   - Today's Summary
   - Pending Approvals
   - Recent Activity
   - Quick Stats
   - System Status
4. Updates "Last Processed" timestamp

## Usage

```
/update-dashboard
```

## What Gets Counted

| Folder | Metric |
|--------|--------|
| Needs_Action | Priority Items |
| Pending_Approval | Pending Approvals |
| Done/emails today | Emails Processed |
| Done/tasks today | Tasks Completed |
| Logs | Activity entries |

## Rules

- Append to Recent Activity, don't replace
- Keep only last 10 activity items
- Update timestamp to ISO format
- Preserve all other dashboard content
