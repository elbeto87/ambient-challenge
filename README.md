# Ambient Challenge API

A RESTful API built with FastAPI for managing dwellings, devices, and hubs in the Ambient Challenge project.

## 🚀 Features

- **Complete REST API** with FastAPI
- **Database integration** with SQLAlchemy ORM
- **Clean architecture** with layer separation (routers, services, repositories)
- **Integrated logging** for monitoring and debugging
- **Static code analysis** with Ruff
- **Docker containerization**
- **Automatic documentation** with Swagger/OpenAPI

## 📋 Functionality

### Dwelling Management
- Create new dwellings
- Update occupancy status
- Query dwelling information
- Install hubs in dwellings

### Device Management
- Create and delete devices
- Query device status
- Modify device state
- List all devices

### Hub Management
- Create and manage hubs
- Pair devices with hubs
- Query devices by hub
- Remove devices from hubs
- Query specific device status

## 🛠️ Technologies

- **FastAPI** - Modern, fast web framework
- **SQLAlchemy** - Database ORM
- **Pydantic** - Data validation and serialization
- **Docker** - Containerization
- **Ruff** - Code linter and formatter
- **Python Logging** - Integrated logging system

## 🏗️ Architecture

The project follows a layered architecture:

```
app/
├── routers/          # API endpoints
├── services/         # Business logic
├── repositories/     # Data access layer
├── models/           # Database models
├── schemas/          # Pydantic schemas
├── database/         # Database configuration
└── exceptions/       # Custom exceptions
```

## 🐳 Docker Setup

The application is containerized with Docker for easy deployment and development.

## 📊 Logging

Comprehensive logging is implemented throughout the application for monitoring and debugging purposes.

## 🔍 Code Quality

- **Ruff** is used for static code analysis, linting, and code formatting
- Ensures consistent code style and catches potential issues

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Docker (optional)

### Installation

1. Clone the repository
2. Install dependencies
3. Set up environment variables
4. Run the application

### API Documentation

Once the application is running, you can access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/v1/docs`
- ReDoc: `http://localhost:8000/v1/redoc`

## 📚 API Endpoints

### Dwellings
- `POST /v1/dwellings/create` - Create a new dwelling
- `GET /v1/dwellings/` - Get all dwellings
- `GET /v1/dwellings/{dwelling_id}` - Get specific dwelling
- `PUT /v1/dwellings/{dwelling_id}` - Update dwelling occupancy
- `PUT /v1/dwellings/{dwelling_id}/{hub_id}` - Install hub in dwelling

### Devices
- `POST /v1/device/` - Create a new device
- `GET /v1/device/` - Get all devices
- `GET /v1/device/{device_id}` - Get device state
- `PUT /v1/device/{device_id}` - Modify device state
- `DELETE /v1/device/{device_id}` - Delete device

### Hubs
- `POST /v1/hub/` - Create a new hub
- `GET /v1/hub/` - Get all hubs
- `GET /v1/hub/{hub_id}` - Get devices by hub
- `PUT /v1/hub/{hub_id}` - Pair device with hub
- `DELETE /v1/hub/{hub_id}` - Remove device from hub
- `GET /v1/hub/{hub_id}/{device_id}` - Get device status
