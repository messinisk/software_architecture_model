# utils/fs.py
"""Filesystem helpers."""

from pathlib import Path


def ensure_directory(path: str | Path) -> Path:
    """Create a directory if it does not exist and return its path."""
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def read_text(path: str | Path) -> str:
    """Read a UTF-8 text file and return its contents."""
    return Path(path).read_text(encoding="utf-8")


def write_text(path: str | Path, content: str) -> None:
    """Write UTF-8 text content to a file."""
    Path(path).write_text(content, encoding="utf-8")
