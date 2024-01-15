import json
import time
import unittest
from pathlib import Path

import numpy.testing as npt

from reus.fotmob import fm_season_stat_leaders


class TestFmSeasonStatLeaders(unittest.TestCase):
    current_dir = Path(__file__).resolve().parent
    data_path = current_dir / "data"

    def test_epl_g_a_leaders(self):
        with open(self.data_path / "epl_g_a_season_stat_leaders_2022_2023.json") as f:
            expected = json.load(f)

        actual = fm_season_stat_leaders(
            league_id=47,
            team_or_player="players",
            stat_name="Goals + Assists",
            season="2022/2023",
        ).to_dict(orient="records")

        time.sleep(4)

        npt.assert_array_equal(actual, expected)

    def test_epl_pen_won_leaders(self):
        with open(
            self.data_path / "epl_pen_won_season_stat_leaders_2021_2022.json"
        ) as f:
            expected = json.load(f)

        actual = fm_season_stat_leaders(
            league_id=47,
            team_or_player="players",
            stat_name="Penalties won",
            season="2021/2022",
        ).to_dict(orient="records")

        time.sleep(4)

        npt.assert_array_equal(actual, expected)

    def test_epl_big_chances_created_leaders(self):
        with open(
            self.data_path
            / "epl_big_chances_created_season_stat_leaders_2020_2021.json"  # noqa: W503
        ) as f:
            expected = json.load(f)

        actual = fm_season_stat_leaders(
            league_id=47,
            team_or_player="teams",
            stat_name="Big chances",
            season="2020/2021",
        ).to_dict(orient="records")

        time.sleep(4)

        npt.assert_array_equal(actual, expected)


if __name__ == "__main__":
    unittest.main()
