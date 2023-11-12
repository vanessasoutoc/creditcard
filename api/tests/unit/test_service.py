import mongomock
import unittest
import pytest
from mongoengine import connect, disconnect

from src.v1.creditcard.serializer import CreditCardRequestSerializer
from src.v1.creditcard.service import CreditCardService

@pytest.fixture
def mock_collection():
    connect('mongoenginetest', host='mongodb://localhost', mongo_client_class=mongomock.MongoClient, uuidRepresentation=True)

@pytest.fixture
def credit_card() -> CreditCardRequestSerializer:
    return CreditCardRequestSerializer(**{
            'number':'4111111111111111',
            'exp_date':'02/2024',
            'holder':'Joana Darc Santos',
            'cvv':'123',
            'brand':'visa'
    })

def test_creditcard_save_success(mock_collection, credit_card):
    creditcard = CreditCardService().save(credit_card)

    assert creditcard.cvv ==  '123'

