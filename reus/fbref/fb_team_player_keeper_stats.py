from ..util import get_page_soup


def fb_team_player_keeper_stats(pageSoup=None, url: str = None) -> list:
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
        # general
        th = row.find("th")
        try:
            name = th.text
        except AttributeError:
            name = th["csk"]
        player_id = th.find("a", href=True)["href"].split("/")[3]
        nation = row.find("td", {"data-stat": "nationality"}).text
        position = row.find("td", {"data-stat": "position"}).text
        age = row.find("td", {"data-stat": "age"}).text.split("-")
        try:
            age = int(age[0]) + int(age[1]) / 365
        except IndexError:
            age = int(age[0])
        except ValueError:
            age = None

        # playing time
        matches = row.find("td", {"data-stat": "gk_games"}).text
        starts = row.find("td", {"data-stat": "gk_games_starts"}).text
        minutes = row.find("td", {"data-stat": "gk_minutes"}).text
        minutes_90 = row.find("td", {"data-stat": "minutes_90s"}).text

        # performance
        goals_allowed = row.find("td", {"data-stat": "gk_goals_against"}).text
        goals_allowed_p90 = row.find("td", {"data-stat": "gk_goals_against_per90"}).text
        shots_against = row.find("td", {"data-stat": "gk_shots_on_target_against"}).text
        saves = row.find("td", {"data-stat": "gk_saves"}).text
        save_pct = row.find("td", {"data-stat": "gk_save_pct"}).text
        wins = row.find("td", {"data-stat": "gk_wins"}).text
        draws = row.find("td", {"data-stat": "gk_ties"}).text
        losses = row.find("td", {"data-stat": "gk_losses"}).text
        clean_sheets = row.find("td", {"data-stat": "gk_clean_sheets"}).text
        cleen_sheet_pct = row.find("td", {"data-stat": "gk_clean_sheets_pct"}).text

        # penalty kicks
        pk_against = row.find("td", {"data-stat": "gk_pens_att"}).text
        pk_allowed = row.find("td", {"data-stat": "gk_pens_allowed"}).text
        pk_saves = row.find("td", {"data-stat": "gk_pens_saved"}).text
        pk_missed = row.find("td", {"data-stat": "gk_pens_missed"}).text
        pk_save_pct = row.find("td", {"data-stat": "gk_pens_save_pct"}).text

        # match logs
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
