import pytest

from src.oralite.ajd.client import *
from src.oralite.core import model, tenancy


@pytest.fixture
def model_ajd_name():
    name = model_ajds[0]["display_name"]
    return name

def test_client():
    assert client

def test_tenancy():
    assert tenancy

def test_get_ajd_id(model_ajd_name):
    container_id = get_ajd_id(model_ajds, model_ajd_name)
    print(container_id)
    assert container_id