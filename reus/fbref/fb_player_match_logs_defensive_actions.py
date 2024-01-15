from ..util import get_page_soup
from .util import match_log_iterator


def fb_player_match_logs_defensive_actions(
    pageSoup=None, season_end: str = None, player_id: str = None
) -> list:
    """Retrieves a players defensive actions match log for a given season

    Args:
        pageSoup (bs4, optional): bs4 object of a players defensive actions match log page. Defaults to None.
        season_end (str): ending year of a season
        player_id (str): unique identifier for a player

    Returns:
        list: defensive actions match log for a player in a given season
    """

    url = f"https://fbref.com/en/players/{player_id}/matchlogs/{int(season_end)-1}-{season_end}/defense/"

    assert (
        pageSoup is not None or player_id is not None
    ), "Either pageSoup or player_id must be provided"

    if pageSoup is None:
        pageSoup = get_page_soup(url)

    table = pageSoup.find("table")
    tbody = table.find("tbody")
    rows = tbody.find_all("tr")

    attributes = [
        "date",
        "url",
        "dayofweek",
        "comp",
        "round",
        "venue",
        "result",
        "team",
        "opponent",
        "game_started",
        "position",
        "minutes",
        "tackles",
        "tackles_won",
        "tackles_def_3rd",
        "tackles_mid_3rd",
        "tackles_att_3rd",
        "challenge_tackles",
        "challenges",
        "challenge_tackles_pct",
        "challenges_lost",
        "blocks",
        "blocked_shots",
        "blocked_passes",
        "interceptions",
        "tackles_interceptions",
        "clearances",
        "errors",
    ]

    mylist = match_log_iterator(rows=rows, attributes=attributes)

    return mylist
