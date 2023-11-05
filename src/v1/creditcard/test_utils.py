from utils import Card
from creditcard.exceptions import BrandNotFound

def test_is_valid_card_success():
    valid = Card('38520000023237').is_valid_card()
    assert valid == True

def test_is_valid_card_error():
    valid = Card('1111111111111111').is_valid_card()
    assert valid == False

def test_brand_card_success():
    brand = Card('4111111111111111').brand_card()
    assert brand == 'visa'

def test_brand_card_error():
    brand = Card('1111111111111111').brand_card()
    assert brand == BrandNotFound
