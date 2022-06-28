import json

from tests.v1.constants import ROUTE


def test_create_user(client):
    data = {
        "username": "testuser",
        "email": "testuser@nofoobar.com",
        "password": "testing"
    }
    response = client.post(f"{ROUTE}/users/", json.dumps(data))

    assert response.status_code == 200
    assert response.json()["email"] == "testuser@nofoobar.com"
    assert response.json()["is_active"] is True
