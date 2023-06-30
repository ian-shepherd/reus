import unittest
import numpy.testing as npt
from pathlib import Path
import json
from reus.fbref import fb_match_data
import time


class TestFbMatchData(unittest.TestCase):
    current_dir = Path(__file__).resolve().parent
    data_path = current_dir / "data"

    with open(data_path / "dff22d13.json", "r") as f:
        expected = json.load(f)

    actual = fb_match_data(
        "/en/matches/dff22d13/Newcastle-United-Tottenham-Hotspur-April-23-2023-Premier-League"
    )

    time.sleep(4)

    def test_metadata(self):
        npt.assert_array_equal(self.actual[0], self.expected[0])

    def test_officials(self):
        npt.assert_array_equal(self.actual[1], self.expected[1])

    def test_lineups(self):
        npt.assert_array_equal(self.actual[2], self.expected[2])

    def test_summary(self):
        npt.assert_array_equal(self.actual[3], self.expected[3])

    def test_stats(self):
        npt.assert_array_equal(self.actual[4], self.expected[4])

    def test_summary_stats_x(self):
        npt.assert_array_equal(self.actual[5], self.expected[5])

    def test_summary_stats_y(self):
        npt.assert_array_equal(self.actual[6], self.expected[6])

    def test_passing_stats_x(self):
        npt.assert_array_equal(self.actual[7], self.expected[7])

    def test_passing_stats_y(self):
        npt.assert_array_equal(self.actual[8], self.expected[8])

    def test_passing_types_x(self):
        npt.assert_array_equal(self.actual[9], self.expected[9])

    def test_passing_types_y(self):
        npt.assert_array_equal(self.actual[10], self.expected[10])

    def test_defense_stats_x(self):
        npt.assert_array_equal(self.actual[11], self.expected[11])

    def test_defense_stats_y(self):
        npt.assert_array_equal(self.actual[12], self.expected[12])

    def test_possession_stats_x(self):
        npt.assert_array_equal(self.actual[13], self.expected[13])

    def test_possession_stats_y(self):
        npt.assert_array_equal(self.actual[14], self.expected[14])

    def test_misc_stats_x(self):
        npt.assert_array_equal(self.actual[15], self.expected[15])

    def test_misc_stats_y(self):
        npt.assert_array_equal(self.actual[16], self.expected[16])

    def test_keeper_stats_x(self):
        npt.assert_array_equal(self.actual[17], self.expected[17])

    def test_keeper_stats_y(self):
        npt.assert_array_equal(self.actual[18], self.expected[18])

    def test_shots(self):
        npt.assert_array_equal(self.actual[19], self.expected[19])


if __name__ == "__main__":
    unittest.main()
