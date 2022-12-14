from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_root():
    res = client.get("/")
    assert res.json().get("message") == "Hello World"


def test_create_user():
    res = client.post("/users/", json={"username": "test_user2", "password": "test_password"})
    assert res.status_code == 201
    assert res.json().get("username") == "test_user2"
