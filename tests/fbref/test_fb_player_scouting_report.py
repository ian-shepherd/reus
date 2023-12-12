import json
import time
import unittest
from pathlib import Path

import numpy.testing as npt

from reus.fbref import fb_player_scouting_report


class TestFbPlayerScoutingReport(unittest.TestCase):
    current_dir = Path(__file__).resolve().parent
    data_path = current_dir / "data"

    def test_scouting_report(self):
        with open(self.data_path / "pulisic_2019_2020_scouting.json", "r") as f:
            expected = json.load(f)

        actual = fb_player_scouting_report(
            url="https://fbref.com/en/players/1bf33a9a/scout/3232/Christian-Pulisic-Scouting-Report"
        )

        time.sleep(4)
        npt.assert_array_equal(actual, expected)

    def test_player_redirect(self):
        with open(self.data_path / "reus_2018_2019_scouting.json", "r") as f:
            expected = json.load(f)

        player_url = "https://fbref.com/en/players/36a3ff67/Marco-Reus"
        comp_league = "2018-2019 Bundesliga"
        actual = fb_player_scouting_report(
            player_url=player_url, comp_league=comp_league
        )

        time.sleep(4)
        npt.assert_array_equal(actual, expected)


if __name__ == "__main__":
    unittest.main()
