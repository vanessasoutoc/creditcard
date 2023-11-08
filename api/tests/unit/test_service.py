import mongomock
import unittest
import pytest
from mongoengine import connect, disconnect

from src.v1.creditcard.serializer import CreditCardSerializer
from src.v1.creditcard.service import CreditCardService

class TestCreditCardService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connect('mongoenginetest', host='mongodb://localhost', mongo_client_class=mongomock.MongoClient, uuidRepresentation=True)

    @classmethod
    def tearDownClass(cls):
       disconnect()

    @pytest.fixture
    def credit_card(self) -> CreditCardSerializer:
        return {
                'number':'4111111111111111',
                'exp_date':'02/2024',
                'holder':'Joana Darc Santos',
                'cvv':'123',
                'brand':'visa'
        }

    def test_creditcard_save_success(credit_card):
        creditcard = CreditCardService().save(credit_card)

        assert creditcard.cvv ==  '123'

