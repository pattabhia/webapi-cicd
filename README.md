# FastAPI CICD - Production-Ready API

A production-ready FastAPI application with best practices for code quality, testing, and CI/CD deployment.

## 🚀 Features

- ✅ **Proper Project Structure** - Organized, scalable architecture
- ✅ **Configuration Management** - Environment-based settings with Pydantic
- ✅ **Structured Logging** - JSON logging with request tracking
- ✅ **Error Handling** - Global exception handlers with proper error responses
- ✅ **API Versioning** - `/api/v1` prefix for future compatibility
- ✅ **Request/Response Models** - Pydantic models for validation
- ✅ **Middleware** - CORS, request ID, logging, trusted hosts
- ✅ **Health Checks** - Health and readiness endpoints
- ✅ **Comprehensive Testing** - Unit tests with pytest
- ✅ **Docker Support** - Containerized deployment
- ✅ **CI/CD Pipeline** - Jenkins pipeline configuration

## 📁 Project Structure

```
webapi-cicd/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Application entry point
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── router.py       # API v1 router
│   │       └── endpoints/
│   │           ├── __init__.py
│   │           └── health.py   # Health check endpoints
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py           # Configuration management
│   │   ├── logging.py          # Logging configuration
│   │   ├── middleware.py       # Custom middleware
│   │   ├── exceptions.py       # Custom exceptions
│   │   └── error_handlers.py  # Exception handlers
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py          # Pydantic models
│   ├── services/               # Business logic
│   │   └── __init__.py
│   └── utils/                  # Utility functions
│       └── __init__.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py             # Pytest fixtures
│   └── test_main.py            # Tests
├── requirements/
│   ├── base.txt                # Base dependencies
│   ├── dev.txt                 # Development dependencies
│   └── prod.txt                # Production dependencies
├── .env.example                # Environment variables template
├── .dockerignore               # Docker ignore file
├── Dockerfile                  # Docker configuration
├── Jenkinsfile                 # CI/CD pipeline
├── Makefile                    # Development commands
├── pyproject.toml              # Python project configuration
├── pytest.ini                  # Pytest configuration
└── README.md
```

## 🛠️ Setup

### Prerequisites

- Python 3.11+
- Docker (optional)
- Make (optional)

### Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd webapi-cicd
   ```

2. **Create virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   # For development
   pip install -r requirements/dev.txt

   # For production
   pip install -r requirements/prod.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

## 🚀 Running the Application

### Local Development

```bash
# Using uvicorn directly
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Using make
make run
```

### Production

```bash
# Using gunicorn with uvicorn workers
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Docker

```bash
# Build image
docker build -t fastapi-cicd:latest .

# Run container
docker run -p 8000:80 fastapi-cicd:latest

# Using make
make docker-build
make docker-run
```

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test markers
pytest -m unit
pytest -m integration

# Using make
make test
```

## 📊 API Documentation

Once the application is running, visit:

- **Swagger UI**: http://localhost:8000/api/v1/docs
- **ReDoc**: http://localhost:8000/api/v1/redoc
- **OpenAPI JSON**: http://localhost:8000/api/v1/openapi.json

## 🔍 Available Endpoints

- `GET /` - Root endpoint with API information
- `GET /api/v1/health` - Health check endpoint
- `GET /api/v1/ready` - Readiness check endpoint

## ⚙️ Configuration

Configuration is managed through environment variables. See `.env.example` for all available options.

Key configurations:

- `ENVIRONMENT` - Environment (development/staging/production)
- `LOG_LEVEL` - Logging level (DEBUG/INFO/WARNING/ERROR)
- `API_V1_PREFIX` - API version prefix
- `CORS_ORIGINS` - Allowed CORS origins
- `RATE_LIMIT_PER_MINUTE` - Rate limiting configuration

## 🔒 Security Features

- CORS middleware with configurable origins
- Trusted host middleware
- Request ID tracking
- Rate limiting support
- Structured error responses
- Input validation with Pydantic

## 📝 Development

### Code Quality

```bash
# Format code
black app tests
isort app tests

# Lint
flake8 app tests
pylint app

# Type checking
mypy app
```

### Make Commands

```bash
make run          # Run the FastAPI server locally
make test         # Run tests with coverage
make install      # Install dependencies
make docker-build # Build Docker image
make docker-run   # Run Docker container
make clean        # Clean cache files
```

## 🚢 Deployment

The project includes a Jenkins pipeline (`Jenkinsfile`) for CI/CD:

1. **Checkout** - Clone repository
2. **Install & Test** - Install dependencies and run tests
3. **Build & Push** - Build Docker image and push to registry
4. **Deploy** - Deploy to target environment

## 📈 Monitoring

- Prometheus metrics support (via `prometheus-fastapi-instrumentator`)
- Structured JSON logging for log aggregation
- Request ID tracking for distributed tracing
- Health and readiness endpoints for orchestration

## 🤝 Contributing

1. Create a feature branch
2. Make your changes
3. Run tests and linting
4. Submit a pull request

## 📄 License

[Your License Here]
