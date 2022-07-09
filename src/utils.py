from datetime import datetime, timedelta
import logging
import os
import json

import pandas as pd
import requests

try:
    from .exceptions import ApexApiException
except:
    from exceptions import ApexApiException


class Apex_API:
    def __init__(self, api_key: str):
        self.api_key = api_key

        logging.basicConfig(
            level=logging.INFO,
            format="[%(levelname)s] %(asctime)s %(message)s",
            datefmt="%Y-%m-%d %I:%M:%S %p",  # this defines the date format for the (asctime) part above
            handlers=[logging.StreamHandler()],
            # this means store logs to a example.log file as well as print them to the terminal
        )
        logging.getLogger("requests").setLevel(
            logging.WARNING
        )  # get rid of https debug gahbage

    def ___iter__(self):
        logging.info("what")

    def __str__(self):
        return "Apex API Client Object"

    def __repr__(self):
        return "Apex API"

    def get_apex_player_stats(self, player: str) -> pd.DataFrame:
        try:
            data = requests.get(
                f"https://api.mozambiquehe.re/bridge?version=5&platform=PC&player={player}&auth={self.api_key}"
            )
            logging.info(
                f"Grabbing data for Player {player}, Status Code was {data.status_code}"
            )
            df = data.json()
            return df
        except BaseException as e:
            logging.error(e)
            raise ApexApiException

    def get_apex_map_rotation(self) -> pd.DataFrame:
        try:
            data = requests.get(
                f"https://api.mozambiquehe.re/maprotation?version=2&auth={self.api_key}"
            )
            logging.info(
                f"Grabbing data for current Map Rotation, Status Code was {data.status_code}"
            )
            df = data.json()

            df_current = pd.DataFrame([df["battle_royale"]["current"]])
            df_current["type"] = "current"

            df_next = pd.DataFrame([df["battle_royale"]["next"]])
            df_next["remainingSecs"] = 0
            df_next["remainingMins"] = 0
            df_next["remainingTimer"] = "00:00:00"
            df_next["type"] = "next"

            df_combo = pd.concat([df_current, df_next])
            logging.info(f"Grabbing {len(df_combo)} Records for Apex Map Rotation")

            return df_combo
        except BaseException as e:
            logging.error(e)
            raise ApexApiException
