from plates import is_valid

def test_alpha_start():
    assert is_valid('LFPS') == True
    assert is_valid('LF') == True
    assert is_valid('LF10') == True

def test_incorrect_start():
    assert is_valid('L F12') == False
    assert is_valid(' LF12') == False
    assert is_valid('L.F123') == False
    assert is_valid('1LFPS') == False
    assert is_valid('L2FPS') == False
    assert is_valid('') == False
    assert is_valid('@!LFPS') == False
    assert is_valid('!LFPS') == False
    assert is_valid('L123') == False
    assert is_valid('1LFPS') == False
    assert is_valid('*LF10') == False

def test_max_length():
    assert is_valid('AB1234') == True
    assert is_valid('ABCD12') == True

def test_incorrect_length():
    assert is_valid('L') == False
    assert is_valid('LFPS132') == False

def test_no_special_characters():
    assert is_valid('LFPS!') == False
    assert is_valid('@LFPS') == False
    assert is_valid('@!') == False

def test_numbers_in_middle():
    assert is_valid('LF1PS3') == False
    assert is_valid('7FP3S') == False

def test_first_number_zero():
    assert is_valid('LF0132') == False
    assert is_valid('LFPS0') == False
