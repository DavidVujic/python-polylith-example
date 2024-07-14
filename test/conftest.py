import pytest


@pytest.fixture
def set_some_environment_variables(monkeypatch):
    monkeypatch.setenv("HELLO", "world")


@pytest.fixture
def fake_data():
    return {"hello": "world", "good": ["morning", "day", "afternoon"]}
