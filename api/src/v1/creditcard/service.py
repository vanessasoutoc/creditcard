from .serializer import CreditCardResponseSerializer, CreditCardRequestSerializer
from .document import CreditCard
from .utils import validate_exp_date, brand_card, exp_date_format
from .cryptografy import encode

class CreditCardService:
    def list(self) -> []:
        return list(CreditCard.objects())

    def save(self, credit_card: CreditCardRequestSerializer)->CreditCardResponseSerializer:
        validate_exp_date(credit_card.exp_date)
        brand = brand_card(credit_card.number)
        card = CreditCard(
            exp_date=exp_date_format(credit_card.exp_date),
            number=encode(credit_card.number),
            holder=credit_card.holder,
            cvv=credit_card.cvv,
            brand=brand
            )
        card.save()
        return card

    def detail(self, id: str)->CreditCardResponseSerializer:
        return CreditCard.objects.get(id=id)
