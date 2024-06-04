from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/2") == 50
    assert convert("0/1") == 0
    assert convert("6/6") == 100


def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(1)=="E"
    assert gauge(99.5)=="F"


def test_value_error():
    with pytest.raises(ValueError):
        convert("x/y")

def test_zero_divison_error():
    with pytest.raises(ZeroDivisonError):
        convert("5/0")
