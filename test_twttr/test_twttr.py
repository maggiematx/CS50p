from twttr import shorten

def test_basic_argument():
    # Basic test cases
    assert shorten("hello world") == "hll wrld"

def test_vowel():
    assert shorten("aeiou") == ""

def test_no_input():
    assert shorten("") == ""

def test_caps():
    assert shorten("HELLO WORLD") == "HLL WRLD"
    assert shorten("AEIOU") == ""

def test_numbers():
    assert shorten("12345") == "12345"
    assert shorten("hello123") == "hll123"

def test_special():
    assert shorten("hello!") == "hll!"

if __name__ == "__main__":
    test_argument()
