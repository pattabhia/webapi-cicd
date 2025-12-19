"""Tests for main application endpoints."""

import pytest
from fastapi import status
from fastapi.testclient import TestClient


@pytest.mark.unit
def test_root_endpoint(test_client: TestClient) -> None:
    """Test root endpoint returns welcome message.

    Args:
        test_client: FastAPI test client fixture
    """
    response = test_client.get("/")

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "message" in data
    assert "version" in data
    assert "docs" in data
    assert "health" in data


@pytest.mark.unit
def test_health_check(test_client: TestClient) -> None:
    """Test health check endpoint.

    Args:
        test_client: FastAPI test client fixture
    """
    response = test_client.get("/api/v1/health")

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["status"] == "healthy"
    assert "version" in data
    assert "environment" in data
    assert "timestamp" in data


@pytest.mark.unit
def test_readiness_check(test_client: TestClient) -> None:
    """Test readiness check endpoint.

    Args:
        test_client: FastAPI test client fixture
    """
    response = test_client.get("/api/v1/ready")

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "ready" in data
    assert "checks" in data
    assert "timestamp" in data


@pytest.mark.unit
def test_request_id_header(test_client: TestClient) -> None:
    """Test that request ID is added to response headers.

    Args:
        test_client: FastAPI test client fixture
    """
    response = test_client.get("/api/v1/health")

    assert "X-Request-ID" in response.headers
    assert len(response.headers["X-Request-ID"]) > 0


@pytest.mark.unit
def test_404_error_handling(test_client: TestClient) -> None:
    """Test 404 error handling.

    Args:
        test_client: FastAPI test client fixture
    """
    response = test_client.get("/api/v1/nonexistent")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    data = response.json()
    assert data["success"] is False
    assert "error" in data
    assert "request_id" in data["error"]


@pytest.mark.unit
def test_openapi_docs_available(test_client: TestClient) -> None:
    """Test that OpenAPI documentation is available.

    Args:
        test_client: FastAPI test client fixture
    """
    response = test_client.get("/api/v1/docs")
    assert response.status_code == status.HTTP_200_OK

    response = test_client.get("/api/v1/openapi.json")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "openapi" in data
    assert "info" in data
    assert "paths" in data
