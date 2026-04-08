import re
from pathlib import Path


def read_text_file(file_path: str) -> str:
    """Read content from a .txt file."""
    path = Path(file_path)
    if path.suffix.lower() != ".txt":
        raise ValueError("Supported file extension is .txt")
    return path.read_text(encoding="utf-8")


def count_words(text: str) -> int:
    """Count words in text. Delimiters: space, comma, colon, semicolon."""
    if not text or not text.strip():
        return 0
    words = re.split(r"[ ,;:]+", text.strip())
    return len([w for w in words if w])


def count_sentences(text: str) -> int:
    """Count sentences. Endings: '.', '!', '?', '...'"""
    if not text or not text.strip():
        return 0
    parts = re.split(r"[.!?]+", text)
    return len([p for p in parts if p.strip()])
