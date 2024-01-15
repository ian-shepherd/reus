import json
import time
import unittest
from pathlib import Path

import numpy.testing as npt

from reus.transfermarkt import tm_team_player_data


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

        # drop name, number, position, signed_from, currency, and contracted
        for dicts in expected:
            dicts.pop("name", None)
            dicts.pop("number", None)
            dicts.pop("position", None)
            dicts.pop("signed_from", None)
            dicts.pop("currency", None)
            dicts.pop("contracted", None)
            dicts.pop("arrival_type", None)
        for dicts in actual:
            dicts.pop("name", None)
            dicts.pop("number", None)
            dicts.pop("position", None)
            dicts.pop("signed_from", None)
            dicts.pop("currency", None)
            dicts.pop("contracted", None)

        npt.assert_array_equal(actual, expected)


if __name__ == "__main__":
    unittest.main()
