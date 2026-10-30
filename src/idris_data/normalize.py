"""Conservative text normalization helpers.

The default normalizer applies Unicode NFC and whitespace cleanup only. It does
not transliterate, remove diacritics, rewrite spelling, or erase dialect forms.
"""

from __future__ import annotations

import unicodedata


def normalize_text(text: str) -> str:
    """Normalize Unicode composition and collapse whitespace without rewriting words."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    normalized = unicodedata.normalize("NFC", text)
    return " ".join(normalized.split())
