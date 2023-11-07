import mongomock
from mongoengine import connect
import pytest
from src.v1.creditcard.service import CreditCardService
from src.v1.creditcard.document import CreditCard
from src.v1.creditcard.utils import exp_date_format
class TestService:
    @pytest.fixture
    def creditcard(self):
        yield CreditCard(
                number='4111111111111111',
                exp_date='02/2024',
                holder='Joana Darc Santos',
                cvv='123',
                brand='visa'
            )
    @pytest.fixture
    def client_mock(self):
        yield connect(
                'mongoenginetest',
                host='mongodb://localhost',
                mongo_client_class=mongomock.MongoClient,
                uuidRepresentation='standard',
                alias='default'
            )
    @pytest.fixture
    def mock_db(self, client_mock):
        yield client_mock.db
    def test_save(self, mock_db, creditcard):
        mock_db
        result = CreditCardService.save(self, creditcard)
        assert result.number
    def test_list(self, mock_db):
        mock_db
        result = CreditCardService.list(self)
        assert list(result)

