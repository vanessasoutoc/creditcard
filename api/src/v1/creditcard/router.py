import json
from fastapi import APIRouter, HTTPException
from .serializer import CreditCardModel
from .document import CreditCard
from .service import CreditCardService
from mongoengine import NotUniqueError

router = APIRouter(prefix='/credit-card')

@router.get(
    path='',
    description='Lista de cartões de crédito',
    status_code=200
    )
def list() -> list[CreditCardModel]:
    creditcards = CreditCardService.list()
    return json.loads(creditcards.to_json())

@router.post(
    path='',
    description='Adiciona um cartão de crédito',
    status_code=200
    )
def create(credit_card: CreditCardModel) -> CreditCardModel:
    try:
        creditcard = CreditCardService.save(credit_card)
        return json.loads(creditcard.to_json())
    except Exception as error:
        raise HTTPException(status_code=422, detail=str('Error %s' % (error)))
