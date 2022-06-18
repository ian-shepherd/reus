from .fb_match_metadata import fb_match_metadata
from ..util import get_page_soup


def fb_match_summary_stats(pageSoup=None, url: str = None):
    """Extracts summary statistics for each player in a given match that includes StatsBomb data

    Args:
        pageSoup (bs4, optional): bs4 object of a match. Defaults to None.
        url (str, optional): path of fbref match page. Defaults to None.

    Returns:
        tuple: summary stats for home and away team players
            list: summary stats of home team players
            list: summary stats of away team players
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
        id_ = "stats_" + team_id + "_summary"

        # find summary object
        stats_players = pageSoup.find("table", {"id": id_})
        stats_players = stats_players.find_all("tr")

        # iterate through each player and store metrics
        for row in stats_players[2:-1]:
            th = row.find("th")
            name = th["csk"]
            player_id = th.find("a", href=True)["href"].split("/")[3]

            shirtnumber = row.find("td", {"data-stat": "shirtnumber"}).text
            nation = row.find("td", {"data-stat": "nationality"}).text
            position = row.find("td", {"data-stat": "position"}).text
            age = row.find("td", {"data-stat": "age"}).text.split("-")
            age = int(age[0]) + int(age[1]) / 365
            minutes = row.find("td", {"data-stat": "minutes"}).text
            goals = row.find("td", {"data-stat": "goals"}).text
            assists = row.find("td", {"data-stat": "assists"}).text
            pk = row.find("td", {"data-stat": "pens_made"}).text
            pk_attempted = row.find("td", {"data-stat": "pens_att"}).text
            shots = row.find("td", {"data-stat": "shots_total"}).text
            shots_on_target = row.find("td", {"data-stat": "shots_on_target"}).text
            card_yellow = row.find("td", {"data-stat": "cards_yellow"}).text
            card_red = row.find("td", {"data-stat": "cards_red"}).text
            touches = row.find("td", {"data-stat": "touches"}).text
            pressures = row.find("td", {"data-stat": "pressures"}).text
            tackles = row.find("td", {"data-stat": "tackles"}).text
            interceptions = row.find("td", {"data-stat": "interceptions"}).text
            blocks = row.find("td", {"data-stat": "blocks"}).text
            xG = row.find("td", {"data-stat": "xg"}).text
            npxG = row.find("td", {"data-stat": "npxg"}).text
            xA = row.find("td", {"data-stat": "xa"}).text
            shot_creating_actions = row.find("td", {"data-stat": "sca"}).text
            goal_creating_actions = row.find("td", {"data-stat": "gca"}).text
            passes_completed = row.find("td", {"data-stat": "passes_completed"}).text
            passes_attempted = row.find("td", {"data-stat": "passes"}).text
            pass_accuracy = row.find("td", {"data-stat": "passes_pct"}).text
            pass_progressive_distance = row.find(
                "td", {"data-stat": "progressive_passes"}
            ).text
            carries = row.find("td", {"data-stat": "carries"}).text
            dribble_progressive_distance = row.find(
                "td", {"data-stat": "progressive_carries"}
            ).text
            dribble_success = row.find("td", {"data-stat": "dribbles_completed"}).text
            dribble_attempt = row.find("td", {"data-stat": "dribbles"}).text

            # generate dictionary for team
            mydict = {
                "player_id": player_id,
                "name": name,
                "shirtnumber": shirtnumber,
                "nation": nation,
                "position": position,
                "age": age,
                "minutes": minutes,
                "goals": goals,
                "assists": assists,
                "pk": pk,
                "pk_attempted": pk_attempted,
                "shots": shots,
                "shots_on_target": shots_on_target,
                "card_yellow": card_yellow,
                "card_red": card_red,
                "touches": touches,
                "pressures": pressures,
                "tackles": tackles,
                "interceptions": interceptions,
                "blocks": blocks,
                "xG": xG,
                "npxG": npxG,
                "xA": xA,
                "shot_creating_actions": shot_creating_actions,
                "goal_creating_actions": goal_creating_actions,
                "passes_completed": passes_completed,
                "passes_attempted": passes_attempted,
                "passes_accuracy": pass_accuracy,
                "pass_progressive_distance": pass_progressive_distance,
                "carries": carries,
                "dribble_progressive_distance": dribble_progressive_distance,
                "dribble_success": dribble_success,
                "dribble_attempt": dribble_attempt,
            }

            # add to empty list
            mylist.append(mydict)

        # assign list to appropriate team
        if team_id == id_x:
            players_summary_stats_x = mylist.copy()
        else:
            players_summary_stats_y = mylist.copy()

    return players_summary_stats_x, players_summary_stats_y
