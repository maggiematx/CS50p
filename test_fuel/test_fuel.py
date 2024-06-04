from fuel import convert and gauge

def test_basic_argument():
    assert convert("1/2") == 50%
    assert gauge("50%) == .5

def test_len():
    assert is_valid("CS50909") == False
    assert is_valid("MAMAMAMA") == False

def test_num():
    assert is_valid("88") == False
    assert is_valid("50CS") == False
    assert is_valid("CS0505") == False
    assert is_valid("CS50") == True  # valid example
    assert is_valid("C50") == False  # invalid, not enough initial letters

def test_special_char():
    assert is_valid("#$ma") == False
    assert is_valid("CS50#$") == False

def test_edge_cases():
    assert is_valid("HI") == True
    assert is_valid("H1") == False
    assert is_valid("H12") == False
    assert is_valid("HI1234") == True

def test_number_placement():
    assert is_valid("CS50A") == False
    assert is_valid("CS05") == False
    assert is_valid("CS5") == True






