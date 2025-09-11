import json
import sys
import os

# Add the src directory to Python path so we can import from inference
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from inference.app import app

def test_health_check():
    """Test if the main route returns 200 status"""
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    # Note: Your app returns HTML, not JSON, so we check for HTML content
    assert b"<!DOCTYPE html>" in response.data or b"<html" in response.data

def test_prediction():
    """Test prediction endpoint"""
    client = app.test_client()
    # Use form data since your app expects form submission, not JSON
    response = client.post(
        "/predict",
        data={
            "sepal_length_cm": "5.1",
            "sepal_width_cm": "3.5", 
            "petal_length_cm": "1.4",
            "petal_width_cm": "0.2"
        }
    )
    assert response.status_code == 200
    # Check that the response contains prediction results
    assert b"prediction" in response.data.lower() or b"setosa" in response.data.lower()