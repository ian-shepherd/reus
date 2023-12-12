from ..util import get_page_soup
from .util import match_log_iterator


def fb_player_match_logs_gca_sca(
    pageSoup=None, season_end: str = None, player_id: str = None
) -> list:
    url = f"https://fbref.com/en/players/{player_id}/matchlogs/{int(season_end)-1}-{season_end}/gca/"

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
        "sca",
        "sca_passes_live",
        "sca_passes_dead",
        "sca_take_ons",
        "sca_shots",
        "sca_fouled",
        "sca_defense",
        "gca",
        "gca_passes_live",
        "gca_passes_dead",
        "gca_take_ons",
        "gca_shots",
        "gca_fouled",
        "gca_defense",
    ]

    mylist = match_log_iterator(rows=rows, attributes=attributes)

    return mylist


# TODO: documentation
