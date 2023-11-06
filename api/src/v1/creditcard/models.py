from pydantic import BaseModel, Field, field_validator, ValidationError, PydanticUserError
import uuid

class CreditCardModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    exp_date: str = Field(...)
    holder: str = Field(...)
    number: str = Field(...)
    cvv: str = Field(...)
    class Config:
        json_schema_extra = {
            "example": {
                "exp_date": "12/2023",
                "holder": "Armindo Juvenal Soares",
                "number": "4111111111111111",
                "cvv": '100',
            }
        }
