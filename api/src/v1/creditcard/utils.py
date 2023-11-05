from creditcard import CreditCard
from creditcard.exceptions import BrandNotFound

class Card:
    def __init__(self, number: str):
        self.number = number

    def is_valid_card(self):
        return CreditCard(self.number).is_valid()

    def brand_card(self):
        try:
            return CreditCard(self.number).get_brand()
        except BrandNotFound:
            return BrandNotFound
