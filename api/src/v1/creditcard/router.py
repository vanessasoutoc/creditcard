import json
from fastapi import APIRouter
from .models import CreditCardModel
from .document import CreditCard
from .utils import Utils

router = APIRouter(prefix='/credit-card')

@router.get("")
def list():
    creditcards = CreditCard.objects()
    return{"cards": json.loads(creditcards.to_json())}

@router.post("")
def create(credit_card: CreditCardModel):
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
        card.save()
        return json.loads(card.to_json())
    except Exception as error:
        return "Error %s" % (error)
