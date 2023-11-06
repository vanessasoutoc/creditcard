import json
from fastapi import APIRouter, HTTPException
from .serializer import CreditCardSerializer
from .document import CreditCard
from .service import CreditCardService
from mongoengine import NotUniqueError

router = APIRouter(prefix='/credit-card')

@router.get(
    path='',
    description='Lista de cartões de crédito',
    status_code=200
    )
def list() -> list[CreditCardSerializer]:
    creditcards = CreditCardService().list()
    return [CreditCardSerializer(**card.to_mongo()) for card in creditcards]

@router.post(
    path='',
    description='Adiciona um cartão de crédito',
    status_code=200
    )
def create(credit_card: CreditCardSerializer) -> CreditCardModel:
    try:
        creditcard = CreditCardService().save(credit_card)
        return [CreditCardSerializer(**card.to_mongo()) for card in creditcard]
    except Exception as error:
        raise HTTPException(status_code=422, detail=str('Error %s' % (error)))
