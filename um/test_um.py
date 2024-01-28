import pytest
from um import count

def test_valid():
    assert count('haha, um, lets say, um, this is cool') == 2
    assert count('haha, um, lets say, um, this is cool...um!') == 3

def test_invalid():
    assert not count('haha, um, leumts say, um, this is cool') == 3
    assert not count('haha, um, lets say, um, this is coolum') == 3

def test_case_insensitive():
    assert count('haha, UM, lets, uM, say, Um, this is cool.. um') == 4

def test_none():
    with pytest.raises(TypeError):
        assert count()

