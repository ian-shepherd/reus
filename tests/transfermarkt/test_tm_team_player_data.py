import unittest
import numpy.testing as npt
from pathlib import Path
import json
from reus.transfermarkt import tm_team_player_data
import time


class TestTmPlayerData(unittest.TestCase):
    current_dir = Path(__file__).resolve().parent
    data_path = current_dir / "data"

    def test_player_data(self):
        with open(self.data_path / "dortmund_players.json", "r") as f:
            expected = json.load(f)

        actual = tm_team_player_data(
            club="Borussia Dortmund",
            season="2022",
        )

        time.sleep(4)

        for dicts in expected:
            dicts.pop("contracted", None)
        for dicts in actual:
            dicts.pop("contracted", None)

        npt.assert_array_equal(actual, expected)


if __name__ == "__main__":
    unittest.main()
