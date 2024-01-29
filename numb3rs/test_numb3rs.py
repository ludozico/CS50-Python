from numb3rs import validate

def test_valid_ip():
    assert validate('200.100.50.1') == True

def test_validate_notnumba():
    assert validate('haha.hehe.hihi.hoho') == False
    assert validate('haha.111.111.111') == False
    assert validate('111.hehe.111.111') == False
    assert validate('111.111.hihi.111') == False
    assert validate('111.111.111.hoho') == False

def test_validate_highnumba():
    assert validate('300.299.298.297') == False
    assert validate('200.299.198.197') == False
    assert validate('200.19.298.197') == False
    assert validate('100.99.198.297') == False
