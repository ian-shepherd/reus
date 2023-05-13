from ..util import get_page_soup


def fb_team_player_summary_stats(pageSoup=None, url: str = None) -> list:
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
        except ValueError:
            age = None
        minutes = row.find("td", {"data-stat": "minutes"}).text
        minutes_90 = row.find("td", {"data-stat": "minutes_90s"}).text

        # performance
        goals = row.find("td", {"data-stat": "goals"}).text
        assists = row.find("td", {"data-stat": "assists"}).text
        g_a = row.find("td", {"data-stat": "goals_assists"}).text
        npg = row.find("td", {"data-stat": "goals_pens"}).text
        pk = row.find("td", {"data-stat": "pens_made"}).text
        pk_attempted = row.find("td", {"data-stat": "pens_att"}).text
        card_yellow = row.find("td", {"data-stat": "cards_yellow"}).text
        card_red = row.find("td", {"data-stat": "cards_red"}).text

        # expected
        try:
            xG = row.find("td", {"data-stat": "xg"}).text
            npxG = row.find("td", {"data-stat": "npxg"}).text
            xAG = row.find("td", {"data-stat": "xg_assist"}).text
            npxg_xga = row.find("td", {"data-stat": "npxg_xg_assist"}).text
        except AttributeError:
            xG = npxG = xAG = npxg_xga

        # progression
        progressive_carries = row.find("td", {"data-stat": "progressive_carries"}).text
        progressive_passes = row.find("td", {"data-stat": "progressive_passes"}).text
        progressive_passes_received = row.find(
            "td", {"data-stat": "progressive_passes_received"}
        ).text

        # performance per 90 minutes
        goalp90 = row.find("td", {"data-stat": "goals_per90"}).text
        assistsp90 = row.find("td", {"data-stat": "assists_per90"}).text
        g_ap90 = row.find("td", {"data-stat": "goals_assists_per90"}).text
        npgp90 = row.find("td", {"data-stat": "goals_pens_per90"}).text
        npg_ap90 = row.find("td", {"data-stat": "goals_assists_pens_per90"}).text

        # expected per 90 minutes
        try:
            xGp90 = row.find("td", {"data-stat": "xg_per90"}).text
            xAGp90 = row.find("td", {"data-stat": "xg_assist_per90"}).text
            xG_xAGp90 = row.find("td", {"data-stat": "xg_xg_assist_per90"}).text
            npxGp90 = row.find("td", {"data-stat": "npxg_per90"}).text
            npxG_xAGp90 = row.find("td", {"data-stat": "npxg_xg_assist_per90"}).text
        except AttributeError:
            xGp90 = xAGp90 = xG_xAGp90 = npxGp90 = npxG_xAGp90 = None

        # match logs
        try:
            match_logs = row.find("td", {"data-stat": "matches"}).find("a", href=True)[
                "href"
            ]
        except TypeError:
            match_logs = None

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
            "goals+assists": g_a,
            "npg": npg,
            "pk": pk,
            "pk_attempted": pk_attempted,
            "card_yellow": card_yellow,
            "card_red": card_red,
            "xG": xG,
            "npxG": npxG,
            "xAG": xAG,
            "npxG+xA": npxg_xga,
            "progressive_carries": progressive_carries,
            "progressive_passes": progressive_passes,
            "progressive_passes_received": progressive_passes_received,
            "goals_p90": goalp90,
            "assists_p90": assistsp90,
            "goals+assists_p90": g_ap90,
            "npg_p90": npgp90,
            "npg+assists_p90": npg_ap90,
            "xG_p90": xGp90,
            "xAG_p90": xAGp90,
            "xG+xAGp90": xG_xAGp90,
            "npxG_p90": npxGp90,
            "npxG+xAG_p90": npxG_xAGp90,
            "match_logs": match_logs,
        }

        # add to empty list
        mylist.append(mydict)

    return mylist
