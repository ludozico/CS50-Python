""" testing seasons """
import pytest
from seasons import ageinmin
import datetime

def test_valid():
    assert ageinmin(datetime.datetime.strptime('1996-06-11', '%Y-%m-%d').date()) == 'Fourteen million, five hundred thirteen thousand, seven hundred sixty minutes'

def test_invalid_dates_formats():
   with pytest.raises(ValueError):
       ageinmin(datetime.datetime.strptime('11-06-1996', 'Y-%m-%d').date())

   with pytest.raises(ValueError):
       ageinmin(datetime.datetime.strptime('1996-13-11', '%Y-%m-%d').date())

