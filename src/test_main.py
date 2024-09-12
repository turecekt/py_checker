"""Unit testy."""
import main


def test_translation_from_alphabet_to_morse_code():
    """Překlad z Abecedy do Morseovy abecedy."""
    assert (main.translation("\"Jmenuji se Martin\"", True) ==
            ".-----.-...-.---.. .... --.-.-.-..-.")


def test_translation_from_alphabet_to_morse_code_autobus():
    """Překlad z Abecedy do Morseovy abecedy - autobus."""
    assert main.translation("\"Autobus\"", True) == ".-..------.....-..."


def test_translation_from_alphabet_to_morse_code_SOS():
    """Překlad z Abecedy do Morseovy abecedy - SOS."""
    assert main.translation("\"SOS\"", True) == "...---..."


def test_translation_from_alphabet_to_morse_code_white_space():
    """Překlad z Abecedy do Morseovy abecedy - mezery."""
    assert main.translation("\"  \"", True) == ""


def test_white_space_end():
    """Mezera na konci slova."""
    assert (main.translation("\"--|.-|--| |....|.-..|.-|-..  \"", False) ==
            "mam hlad")


def test_white_space_start():
    """Mezera na začátku slova."""
    assert (main.translation("\" -|---| |.---|...|.|--| |.---|.-\"", False) ==
            "to jsem ja")


def test_white_space_start_end():
    """Mezera na začátku a konci slova."""
    assert (main.translation("\"  .-..|.-|...-|..|-.-.|.| |.-| |-|.-|-..."
                             "|..-|.-..|.  \"", False) == "lavice a tabule")


def test_none():
    """None string."""
    assert main.translation(None, True) == ""


def test_empty_string():
    """Prázdný string."""
    assert main.translation("", True) == ""


def test_translation_from_morse_code_to_alphabet_SOS():
    """Překlad z Morseovy abecedy do Abecedy - SOS."""
    assert main.translation("\"...|---|...\"", False) == "sos"


def test_translation_from_morse_code_to_alphabet():
    """Překlad z Morseovy abecedy do Abecedy - ahoj jmenuji se martin."""
    assert (main.translation("\".-|....|---|.---| |.---|--|.|-.|..-|.---"
                             "|..| |...|.| |--|.-|.-.|-|..|-.\"", False) ==
            "ahoj jmenuji se martin")


def test_translation_from_morse_code_to_alphabet_autobus():
    """Překlad z Morseovy abecedy do Abecedy - autobus."""
    assert (main.translation("\".-|..-|-|---|-...|..-|...\"", False) ==
            "autobus")


def test_morseCodeTranslation_koberec_nebo_parkety():
    """Překlad z Morseovy abecedy do Abecedy - koberec nebo parkety."""
    assert (main.morseCodeTranslation("-.-|---|-...|.|.-.|.|-.-.| |-.|"
                                      ".|-...|---| |.--.|.-|.-.|-.-|.|-|"
                                      "-.--") ==
            "koberec nebo parkety")


def test_alphabetTranslation_v_lese_jsou_stromy():
    """Překlad z Morseovy abecedy do Abecedy - v lese jsou stromy."""
    assert (main.alphabetTranslation("v lese jsou stromy") == "...- .-......."
            " .---...---..- ...-.-.------.--")
