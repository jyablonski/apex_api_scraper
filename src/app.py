from datetime import datetime
import os

import pandas as pd

from utils import Apex_API

if __name__ == "__main__":
    api = Apex_API(os.environ.get("apex_key"))

    maps = api.get_apex_map_rotation()

    # my_data = api.get_apex_player_stats("kickn97")

    print(maps)
