import unittest
import numpy.testing as npt
from pathlib import Path
import json
from reus.transfermarkt import tm_player_injury
import time


class TestTmPlayerData(unittest.TestCase):
    current_dir = Path(__file__).resolve().parent
    data_path = current_dir / "data"

    with open(data_path / "reus_injury_data.json", "r") as f:
        expected = json.load(f)

    actual = tm_player_injury(
        url="https://www.transfermarkt.us/marco-reus/verletzungen/spieler/35207"
    )[-68:]

    time.sleep(4)

    def test_injury_data(self):
        npt.assert_array_equal(self.actual, self.expected)


if __name__ == "__main__":
    unittest.main()
