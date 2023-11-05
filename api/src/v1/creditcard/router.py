from fastapi import APIRouter

router = APIRouter(prefix='/creditcard')
import os

@router.get("")
def read_root():
    print(os.environ['DATABASE_URL'])
    return {"Hello": "World"}
