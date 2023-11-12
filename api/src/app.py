from contextlib import asynccontextmanager
from fastapi import FastAPI, APIRouter

from src.database import MongoClient
from src.v1.creditcard.router import router as v1_creditcard_router
from fastapi.middleware.cors import CORSMiddleware


origins = [
    'http://localhost:8000',
    'http://localhost:3000'
]

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

app = FastAPI(title='CreditCardApi', swagger_ui_parameters={'syntaxHighlight': False}, lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

route.include_router(v1_creditcard_router, prefix='/v1')
app.include_router(route)
