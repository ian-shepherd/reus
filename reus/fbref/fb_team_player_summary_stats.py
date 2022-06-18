from ..util import get_page_soup


def fb_team_player_summary_stats(pageSoup=None, url: str = None):
    """Extracts summary stats for each player in a given team

    Args:
        pageSoup (bs4, optional): bs4 object of a team. Defaults to None.
        url (str, optional): path of fbref team page. Defaults to None.

    Returns:
        list: summary stats for each player
    """

    assert (
        pageSoup is not None or url is not None
    ), "Either pageSoup or url must be provided"

    if pageSoup is None:
        pageSoup = get_page_soup(url)

    # Find table object
    table = pageSoup.find("table")
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
        minutes = row.find("td", {"data-stat": "minutes"}).text
        minutes_90 = row.find("td", {"data-stat": "minutes_90s"}).text

        goals = row.find("td", {"data-stat": "goals"}).text
        assists = row.find("td", {"data-stat": "assists"}).text
        npg = row.find("td", {"data-stat": "goals_pens"}).text
        pk = row.find("td", {"data-stat": "pens_made"}).text
        pk_attempted = row.find("td", {"data-stat": "pens_att"}).text
        card_yellow = row.find("td", {"data-stat": "cards_yellow"}).text
        card_red = row.find("td", {"data-stat": "cards_red"}).text

        goalp90 = row.find("td", {"data-stat": "goals_per90"}).text
        assistsp90 = row.find("td", {"data-stat": "assists_per90"}).text
        g_ap90 = row.find("td", {"data-stat": "goals_assists_per90"}).text
        npgp90 = row.find("td", {"data-stat": "goals_pens_per90"}).text
        npg_ap90 = row.find("td", {"data-stat": "goals_assists_pens_per90"}).text

        try:
            xG = row.find("td", {"data-stat": "xg"}).text
            npxG = row.find("td", {"data-stat": "npxg"}).text
            xA = row.find("td", {"data-stat": "xa"}).text
            npxG_a = row.find("td", {"data-stat": "npxg_xa"}).text
            xGp90 = row.find("td", {"data-stat": "xg_per90"}).text
            xAp90 = row.find("td", {"data-stat": "xa_per90"}).text
            xG_xAp90 = row.find("td", {"data-stat": "xg_xa_per90"}).text
            npxGp90 = row.find("td", {"data-stat": "npxg_per90"}).text
            npxG_ap90 = row.find("td", {"data-stat": "npxg_xa_per90"}).text
        except AttributeError:
            xG = (
                npxG
            ) = xA = npxG_a = xGp90 = xAp90 = xG_xAp90 = npxGp90 = npxG_ap90 = None

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
            "90s": minutes_90,
            "goals": goals,
            "assists": assists,
            "npg": npg,
            "pk": pk,
            "pk_attempted": pk_attempted,
            "card_yellow": card_yellow,
            "card_red": card_red,
            "goals_p90": goalp90,
            "assists_p90": assistsp90,
            "goals+assists_p90": g_ap90,
            "npg_p90": npgp90,
            "npg+assists_p90": npg_ap90,
            "xG": xG,
            "npxG": npxG,
            "xA": xA,
            "npxG+xA": npxG_a,
            "xG_p90": xGp90,
            "xA_p90": xAp90,
            "xG+xA_p90": xG_xAp90,
            "npxG_p90": npxGp90,
            "npxG+xA_p90": npxG_ap90,
            "npxG+xA": npxG_a,
            "match_logs": match_logs,
        }

        # add to empty list
        mylist.append(mydict)

    return mylist
