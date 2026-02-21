# Claude Code Hooks Configuration

This folder contains project-level hooks for Claude Code.

## Available Hooks

### UserPromptSubmit
Runs after user submits a prompt, before Claude processes it.

### SessionStart
Runs when a new Claude session starts.

### Stop (Ralph Wiggum Loop)
Runs when Claude attempts to exit. Used for autonomous multi-step tasks.

## Hook Setup

To enable hooks, add them to your `.claude/settings/hooks.json`:

```json
{
  "hooks": {
    "UserPromptSubmit": "node .claude/hooks/user-prompt-submit.js",
    "Stop": "python3 .claude/hooks/ralph-wiggum.py"
  }
}
```

## Ralph Wiggum Hook (Gold Tier)

The Ralph Wiggum hook prevents Claude from exiting until a task is complete.
This will be implemented in Gold tier.

## Current Status

- [ ] UserPromptSubmit hook
- [ ] Stop hook (Ralph Wiggum)
- [ ] SessionStart hook
