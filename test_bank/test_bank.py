from bank import value

def test_basic_argument():
    assert value("hello world") == 0
    assert value("hello")==0
    assert value("how are you?")==20

def test_number():
    assert value(123)==100

def test_cap():
    assert value(" hi ")==20

def test_special():
    assert value("@#4")==100


