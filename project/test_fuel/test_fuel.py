import pytest
from fuel import convert, gauge

def test_convert_valid():
    assert convert("1/4") == 25
    assert convert("0/1") == 0

def test_convert_invalid_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert_invalid_bigger():
    with pytest.raises(ValueError):
        convert("5/3")

def test_gauge_F():
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'

def test_gauge_E():
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'

def test_gauge_percen():
    assert gauge(50) == '50%'
