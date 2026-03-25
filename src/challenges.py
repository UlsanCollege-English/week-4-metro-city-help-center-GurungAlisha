"""Weekly Coding #3 starter code: Metro City Help Center.

Implement the required classes and functions below.
Use standard library only.
"""

from __future__ import annotations

from collections import deque


class ActionStack:
    """Stack of recent help-center actions using a Python list."""

    def __init__(self) -> None:
        self.items: list[str] = []

    def push(self, action: str) -> None:
        """Add an action to the top of the stack."""
        raise NotImplementedError

    def pop(self) -> str | None:
        """Remove and return the top action, or None if empty."""
        raise NotImplementedError

    def peek(self) -> str | None:
        """Return the top action without removing it, or None if empty."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        """Return True if the stack has no actions."""
        raise NotImplementedError


class RequestQueue:
    """Queue of waiting citizens using collections.deque."""

    def __init__(self) -> None:
        self.items: deque[str] = deque()

    def enqueue(self, name: str) -> None:
        """Add a citizen name to the back of the queue."""
        raise NotImplementedError

    def dequeue(self) -> str | None:
        """Remove and return the front citizen, or None if empty."""
        raise NotImplementedError

    def peek(self) -> str | None:
        """Return the front citizen without removing it, or None if empty."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        """Return True if the queue has no waiting citizens."""
        raise NotImplementedError


def is_note_balanced(note: str) -> bool:
    """Return True if (), [], and {} are balanced correctly in a note."""
    raise NotImplementedError


def process_request_line(citizens: list[str]) -> list[str]:
    """Return citizens in the order they are served."""
    raise NotImplementedError


def undo_recent_actions(actions: list[str], undo_count: int) -> list[str]:
    """Optional stretch: remove the most recent undo_count actions."""
    raise NotImplementedError
