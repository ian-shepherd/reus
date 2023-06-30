import unittest
import numpy.testing as npt
from pathlib import Path
import json
from reus.fotmob import fm_match_data
import time


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

    def test_shots(self):
        npt.assert_array_equal(self.actual[2], self.expected[2])

    def test_benches(self):
        npt.assert_array_equal(self.actual[3], self.expected[3])

    def test_starters(self):
        npt.assert_array_equal(self.actual[4], self.expected[4])

    def test_unavailable_players(self):
        npt.assert_array_equal(self.actual[5], self.expected[5])

    def test_shootout(self):
        npt.assert_array_equal(self.actual[6], self.expected[6])

    def test_shootout2(self):
        with open(self.data_path / "3370572.json", "r") as f:
            expected = json.load(f)

        actual = fm_match_data("3370572")

        time.sleep(4)
        npt.assert_array_equal(actual[6], expected[6])
