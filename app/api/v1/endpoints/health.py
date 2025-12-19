"""Health check endpoints."""

from fastapi import APIRouter, status
from app.models.schemas import HealthCheckResponse, ReadinessCheckResponse
from app.core.config import settings
from app.core.logging import get_logger
from app import __version__

logger = get_logger(__name__)

router = APIRouter(tags=["Health"])


@router.get(
    "/health",
    response_model=HealthCheckResponse,
    status_code=status.HTTP_200_OK,
    summary="Health Check",
    description="Check if the service is running and healthy",
    responses={
        200: {
            "description": "Service is healthy",
            "content": {
                "application/json": {
                    "example": {
                        "status": "healthy",
                        "timestamp": "2024-01-01T00:00:00",
                        "version": "1.0.0",
                        "environment": "production"
                    }
                }
            }
        }
    }
)
async def health_check() -> HealthCheckResponse:
    """Perform health check.
    
    Returns:
        HealthCheckResponse: Health status information
    """
    logger.debug("Health check requested")
    
    return HealthCheckResponse(
        status="healthy",
        version=__version__,
        environment=settings.ENVIRONMENT
    )


@router.get(
    "/ready",
    response_model=ReadinessCheckResponse,
    status_code=status.HTTP_200_OK,
    summary="Readiness Check",
    description="Check if the service is ready to accept traffic",
    responses={
        200: {
            "description": "Service is ready",
        },
        503: {
            "description": "Service is not ready",
        }
    }
)
async def readiness_check() -> ReadinessCheckResponse:
    """Perform readiness check.
    
    This endpoint checks if all dependencies (database, cache, etc.) are available.
    
    Returns:
        ReadinessCheckResponse: Readiness status information
    """
    logger.debug("Readiness check requested")
    
    checks = {}
    
    # TODO: Add actual dependency checks
    # Example:
    # checks["database"] = await check_database_connection()
    # checks["redis"] = await check_redis_connection()
    
    # For now, always ready
    all_ready = True  # all(checks.values()) if checks else True
    
    return ReadinessCheckResponse(
        ready=all_ready,
        checks=checks
    )

