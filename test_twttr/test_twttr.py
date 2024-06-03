from twttr import shortened

def test_argument():
    # Basic test cases
    assert shortened("hello world") == "hll wrld"
    assert shortened("aeiou") == ""
    assert shortened("") == ""

    # Edge test cases
    assert shortened("HELLO WORLD") == "HLL WRLD"  # Test uppercase letters
    assert shortened("AEIOU") == ""  # Uppercase vowels should also be removed
    assert shortened("12345") == "12345"  # Numbers should remain unchanged
    assert shortened("hello123") == "hll123"  # Mixed letters and numbers
    assert shortened("hello!") == "hll!"  # Special characters should remain unchanged

if __name__ == "__main__":
    test_argument()
 