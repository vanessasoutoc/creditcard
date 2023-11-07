from unittest.mock import patch
from fastapi.testclient import TestClient
import pytest


@pytest.fixture()
def database_instance(self):
    with patch('database.MongoClient') as MockClass:
        instance = MockClass.return_value
        # instance.get_data.return_value = 'bar'
        yield instance

@pytest.fixture(scope="session", autouse=True,)
def test_client():
    from src.main import app
    from src.database import MongoClient
    client = TestClient(app)
    with client as test_client:
        yield test_client

def test_health_check():
    response = test_client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {
        "health": "ok"
    }
