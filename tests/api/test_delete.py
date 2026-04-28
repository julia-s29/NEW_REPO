from conftest import BASE_URL


def test_delete_user(api_session):

    response = api_session.delete(f"{BASE_URL}/users/2")

    assert response.status_code == 204
    assert response.text == ""