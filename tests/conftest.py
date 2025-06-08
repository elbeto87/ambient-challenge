import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database.base import Base
from app.database.database import get_db


@pytest.fixture(scope="function")
def engine():
    from app.models.dwelling import DwellingModel  # noqa
    from app.models.hub import HubModel  # noqa
    from app.models.device import DeviceModel  # noqa
    engine = create_engine(
        "sqlite://",
        echo=True,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def session(engine):
    """Create a new database session for each test."""
    TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = TestSessionLocal()
    yield session
    session.rollback()
    session.close()

@pytest.fixture(scope="function")
def client(session):
    """Create a new database client for each test."""
    from app.main import app
    app.dependency_overrides[get_db] = lambda: session
    client = TestClient(app)
    yield client
    app.dependency_overrides = {}
