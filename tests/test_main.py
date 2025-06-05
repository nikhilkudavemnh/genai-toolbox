import pytest
import os
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_heartbeat():
    response = client.get("/heartbeat")
    assert response.status_code == 200
    assert response.json() == {"status": "alive"}

def test_heartbeat_response_type():
    response = client.get("/heartbeat")
    assert response.headers["content-type"] == "application/json"

def test_app_title():
    response = client.get("/docs")
    assert response.status_code == 200

def test_invalid_endpoint():
    response = client.get("/nonexistent")
    assert response.status_code == 404