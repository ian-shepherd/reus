import unittest
import numpy.testing as npt
from pathlib import Path
from reus.fbref import fb_match_urls
import pandas as pd
import time


class TestFbMatchUrls(unittest.TestCase):
    current_dir = Path(__file__).resolve().parent
    data_path = current_dir / "data"

    def test_epl_match_urls(self):
        expected = pd.read_csv(self.data_path / "epl_match_urls_2021_2022.csv")

        actual = fb_match_urls(
            "https://fbref.com/en/comps/9/2021-2022/schedule/2021-2022-Premier-League-Scores-and-Fixtures"
        )
        actual = pd.DataFrame(actual)

        time.sleep(4)

        npt.assert_array_equal(actual.to_numpy(), expected.to_numpy())


if __name__ == "__main__":
    unittest.main()
