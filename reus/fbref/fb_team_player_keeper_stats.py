from ..util import get_page_soup


def fb_team_player_keeper_stats(pageSoup=None, url: str = None):
    """Extracts basic keeper stats for each player in a given team

    Args:
        pageSoup (bs4, optional): bs4 object of a team. Defaults to None.
        url (str, optional): path of fbref team page. Defaults to None.

    Returns:
        list: goalkeeper stats for each player
    """

    assert (
        pageSoup is not None or url is not None
    ), "Either pageSoup or url must be provided"

    if pageSoup is None:
        pageSoup = get_page_soup(url)

    # Find table object
    div = pageSoup.find("div", {"id": "all_stats_keeper"})

    table = div.find("table")
    tbody = table.find("tbody")
    rows = tbody.find_all("tr")

    # Generate empty list
    mylist = []

    # iterate through each player and store attributes
    for row in rows:
        th = row.find("th")
        name = th["csk"]
        player_id = th.find("a", href=True)["href"].split("/")[3]
        nation = row.find("td", {"data-stat": "nationality"}).text
        position = row.find("td", {"data-stat": "position"}).text
        age = row.find("td", {"data-stat": "age"}).text.split("-")
        if len(age) > 1:
            age = int(age[0]) + int(age[1]) / 365
        else:
            age = age[0]
        matches = row.find("td", {"data-stat": "games_gk"}).text
        starts = row.find("td", {"data-stat": "games_starts_gk"}).text
        minutes = row.find("td", {"data-stat": "minutes_gk"}).text
        minutes_90 = row.find("td", {"data-stat": "minutes_90s"}).text

        goals_allowed = row.find("td", {"data-stat": "goals_against_gk"}).text
        goals_allowed_p90 = row.find("td", {"data-stat": "goals_against_per90_gk"}).text
        shots_against = row.find("td", {"data-stat": "shots_on_target_against"}).text
        saves = row.find("td", {"data-stat": "saves"}).text
        save_pct = row.find("td", {"data-stat": "save_pct"}).text
        wins = row.find("td", {"data-stat": "wins_gk"}).text
        draws = row.find("td", {"data-stat": "draws_gk"}).text
        losses = row.find("td", {"data-stat": "losses_gk"}).text
        clean_sheets = row.find("td", {"data-stat": "clean_sheets"}).text
        cleen_sheet_pct = row.find("td", {"data-stat": "clean_sheets_pct"}).text

        pk_against = row.find("td", {"data-stat": "pens_att_gk"}).text
        pk_allowed = row.find("td", {"data-stat": "pens_allowed"}).text
        pk_saves = row.find("td", {"data-stat": "pens_saved"}).text
        pk_missed = row.find("td", {"data-stat": "pens_missed_gk"}).text
        pk_save_pct = row.find("td", {"data-stat": "pens_save_pct"}).text

        match_logs = row.find("td", {"data-stat": "matches"}).find("a", href=True)[
            "href"
        ]

        # generate dictionary for player
        mydict = {
            "player_id": player_id,
            "name": name,
            "nation": nation,
            "position": position,
            "age": age,
            "matches": matches,
            "starts": starts,
            "minutes": minutes,
            "90s": minutes_90,
            "goals_allowed": goals_allowed,
            "goals_allowed_p90": goals_allowed_p90,
            "shots_against": shots_against,
            "saves": saves,
            "saves_pct": save_pct,
            "wins": wins,
            "draws": draws,
            "losses": losses,
            "clean_sheets": clean_sheets,
            "clean_sheets_pct": cleen_sheet_pct,
            "pk_against": pk_against,
            "pk_allowed": pk_allowed,
            "pk_saves": pk_saves,
            "pk_missed": pk_missed,
            "pk_save_pct": pk_save_pct,
            "match_logs": match_logs,
        }

        # add to empty list
        mylist.append(mydict)

    return mylist
