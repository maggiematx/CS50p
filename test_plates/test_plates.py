from plates import is_valid

def test_basic_argument():
    assert is_valid("CS50") == "Valid"

def test_num():
    assert is_valid(" 88 ") == "Invalid"

def test_special_char():
    assert is_valid("#$ma") == "Invalid"






