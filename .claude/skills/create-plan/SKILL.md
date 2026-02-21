# Create Plan

Creates an execution plan for a task in /Needs_Action.

## What This Skill Does

1. Reads a specific file from /Needs_Action
2. Analyzes the requirements
3. Creates a PLAN_*.md file in /Plans/
4. Moves original to /In_Progress/

## Usage

```
/create-plan <filename>
```

or

```
Create a plan for: [task description]
```

## Plan Template

```markdown
---
created: 2026-02-21T10:30:00Z
status: pending
original_file: NEEDS_ACTION_filename.md
priority: high|medium|low
---

# Objective: [Brief description]

## Context

[What triggered this task]

## Steps

- [ ] Step 1
- [ ] Step 2
- [ ] Step 3

## Approval Required

[Yes/No - explain if yes]

## Resources Needed

- [ ] Information from Company_Handbook.md
- [ ] Client input
- [ ] External tool (MCP server)

## Expected Outcome

[What "done" looks like]
```

## Rules

- Check Company_Handbook.md before suggesting actions
- Flag any step that needs approval
- Estimate time for each step
- Identify bottlenecks
