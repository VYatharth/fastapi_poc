import os
import pydantic_core
from my_app.common.models.portfolio_dto import PortfolioDto
from my_app.domain.repository_interfaces.portfolio_repository import PortfolioRepository


class PortfolioRepositoryImpl(PortfolioRepository):
    
    def get_portfolio(self) -> PortfolioDto:
        root_path = os.getcwd()
        # use Pydantic model and parse json into it
        with open(f"{root_path}/my_app/data/resources/portfolio-data.json", 'r') as json_file:
            data = json_file.read()
            portfolio = PortfolioDto.model_validate(pydantic_core.from_json(data, allow_partial=True))
            return portfolio
