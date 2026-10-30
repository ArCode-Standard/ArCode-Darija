from idris_data.normalize import normalize_text


def test_normalize_preserves_darija_words_and_script():
    value = "  شنو   بغيتي؟  "
    assert normalize_text(value) == "شنو بغيتي؟"


def test_normalize_uses_unicode_nfc():
    assert normalize_text("e\u0301") == "é"


def test_normalize_rejects_non_string():
    try:
        normalize_text(42)  # type: ignore[arg-type]
    except TypeError:
        pass
    else:
        raise AssertionError("expected TypeError")
