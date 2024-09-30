import json
import time
import unittest
from pathlib import Path

import numpy.testing as npt

from reus.fbref import fb_team_player_data


class TestFbTeamPlayerData(unittest.TestCase):
    current_dir = Path(__file__).resolve().parent
    data_path = current_dir / "data"

    with open(data_path / "newcastle_player_stats_2021_2022.json", "r") as f:
        expected = json.load(f)

    actual = fb_team_player_data("/en/squads/b2b47a98/2021-2022/Newcastle-United-Stats")

    time.sleep(4)

    def test_summary_stats(self):
        npt.assert_array_equal(self.actual[0], self.expected[0])

    def test_keeper_stats(self):
        npt.assert_array_equal(self.actual[1], self.expected[1])

    def test_advanced_keeper_stats(self):
        npt.assert_array_equal(self.actual[2], self.expected[2])

    def test_shooting_stats(self):
        npt.assert_array_equal(self.actual[3], self.expected[3])

    def test_passing_stats(self):
        npt.assert_array_equal(self.actual[4], self.expected[4])

    def test_passing_types(self):
        npt.assert_array_equal(self.actual[5], self.expected[5])

    def test_goal_and_shot_creation(self):
        npt.assert_array_equal(self.actual[6], self.expected[6])

    def test_defensive_actions(self):
        npt.assert_array_equal(self.actual[7], self.expected[7])

    def test_possession_stats(self):
        npt.assert_array_equal(self.actual[8], self.expected[8])

    def test_playing_time_stats(self):
        npt.assert_array_equal(self.actual[9], self.expected[9])

    def test_misc_stats(self):
        npt.assert_array_equal(self.actual[10], self.expected[10])


if __name__ == "__main__":
    unittest.main()
