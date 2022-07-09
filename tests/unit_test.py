from datetime import datetime, timedelta
import json
import hashlib
import os

import pandas as pd
import pytest

# assert that the item was written to dynamodb, and that the hash PK is properly 32 characters long
def test_player_stats(mock_api_stats):
    df = mock_api_stats.get_apex_player_stats("fake_name_0001")
    assert df["global"]["name"] == "fake_name_0001"
    assert isinstance(df, dict) == True


def test_map_rotation(mock_api_map):
    df = mock_api_map.get_apex_map_rotation()
    assert len(df) == 2
    assert isinstance(df, pd.DataFrame) == True
