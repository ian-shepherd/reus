from ..util import get_page_soup


def fb_team_player_playing_time_stats(pageSoup=None, url: str = None):
    """Extracts playing time stats for each player in a given team

    Args:
        pageSoup (bs4, optional): bs4 object of a team. Defaults to None.
        url (str, optional): path of fbref team page. Defaults to None.

    Returns:
        list: playing time for each player
    """

    assert (
        pageSoup is not None or url is not None
    ), "Either pageSoup or url must be provided"

    if pageSoup is None:
        pageSoup = get_page_soup(url)

    # Find table object
    div = pageSoup.find("div", {"id": "all_stats_playing_time"})
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

        matches = row.find("td", {"data-stat": "games"}).text
        minutes = row.find("td", {"data-stat": "minutes"}).text
        minutes_per_match = row.find("td", {"data-stat": "minutes_per_game"}).text
        minutes_pct = row.find("td", {"data-stat": "minutes_pct"}).text
        minutes_90 = row.find("td", {"data-stat": "minutes_90s"}).text

        starts = row.find("td", {"data-stat": "games_starts"}).text
        minutes_per_start = row.find("td", {"data-stat": "minutes_per_start"}).text
        full_90 = row.find("td", {"data-stat": "games_complete"}).text

        subs = row.find("td", {"data-stat": "games_subs"}).text
        minutes_per_sub = row.find("td", {"data-stat": "minutes_per_sub"}).text
        unused_sub = row.find("td", {"data-stat": "unused_subs"}).text

        ppm = row.find("td", {"data-stat": "points_per_match"}).text
        goals = row.find("td", {"data-stat": "on_goals_for"}).text
        goals_allowed = row.find("td", {"data-stat": "on_goals_against"}).text
        plus_minus = row.find("td", {"data-stat": "plus_minus"}).text
        plus_minus_p90 = row.find("td", {"data-stat": "plus_minus_per90"}).text
        plus_minus_on_off = row.find("td", {"data-stat": "plus_minus_wowy"}).text

        try:
            xG = row.find("td", {"data-stat": "on_xg_for"}).text
            xGA = row.find("td", {"data-stat": "on_xg_against"}).text
            xG_plus_minus = row.find("td", {"data-stat": "xg_plus_minus"}).text
            xG_plus_minus_p90 = row.find(
                "td", {"data-stat": "xg_plus_minus_per90"}
            ).text
            xG_plus_minus_on_off = row.find(
                "td", {"data-stat": "xg_plus_minus_wowy"}
            ).text
        except AttributeError:
            xG = xGA = xG_plus_minus = xG_plus_minus_p90 = xG_plus_minus_on_off = None

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
            "minutes": minutes,
            "minutes_per_match": minutes_per_match,
            "minutes_pct": minutes_pct,
            "90s": minutes_90,
            "starts": starts,
            "minutes_per_start": minutes_per_start,
            "full_90": full_90,
            "subs": subs,
            "minutes_per_sub": minutes_per_sub,
            "unused_sub": unused_sub,
            "ppm": ppm,
            "goals": goals,
            "goals_allowed": goals_allowed,
            "plus_minus": plus_minus,
            "plus_minus_p90": plus_minus_p90,
            "plus_minus_on_off": plus_minus_on_off,
            "xG": xG,
            "xGA": xGA,
            "xG_plus_minus": xG_plus_minus,
            "xG_plus_minus_p90": xG_plus_minus_p90,
            "xG_plus_minus_on_off": xG_plus_minus_on_off,
            "match_logs": match_logs,
        }

        # add to empty list
        mylist.append(mydict)

    return mylist
