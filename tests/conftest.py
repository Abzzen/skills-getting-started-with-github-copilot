import copy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


_INITIAL_ACTIVITIES = copy.deepcopy(app_module.activities)


@pytest.fixture
def client():
    return TestClient(app_module.app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    # Arrange
    app_module.activities = copy.deepcopy(_INITIAL_ACTIVITIES)

    yield

    # Cleanup
    app_module.activities = copy.deepcopy(_INITIAL_ACTIVITIES)
