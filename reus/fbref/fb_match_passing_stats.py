from .fb_match_metadata import fb_match_metadata
from ..util import get_page_soup


def fb_match_passing_stats(pageSoup=None, url: str = None) -> list:
    """Extracts passing stats for each player in a given match that includes advanced data

    Args:
        pageSoup (bs4, optional): bs4 object of a match. Defaults to None.
        url (str, optional): path of fbref match page. Defaults to None.

    Returns:
        tuple: passing stats for home and away team players
            list: passing stats of home team players
            list: passing stats of away team players
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
        id_ = "stats_" + team_id + "_passing"

        # find passing object
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

            # total
            passes_completed = row.find("td", {"data-stat": "passes_completed"}).text
            passes_attempted = row.find("td", {"data-stat": "passes"}).text
            pass_accuracy = row.find("td", {"data-stat": "passes_pct"}).text
            if pass_accuracy == "":
                pass_accuracy = None
            total_distance = row.find("td", {"data-stat": "passes_total_distance"}).text
            progressive_distance = row.find(
                "td", {"data-stat": "passes_progressive_distance"}
            ).text

            # short
            short_passes_completed = row.find(
                "td", {"data-stat": "passes_completed_short"}
            ).text
            short_passes_attempted = row.find("td", {"data-stat": "passes_short"}).text
            short_pass_accuracy = row.find("td", {"data-stat": "passes_pct_short"}).text
            if short_pass_accuracy == "":
                short_pass_accuracy = None

            # medium
            medium_passes_completed = row.find(
                "td", {"data-stat": "passes_completed_medium"}
            ).text
            medium_passes_attempted = row.find(
                "td", {"data-stat": "passes_medium"}
            ).text
            medium_pass_accuracy = row.find(
                "td", {"data-stat": "passes_pct_medium"}
            ).text
            if medium_pass_accuracy == "":
                medium_pass_accuracy = None

            # long
            long_passes_completed = row.find(
                "td", {"data-stat": "passes_completed_long"}
            ).text
            long_passes_attempted = row.find("td", {"data-stat": "passes_long"}).text
            long_pass_accuracy = row.find("td", {"data-stat": "passes_pct_long"}).text
            if long_pass_accuracy == "":
                long_pass_accuracy = None

            # other
            assists = row.find("td", {"data-stat": "assists"}).text
            xg_assist = row.find("td", {"data-stat": "xg_assist"}).text
            xA = row.find("td", {"data-stat": "pass_xa"}).text
            key_passes = row.find("td", {"data-stat": "assisted_shots"}).text
            passes_into_final_third = row.find(
                "td", {"data-stat": "passes_into_final_third"}
            ).text
            passes_into_penalty_area = row.find(
                "td", {"data-stat": "passes_into_penalty_area"}
            ).text
            crosses_into_penalty_area = row.find(
                "td", {"data-stat": "crosses_into_penalty_area"}
            ).text
            progressive_passes = row.find(
                "td", {"data-stat": "progressive_passes"}
            ).text

            # generate dictionary for player
            mydict = {
                "player_id": player_id,
                "name": name,
                "nation": nation,
                "position": position,
                "age": age,
                "passes_completed": passes_completed,
                "passes_attempted": passes_attempted,
                "pass_accuracy": pass_accuracy,
                "total_distance": total_distance,
                "progressive_distance": progressive_distance,
                "short_passes_completed": short_passes_completed,
                "short_passes_attempted": short_passes_attempted,
                "short_pass_accuracy": short_pass_accuracy,
                "medium_passes_completed": medium_passes_completed,
                "medium_passes_attempted": medium_passes_attempted,
                "medium_pass_accuracy": medium_pass_accuracy,
                "long_passes_completed": long_passes_completed,
                "long_passes_attempted": long_passes_attempted,
                "long_pass_accuracy": long_pass_accuracy,
                "assists": assists,
                "xg_assist": xg_assist,
                "xA": xA,
                "key_passes": key_passes,
                "passes_into_final_third": passes_into_final_third,
                "passes_into_penalty_area": passes_into_penalty_area,
                "crosses_into_penalty_area": crosses_into_penalty_area,
                "progressive_passes": progressive_passes,
            }

            # add to team list
            mylist.append(mydict)

        # assign list to appropriate team
        if team_id == id_x:
            players_passing_stats_x = mylist.copy()
        else:
            players_passing_stats_y = mylist.copy()

    return players_passing_stats_x, players_passing_stats_y
