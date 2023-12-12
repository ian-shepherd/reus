from ..util import get_page_soup
from .util import match_log_iterator


def fb_player_match_logs_misc(
    pageSoup=None, season_end: str = None, player_id: str = None
) -> list:
    url = f"https://fbref.com/en/players/{player_id}/matchlogs/{int(season_end)-1}-{season_end}/misc/"

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
        "cards_yellow",
        "cards_red",
        "cards_yellow_red",
        "fouls",
        "fouled",
        "offsides",
        "crosses",
        "interceptions",
        "tackles_won",
        "pens_won",
        "pens_conceded",
        "own_goals",
        "ball_recoveries",
        "aerials_won",
        "aerials_lost",
        "aerials_won_pct",
    ]

    mylist = match_log_iterator(rows=rows, attributes=attributes)

    return mylist


# TODO: documentation
