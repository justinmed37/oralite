import pytest

import src.oralite.core
from src.oralite.core import model
import json

def test_oralite_core_model():
    # check that the model is a valid dictionary
    assert type(model) == dict