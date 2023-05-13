from .fb_match_metadata import fb_match_metadata
from ..util import get_page_soup


def fb_match_passing_type_stats(pageSoup=None, url: str = None) -> list:
    """Extracts passing type stats for each player in a given match that includes advanced data

    Args:
        pageSoup (bs4, optional): bs4 object of a match. Defaults to None.
        url (str, optional): path of fbref match page. Defaults to None.

    Returns:
        tuple: passing type stats for home and away team players
            list: passing type stats of home team players
            list: passing type stats of away team players
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
        id_ = "stats_" + team_id + "_passing_types"

        # find passing type object
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
            passes_attempted = row.find("td", {"data-stat": "passes"}).text

            # pass types
            live = row.find("td", {"data-stat": "passes_live"}).text
            dead = row.find("td", {"data-stat": "passes_dead"}).text
            free_kicks = row.find("td", {"data-stat": "passes_free_kicks"}).text
            through_balls = row.find("td", {"data-stat": "through_balls"}).text
            switches = row.find("td", {"data-stat": "passes_switches"}).text
            crosses = row.find("td", {"data-stat": "crosses"}).text
            throw_ins = row.find("td", {"data-stat": "throw_ins"}).text
            corner_kicks = row.find("td", {"data-stat": "corner_kicks"}).text

            # corner kicks
            ck_in = row.find("td", {"data-stat": "corner_kicks_in"}).text
            ck_out = row.find("td", {"data-stat": "corner_kicks_out"}).text
            ck_straight = row.find("td", {"data-stat": "corner_kicks_straight"}).text

            # outcomes
            completed = row.find("td", {"data-stat": "passes_completed"}).text
            offsides = row.find("td", {"data-stat": "passes_offsides"}).text
            blocked = row.find("td", {"data-stat": "passes_blocked"}).text

            # generate dictionary for player
            mydict = {
                "player_id": player_id,
                "name": name,
                "nation": nation,
                "position": position,
                "age": age,
                "minutes": minutes,
                "passes_attempted": passes_attempted,
                "live": live,
                "dead": dead,
                "free_kicks": free_kicks,
                "through_balls": through_balls,
                "switches": switches,
                "crosses": crosses,
                "throw_ins": throw_ins,
                "corner_kicks": corner_kicks,
                "ck_in": ck_in,
                "ck_out": ck_out,
                "ck_straight": ck_straight,
                "completed": completed,
                "offsides": offsides,
                "blocked": blocked,
            }

            # add to team list
            mylist.append(mydict)

        # assign list to appropriate team
        if team_id == id_x:
            player_passing_type_stats_x = mylist.copy()
        else:
            player_passing_type_stats_y = mylist.copy()

    return player_passing_type_stats_x, player_passing_type_stats_y
