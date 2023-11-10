from typing import Optional, Any
from pydantic import BaseModel, Field, ValidationError, field_validator, model_validator
from datetime import datetime
from .cryptografy import decode
from .utils import matching_credit_card_number

class CreditCardSerializer(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    exp_date: Any = Field(...)
    holder: str = Field(...)
    number: str = Field(...)
    cvv: str = Field(...)
    brand: Optional[str] = Field(None)

    @field_validator('exp_date')
    def sync_exp_date(cls, value):
        if isinstance(value, datetime):
            return datetime.strftime(value, "%m/%y")
        return value

    @model_validator(mode='before')
    def number_match(cls, m):
        print(len(m['number']))
        if(len(m['number']) > 16):
            m['number'] = matching_credit_card_number(decode(m['number']))
            return m
        return m

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
