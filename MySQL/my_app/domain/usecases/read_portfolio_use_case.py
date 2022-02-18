from my_app.common.models.portfolio_dto import PortfolioDto
from my_app.domain.repository_interfaces.portfolio_repository import PortfolioRepository

def read_portfolio_use_case(repo: PortfolioRepository ) -> PortfolioDto:
    return repo.get_portfolio()
    