import json
import time
import unittest
from pathlib import Path

import numpy.testing as npt

from reus.fotmob import fm_match_data


class TestFbMatchData(unittest.TestCase):
    current_dir = Path(__file__).resolve().parent
    data_path = current_dir / "data"

    with open(data_path / "3901251.json", "r") as f:
        expected = json.load(f)

    actual = fm_match_data("3901251")

    time.sleep(4)

    def test_metadata(self):
        npt.assert_array_equal(self.actual[0], self.expected[0])

    def test_events(self):
        npt.assert_array_equal(self.actual[1], self.expected[1])

    def test_stats(self):
        npt.assert_array_equal(self.actual[2], self.expected[2])

    def test_shots(self):
        npt.assert_array_equal(self.actual[3], self.expected[3])

    def test_benches(self):
        npt.assert_array_equal(self.actual[4], self.expected[4])

    def test_starters(self):
        npt.assert_array_equal(self.actual[5], self.expected[5])

    def test_unavailable_players(self):
        # remove expected_return
        for i in range(len(self.actual[6])):
            self.actual[6][i].pop("expected_return", None)
            self.expected[6][i].pop("expected_return", None)

        npt.assert_array_equal(self.actual[6], self.expected[6])

    def test_shootout(self):
        npt.assert_array_equal(self.actual[7], self.expected[7])

    def test_momentum(self):
        npt.assert_array_equal(self.actual[8], self.expected[8])

    def test_shootout2(self):
        with open(self.data_path / "3370572.json", "r") as f:
            expected = json.load(f)

        actual = fm_match_data("3370572")

        time.sleep(4)
        npt.assert_array_equal(actual[7], expected[7])
