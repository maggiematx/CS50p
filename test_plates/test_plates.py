from plates import is_valid

def test_basic_argument():
    assert is_valid("CS50") == True
    assert is_valid("CS") == True
    assert is_valid("C50") == False

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
    assert is_valid("CS50A") == False  # Letter after number
    assert is_valid("CS05") == False   # Number starting with 0
    assert is_valid("CS5") == True     # Valid plate, single digit

if __name__ == "__main__":
    test_basic_argument()
    test_len()
    test_num()
    test_special_char()
    test_edge_cases()
    test_number_placement()







