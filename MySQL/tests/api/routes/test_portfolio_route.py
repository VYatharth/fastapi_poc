from unittest.mock import MagicMock
from fastapi.testclient import TestClient

def test_portfolio(client: TestClient, monkeypatch) -> None:
    portfolio_data = {
        "personal_details": 'test',
        "skills": {},
        "achievements": {},
        "experience": {},
        "activities": {},
        "contact_info": {},
    }
    read_portfolio_use_case_mock = MagicMock(return_value=portfolio_data)
    monkeypatch.setattr(
        "my_app.api.routes.portfolio_route.read_portfolio_use_case", read_portfolio_use_case_mock
    )
    """Test the portfolio route."""
    response = client.get("/portfolio")

    assert response.status_code == 200
    content = response.json()
    assert content['personal_details'] == 'test'
    assert "contact_info" in content
