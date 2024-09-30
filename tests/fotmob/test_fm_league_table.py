import json
import time
import unittest
from pathlib import Path

import numpy.testing as npt

from reus.fotmob import fm_league_table


class TestFmLeagueTable(unittest.TestCase):
    current_dir = Path(__file__).resolve().parent
    data_path = current_dir / "data"

    def test_epl_table(self):
        with open(self.data_path / "epl_table_2022_2023.json") as f:
            expected = json.load(f)

        actual = (
            fm_league_table(league_id=47, season="2022/2023")
            .get("Premier League")
            .to_dict(orient="records")
        )

        time.sleep(4)

        npt.assert_equal(actual, expected)

    def test_la_liga_home_table(self):
        with open(self.data_path / "la_liga_home_table_2022_2023.json") as f:
            expected = json.load(f)

        actual = (
            fm_league_table(league_id=87, season="2022/2023", matches="Home")
            .get("LaLiga")
            .to_dict(orient="records")
        )

        time.sleep(4)

        npt.assert_equal(actual, expected)

    def test_ligue_1_away_table(self):
        with open(self.data_path / "ligue_1_away_table_2022_2023.json") as f:
            expected = json.load(f)

        actual = (
            fm_league_table(league_id=53, season="2022/2023", matches="Away")
            .get("Ligue 1")
            .to_dict(orient="records")
        )

        time.sleep(4)

        npt.assert_equal(actual, expected)

    def test_bundesliga_form_table(self):
        with open(self.data_path / "bundesliga_form_table_2022_2023.json") as f:
            expected = json.load(f)

        actual = (
            fm_league_table(league_id=54, season="2022/2023", matches="Form")
            .get("Bundesliga")
            .to_dict(orient="records")
        )

        time.sleep(4)

        npt.assert_equal(actual, expected)


if __name__ == "__main__":
    unittest.main()
