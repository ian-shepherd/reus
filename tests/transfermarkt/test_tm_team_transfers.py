import json
import time
import unittest
from pathlib import Path

import numpy.testing as npt

from reus.transfermarkt import tm_team_transfers


class TestTmTeamTransfers(unittest.TestCase):
    current_dir = Path(__file__).resolve().parent
    data_path = current_dir / "data"

    def test_all_transfers(self):
        with open(self.data_path / "dortmund_transfers.json", "r") as f:
            expected = json.load(f)

        actual = tm_team_transfers(club="Borussia Dortmund", season="2022")

        time.sleep(4)

        npt.assert_array_equal(actual, expected)

    def test_summer_transfers(self):
        with open(self.data_path / "newcastle_summer_transfers.json", "r") as f:
            expected = json.load(f)

        actual = tm_team_transfers(
            club="Newcastle United", season="2022", window="Summer"
        )

        time.sleep(4)

        npt.assert_array_equal(actual, expected)

    def test_winter_transfers(self):
        with open(self.data_path / "liverpool_winter_transfers.json", "r") as f:
            expected = json.load(f)

        actual = tm_team_transfers(club="Liverpool", season="2022", window="Winter")

        time.sleep(4)

        npt.assert_array_equal(actual, expected)

    def test_striker_transfers(self):
        with open(self.data_path / "man_city_strikers_transfers.json", "r") as f:
            expected = json.load(f)

        actual = tm_team_transfers(
            club="Manchester City", season="2022", position_group="Strikers"
        )

        time.sleep(4)

        npt.assert_array_equal(actual, expected)


if __name__ == "__main__":
    unittest.main()
