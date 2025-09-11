import json
from app import app

def test_health_check():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}

def test_prediction():
    client = app.test_client()
    response = client.post(
        "/predict",
        data=json.dumps({"features": [5.1, 3.5, 1.4, 0.2]}),
        content_type="application/json"
    )
    data = response.get_json()
    assert response.status_code == 200
    assert "prediction" in data
    assert "label" in data
