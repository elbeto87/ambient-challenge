import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database.base import Base
from app.database.database import get_db


def populate_db(session):
    from app.models.device import DeviceType
    from app.models import DwellingModel, HubModel, DeviceModel
    dwellings = [
        DwellingModel(address="123 Main Street"),
        DwellingModel(address="456 Elm Street", occupied=True),
    ]
    session.add_all(dwellings)
    session.flush()
    hubs = [
        HubModel(name="Hub 1", dwelling=dwellings[0]),
        HubModel(name="Hub 2", dwelling=dwellings[1]),
    ]
    session.add_all(hubs)
    session.flush()
    devices = [
        DeviceModel(name="Device 1", hub=hubs[0], type=DeviceType.SWITCH, state={"on": True}),
        DeviceModel(name="Device 2", hub=hubs[1], type=DeviceType.LOCK, state={"locked": False}),
        DeviceModel(name="Device 3", hub=hubs[0], type=DeviceType.THERMOSTAT, state={"temp": 22}),
    ]
    session.add_all(devices)
    session.commit()

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
    populate_db(session)
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
