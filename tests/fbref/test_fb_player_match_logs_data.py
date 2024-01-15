import json
import time
import unittest
from pathlib import Path

import numpy.testing as npt

from reus.fbref import fb_player_match_logs_data


class TestFbPlayerMatchLogsData(unittest.TestCase):
    current_dir = Path(__file__).resolve().parent
    data_path = current_dir / "data"

    with open(data_path / "reus_match_logs_2022_2023.json", "r") as f:
        expected = json.load(f)

    actual = fb_player_match_logs_data(season_end=2023, player_id="36a3ff67")

    time.sleep(4)

    def test_summary_stats(self):
        npt.assert_array_equal(self.actual.get("summary"), self.expected.get("summary"))

    def test_passing_stats(self):
        npt.assert_array_equal(self.actual.get("passing"), self.expected.get("passing"))

    def test_passing_type_stats(self):
        npt.assert_array_equal(
            self.actual.get("passing_type"), self.expected.get("passing_type")
        )

    def test_gca_sca_stats(self):
        npt.assert_array_equal(self.actual.get("gca_sca"), self.expected.get("gca_sca"))

    def test_defensive_actions_stats(self):
        npt.assert_array_equal(
            self.actual.get("defensive_actions"),
            self.expected.get("defensive_actions"),
        )

    def test_possession_stats(self):
        npt.assert_array_equal(
            self.actual.get("possession"), self.expected.get("possession")
        )

    def test_misc_stats(self):
        npt.assert_array_equal(self.actual.get("misc"), self.expected.get("misc"))


if __name__ == "__main__":
    unittest.main()
