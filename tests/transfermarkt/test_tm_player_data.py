import unittest
import numpy.testing as npt
from pathlib import Path
import json
from reus.transfermarkt import tm_player_data
import time


class TestTmPlayerData(unittest.TestCase):
    current_dir = Path(__file__).resolve().parent
    data_path = current_dir / "data"

    with open(data_path / "reus_player_data.json", "r") as f:
        expected = json.load(f)

    actual = tm_player_data(url="/marco-reus/profil/spieler/35207")

    time.sleep(4)

    def test_metadata(self):
        npt.assert_array_equal(self.actual[0], self.expected[0])

    def test_market_value(self):
        npt.assert_array_equal(self.actual[1], self.expected[1])

    def test_transfers(self):
        npt.assert_array_equal(self.actual[2], self.expected[2])


if __name__ == "__main__":
    unittest.main()
