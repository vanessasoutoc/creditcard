from fastapi import APIRouter, HTTPException
from .serializer import CreditCardRequestSerializer, CreditCardResponseSerializer
from .service import CreditCardService

router = APIRouter(prefix='/credit-card')

creditcard_service = CreditCardService()

@router.get(
    path='',
    description='Lista de cartões de crédito',
    status_code=200,
    response_model=list[CreditCardResponseSerializer]
    )
def list():
    credit_cards = creditcard_service.list()
    return [CreditCardResponseSerializer(**card.to_mongo()) for card in credit_cards]

@router.post(
    path='',
    description='Adiciona um cartão de crédito',
    status_code=200,
    response_model=CreditCardResponseSerializer
    )
def create(credit_card: CreditCardRequestSerializer):
    try:
        creditcard = creditcard_service.save(credit_card)
        return CreditCardResponseSerializer(**creditcard.to_mongo())
    except Exception as error:
        raise HTTPException(status_code=422, detail=str('Error %s' % (error)))
