from datetime import datetime, timedelta
import json
import os

import pandas as pd
import pytest

# import pytest_mock

from src.utils import Apex_API
from src.exceptions import ApexApiException

# had to separate the mocks out for each requests.get in each method call for class,


@pytest.fixture(scope="function")
def mock_api_stats(mocker):
    fname1 = os.path.join(os.path.dirname(__file__), "fixtures/player_stats.json")
    with open(fname1, "rb") as fp:
        player_stats_json = json.loads(fp.read())

    # mocker.patch("src.utils.requests.get").return_value = 1
    mocker.patch(
        "src.utils.requests.get"
    ).return_value.json.return_value = player_stats_json
    # if it's a method then you need to get requests.get().return value and df.json().return value.

    # mocker.patch("src.utils.Apex_API.get_apex_player_stats").return_value = player_stats_json
    # mocker.patch("src.utils.Apex_API.get_apex_map_rotation").return_value = map_rotation_csv

    api = Apex_API(api_key="FAKE")

    return api


@pytest.fixture(scope="function")
def mock_api_map(mocker):
    fname2 = os.path.join(os.path.dirname(__file__), "fixtures/map_rotation.json")
    with open(fname2, "rb") as fp:
        map_rotation_json = json.loads(fp.read())

    mocker.patch(
        "src.utils.requests.get"
    ).return_value.json.return_value = map_rotation_json

    api = Apex_API(api_key="FAKE")

    return api
