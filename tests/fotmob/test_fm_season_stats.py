import json
import time
import unittest
from pathlib import Path

import numpy.testing as npt

from reus.fotmob import fm_season_stats


class TestFmSeasonStats(unittest.TestCase):
    current_dir = Path(__file__).resolve().parent
    data_path = current_dir / "data"

    def test_epl_big_chances_created(self):
        with open(
            self.data_path
            / "epl_big_chances_created_complete_season_stat_2020_2021.json"  # noqa: W503
        ) as f:
            expected = json.load(f)

        actual = fm_season_stats(
            league_id=47,
            team_or_player="teams",
            stat_name="Big chances",
            season="2020/2021",
        ).to_dict(orient="records")

        time.sleep(4)

        npt.assert_array_equal(actual, expected)


if __name__ == "__main__":
    unittest.main()
