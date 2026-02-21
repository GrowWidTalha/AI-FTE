#!/usr/bin/env python3
"""
File System Watcher
Monitors a drop folder for new files and creates action items.
"""

import os
import shutil
import logging
from pathlib import Path
from datetime import datetime
from typing import Optional

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent


class DropFolderHandler(FileSystemEventHandler):
    """Handler for file system events."""

    def __init__(self, vault_path: str):
        super().__init__()
        self.vault_path = Path(vault_path).expanduser()
        self.needs_action = self.vault_path / 'Needs_Action'
        self.inbox = self.vault_path / 'Inbox'
        self.logger = logging.getLogger('DropFolderHandler')

    def on_created(self, event: FileSystemEvent):
        """Handle file creation events."""
        if event.is_directory:
            return

        source = Path(event.src_path)

        # Skip hidden files and temporary files
        if source.name.startswith('.') or source.name.startswith('~'):
            return

        self.logger.info(f'New file detected: {source.name}')

        try:
            # Copy to Needs_Action
            dest = self.needs_action / f'FILE_{source.name}'
            shutil.copy2(source, dest)

            # Create metadata file
            self._create_metadata(source, dest)

            # Move to Inbox/Processed
            inbox_processed = self.inbox / 'Processed'
            inbox_processed.mkdir(exist_ok=True)
            shutil.move(str(source), inbox_processed / source.name)

            self.logger.info(f'Created action file: {dest.name}')

        except Exception as e:
            self.logger.error(f'Error processing file: {e}')

    def _create_metadata(self, source: Path, dest: Path):
        """Create metadata markdown file."""
        meta_path = dest.with_suffix('.md')

        # Get file info
        stat = source.stat()
        size_mb = stat.st_size / (1024 * 1024)

        content = f"""---
type: file_drop
original_name: {source.name}
size: {stat.st_size} bytes ({size_mb:.2f} MB)
created: {datetime.fromtimestamp(stat.st_ctime).isoformat()}
modified: {datetime.fromtimestamp(stat.st_mtime).isoformat()}
status: pending
---

# File Dropped for Processing

**File:** {source.name}
**Size:** {size_mb:.2f} MB
**Type:** {source.suffix or 'Unknown'}

## Suggested Actions

- [ ] Review the file content
- [ ] Determine what action is needed
- [ ] Process according to Company_Handbook.md

## Notes

Add any notes about this file here.
"""

        meta_path.write_text(content)


class FileSystemWatcher:
    """Watcher that monitors a folder for new files."""

    def __init__(self, vault_path: str, watch_folder: Optional[str] = None):
        """
        Initialize the filesystem watcher.

        Args:
            vault_path: Path to the Obsidian vault
            watch_folder: Path to folder to monitor (defaults to vault/Inbox)
        """
        self.vault_path = Path(vault_path).expanduser()
        self.watch_folder = Path(watch_folder).expanduser() if watch_folder else self.vault_path / 'Inbox'

        # Ensure folders exist
        self.watch_folder.mkdir(parents=True, exist_ok=True)
        (self.vault_path / 'Needs_Action').mkdir(parents=True, exist_ok=True)
        (self.vault_path / 'Inbox').mkdir(exist_ok=True)

        self.logger = logging.getLogger(self.__class__.__name__)
        self.handler = DropFolderHandler(str(self.vault_path))
        self.observer = Observer()

    def run(self):
        """Start watching the folder."""
        self.observer.schedule(self.handler, str(self.watch_folder), recursive=False)
        self.observer.start()
        self.logger.info(f'Watching folder: {self.watch_folder}')

        try:
            import time
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()


def main():
    """Entry point for ai-watch command."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Try to load .env from project root
    from dotenv import load_dotenv
    project_root = Path(__file__).parent.parent.parent
    env_file = project_root / '.env'
    if env_file.exists():
        load_dotenv(env_file)

    vault_path = os.getenv('VAULT_PATH', str(project_root))
    watch_folder = os.getenv('WATCH_FOLDER', str(project_root / 'Inbox'))

    print(f"""
╔═══════════════════════════════════════════════════════════════╗
║                   📁 File System Watcher                      ║
╚═══════════════════════════════════════════════════════════════╝

Watching: {watch_folder}
Vault:    {vault_path}

Press Ctrl+C to stop...
    """)

    watcher = FileSystemWatcher(
        vault_path=vault_path,
        watch_folder=watch_folder
    )
    watcher.run()


if __name__ == '__main__':
    main()
