from typing import Optional, Any, Union, List
from pydantic import BaseModel, Field, validator
from datetime import datetime

class CreditCardSerializer(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    exp_date: Any = Field(...)
    holder: str = Field(...)
    number: str = Field(...)
    cvv: str = Field(...)

    @validator("exp_date")
    def sync_exp_date(cls, value):
        if isinstance(value, datetime):
            return datetime.strftime(value, "%m/%Y")
        return value

    class Config:
        json_schema_extra = {
            "example": {
                "exp_date": "12/2023",
                "holder": "Armindo Juvenal Soares",
                "number": "4111111111111111",
                "cvv": '100',
            }
        }
