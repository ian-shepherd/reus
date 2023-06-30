import unittest
import numpy.testing as npt
from reus.fotmob import fm_leagues


class TestFmLeagueIds(unittest.TestCase):
    def test_epl_league_ids(self):
        expected = {
            "competition_type": "Domestic Leagues - 1st Tier",
            "competition_name": "Premier League",
            "ccode": "ENG",
            "country": "England",
            "gender": "M",
            "id": 47,
            "league_url": "/leagues/47/overview/premier-league",
        }
        actual = (
            fm_leagues(
                ccode="ENG", competition_type="Domestic Leagues - 1st Tier", gender="M"
            )
            .iloc[0]
            .to_dict()
        )

        npt.assert_equal(actual, expected)

    def test_wsl_league_ids(self):
        expected = {
            "competition_type": "Domestic Leagues - 1st Tier",
            "competition_name": "WSL",
            "ccode": "ENG",
            "country": "England",
            "gender": "W",
            "id": 9227,
            "league_url": "/leagues/9227/overview/wsl",
        }
        actual = (
            fm_leagues(
                ccode="ENG", competition_type="Domestic Leagues - 1st Tier", gender="W"
            )
            .iloc[0]
            .to_dict()
        )

        npt.assert_equal(actual, expected)


if __name__ == "__main__":
    unittest.main()
