from twttr import shortened

def test_argument():
    assert shortened("hello world")=="hll wrld"
    assert shortened("aeiou")==""
    assert shortened("")==""
    
if __name__ == "__main__":
    test_argument()
