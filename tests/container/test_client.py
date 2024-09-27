import pytest

from src.oralite.container.client import *
from src.oralite.core import model, tenancy


@pytest.fixture
def model_container_name():
    name = model_containers[0]["display_name"]
    return name

def test_client():
    assert client

def test_tenancy():
    assert tenancy

def test_get_container_id(model_container_name):
    container_id = get_container_id(model_containers, model_container_name)
    print(container_id)
    assert container_id