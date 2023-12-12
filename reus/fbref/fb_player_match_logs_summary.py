from ..util import get_page_soup
from .util import match_log_iterator


def fb_player_match_logs_summary(
    pageSoup=None, season_end: str = None, player_id: str = None
) -> list:
    url = f"https://fbref.com/en/players/{player_id}/matchlogs/{int(season_end)-1}-{season_end}/"

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
        "goals",
        "assists",
        "pens_made",
        "shots",
        "shots_on_target",
        "cards_yellow",
        "touches",
        "tackles",
        "interceptions",
        "blocks",
        "xg",
        "npxg",
        "xg_assist",
        "sca",
        "gca",
        "passes_completed",
        "passes",
        "passes_pct",
        "progressive_passes",
        "carries",
        "progressive_carries",
        "take_ons",
        "take_ons_won",
    ]

    mylist = match_log_iterator(rows=rows, attributes=attributes)

    return mylist


if __name__ == "__main__":
    data = fb_player_match_logs_summary(season_end="2023", player_id="1bf33a9a")
    import pandas as pd

    print(pd.DataFrame(data))

# TODO: documentation
