from fastapi import APIRouter
from my_app.api.routes import login, portfolio_route, question_route

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(portfolio_route.router)
api_router.include_router(question_route.router, prefix="/question", tags=["question"])
# api_router.include_router(scan_pdf_route.router, prefix="/pdf", tags=["pdf"])
