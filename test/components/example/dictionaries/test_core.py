from example.dictionaries.core import omit, pick

from ci.utils import hello


def test_pick(fake_data):
    assert pick(fake_data, {"good"}) == {"good": ["morning", "day", "afternoon"]}


def test_omit(fake_data):
    assert omit(fake_data, {"good"}) == {"hello": "world"}


def test_environment_customization(set_some_environment_variables):
    import os

    data = os.getenv("HELLO")

    assert data == "world"


def test_shared_code():
    assert hello() == "world"
