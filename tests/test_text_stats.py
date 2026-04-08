from pathlib import Path

import pytest

from src.text_stats import count_sentences, count_words, read_text_file


# ── fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture
def sample_txt_file(tmp_path: Path) -> Path:
    file_path = tmp_path / "sample.txt"
    file_path.write_text("Привіт, світ! Як справи? Добре.", encoding="utf-8")
    return file_path


@pytest.fixture
def empty_txt_file(tmp_path: Path) -> Path:
    file_path = tmp_path / "empty.txt"
    file_path.write_text("", encoding="utf-8")
    return file_path


@pytest.fixture
def non_txt_file(tmp_path: Path) -> Path:
    file_path = tmp_path / "document.docx"
    file_path.write_text("content", encoding="utf-8")
    return file_path


# ── read_text_file ─────────────────────────────────────────────────────────────

def test_read_text_file_returns_content(sample_txt_file: Path) -> None:
    content = read_text_file(str(sample_txt_file))
    assert "Привіт" in content


def test_read_text_file_empty(empty_txt_file: Path) -> None:
    assert read_text_file(str(empty_txt_file)) == ""


def test_read_text_file_invalid_extension(non_txt_file: Path) -> None:
    with pytest.raises(ValueError):
        read_text_file(str(non_txt_file))


# ── count_words ────────────────────────────────────────────────────────────────

@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello world", 2),
        ("Hello, world", 2),
        ("one two three", 3),
        ("a:b;c,d e", 5),
        ("", 0),
        ("  ", 0),
        ("word", 1),
        ("Hello; world: test, foo bar", 5),
    ],
)
def test_count_words(text: str, expected: int) -> None:
    assert count_words(text) == expected


def test_count_words_from_file(sample_txt_file: Path) -> None:
    content = read_text_file(str(sample_txt_file))
    assert count_words(content) > 0


# ── count_sentences ────────────────────────────────────────────────────────────

@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello! World.", 2),
        ("One sentence.", 1),
        ("First. Second! Third?", 3),
        ("Wait... Really?", 2),
        ("", 0),
        ("No ending", 1),
        ("Hello world", 1),
    ],
)
def test_count_sentences(text: str, expected: int) -> None:
    assert count_sentences(text) == expected


def test_count_sentences_from_file(sample_txt_file: Path) -> None:
    content = read_text_file(str(sample_txt_file))
    assert count_sentences(content) == 3
