from conftest import BASE_URL


def test_create_user(api_session):

    payload = {
        "name": "Hercules",
        "job": "Team Lead"
    }

    response = api_session.post(f"{BASE_URL}/users", json=payload)

    assert response.status_code == 201

    body = response.json()

    assert body["name"] == payload["name"]
    assert body["job"] == payload["job"]
    assert "id" in body and body["id"] != ""
    assert "createdAt" in body and body["createdAt"] != ""