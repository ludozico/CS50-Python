import pytest
from working import convert

def test_valid_conv():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'

def test_inexis_time1():
    with pytest.raises(ValueError):
        convert('9:00 AM to 5:60 PM')
def test_inexis_time2():
    with pytest.raises(ValueError):
        convert('9:70 AM to 5:30 PM')
def test_inexis_time3():
    with pytest.raises(ValueError):
        convert('-9:20 AM to 5:30 PM')
def test_inexis_time4():
    with pytest.raises(ValueError):
        convert('9:-10 AM to 5:30 PM')
def test_inexis_time5():
    with pytest.raises(ValueError):
        convert('9:00 AM to -4:30 PM')
def test_inexis_time6():
    with pytest.raises(ValueError):
        convert('9:20 AM to 5:-30 PM')
def test_incorr_input():
    with pytest.raises(ValueError):
        assert convert('haha')
        assert convert()




