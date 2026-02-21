#!/usr/bin/env python3
"""
AI Employee - Main Entry Point
Turbo Launch Autonomous FTE

Usage:
    ai-employee          - Show this help
    ai-watch             - Start file watcher
    ai-orchestrate       - Start orchestrator
"""

import os
import sys
import argparse
from pathlib import Path


def show_help():
    """Display help information."""
    print("""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║           🤖 Turbo Launch AI Employee v0.1.0                  ║
║                  Bronze Tier Foundation                       ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝

📍 Project: /mnt/d/class/AI_EMPLOYEE_FTE
📁 Windows: D:\\class\\AI_EMPLOYEE_FTE

Available Commands:
─────────────────────────────────────────────────────────────────

    ai-employee          Show this help message

    ai-watch             Start the file watcher (polling mode)
                        Monitors /Inbox for new files every 2s

    ai-orchestrate       Start the orchestrator
                        Coordinates watchers and triggers Claude

Environment Setup:
─────────────────────────────────────────────────────────────────

    1. Copy .env.example to .env
    2. Fill in your API credentials (Gmail, etc.)
    3. Run: uv sync

Getting Started:
─────────────────────────────────────────────────────────────────

    1. Open the vault in Obsidian
    2. Start Claude Code: claude --cwd .
    3. Try skills: /update-dashboard, /process-inbox

For more information, see README.md
    """)


def start_watcher():
    """Start the file system watcher."""
    from watchers.simple_file_watcher import main as watcher_main
    watcher_main()


def start_orchestrator():
    """Start the orchestrator."""
    from orchestrator.orchestrator import main as orch_main
    orch_main()


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Turbo Launch AI Employee",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        "command",
        nargs="?",
        choices=["watch", "orchestrate"],
        help="Command to run"
    )

    args = parser.parse_args()

    if args.command == "watch":
        start_watcher()
    elif args.command == "orchestrate":
        start_orchestrator()
    else:
        show_help()


if __name__ == "__main__":
    main()
