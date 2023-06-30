import unittest
import numpy.testing as npt
from reus.fbref import fb_season_fixture_urls


class TestFbSeasonFixtureUrls(unittest.TestCase):
    def test_epl_fixture_urls(self):
        expected = "https://fbref.com/en/comps/9/2021-2022/schedule/2021-2022-Premier-League-Scores-and-Fixtures"
        actual = fb_season_fixture_urls(
            competition_name="Premier League", season_end_year=2022
        ).iloc[0]

        npt.assert_equal(actual, expected)

    def test_nwsl_fixture_urls(self):
        expected = (
            "https://fbref.com/en/comps/182/2021/schedule/2021-NWSL-Scores-and-Fixtures"
        )
        actual = fb_season_fixture_urls(
            competition_name="National Women's Soccer League", season_end_year=2021
        ).iloc[0]

        npt.assert_equal(actual, expected)


if __name__ == "__main__":
    unittest.main()
