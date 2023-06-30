import unittest
import numpy.testing as npt
from pathlib import Path
import json
from reus.fbref import fb_league_table
import time


class TestFbLeagueTable(unittest.TestCase):
    current_dir = Path(__file__).resolve().parent
    data_path = current_dir / "data"

    def test_epl_table(self):
        with open(self.data_path / "epl_table_2021_2022.json", "r") as f:
            expected = json.load(f)

        actual = fb_league_table(
            "https://fbref.com/en/comps/9/2021-2022/2021-2022-Premier-League-Stats"
        )

        time.sleep(4)

        npt.assert_array_equal(actual, expected)


if __name__ == "__main__":
    unittest.main()
