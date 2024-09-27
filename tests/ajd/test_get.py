# Test the container client using a container instance from the model
import pytest

from src.oralite.core import wrapper
from src.oralite.ajd.get import client_function, main
from src.oralite.ajd.client import model_ajds
from src.oralite.core import model


@pytest.fixture
def model_ajd_ocid():
    id = model_ajds[0]["id"]
    return id

def test_ajd_ocid_fixture(model_ajd_ocid):
    assert model_ajds
    assert model_ajd_ocid

def test_wrapper_function_get(model_ajd_ocid):
    assert client_function

    resp = wrapper(client_function, model_ajd_ocid)
    print(resp.data)

    assert resp.status == 200
    assert resp.data.id == model_ajd_ocid

def test_ajd_get_main(model_ajd_ocid):
    resp = main(client_function, model_ajd_ocid)

    assert resp.status == 200
    assert resp.data.id == model_ajd_ocid