import pytest
from unittest.mock import patch, MagicMock

# Mock the Claude response
def mock_claude_response(prompt):
    return "Playwright is a testing framework by Microsoft. You can install it using npm in GitHub Codespaces."

# TEST 1: Keyword validation
def test_playwright_response_contains_keywords():
    response = mock_claude_response(
        "How to create playwright project using github codespace"
    )
    
    assert "playwright" in response.lower()
    assert "github" in response.lower()
    assert len(response) > 10

# TEST 2: Hallucination detection
def test_no_hallucination_on_known_fact():
    response = mock_claude_response(
        "Who created Playwright testing framework?"
    )
    
    assert "microsoft" in response.lower()
    assert "google" not in response.lower()


# TEST 3: Response quality check
def test_response_quality():
    response = mock_claude_response(
        "Explain what is API testing"
    )
    
    # assertions here
    
    assert response != ""           # not empty
    assert len(response) > 30       # length check
    assert "api" in response.lower() # keyword check 

def mock_claude_response(prompt):
    responses = {
        "playwright": "Playwright is a testing framework by Microsoft. You can install it using npm in GitHub Codespaces.",
        "who created": "Playwright was created by Microsoft engineers.",
        "api testing": "API testing involves validating REST endpoints, checking response codes, and verifying response bodies."
    }
    
    for key in responses:
        if key in prompt.lower():
            return responses[key]
    
    return "Default response for testing purposes."