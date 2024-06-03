from plates import is_valid

def test_basic_argument():
    assert is_valid("CS50") == True
    assert is_valid("CS")== True

def test_len():
    assert is_valid("CS50909")==False
    assert is_valid("MAMAMAMA")==False

def test_num():
    assert is_valid(" 88 ") == False
    assert is_valid("CS0505")==False

def test_special_char():
    assert is_valid("#$ma") == False
    assert is_valid("CS50#$)== False








