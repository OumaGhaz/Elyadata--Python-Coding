from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    # Send a GET request to the root URL
    response = client.get("/")

    # Assert that the response status code is 200 OK
    assert response.status_code == 200

    # Assert that the response contains the expected JSON body
    assert response.json() == {"message": "Welcome to my FastAPI application!"}
