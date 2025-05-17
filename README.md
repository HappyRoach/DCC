# DCC (Digital Client Constructor)

A FastAPI-based web application for data management and control.

## Features

- RESTful API built with FastAPI
- PostgreSQL database integration
- Database migrations with Alembic
- Docker containerization support
- CORS middleware enabled
- JWT authentication support

## Prerequisites

- Python 3.12+
- PostgreSQL
- Docker (optional)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/HappyRoach/DCC.git
cd DCC
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
- Create a PostgreSQL database
- Update the database connection settings in `setting.py`

5. Run database migrations:
```bash
alembic upgrade head
```

## Running the Application

### Development Mode

```bash
python init_db.py
```

```bash
python main.py
```

The server will start at `http://localhost:9667`

### Docker

Build and run using Docker Compose:
```bash
docker-compose up --build
```

## API Documentation

Once the server is running, you can access the API documentation at:
- Swagger UI: `http://localhost:9667/docs`
- ReDoc: `http://localhost:9667/redoc`