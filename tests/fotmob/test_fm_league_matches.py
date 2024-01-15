import time
import unittest
from pathlib import Path

import numpy.testing as npt
import pandas as pd

from reus.fotmob import fm_league_matches


class TestFmLeagueMatches(unittest.TestCase):
    current_dir = Path(__file__).resolve().parent
    data_path = current_dir / "data"

    def test_epl_matches(self):
        expected = pd.read_csv(self.data_path / "epl_matches_2022_2023.csv")
        actual = fm_league_matches(league_id=47, season="2022/2023")

        drop_cols = ["pageUrl", "round", "roundName", "utcTime"]
        expected.drop(columns=drop_cols, inplace=True)
        actual.drop(columns=drop_cols, inplace=True)

        actual = actual.astype(expected.dtypes.to_dict())

        npt.assert_equal(actual.to_numpy(), expected.to_numpy())

        time.sleep(4)

    def test_mls_matches(self):
        expected = pd.read_csv(self.data_path / "mls_matches_2022.csv")
        actual = fm_league_matches(league_id=130, season="2022")

        drop_cols = ["pageUrl", "round", "roundName", "utcTime"]
        expected.drop(columns=drop_cols, inplace=True)
        actual.drop(columns=drop_cols, inplace=True)

        actual = actual.astype(expected.dtypes.to_dict())

        npt.assert_equal(actual.to_numpy(), expected.to_numpy())

        time.sleep(4)


if __name__ == "__main__":
    unittest.main()
