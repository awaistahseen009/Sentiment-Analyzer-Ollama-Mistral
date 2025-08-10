import pytest
from fastapi.testclient import TestClient
from backend.main import app
from unittest.mock import patch

client = TestClient(app)

@pytest.fixture
def mock_llm_invoke():
    with patch('backend.main.llm.invoke') as mock_invoke:
        yield mock_invoke

def test_analyze_endpoint_positive(mock_llm_invoke):
    mock_llm_invoke.return_value = "Positive"
    response = client.post("/analyze/", data={"text": "I love this!"})
    assert response.status_code == 200
    json_response = response.json()
    assert "sentiment" in json_response
    assert json_response["sentiment"] == "Positive"

def test_analyze_endpoint_negative(mock_llm_invoke):
    mock_llm_invoke.return_value = "Negative"
    response = client.post("/analyze/", data={"text": "I hate this."})
    assert response.status_code == 200
    assert response.json()["sentiment"] == "Negative"

def test_analyze_endpoint_neutral(mock_llm_invoke):
    mock_llm_invoke.return_value = "Neutral"
    response = client.post("/analyze/", data={"text": "It is a day."})
    assert response.status_code == 200
    assert response.json()["sentiment"] == "Neutral"

def test_analyze_endpoint_empty_input(mock_llm_invoke):
    mock_llm_invoke.return_value = "Neutral"
    response = client.post("/analyze/", data={"text": ""})
    assert response.status_code == 200
    assert response.json()["sentiment"] == "Neutral"

def test_analyze_endpoint_error(monkeypatch):
    def raise_error(*args, **kwargs):
        raise Exception("Model error")
    monkeypatch.setattr("backend.main.llm.invoke", raise_error)
    response = client.post("/analyze/", data={"text": "Test error"})
    assert response.status_code == 500 or "sentiment" not in response.json()  # Adjust if you add error handling 