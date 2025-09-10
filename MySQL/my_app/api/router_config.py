from fastapi import APIRouter
from my_app.api.routes import users

api_router = APIRouter()
api_router.include_router(users.router)
