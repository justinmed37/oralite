# Test the container client using a container instance from the model
import pytest

from src.oralite.core import wrapper
from src.oralite.ajd.start import client_function, main
from src.oralite.ajd.client import model_ajds
from src.oralite.core import model
from src.oralite.ajd.get import client_function as alt_client_function


@pytest.fixture
def model_ajd_ocid():
    id = model_ajds[0]["id"]
    return id

def test_ajd_ocid_fixture(model_ajd_ocid):
    assert model_ajds
    assert model_ajd_ocid

def test_client_function():
    assert client_function
    assert main

def test_ajd_start_main(model_ajd_ocid):
    resp = main(alt_client_function, model_ajd_ocid)

    assert resp.status == 200
    assert resp.data.id == model_ajd_ocid