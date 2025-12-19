"""Custom exceptions for the application."""

from typing import Any, Dict, Optional


class AppException(Exception):
    """Base application exception."""

    def __init__(
        self,
        message: str,
        status_code: int = 500,
        details: Optional[Dict[str, Any]] = None
    ) -> None:
        """Initialize exception.
        
        Args:
            message: Error message
            status_code: HTTP status code
            details: Additional error details
        """
        self.message = message
        self.status_code = status_code
        self.details = details or {}
        super().__init__(self.message)


class NotFoundException(AppException):
    """Resource not found exception."""

    def __init__(self, message: str = "Resource not found", details: Optional[Dict[str, Any]] = None) -> None:
        """Initialize exception."""
        super().__init__(message=message, status_code=404, details=details)


class BadRequestException(AppException):
    """Bad request exception."""

    def __init__(self, message: str = "Bad request", details: Optional[Dict[str, Any]] = None) -> None:
        """Initialize exception."""
        super().__init__(message=message, status_code=400, details=details)


class UnauthorizedException(AppException):
    """Unauthorized exception."""

    def __init__(self, message: str = "Unauthorized", details: Optional[Dict[str, Any]] = None) -> None:
        """Initialize exception."""
        super().__init__(message=message, status_code=401, details=details)


class ForbiddenException(AppException):
    """Forbidden exception."""

    def __init__(self, message: str = "Forbidden", details: Optional[Dict[str, Any]] = None) -> None:
        """Initialize exception."""
        super().__init__(message=message, status_code=403, details=details)


class ConflictException(AppException):
    """Conflict exception."""

    def __init__(self, message: str = "Conflict", details: Optional[Dict[str, Any]] = None) -> None:
        """Initialize exception."""
        super().__init__(message=message, status_code=409, details=details)


class ValidationException(AppException):
    """Validation exception."""

    def __init__(self, message: str = "Validation error", details: Optional[Dict[str, Any]] = None) -> None:
        """Initialize exception."""
        super().__init__(message=message, status_code=422, details=details)


class InternalServerException(AppException):
    """Internal server error exception."""

    def __init__(self, message: str = "Internal server error", details: Optional[Dict[str, Any]] = None) -> None:
        """Initialize exception."""
        super().__init__(message=message, status_code=500, details=details)

