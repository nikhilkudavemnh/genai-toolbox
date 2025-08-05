## Structure of a FastAPI Project
```markdown
myapp/
├── app/
│   ├── api/                  # API route handlers (organized by module)
│   │   ├── v1/
│   │   │   ├── routes/
│   │   │   │   ├── user.py
│   │   │   │   └── item.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── core/                 # Core settings, configs, utils
│   │   ├── config.py         # Environment & settings via Pydantic
│   │   ├── security.py
│   │   └── logger.py
│   ├── db/                   # Database config and models
│   │   ├── base.py
│   │   ├── session.py
│   │   └── models/
│   │       ├── user.py
│   │       └── __init__.py
│   ├── schemas/              # Pydantic models for request/response
│   │   ├── user.py
│   │   └── __init__.py
│   ├── services/             # Business logic layer
│   │   ├── user_service.py
│   │   └── __init__.py
│   ├── main.py               # Entry point (FastAPI app)
│   └── __init__.py
├── alembic/                  # Alembic for migrations
│   └── versions/
├── tests/                    # Unit and integration tests
│   ├── api/
│   └── conftest.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```