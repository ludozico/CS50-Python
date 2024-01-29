from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    jar.deposit(5)
    assert str(jar) == '\U0001F36A\U0001F36A\U0001F36A\U0001F36A\U0001F36A'

def test_deposit():
    jar = Jar()
    jar.deposit(12)
    assert jar.size == jar.capacity
    with pytest.raises(ValueError):
        assert jar.deposit(1)

def test_withdraw():
    jar = Jar()
    jar.deposit(4)
    jar.withdraw(3)
    assert jar.size == 1
    with pytest.raises(ValueError):
        assert jar.withdraw(3)


