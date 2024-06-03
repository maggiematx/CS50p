from plates import is_valid

def test_basic_argument():
    assert value("CS50") == Valid

def test_num():
    assert value(" 88 ") == Invalid

def test_special_char():
    assert value("#$ma") == Invalid






