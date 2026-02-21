#!/usr/bin/env python3
"""
AI Employee Orchestrator
Master process that coordinates watchers and triggers Claude Code processing.
"""

import os
import subprocess
import time
import signal
import logging
from pathlib import Path
from typing import List
import json


class Orchestrator:
    """Main orchestrator for the AI Employee system."""

    def __init__(self, vault_path: str):
        self.vault_path = Path(vault_path).expanduser()
        self.needs_action = self.vault_path / 'Needs_Action'
        self.plans = self.vault_path / 'Plans'
        self.pending_approval = self.vault_path / 'Pending_Approval'
        self.approved = self.vault_path / 'Approved'
        self.done = self.vault_path / 'Done'

        self.processes: List[subprocess.Popen] = []
        self.running = True
        self.logger = logging.getLogger('Orchestrator')

        # Setup signal handlers
        signal.signal(signal.SIGINT, self._shutdown)
        signal.signal(signal.SIGTERM, self._shutdown)

    def _shutdown(self, signum, frame):
        """Gracefully shutdown all processes."""
        self.logger.info(f'Received signal {signum}, shutting down...')
        self.running = False
        for proc in self.processes:
            proc.terminate()

    def start_watcher(self, watcher_script: str, args: List[str] = None) -> subprocess.Popen:
        """Start a watcher process."""
        scripts_dir = Path(__file__).parent.parent
        script_path = scripts_dir / 'watchers' / watcher_script

        cmd = ['python3', str(script_path)]
        if args:
            cmd.extend(args)

        self.logger.info(f'Starting watcher: {watcher_script}')
        proc = subprocess.Popen(cmd)
        self.processes.append(proc)
        return proc

    def check_needs_action(self) -> List[Path]:
        """Check for files needing action."""
        if not self.needs_action.exists():
            return []
        return list(self.needs_action.glob('*.md'))

    def trigger_claude_processing(self, files: List[Path]):
        """Trigger Claude Code to process files."""
        if not files:
            return

        self.logger.info(f'Triggering Claude to process {len(files)} files')

        # Create a processing prompt
        prompt = f"""Process the following files in /Needs_Action:

{', '.join(f.name for f in files)}

For each file:
1. Read and understand the content
2. Check Company_Handbook.md for rules
3. Create a plan in /Plans if needed
4. For sensitive actions, create an approval request in /Pending_Approval
5. Move processed files to /Done

Update Dashboard.md when complete."""

        # Write prompt to a file for Claude to find
        trigger_file = self.vault_path / '.claude_trigger.txt'
        trigger_file.write_text(prompt)

        self.logger.info(f'Trigger file created: {trigger_file}')

    def monitor_approvals(self):
        """Monitor approved folder and execute actions."""
        if not self.approved.exists():
            return

        approved_files = list(self.approved.glob('*.md'))

        for filepath in approved_files:
            self.logger.info(f'Executing approved action: {filepath.name}')
            # Move to Done after execution
            self.done.mkdir(exist_ok=True)
            filepath.rename(self.done / filepath.name)

    def run(self):
        """Main orchestrator loop."""
        self.logger.info('Starting AI Employee Orchestrator')

        # Start watchers (uncomment when ready)
        # self.start_watcher('filesystem_watcher.py')

        last_check = 0
        check_interval = 30  # seconds

        while self.running:
            try:
                # Check for new action items
                if time.time() - last_check > check_interval:
                    files = self.check_needs_action()
                    if files:
                        self.trigger_claude_processing(files)
                    last_check = time.time()

                # Monitor approvals
                self.monitor_approvals()

                # Check process health
                for proc in self.processes:
                    if proc.poll() is not None:
                        self.logger.warning(f'Process {proc.pid} exited')

                time.sleep(5)

            except Exception as e:
                self.logger.error(f'Error in main loop: {e}')
                time.sleep(10)

        self.logger.info('Orchestrator stopped')


def main():
    """Entry point for ai-orchestrate command."""
    from dotenv import load_dotenv

    # Load .env from project root
    project_root = Path(__file__).parent.parent.parent
    env_file = project_root / '.env'
    if env_file.exists():
        load_dotenv(env_file)

    vault_path = os.getenv('VAULT_PATH', str(project_root))
    log_file = project_root / 'Logs' / 'orchestrator.log'
    log_file.parent.mkdir(exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

    print(f"""
╔═══════════════════════════════════════════════════════════════╗
║                 🎵 AI Employee Orchestrator                  ║
╚═══════════════════════════════════════════════════════════════╝

Vault: {vault_path}
Log:   {log_file}

Coordinating watchers and triggering Claude processing...
Press Ctrl+C to stop...
    """)

    orchestrator = Orchestrator(vault_path)
    orchestrator.run()


if __name__ == '__main__':
    main()
