from fuel import convert and gauge

def test_convert():
    assert convert("1/2") == 50
    assert conver("0/1") == 0
    assert convert("6/6") == 0


def test_gauge():
    assert gauge("50%") == 50%
    assert gauge("1%")==E
    assert guage("99%")==F


def test_value_error():
    with pytest.raises(ValueError):
        convert("x/y)

def test_zero_divison_error():
    with pytest.raises(ZeroDivisonError):
        convert("5/0")
