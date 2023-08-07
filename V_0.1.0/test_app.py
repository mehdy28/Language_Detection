from fastapi.testclient import TestClient
from app import app  # Import your FastAPI app (adjust the path accordingly)

client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"health_check": "OK", "model_version": "0.1.0"}

def test_predict_endpoint():
    test_text = "This is a test text."
    response = client.post("/predict", json={"text": test_text})
    assert response.status_code == 200
    assert "language" in response.json()
