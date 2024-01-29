from bank import value

def test_hello_greeting():
    assert value('hello') == 0
def test_HELLO_greeting():
    assert value('HELLO') == 0
def test_h_greeting():
    assert value("hi") == 20
def test_H_greeting():
    assert value('HI') == 20
def test_other_Whats_up():
    assert value('Whats up fellah?') == 100
def test_whitespace_greeting():
    assert value('hello') == 0
def test_empty_string():
    assert value('') == 100
