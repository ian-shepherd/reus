from .fb_match_metadata import fb_match_metadata
from ..util import get_page_soup


def fb_match_misc_stats(pageSoup=None, url: str = None) -> tuple:
    """Extracts miscellaneous stats for each player in a given match that includes advanced data

    Args:
        pageSoup (bs4, optional): bs4 object of a match. Defaults to None.
        url (str, optional): path of fbref match page. Defaults to None.

    Returns:
        tuple: miscellaneous stats for home and away team players
            list: miscellaneous stats of home team players
            list: miscellaneous stats of away team players
    """

    assert (
        pageSoup is not None or url is not None
    ), "Either pageSoup or url must be provided"

    if pageSoup is None:
        pageSoup = get_page_soup(url)

    # Get team ids
    metadata = fb_match_metadata(pageSoup)[0]
    id_x = metadata.get("id_x")
    id_y = metadata.get("id_y")

    # Loop through both teams
    for team_id in [id_x, id_y]:
        # generate empty list for each team
        mylist = []
        # generate html id
        id_ = "stats_" + team_id + "_misc"

        # find miscellaneous stats object
        stats_players = pageSoup.find("table", {"id": id_})
        stats_players = stats_players.find_all("tr")

        # iterate through each player and store metrics
        for row in stats_players[2:-1]:
            th = row.find("th")

            # general
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

            # generate dictionary for team
            mydict = {
                "player_id": player_id,
                "name": name,
                "nation": nation,
                "position": position,
                "age": age,
                "minutes": minutes,
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
            }

            # add to empty list
            mylist.append(mydict)

        # assign list to appropriate team
        if team_id == id_x:
            players_misc_stats_x = mylist.copy()
        else:
            players_misc_stats_y = mylist.copy()

    return players_misc_stats_x, players_misc_stats_y
