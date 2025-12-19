"""Pytest configuration and fixtures."""

import pytest
from typing import Generator
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def test_client() -> Generator[TestClient, None, None]:
    """Create a test client for the FastAPI application.
    
    Yields:
        TestClient instance
    """
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="function")
def test_client_function() -> Generator[TestClient, None, None]:
    """Create a function-scoped test client.
    
    Yields:
        TestClient instance
    """
    with TestClient(app) as client:
        yield client

