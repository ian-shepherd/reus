import unittest
import numpy.testing as npt
from pathlib import Path
import json
from reus.fotmob import fm_season_stats
import time


class TestFmSeasonStatLeaders(unittest.TestCase):
    current_dir = Path(__file__).resolve().parent
    data_path = current_dir / "data"

    def test_epl_big_chances_created_leaders(self):
        with open(
            self.data_path
            / "epl_big_chances_created_complete_season_stat_2020_2021.json"
        ) as f:
            expected = json.load(f)

        actual = fm_season_stats(
            league_id=47,
            team_or_player="teams",
            stat_name="Big chances created",
            season="2020/2021",
        ).to_dict(orient="records")

        time.sleep(4)

        npt.assert_array_equal(actual, expected)


if __name__ == "__main__":
    unittest.main()
