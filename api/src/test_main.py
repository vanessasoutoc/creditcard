from fastapi.testclient import TestClient
from pytest import fixture
#from database import MongoClient



@fixture(scope="session", autouse=True)
def test_client():
    from .main import app
    from .database import MongoClient
    client = TestClient(app)
    with client as test_client:
        MongoClient()
        yield test_client

def test_health_check():
    response = test_client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {
        "health": "ok"
    }
