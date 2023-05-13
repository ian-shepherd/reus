from ..util import get_page_soup


def fb_team_player_misc_stats(pageSoup=None, url: str = None) -> list:
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

        # performance
        cards_yellow = row.find("td", {"data-stat": "cards_yellow"}).text
        cards_red = row.find("td", {"data-stat": "cards_red"}).text
        cards_yellow_red = row.find("td", {"data-stat": "cards_yellow_red"}).text
        fouls = row.find("td", {"data-stat": "fouls"}).text
        fouled = row.find("td", {"data-stat": "fouled"}).text
        offsides = row.find("td", {"data-stat": "offsides"}).text
        crosses = row.find("td", {"data-stat": "crosses"}).text
        interceptions = row.find("td", {"data-stat": "interceptions"}).text
        tackles_won = row.find("td", {"data-stat": "tackles_won"}).text
        penalties_won = row.find("td", {"data-stat": "pens_won"}).text
        penalties_conceded = row.find("td", {"data-stat": "pens_conceded"}).text
        own_goals = row.find("td", {"data-stat": "own_goals"}).text
        recoveries = row.find("td", {"data-stat": "ball_recoveries"}).text

        # aerial duels
        aerials_won = row.find("td", {"data-stat": "aerials_won"}).text
        aerials_lost = row.find("td", {"data-stat": "aerials_lost"}).text
        aerials_won_pct = row.find("td", {"data-stat": "aerials_won_pct"}).text
        if aerials_won_pct == "":
            aerials_won_pct = None

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
            "cards_yellow": cards_yellow,
            "cards_red": cards_red,
            "cards_yellow_red": cards_yellow_red,
            "fouls": fouls,
            "fouled": fouled,
            "offsides": offsides,
            "crosses": crosses,
            "interceptions": interceptions,
            "tackles_won": tackles_won,
            "pk_won": penalties_won,
            "pk_con": penalties_conceded,
            "own_goals": own_goals,
            "recoveries": recoveries,
            "aerials_won": aerials_won,
            "aerials_lost": aerials_lost,
            "aerials_won_pct": aerials_won_pct,
            "match_logs": match_logs,
        }

        # add to empty list
        mylist.append(mydict)

    return mylist
