from unittest.mock import MagicMock
from my_app.domain.usecases.read_portfolio_use_case import read_portfolio_use_case


def test_read_portfolio_use_case() -> None:
    portfolio_repo = MagicMock()

    read_portfolio_use_case(portfolio_repo)

    portfolio_repo.get_portfolio.assert_called_once()
