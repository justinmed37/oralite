import pytest

from src.oralite.container.client import wrapper
from src.oralite.container.get import client_function

TEST_OCID = "ocid1.computecontainerinstance.oc1.iad.anuwcljr232wu5aa2zsrpgnirt7v5wk6wvwyvf77q27sllfiua32b2dkotma"

def test_container_get():
    resp = wrapper(client_function, TEST_OCID)
    print(resp.data)

    assert resp.status == 200
    assert resp.data.id == TEST_OCID