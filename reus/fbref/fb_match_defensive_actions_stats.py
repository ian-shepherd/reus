from .fb_match_metadata import fb_match_metadata
from ..util import get_page_soup


def fb_match_defensive_actions_stats(pageSoup=None, url: str = None) -> tuple:
    """Extracts defensive action stats for each player in a given match that includes advanced data

    Args:
        pageSoup (bs4, optional): bs4 object of a match. Defaults to None.
        url (str, optional): path of fbref match page. Defaults to None.

    Returns:
        tuple: defensive stats for home and away team
            list: defensive stats for home team players
            list: defensive stats for away team players
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
        id_ = "stats_" + team_id + "_defense"

        # find defensive action object
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

            # tackles
            tackles_attempted = row.find("td", {"data-stat": "tackles"}).text
            tackles_successful = row.find("td", {"data-stat": "tackles_won"}).text
            tackles_defensive_third = row.find(
                "td", {"data-stat": "tackles_def_3rd"}
            ).text
            tackles_middle_third = row.find("td", {"data-stat": "tackles_mid_3rd"}).text
            tackles_attacking_third = row.find(
                "td", {"data-stat": "tackles_att_3rd"}
            ).text

            # challenges
            challenges_successful = row.find(
                "td", {"data-stat": "challenge_tackles"}
            ).text
            challenges_attempted = row.find("td", {"data-stat": "challenges"}).text
            challenge_success_rate = row.find(
                "td", {"data-stat": "challenge_tackles_pct"}
            ).text
            if challenge_success_rate == "":
                challenge_success_rate = None
            challenges_lost = row.find("td", {"data-stat": "challenges_lost"}).text

            # blocks
            blocks = row.find("td", {"data-stat": "blocks"}).text
            blocked_shots = row.find("td", {"data-stat": "blocked_shots"}).text
            blocked_passes = row.find("td", {"data-stat": "blocked_passes"}).text

            # other
            interceptions = row.find("td", {"data-stat": "interceptions"}).text
            tkl_int = row.find("td", {"data-stat": "tackles_interceptions"}).text
            clearances = row.find("td", {"data-stat": "clearances"}).text
            errors = row.find("td", {"data-stat": "errors"}).text

            # generate dictionary for player
            mydict = {
                "player_id": player_id,
                "name": name,
                "nation": nation,
                "position": position,
                "age": age,
                "minutes": minutes,
                "tackles_attempted": tackles_attempted,
                "tackles_successful": tackles_successful,
                "tackles_defensive_third": tackles_defensive_third,
                "tackles_middle_third": tackles_middle_third,
                "tackles_attacking_third": tackles_attacking_third,
                "challenges_successful": challenges_successful,
                "challenges_attempted": challenges_attempted,
                "challenge_success_rate": challenge_success_rate,
                "challenges_lost": challenges_lost,
                "blocks": blocks,
                "blocked_shots": blocked_shots,
                "blocked_passes": blocked_passes,
                "interceptions": interceptions,
                "tkl_int": tkl_int,
                "clearances": clearances,
                "errors": errors,
            }

            # add to team list
            mylist.append(mydict)

        # assign list to appropriate team
        if team_id == id_x:
            player_defensive_actions_stats_x = mylist.copy()
        else:
            player_defensive_actions_stats_y = mylist.copy()

    return player_defensive_actions_stats_x, player_defensive_actions_stats_y
