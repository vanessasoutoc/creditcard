import pytest
from fastapi.testclient import TestClient
from mongoengine import connect
import mongomock


from src.app import app
from src.v1.creditcard.serializer import CreditCardRequestSerializer, CreditCardResponseSerializer

client = TestClient(app)

@pytest.fixture
def memory_mongo():
    connect('mongoenginetest', host='mongodb://localhost', mongo_client_class=mongomock.MongoClient,
            uuidRepresentation=True)

@pytest.fixture
def mock_credit_card() -> CreditCardRequestSerializer:
    return CreditCardRequestSerializer(**{
            'number':'4111111111111111',
            'exp_date':'02/2024',
            'holder':'Joana Darc Santos',
            'cvv':'123',
            'brand':'visa'
    })

def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {
        "health": "ok"
    }

def test_save_card_success(memory_mongo, mock_credit_card):
    data = mock_credit_card.model_dump()
    credit_card = client.post("/api/v1/credit-card", json=data)

    assert credit_card.status_code == 200
    assert credit_card
    assert credit_card.json().get('_id')
    assert credit_card.json().get('cvv') == mock_credit_card.cvv


