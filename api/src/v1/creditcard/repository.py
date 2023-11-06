from .models import CreditCardModel
from .document import CreditCard
from .utils import Utils
from mongoengine import *

class CreditCardRepository:
    def save(credit_card: CreditCardModel):
        try:
            Utils.validate_exp_date(credit_card.exp_date)
            brand = Utils.brand_card(credit_card.number)
            card = CreditCard(
                exp_date=Utils.exp_date_format(credit_card.exp_date),
                number=credit_card.number,
                holder=credit_card.holder,
                cvv=credit_card.cvv,
                brand=brand
                )
            card.validate()
            card.save()
            return card
        except errors.NotUniqueError as error:
            raise error
