from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_user():
    response = client.post("/v1/user/?email=test@test.com&password=123")
    assert response.status_code == 200
    assert response.json()["email"] == "test@test.com"


def test_token_usage():
    response = client.post("/v1/user/?email=test2@test.com&password=123")
    user_id = response.json()["id"]

    response = client.get(f"/v1/sport/football?user_id={user_id}")
    assert response.status_code == 200
    assert "tokens_left" in response.json()