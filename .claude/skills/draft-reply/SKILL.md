# Draft Reply

Creates a draft reply for an email or message.

## What This Skill Does

1. Reads an email or message from /Needs_Action or /In_Progress
2. Checks Company_Handbook.md for templates and tone
3. Creates a draft response
4. Saves to /Pending_Approval for review

## Usage

```
/draft-reply <filename>
```

or

```
Draft a reply to: [message description]
```

## Draft Template

```markdown
---
type: draft_reply
original_file: EMAIL_xxx.md
to: [recipient]
subject: [subject]
requires_approval: true
created: 2026-02-21T10:30:00Z
---

# Draft Reply

**To:** [recipient]
**Subject:** [subject]

## Draft

[Your draft here]

## Notes

- Used template: [template name]
- Checked handbook: [relevant section]
- Reasoning: [why this approach]

## To Approve

1. Review the draft
2. Edit if needed
3. Move to /Approved to send
4. Move to /Rejected to cancel
```

## Rules

- ALWAYS use Turbo Launch tone (professional but direct)
- NEVER include legal promises
- ALWAYS use "approximately" for timelines
- Check for trigger words in original before drafting
- Use templates from Company_Handbook.md when available
