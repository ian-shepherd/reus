import time

from .fb_player_match_logs_defensive_actions import (
    fb_player_match_logs_defensive_actions,
)
from .fb_player_match_logs_gca_sca import fb_player_match_logs_gca_sca
from .fb_player_match_logs_misc import fb_player_match_logs_misc
from .fb_player_match_logs_passing import fb_player_match_logs_passing
from .fb_player_match_logs_passing_type import fb_player_match_logs_passing_type
from .fb_player_match_logs_possession import fb_player_match_logs_possession
from .fb_player_match_logs_summary import fb_player_match_logs_summary


def fb_player_match_logs_data(season_end: str, player_id: str) -> dict:
    """Retrieves all match logs for a player in a given season

    Args:
        season_end (str): ending year of a season
        player_id (str): unique identifier for a player

    Returns:
        dict: match logs for a player in a given season
    """

    summary = fb_player_match_logs_summary(season_end=season_end, player_id=player_id)
    time.sleep(4)

    passing = fb_player_match_logs_passing(season_end=season_end, player_id=player_id)
    time.sleep(4)

    passing_type = fb_player_match_logs_passing_type(
        season_end=season_end, player_id=player_id
    )
    time.sleep(4)

    gca_sca = fb_player_match_logs_gca_sca(season_end=season_end, player_id=player_id)
    time.sleep(4)

    defensive_actions = fb_player_match_logs_defensive_actions(
        season_end=season_end, player_id=player_id
    )
    time.sleep(4)

    possession = fb_player_match_logs_possession(
        season_end=season_end, player_id=player_id
    )
    time.sleep(4)

    misc = fb_player_match_logs_misc(season_end=season_end, player_id=player_id)
    time.sleep(4)

    data = {
        "summary": summary,
        "passing": passing,
        "passing_type": passing_type,
        "gca_sca": gca_sca,
        "defensive_actions": defensive_actions,
        "possession": possession,
        "misc": misc,
    }

    return data
