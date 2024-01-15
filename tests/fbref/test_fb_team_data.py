import json
import time
import unittest
from pathlib import Path

import numpy.testing as npt

from reus.fbref import fb_team_data


class TestFbTeamData(unittest.TestCase):
    current_dir = Path(__file__).resolve().parent
    data_path = current_dir / "data"

    with open(data_path / "epl_team_stats_2021_2022.json", "r") as f:
        expected = json.load(f)

    actual = fb_team_data("/en/comps/9/2021-2022/2021-2022-Premier-League-Stats")

    time.sleep(4)

    def test_summary_stats_for(self):
        npt.assert_array_equal(self.actual[0], self.expected[0])

    def test_summary_stats_against(self):
        npt.assert_array_equal(self.actual[1], self.expected[1])

    def test_keeper_stats_for(self):
        npt.assert_array_equal(self.actual[2], self.expected[2])

    def test_keeper_stats_against(self):
        npt.assert_array_equal(self.actual[3], self.expected[3])

    def test_advanced_keeper_stats_for(self):
        npt.assert_array_equal(self.actual[4], self.expected[4])

    def test_advanced_keeper_stats_against(self):
        npt.assert_array_equal(self.actual[5], self.expected[5])

    def test_shooting_stats_for(self):
        npt.assert_array_equal(self.actual[6], self.expected[6])

    def test_shooting_stats_against(self):
        npt.assert_array_equal(self.actual[7], self.expected[7])

    def test_passing_stats_for(self):
        npt.assert_array_equal(self.actual[8], self.expected[8])

    def test_passing_stats_against(self):
        npt.assert_array_equal(self.actual[9], self.expected[9])

    def test_passing_types_for(self):
        npt.assert_array_equal(self.actual[10], self.expected[10])

    def test_passing_types_against(self):
        npt.assert_array_equal(self.actual[11], self.expected[11])

    def test_goal_and_shot_creation_for(self):
        npt.assert_array_equal(self.actual[12], self.expected[12])

    def test_goal_and_shot_creation_against(self):
        npt.assert_array_equal(self.actual[13], self.expected[13])

    def test_defensive_actions_for(self):
        npt.assert_array_equal(self.actual[14], self.expected[14])

    def test_defensive_actions_against(self):
        npt.assert_array_equal(self.actual[15], self.expected[15])

    def test_possession_stats_for(self):
        npt.assert_array_equal(self.actual[16], self.expected[16])

    def test_possession_stats_against(self):
        npt.assert_array_equal(self.actual[17], self.expected[17])

    def test_playing_time_stats_for(self):
        npt.assert_array_equal(self.actual[18], self.expected[18])

    def test_playing_time_stats_against(self):
        npt.assert_array_equal(self.actual[19], self.expected[19])

    def test_misc_stats_for(self):
        npt.assert_array_equal(self.actual[20], self.expected[20])

    def test_misc_stats_against(self):
        npt.assert_array_equal(self.actual[21], self.expected[21])


if __name__ == "__main__":
    unittest.main()
