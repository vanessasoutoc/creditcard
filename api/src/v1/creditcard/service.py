from .serializer import CreditCardSerializer
from .document import CreditCard
from .utils import validate_exp_date, brand_card, exp_date_format
from .cryptografy import encode

class CreditCardService:
    def list(self) -> []:
        return list(CreditCard.objects())

    def save(self, credit_card: CreditCardSerializer):
        validate_exp_date(credit_card.exp_date)
        brand = brand_card(credit_card.number)
        encrypted_values = encode(credit_card.number)
        card = CreditCard(
            exp_date=exp_date_format(credit_card.exp_date),
            number=encrypted_values['credit_card'],
            key=encrypted_values['key'],
            holder=credit_card.holder,
            cvv=credit_card.cvv,
            brand=brand
            )
        # card.save()
        return card
