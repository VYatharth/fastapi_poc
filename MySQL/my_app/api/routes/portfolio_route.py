from typing import Annotated
from fastapi import APIRouter, Depends

from my_app.api.dependencies import get_portfolio_repository
from my_app.common.models.portfolio_dto import PortfolioDto
from my_app.domain.repository_interfaces.portfolio_repository import PortfolioRepository
from my_app.domain.usecases.read_portfolio_use_case import (
  read_portfolio_use_case,
  )


router = APIRouter(prefix="/portfolio", tags=["portfolio"])

@router.get("/")
def portfolio(portfolio_repository: Annotated[PortfolioRepository, Depends(get_portfolio_repository)]) -> PortfolioDto:
    return  read_portfolio_use_case(portfolio_repository)
  