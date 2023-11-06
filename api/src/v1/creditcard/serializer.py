from pydantic import BaseModel, Field

class CreditCardModel(BaseModel):
    id: str = Field(None, alias="_id")
    exp_date: object = Field(...)
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
