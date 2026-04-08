from pathlib import Path


def read_text_file(file_path: str) -> str:
    """Read content from a .txt file."""
    path = Path(file_path)
    if path.suffix.lower() != ".txt":
        raise ValueError("Supported file extension is .txt")
    return path.read_text(encoding="utf-8")
