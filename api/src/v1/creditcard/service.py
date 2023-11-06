from .serializer import CreditCardSerializer
from .document import CreditCard
from .utils import validate_exp_date, brand_card, exp_date_format

class CreditCardService:
    def list() -> []:
        return CreditCard.objects()

    def save(credit_card: CreditCardSerializer):
        validate_exp_date(credit_card.exp_date)
        brand = brand_card(credit_card.number)
        card = CreditCard(
            exp_date=exp_date_format(credit_card.exp_date),
            number=credit_card.number,
            holder=credit_card.holder,
            cvv=credit_card.cvv,
            brand=brand
            )
        card.save()
        return card
