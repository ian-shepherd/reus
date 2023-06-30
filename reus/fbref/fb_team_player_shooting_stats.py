from ..util import get_page_soup


def fb_team_player_shooting_stats(pageSoup=None, url: str = None) -> list:
    """Extracts shooting stats for each player in a given team

    Args:
        pageSoup (bs4, optional): bs4 object of a match. Defaults to None.
        url (str, optional): path of fbref match page. Defaults to None.

    Returns:
        list: shooting stats for each player
    """

    assert (
        pageSoup is not None or url is not None
    ), "Either pageSoup or url must be provided"

    if pageSoup is None:
        pageSoup = get_page_soup(url)

    # Find table object
    div = pageSoup.find("div", {"id": "all_stats_shooting"})
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
        minutes_90 = row.find("td", {"data-stat": "minutes_90s"}).text

        # standard
        goals = row.find("td", {"data-stat": "goals"}).text
        shots = row.find("td", {"data-stat": "shots"}).text
        shots_on_target = row.find("td", {"data-stat": "shots_on_target"}).text
        shots_on_target_per = row.find("td", {"data-stat": "shots_on_target_pct"}).text
        shots_p90 = row.find("td", {"data-stat": "shots_per90"}).text
        shots_on_target_p90 = row.find(
            "td", {"data-stat": "shots_on_target_per90"}
        ).text
        goals_per_shot = row.find("td", {"data-stat": "goals_per_shot"}).text
        goals_per_sot = row.find("td", {"data-stat": "goals_per_shot_on_target"}).text
        try:
            dist = row.find("td", {"data-stat": "average_shot_distance"}).text
            fk = row.find("td", {"data-stat": "shots_free_kicks"}).text
        except AttributeError:
            dist = fk = None
        pk = row.find("td", {"data-stat": "pens_made"}).text
        pk_attempted = row.find("td", {"data-stat": "pens_att"}).text

        # expected
        try:
            xG = row.find("td", {"data-stat": "xg"}).text
            npxG = row.find("td", {"data-stat": "npxg"}).text
            npxG_per_shot = row.find("td", {"data-stat": "npxg_per_shot"}).text
            goals_xG = row.find("td", {"data-stat": "xg_net"}).text
            npg_xG = row.find("td", {"data-stat": "npxg_net"}).text
        except AttributeError:
            xG = npxG = npxG_per_shot = goals_xG = npg_xG = None

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
            "90s": minutes_90,
            "goals": goals,
            "shots": shots,
            "shots_on_target": shots_on_target,
            "shots_on_target%": shots_on_target_per,
            "shots_p90": shots_p90,
            "shots_on_target_p90": shots_on_target_p90,
            "goals_per_shot": goals_per_shot,
            "goals_per_shot_on_target": goals_per_sot,
            "avg_distance": dist,
            "free_kicks": fk,
            "pk": pk,
            "pk_attempted": pk_attempted,
            "xG": xG,
            "npxG": npxG,
            "npxG_per_shot": npxG_per_shot,
            "goals_minus_xG": goals_xG,
            "npg_minus_xG": npg_xG,
            "match_logs": match_logs,
        }

        # add to empty list
        mylist.append(mydict)

    return mylist
