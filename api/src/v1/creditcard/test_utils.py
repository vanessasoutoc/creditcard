import pytest
from .utils import Utils
from creditcard.exceptions import BrandNotFound

def test_is_valid_card_success():
    valid = Utils.is_valid_card('38520000023237')
    assert valid == True

def test_is_valid_card_error():
    valid = Utils.is_valid_card('1111111111111111')
    assert valid == False

def test_brand_card_success():
    brand = Utils.brand_card('4111111111111111')
    assert brand == 'visa'

def test_brand_card_error():
    with pytest.raises(BrandNotFound) as excinfo:
        Utils.brand_card('1111111111111111')
    assert str(excinfo.value) == "Card number does not match any brand"

def test_exp_date_format():
    date = Utils.exp_date_format('02/2024')
    assert date == '2024-02-29'

def test_validate_exp_date_success():
    valid = Utils.validate_exp_date('02/2024')
    assert valid == True

def test_validate_exp_date_error():
    with pytest.raises(ValueError) as excinfo:
        Utils.validate_exp_date('02-2024')
    assert str(excinfo.value) == "exp_date not valid"
