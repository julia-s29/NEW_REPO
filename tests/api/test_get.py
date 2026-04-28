from conftest import BASE_URL


def test_get_user(api_session):
    response = api_session.get(f"{BASE_URL}/users/2")

    assert response.status_code == 200

    body = response.json()

    assert body["data"]["id"] == 2
    assert body["data"]["email"] is not None
    assert body["data"]["first_name"] == "Janet"
    assert body["data"]["last_name"] == "Weaver"