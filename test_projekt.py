"""Soubor s testy."""


from projekt import MorseCode
morseCode = MorseCode()


def test_get_words():
    """Test funkce pro rozdělení věty podle slov."""
    assert morseCode.get_words("test 123 asd") == ["test", "123", "asd"]


def test_encode():
    """Test funkce pro převod do morseovy abecedy."""
    assert morseCode.encode("test 123 asd") \
        == ("- . ... - ...---... .---- ..--- ...-- "
            "...---... .- ... -.. ...---... ")


def test_decode():
    """Test funkce pro převod z morseovy abecedy."""
    assert morseCode.decode("- . ... - ...---... .---- ..--- "
                            "...-- ...---... .- ... -..") == "test 123 asd "
