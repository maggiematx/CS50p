from plates import is_valid

def test_basic_argument():
    assert is_valid("CS50") == True
    assert is_valid("CS")== True
    assert is_valid("C50") == False

def test_len():
    assert is_valid("CS50909")==False
    assert is_valid("CSCSCS")==True

def test_num():
    assert is_valid(" 88") == False
    assert is_valid("50CS")==False
    assert is_valid("CS0505")==False

def test_special_char():
    assert is_valid("#$ma") == False
    assert is_valid("CS50#$")== False








