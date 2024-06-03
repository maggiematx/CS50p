from twttr import shortened

def test_default():
    assert shortened()
def test_argument():
    assert shortened("hello world")=="hll wrld"
