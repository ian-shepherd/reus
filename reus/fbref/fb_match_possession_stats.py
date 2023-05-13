from .fb_match_metadata import fb_match_metadata
from ..util import get_page_soup


def fb_match_possession_stats(pageSoup=None, url: str = None) -> tuple:
    """Extracts possession statistics for each player in a given match that includes advanced data

    Args:
        pageSoup (bs4, optional): bs4 object of a match. Defaults to None.
        url (str, optional): path of fbref match page. Defaults to None.

    Returns:
        tuple: possession stats for home and away team players
            list: possession stats of home team players
            list: possession stats of away team players
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
        id_ = "stats_" + team_id + "_possession"

        # find possession object
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

            # touches
            touches = row.find("td", {"data-stat": "touches"}).text
            touches_def_pen_area = row.find(
                "td", {"data-stat": "touches_def_pen_area"}
            ).text
            touches_def_3rd = row.find("td", {"data-stat": "touches_def_3rd"}).text
            touches_mid_3rd = row.find("td", {"data-stat": "touches_mid_3rd"}).text
            touches_att_3rd = row.find("td", {"data-stat": "touches_att_3rd"}).text
            touches_att_pen_area = row.find(
                "td", {"data-stat": "touches_att_pen_area"}
            ).text
            touches_live = row.find("td", {"data-stat": "touches_live_ball"}).text

            # take ons
            dribble_attempt = row.find("td", {"data-stat": "take_ons"}).text
            dribble_success = row.find("td", {"data-stat": "take_ons_won"}).text
            dribble_success_pct = row.find("td", {"data-stat": "take_ons_won_pct"}).text
            if dribble_success_pct == "":
                dribble_success_pct = None
            dribble_tackled = row.find("td", {"data-stat": "take_ons_tackled"}).text
            dribble_tackled_pct = row.find(
                "td", {"data-stat": "take_ons_tackled_pct"}
            ).text

            # carries
            carries = row.find("td", {"data-stat": "carries"}).text
            carries_total_distance = row.find(
                "td", {"data-stat": "carries_distance"}
            ).text
            carries_progressive_distance = row.find(
                "td", {"data-stat": "carries_progressive_distance"}
            ).text
            progressive_carries = row.find(
                "td", {"data-stat": "progressive_carries"}
            ).text
            carries_into_final_third = row.find(
                "td", {"data-stat": "carries_into_final_third"}
            ).text
            carries_into_penalty_area = row.find(
                "td", {"data-stat": "carries_into_penalty_area"}
            ).text
            miscontrols = row.find("td", {"data-stat": "miscontrols"}).text
            dispossessed = row.find("td", {"data-stat": "dispossessed"}).text

            # receiving
            passes_received = row.find("td", {"data-stat": "passes_received"}).text
            progressive_passes_received = row.find(
                "td", {"data-stat": "progressive_passes_received"}
            ).text

            # generate dictionary for player
            mydict = {
                "player_id": player_id,
                "name": name,
                "nation": nation,
                "position": position,
                "age": age,
                "minutes": minutes,
                "touches": touches,
                "touches_def_pen_area": touches_def_pen_area,
                "touches_def_3rd": touches_def_3rd,
                "touches_mid_3rd": touches_mid_3rd,
                "touches_att_3rd": touches_att_3rd,
                "touches_att_pen_area": touches_att_pen_area,
                "touches_live": touches_live,
                "dribble_attempt": dribble_attempt,
                "dribble_success": dribble_success,
                "dribble_success_pct": dribble_success_pct,
                "dribble_tackled": dribble_tackled,
                "dribble_tackled_pct": dribble_tackled_pct,
                "carries": carries,
                "carry_total_distance": carries_total_distance,
                "carry_progressive_distance": carries_progressive_distance,
                "progressive_carries": progressive_carries,
                "carries_into_final_third": carries_into_final_third,
                "carries_into_penalty_area": carries_into_penalty_area,
                "miscontrols": miscontrols,
                "dispossessed": dispossessed,
                "passes_received": passes_received,
                "progressive_passes_received": progressive_passes_received,
            }

            # add to team list
            mylist.append(mydict)

        # assign list to appropriate team
        if team_id == id_x:
            player_possession_x = mylist.copy()
        else:
            player_possession_y = mylist.copy()

    return player_possession_x, player_possession_y
