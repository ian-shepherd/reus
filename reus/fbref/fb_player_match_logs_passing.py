from ..util import get_page_soup
from .util import match_log_iterator


def fb_player_match_logs_passing(
    pageSoup=None, season_end: str = None, player_id: str = None
) -> list:
    """Retrieves a players passing match log for a given season

    Args:
        pageSoup (bs4, optional): bs4 object of a players passing match log page. Defaults to None.
        season_end (str): ending year of a season
        player_id (str): unique identifier for a player

    Returns:
        list: passing match log for a player in a given season
    """

    url = f"https://fbref.com/en/players/{player_id}/matchlogs/{int(season_end)-1}-{season_end}/passing/"

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
        "passes_completed",
        "passes",
        "passes_pct",
        "passes_total_distance",
        "passes_progressive_distance",
        "passes_completed_short",
        "passes_short",
        "passes_pct_short",
        "passes_completed_medium",
        "passes_medium",
        "passes_pct_medium",
        "passes_completed_long",
        "passes_long",
        "passes_pct_long",
        "assists",
        "xg_assist",
        "pass_xa",
        "assisted_shots",
        "passes_into_final_third",
        "passes_into_penalty_area",
        "crosses_into_penalty_area",
        "progressive_passes",
    ]

    mylist = match_log_iterator(rows=rows, attributes=attributes)

    return mylist
