#!/usr/bin/env python3
"""
Base Watcher Template
All watchers should inherit from BaseWatcher
"""

import time
import logging
from pathlib import Path
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict, Any
import os


class BaseWatcher(ABC):
    """Base class for all AI Employee watchers."""

    def __init__(self, vault_path: str, check_interval: int = 60):
        """
        Initialize the watcher.

        Args:
            vault_path: Path to the Obsidian vault
            check_interval: Seconds between checks
        """
        self.vault_path = Path(vault_path).expanduser()
        self.needs_action = self.vault_path / 'Needs_Action'
        self.inbox = self.vault_path / 'Inbox'
        self.check_interval = check_interval
        self.logger = logging.getLogger(self.__class__.__name__)

        # Ensure folders exist
        self.needs_action.mkdir(parents=True, exist_ok=True)
        self.inbox.mkdir(parents=True, exist_ok=True)

    @abstractmethod
    def check_for_updates(self) -> List[Dict[str, Any]]:
        """
        Check for new updates.

        Returns:
            List of items to process, each as a dict
        """
        pass

    @abstractmethod
    def create_action_file(self, item: Dict[str, Any]) -> Path:
        """
        Create an .md file in Needs_Action folder.

        Args:
            item: Item dict from check_for_updates

        Returns:
            Path to the created file
        """
        pass

    def log_action(self, action: str, details: Dict[str, Any]):
        """Log an action to the vault's Logs folder."""
        logs_dir = self.vault_path / 'Logs'
        logs_dir.mkdir(exist_ok=True)

        log_file = logs_dir / f"{datetime.now().strftime('%Y-%m-%d')}.json"

        import json
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "watcher": self.__class__.__name__,
            "action": action,
            "details": details
        }

        logs = []
        if log_file.exists():
            with open(log_file, 'r') as f:
                try:
                    logs = json.load(f)
                except json.JSONDecodeError:
                    logs = []

        logs.append(log_entry)

        with open(log_file, 'w') as f:
            json.dump(logs, f, indent=2)

    def run(self):
        """Main loop for the watcher."""
        self.logger.info(f'Starting {self.__class__.__name__}')

        while True:
            try:
                items = self.check_for_updates()
                self.logger.info(f'Found {len(items)} new items')

                for item in items:
                    try:
                        filepath = self.create_action_file(item)
                        self.log_action('created_action_file', {
                            'file': str(filepath),
                            'item': item
                        })
                        self.logger.info(f'Created: {filepath.name}')
                    except Exception as e:
                        self.logger.error(f'Error creating file: {e}')
                        self.log_action('error', {'error': str(e), 'item': item})

            except Exception as e:
                self.logger.error(f'Error in check loop: {e}')
                self.log_action('check_error', {'error': str(e)})

            time.sleep(self.check_interval)


class WatcherError(Exception):
    """Base exception for watcher errors."""
    pass


class TransientError(WatcherError):
    """Error that can be retried (e.g., network timeout)."""
    pass


class AuthenticationError(WatcherError):
    """Authentication failure - needs human intervention."""
    pass
