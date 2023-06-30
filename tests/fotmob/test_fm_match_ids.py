import unittest
import numpy.testing as npt
from pathlib import Path
import json
from reus.fotmob import fm_match_ids
import time


class TestFmMatchIds(unittest.TestCase):
    current_dir = Path(__file__).resolve().parent
    data_path = current_dir / "data"

    def test_epl_match_ids(self):
        with open(self.data_path / "epl_20230528_match_ids.json", "r") as f:
            expected = json.load(f)

        actual = fm_match_ids(match_date="20230528", league_id=47)

        time.sleep(4)

        npt.assert_array_equal(actual, expected)


if __name__ == "__main__":
    unittest.main()
