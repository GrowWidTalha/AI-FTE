# Process Inbox

Processes all files in the /Inbox folder and routes them appropriately.

## What This Skill Does

1. Reads all markdown files in /Inbox
2. Categorizes each item (email, file drop, message, etc.)
3. Routes to appropriate folder:
   - Simple items → /Needs_Action
   - Urgent items → /Needs_Action (with high priority flag)
   - Already handled → /Done
4. Updates Dashboard.md with new item counts

## Usage

```
/process-inbox
```

## Rules

- Always check Company_Handbook.md for trigger words
- Flag items with legal/financial/deadline keywords
- Never delete items, always move them
- Log all actions to /Logs/
