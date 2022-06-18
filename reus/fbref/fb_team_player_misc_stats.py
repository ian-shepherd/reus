from ..util import get_page_soup


def fb_team_player_misc_stats(pageSoup=None, url: str = None):
    """Extracts miscellaneous stats for rach player in a given team

    Args:
        pageSoup (bs4, optional): bs4 object of a team. Defaults to None.
        url (str, optional): path of fbref team page. Defaults to None.

    Returns:
        list: miscellaneous stats for each player
    """

    assert (
        pageSoup is not None or url is not None
    ), "Either pageSoup or url must be provided"

    if pageSoup is None:
        pageSoup = get_page_soup(url)

    # Find table object
    div = pageSoup.find("div", {"id": "all_stats_misc"})
    if div is None:
        return None

    table = div.find("table")
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

        crdY = row.find("td", {"data-stat": "cards_yellow"}).text
        crdR = row.find("td", {"data-stat": "cards_red"}).text
        crdY2 = row.find("td", {"data-stat": "cards_yellow_red"}).text
        fls = row.find("td", {"data-stat": "fouls"}).text
        fld = row.find("td", {"data-stat": "fouled"}).text
        off = row.find("td", {"data-stat": "offsides"}).text
        crs = row.find("td", {"data-stat": "crosses"}).text
        interceptions = row.find("td", {"data-stat": "interceptions"}).text
        tklW = row.find("td", {"data-stat": "tackles_won"}).text
        pk_won = row.find("td", {"data-stat": "pens_won"}).text
        pk_con = row.find("td", {"data-stat": "pens_conceded"}).text
        og = row.find("td", {"data-stat": "own_goals"}).text
        try:
            recov = row.find("td", {"data-stat": "ball_recoveries"}).text
            aerial_won = row.find("td", {"data-stat": "aerials_won"}).text
            aerial_lost = row.find("td", {"data-stat": "aerials_lost"}).text
            aerial_pct = row.find("td", {"data-stat": "aerials_won_pct"}).text
        except AttributeError:
            recov = aerial_won = aerial_lost = aerial_pct = None

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
            "cards_yellow": crdY,
            "cards_red": crdR,
            "cards_second_yellow": crdY2,
            "fouls": fls,
            "fouled": fld,
            "offsides": off,
            "crosses": crs,
            "interceptions": interceptions,
            "tackles_won": tklW,
            "pk_won": pk_won,
            "pk_con": pk_con,
            "own_goals": og,
            "recoveries": recov,
            "aerials_won": aerial_won,
            "aerials_lost": aerial_lost,
            "aerials_pct": aerial_pct,
            "match_logs": match_logs,
        }

        # add to empty list
        mylist.append(mydict)

    return mylist
