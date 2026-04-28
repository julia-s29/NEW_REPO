from conftest import BASE_URL


def test_update_user(api_session):

    payload = {
        "name": "Morpheus",
        "job": "President"
    }

    response = api_session.put(f"{BASE_URL}/users/2", json=payload)

    assert response.status_code == 200

    body = response.json()

    assert body["name"] == payload["name"]
    assert body["job"] == payload["job"]
    assert "updatedAt" in body and body["updatedAt"] != ""

