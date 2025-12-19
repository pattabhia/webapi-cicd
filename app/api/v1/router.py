"""API v1 router configuration."""

from fastapi import APIRouter
from app.api.v1.endpoints import health

# Create API v1 router
api_router = APIRouter()

# Include endpoint routers
api_router.include_router(health.router, prefix="", tags=["Health"])

# Add more routers here as you build more endpoints
# api_router.include_router(users.router, prefix="/users", tags=["Users"])
# api_router.include_router(items.router, prefix="/items", tags=["Items"])

