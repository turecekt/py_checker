"""Testing file for morse."""
from translator import encode, decode

"""Testing encode function."""


def test_encode_normally():
    """Testing the encode function with correct data."""
    desired_result = '- . ... - '
    result = encode('test')
    assert result == desired_result


def test_encode_no_input():
    """Testing encode function with no input."""
    desired_result = ''
    result = encode('')
    assert result == desired_result


def test_encode_cap():
    """Testing encode function with cap."""
    desired_result = '- . ... - '
    result = encode("Test")
    assert result == desired_result


def test_encode_all_caps():
    """Testing encode function with all caps."""
    desired_result = '- . ... - '
    result = encode("TEST")
    assert result == desired_result


def test_encode_error():
    """Testing encode function with error handling."""
    desired_result = 'Data not formatted properly'
    result = encode('123')
    assert result == desired_result


"""Testing decode function."""


def test_decode_normally():
    """Testing the decode function with correct data."""
    desired_result = 'test'
    result = decode('- . ... - ')
    assert result == desired_result


def test_decode_no_input():
    """Testing decode function with no input."""
    desired_result = ''
    result = decode('')
    assert result == desired_result


def test_decode_error():
    """Testing decode function with error handling."""
    desired_result = 'Data not formatted properly'
    result = decode('test')
    assert result == desired_result


def test_decode_space():
    """Testing decode function with space in sentence."""
    desired_result = ' '
    result = decode('/ ')
    assert result == desired_result
