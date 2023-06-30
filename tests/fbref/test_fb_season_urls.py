import unittest
import numpy.testing as npt
from pathlib import Path
from reus.fbref import fb_season_urls
import pandas as pd


class TestFbSeasonUrls(unittest.TestCase):
    current_dir = Path(__file__).resolve().parent
    data_path = current_dir / "data"

    def test_epl_fixture_urls(self):
        expected = pd.read_csv(self.data_path / "epl_season_urls.csv")
        actual = fb_season_urls(competition_name="Premier League")
        actual = pd.DataFrame(actual)

        npt.assert_equal(actual.to_numpy(), expected.to_numpy())


if __name__ == "__main__":
    unittest.main()
