from pydantic import BaseModel

class CreditCardSchema(BaseModel):
    exp_date: str
    holder: str
    number: str
    cvv: str

    class Config:
        schema_extra = {
            "example": {
                "exp_date": "12/2023",
                "holder": "Armindo Juvenal Soares",
                "number": "4111111111111111",
                "cvv": '100',
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
