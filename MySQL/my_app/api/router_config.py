from fastapi import APIRouter
from my_app.api.routes import portfolio_route

api_router = APIRouter()
api_router.include_router(portfolio_route.router)
