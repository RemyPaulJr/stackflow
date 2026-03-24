from models import config
import pytest

@pytest.fixture(scope="module")
def session():
    session = config.session
    yield session
    session.close()