"""Pydantic models for request/response validation."""

from typing import Any, Dict, Generic, Optional, TypeVar
from datetime import datetime
from pydantic import BaseModel, Field

DataT = TypeVar("DataT")


class HealthCheckResponse(BaseModel):
    """Health check response model."""

    status: str = Field(..., description="Service status", example="healthy")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Current timestamp")
    version: str = Field(..., description="Application version", example="1.0.0")
    environment: str = Field(..., description="Environment name", example="production")

    class Config:
        """Pydantic config."""
        json_schema_extra = {
            "example": {
                "status": "healthy",
                "timestamp": "2024-01-01T00:00:00",
                "version": "1.0.0",
                "environment": "production"
            }
        }


class ReadinessCheckResponse(BaseModel):
    """Readiness check response model."""

    ready: bool = Field(..., description="Service readiness status")
    checks: Dict[str, bool] = Field(default_factory=dict, description="Individual component checks")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Current timestamp")

    class Config:
        """Pydantic config."""
        json_schema_extra = {
            "example": {
                "ready": True,
                "checks": {
                    "database": True,
                    "redis": True
                },
                "timestamp": "2024-01-01T00:00:00"
            }
        }


class ErrorDetail(BaseModel):
    """Error detail model."""

    message: str = Field(..., description="Error message")
    details: Optional[Dict[str, Any]] = Field(default=None, description="Additional error details")
    request_id: Optional[str] = Field(default=None, description="Request ID for tracking")

    class Config:
        """Pydantic config."""
        json_schema_extra = {
            "example": {
                "message": "Resource not found",
                "details": {"resource_id": "123"},
                "request_id": "550e8400-e29b-41d4-a716-446655440000"
            }
        }


class ErrorResponse(BaseModel):
    """Error response model."""

    success: bool = Field(default=False, description="Success status")
    error: ErrorDetail = Field(..., description="Error details")

    class Config:
        """Pydantic config."""
        json_schema_extra = {
            "example": {
                "success": False,
                "error": {
                    "message": "Resource not found",
                    "details": {"resource_id": "123"},
                    "request_id": "550e8400-e29b-41d4-a716-446655440000"
                }
            }
        }


class SuccessResponse(BaseModel, Generic[DataT]):
    """Generic success response model."""

    success: bool = Field(default=True, description="Success status")
    data: DataT = Field(..., description="Response data")
    message: Optional[str] = Field(default=None, description="Optional message")

    class Config:
        """Pydantic config."""
        json_schema_extra = {
            "example": {
                "success": True,
                "data": {"id": 1, "name": "Example"},
                "message": "Operation completed successfully"
            }
        }


class PaginationMetadata(BaseModel):
    """Pagination metadata model."""

    page: int = Field(..., ge=1, description="Current page number")
    page_size: int = Field(..., ge=1, le=100, description="Items per page")
    total_items: int = Field(..., ge=0, description="Total number of items")
    total_pages: int = Field(..., ge=0, description="Total number of pages")

    class Config:
        """Pydantic config."""
        json_schema_extra = {
            "example": {
                "page": 1,
                "page_size": 20,
                "total_items": 100,
                "total_pages": 5
            }
        }


class PaginatedResponse(BaseModel, Generic[DataT]):
    """Generic paginated response model."""

    success: bool = Field(default=True, description="Success status")
    data: list[DataT] = Field(..., description="List of items")
    pagination: PaginationMetadata = Field(..., description="Pagination metadata")

    class Config:
        """Pydantic config."""
        json_schema_extra = {
            "example": {
                "success": True,
                "data": [{"id": 1, "name": "Item 1"}],
                "pagination": {
                    "page": 1,
                    "page_size": 20,
                    "total_items": 100,
                    "total_pages": 5
                }
            }
        }

