#!/usr/bin/env python3
"""
Simple Polling File Watcher
Works on any filesystem including /mnt/d/ (WSL-Windows)
"""

import os
import shutil
import time
import logging
from pathlib import Path
from datetime import datetime
from typing import Set


class SimpleFileWatcher:
    """Simple polling-based file watcher."""

    def __init__(self, inbox_path: str, vault_path: str, poll_interval: int = 2):
        """
        Initialize the watcher.

        Args:
            inbox_path: Folder to watch for new files
            vault_path: Root vault path
            poll_interval: Seconds between checks
        """
        self.inbox_path = Path(inbox_path).expanduser()
        self.vault_path = Path(vault_path).expanduser()
        self.needs_action = self.vault_path / 'Needs_Action'
        self.poll_interval = poll_interval

        # Track processed files
        self.processed_files: Set[str] = set()
        self.logger = logging.getLogger('SimpleFileWatcher')

        # Ensure folders exist
        self.inbox_path.mkdir(parents=True, exist_ok=True)
        self.needs_action.mkdir(parents=True, exist_ok=True)
        (self.inbox_path / 'Processed').mkdir(exist_ok=True)

        # Scan existing files so we don't reprocess them
        self._scan_existing()

    def _scan_existing(self):
        """Scan for existing files to skip them."""
        for f in self.inbox_path.iterdir():
            if f.is_file() and not f.name.startswith('.'):
                self.processed_files.add(f.name)

    def _create_metadata(self, source: Path, dest: Path):
        """Create metadata markdown file."""
        meta_path = dest.with_suffix('.md')

        stat = source.stat()
        size_mb = stat.st_size / (1024 * 1024)

        content = f"""---
type: file_drop
original_name: {source.name}
size: {stat.st_size} bytes ({size_mb:.2f} MB)
created: {datetime.fromtimestamp(stat.st_ctime).isoformat()}
status: pending
---

# File Dropped for Processing

**File:** {source.name}
**Size:** {size_mb:.2f} MB

## Content

{source.read_text()[:500]}

## Suggested Actions

- [ ] Review the file content
- [ ] Process according to Company_Handbook.md
- [ ] Move to /Done when complete
"""

        meta_path.write_text(content)

    def _process_file(self, filepath: Path):
        """Process a new file."""
        self.logger.info(f'🔔 New file detected: {filepath.name}')

        try:
            # Copy to Needs_Action
            dest = self.needs_action / f'FILE_{filepath.name}'
            shutil.copy2(filepath, dest)

            # Create metadata
            self._create_metadata(filepath, dest)

            # Move to Processed
            processed = self.inbox_path / 'Processed' / filepath.name
            shutil.move(str(filepath), str(processed))

            self.logger.info(f'✅ Created: {dest.name}')

        except Exception as e:
            self.logger.error(f'❌ Error processing {filepath.name}: {e}')

    def run(self):
        """Main polling loop."""
        self.logger.info(f'📁 Watching: {self.inbox_path}')
        self.logger.info(f'⏱️  Poll interval: {self.poll_interval}s')
        self.logger.info('Press Ctrl+C to stop...')

        try:
            while True:
                # Check for new files
                for filepath in self.inbox_path.iterdir():
                    if filepath.is_file() and not filepath.name.startswith('.'):
                        if filepath.name not in self.processed_files:
                            self._process_file(filepath)
                            self.processed_files.add(filepath.name)

                time.sleep(self.poll_interval)

        except KeyboardInterrupt:
            self.logger.info('🛑 Stopped by user')


def main():
    """Entry point."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    from dotenv import load_dotenv
    project_root = Path(__file__).parent.parent.parent
    env_file = project_root / '.env'
    if env_file.exists():
        load_dotenv(env_file)

    vault_path = os.getenv('VAULT_PATH', str(project_root))
    inbox_path = os.getenv('WATCH_FOLDER', str(project_root / 'Inbox'))

    print(f"""
╔═══════════════════════════════════════════════════════════════╗
║               📁 Simple File Watcher (Polling)                ║
╚═══════════════════════════════════════════════════════════════╝

Watching: {inbox_path}
Vault:    {vault_path}

""")
    watcher = SimpleFileWatcher(inbox_path, vault_path)
    watcher.run()


if __name__ == '__main__':
    main()
