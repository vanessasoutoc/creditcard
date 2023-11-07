from fastapi import APIRouter, HTTPException
from .serializer import CreditCardSerializer
from .service import CreditCardService

router = APIRouter(prefix='/credit-card')

creditcard_service = CreditCardService()

@router.get(
    path='',
    description='Lista de cartões de crédito',
    status_code=200
    )
def list() -> list[CreditCardSerializer]:
    creditcards = creditcard_service.list()
    return [CreditCardSerializer(**card.to_mongo()) for card in creditcards]

@router.post(
    path='',
    description='Adiciona um cartão de crédito',
    status_code=200
    )
def create(credit_card: CreditCardSerializer) -> CreditCardSerializer:
    try:
        creditcard = creditcard_service.save(credit_card)
        return CreditCardSerializer(**creditcard.to_mongo())
    except Exception as error:
        raise HTTPException(status_code=422, detail=str('Error %s' % (error)))
