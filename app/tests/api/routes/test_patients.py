from fastapi.testclient import TestClient
from ....main import app

client = TestClient(app)

def test_patients_hello_world() -> None:
    response = client.get("/patients")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World, patients"}

# TODO: refactor code to be able to use a database mock