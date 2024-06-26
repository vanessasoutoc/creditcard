from typing import Optional, Any
from pydantic import BaseModel, Field, field_validator, model_validator
from datetime import datetime

from .document import CreditCard
from .cryptografy import decode
from .utils import matching_credit_card_number

class CreditCardRequestSerializer(BaseModel):
    exp_date: Any = Field(...)
    holder: str = Field(...)
    number: str = Field(...)
    cvv: str = Field(...)
    brand: Optional[str] = Field(None)

    class ConfigDict:
        json_schema_extra = {
            'example': {
                'exp_date': '12/2023',
                'holder': 'Armindo Juvenal Soares',
                'number': '4111111111111111',
                'cvv': '100',
                'brand': 'visa'
            }
        }

    @field_validator('number')
    def number(cls, value):
        creditcardsSaved = CreditCard.objects()
        if len(creditcardsSaved) > 0:
            for card in creditcardsSaved:
                card_decode = decode(card['number'])
                if(card_decode == value):
                    raise ValueError(f'number {value} exists')
        return value

class CreditCardResponseSerializer(BaseModel):
    id: Optional[str] = Field(None, alias='_id')
    exp_date: Any = Field(...)
    holder: str = Field(...)
    number: str = Field(...)
    cvv: str = Field(...)
    brand: Optional[str] = Field(None)

    class ConfigDict:
        json_schema_extra = {
            'example': {
                'exp_date': '12/2023',
                'holder': 'Armindo Juvenal Soares',
                'number': '4111111111111111',
                'cvv': '100',
                'brand': 'visa'
            }
        }

    @field_validator('exp_date')
    def sync_exp_date(cls, value):
        if isinstance(value, datetime):
            return datetime.strftime(value, "%m/%y")
        return value

    @model_validator(mode='before')
    def number_match(cls, m):
        decode_card = decode(m['number'])
        m['number'] = matching_credit_card_number(decode_card)
        return m
