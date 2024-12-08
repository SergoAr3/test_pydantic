from typing import Generator, Any

import pytest
from starlette.testclient import TestClient

from main import app


@pytest.fixture(scope="function")
def client() -> Generator[TestClient, Any, None]:
    """
    Create a new FastAPI TestClient that uses the `db_session` fixture to override
    the `get_db` dependency that is injected into routes.
    """
    with TestClient(app) as client:
        yield client
