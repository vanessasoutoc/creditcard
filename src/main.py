from fastapi import FastAPI, APIRouter

from src.v1.creditcard.router import router as v1_creditcard_router

route = APIRouter(prefix='/api')

@route.get('/health')
def healt_check():
    return {
        'health':'ok'
    }

app = FastAPI(title='CreditCardApi', swagger_ui_parameters={"syntaxHighlight": False})
route.include_router(v1_creditcard_router, prefix='/v1')
app.include_router(route)

