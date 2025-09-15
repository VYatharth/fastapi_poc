from fastapi import APIRouter
from my_app.api.routes import user_routes
from my_app.api.routes import department_routes

api_router = APIRouter()
api_router.include_router(user_routes.router)
api_router.include_router(department_routes.router)
