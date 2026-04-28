import pytest
import requests

BASE_URL = "https://reqres.in/api"


@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()

    headers = {
        "x-api-key": "reqres_2d378cb2a30346988e33f7df87fcea9c",
        "Content-Type": "application/json"
    }

    session.headers.update(headers)

    print("Setup: session created")

    yield session

    print("Teardown: session closed")
    session.close()