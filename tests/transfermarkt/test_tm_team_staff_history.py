import json
import time
import unittest
from pathlib import Path

import numpy.testing as npt

from reus.transfermarkt import tm_team_staff_history


class TestTmTeamStaffHistoryData(unittest.TestCase):
    current_dir = Path(__file__).resolve().parent
    data_path = current_dir / "data"

    with open(data_path / "newcastle_manager_history_data.json", "r") as f:
        expected = json.load(f)

    actual = tm_team_staff_history(
        club="Newcastle United",
        team_id=762,
        role="Manager",
    )

    time.sleep(4)

    def test_team_staff_history_data(self):
        npt.assert_array_equal(self.actual, self.expected)


if __name__ == "__main__":
    unittest.main()
