import pytest
from twttr import shorten

def test_shorten_default():
    with pytest.raises(TypeError):
        assert shorten()
def test_shorten_arg_alpha():
    assert shorten('Luiz Fillipe') == 'Lz Fllp'

def test_shorten_arg_alphanum():
    assert shorten('LUIz FIllipE 1320') == 'Lz Fllp 1320'

def test_shorten_arg_ponct():
    assert shorten('LUiz!!!') == 'Lz!!!'

