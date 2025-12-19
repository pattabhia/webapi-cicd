"""FastAPI application entry point."""

from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app import __app_name__, __version__
from app.api.v1.router import api_router
from app.core.config import settings
from app.core.error_handlers import setup_exception_handlers
from app.core.logging import get_logger, setup_logging
from app.core.middleware import setup_middleware

# Setup logging first
setup_logging()
logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    """Application lifespan events.

    Args:
        app: FastAPI application instance

    Yields:
        None
    """
    # Startup
    logger.info(
        f"Starting {settings.APP_NAME} v{settings.APP_VERSION}",
        extra={
            "environment": settings.ENVIRONMENT,
            "debug": settings.DEBUG,
        }
    )

    # TODO: Initialize database connections, cache, etc.
    # await database.connect()
    # await cache.connect()

    yield

    # Shutdown
    logger.info(f"Shutting down {settings.APP_NAME}")

    # TODO: Close database connections, cache, etc.
    # await database.disconnect()
    # await cache.disconnect()


def create_application() -> FastAPI:
    """Create and configure FastAPI application.

    Returns:
        Configured FastAPI application instance
    """
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description="FastAPI CICD - Production-ready API with best practices",
        docs_url=f"{settings.API_V1_PREFIX}/docs",
        redoc_url=f"{settings.API_V1_PREFIX}/redoc",
        openapi_url=f"{settings.API_V1_PREFIX}/openapi.json",
        lifespan=lifespan,
        debug=settings.DEBUG,
    )

    # Setup middleware
    setup_middleware(app)

    # Setup exception handlers
    setup_exception_handlers(app)

    # Include API v1 router
    app.include_router(api_router, prefix=settings.API_V1_PREFIX)

    # Root endpoint for backward compatibility
    @app.get("/", include_in_schema=False)
    async def root() -> JSONResponse:
        """Root endpoint - redirects to API docs."""
        return JSONResponse(
            content={
                "message": f"Welcome to {settings.APP_NAME}",
                "version": settings.APP_VERSION,
                "docs": f"{settings.API_V1_PREFIX}/docs",
                "health": f"{settings.API_V1_PREFIX}/health",
            }
        )

    logger.info("Application created successfully")

    return app


# Create application instance
app = create_application()
