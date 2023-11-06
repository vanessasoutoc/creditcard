from contextlib import asynccontextmanager
from fastapi import FastAPI, APIRouter
import uvicorn

from database import MongoClient
from v1.creditcard.router import router as v1_creditcard_router

route = APIRouter(prefix='/api')

@route.get('/health')
def healt_check():
    return {
        'health':'ok'
    }

@asynccontextmanager
async def lifespan(app: FastAPI):
    MongoClient()
    yield

app = FastAPI(title='CreditCardApi', swagger_ui_parameters={"syntaxHighlight": False}, lifespan=lifespan)
route.include_router(v1_creditcard_router, prefix='/v1')
app.include_router(route)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8008)
