from ..util import get_page_soup
from .util import match_log_iterator


def fb_player_match_logs_possession(
    pageSoup=None, season_end: str = None, player_id: str = None
) -> list:
    url = f"https://fbref.com/en/players/{player_id}/matchlogs/{int(season_end)-1}-{season_end}/possession/"

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
        "touches"
        "touches_def_pen_area"
        "touches_def_3rd"
        "touches_mid_3rd"
        "touches_att_3rd"
        "touches_att_pen_area"
        "touches_live_ball"
        "take_ons"
        "take_ons_won"
        "take_ons_won_pct"
        "take_ons_tackled"
        "take_ons_tackled_pct"
        "carries"
        "carries_distance"
        "carries_progressive_distance"
        "progressive_carries"
        "carries_into_final_third"
        "carries_into_penalty_area"
        "miscontrols"
        "dispossessed"
        "passes_received"
        "progressive_passes_received",
    ]

    mylist = match_log_iterator(rows=rows, attributes=attributes)

    return mylist


# TODO: documentation
