import pytest
import requests
from unittest.mock import patch

@patch('requests.post')
def test_frontend_api_call_positive(mock_post):
    mock_post.return_value.json.return_value = {"sentiment": "Positive"}
    mock_post.return_value.status_code = 200
    response = requests.post(
        "http://localhost:8000/analyze/",
        data={"text": "Frontend test text"}
    )
    assert mock_post.called
    assert response.json()["sentiment"] == "Positive"

@patch('requests.post')
def test_frontend_api_call_error(mock_post):
    mock_post.return_value.json.return_value = {"sentiment": "Error generating sentiment."}
    mock_post.return_value.status_code = 200
    response = requests.post(
        "http://localhost:8000/analyze/",
        data={"text": "Bad input"}
    )
    assert "error" in response.json()["sentiment"].lower() 