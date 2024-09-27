# Test the container client using a container instance from the model
import pytest

from src.oralite.core import wrapper
from src.oralite.container.stop import client_function, main
from src.oralite.container.client import model_containers
from src.oralite.core import model
from src.oralite.container.get import client_function as alt_client_function


@pytest.fixture
def model_container_ocid():
    id = model_containers[0]["id"]
    return id

def test_container_ocid_fixture(model_container_ocid):
    assert model_containers
    assert model_container_ocid

def test_client_function():
    assert client_function
    assert main

def test_container_stop_main(model_container_ocid):
    resp = main(alt_client_function, model_container_ocid)

    assert resp.status == 200
    assert resp.data.id == model_container_ocid