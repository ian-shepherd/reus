from .fb_match_metadata import fb_match_metadata
from ..util import get_page_soup


def fb_match_passing_type_stats(pageSoup=None, url: str = None):
    """Extracts passing type statistics for each player in a given match that includes StatsBomb data

    Args:
        pageSoup (bs4, optional): bs4 object of a match. Defaults to None.
        url (str, optional): path of fbref match page. Defaults to None.

    Returns:
        tuple: passing stats for home and away team players
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

        # find passing types object
        stats_players = pageSoup.find("table", {"id": id_})
        stats_players = stats_players.find_all("tr")

        # iterate through each player and store metrics
        for row in stats_players[2:-1]:
            th = row.find("th")
            player_id = th.find("a", href=True)["href"].split("/")[3]

            att = row.find("td", {"data-stat": "passes"}).text
            live = row.find("td", {"data-stat": "passes_live"}).text
            dead = row.find("td", {"data-stat": "passes_dead"}).text
            fk = row.find("td", {"data-stat": "passes_free_kicks"}).text
            tb = row.find("td", {"data-stat": "through_balls"}).text
            press = row.find("td", {"data-stat": "passes_pressure"}).text
            sw = row.find("td", {"data-stat": "passes_switches"}).text
            crs = row.find("td", {"data-stat": "crosses"}).text
            ck = row.find("td", {"data-stat": "corner_kicks"}).text
            ck_in = row.find("td", {"data-stat": "corner_kicks_in"}).text
            ck_out = row.find("td", {"data-stat": "corner_kicks_out"}).text
            ck_straight = row.find("td", {"data-stat": "corner_kicks_straight"}).text
            height_ground = row.find("td", {"data-stat": "passes_ground"}).text
            height_low = row.find("td", {"data-stat": "passes_low"}).text
            height_high = row.find("td", {"data-stat": "passes_high"}).text
            body_left = row.find("td", {"data-stat": "passes_left_foot"}).text
            body_right = row.find("td", {"data-stat": "passes_right_foot"}).text
            body_head = row.find("td", {"data-stat": "passes_head"}).text
            body_ti = row.find("td", {"data-stat": "throw_ins"}).text
            body_other = row.find("td", {"data-stat": "passes_other_body"}).text
            out_cmp = row.find("td", {"data-stat": "passes_completed"}).text
            out_off = row.find("td", {"data-stat": "passes_offsides"}).text
            out_out = row.find("td", {"data-stat": "passes_oob"}).text
            out_int = row.find("td", {"data-stat": "passes_intercepted"}).text
            out_blk = row.find("td", {"data-stat": "passes_blocked"}).text

            # generate dictionary for team
            mydict = {
                "player_id": player_id,
                "attempted": att,
                "live": live,
                "dead": dead,
                "free_kick": fk,
                "through_balls": tb,
                "under_pressure": press,
                "switches": sw,
                "crosses": crs,
                "corner_kicks": ck,
                "corner_inswing": ck_in,
                "corner_outswing": ck_out,
                "corner_straight": ck_straight,
                "height_ground": height_ground,
                "height_low": height_low,
                "height_high": height_high,
                "body_left": body_left,
                "body_right": body_right,
                "body_head": body_head,
                "body_throw_in": body_ti,
                "body_other": body_other,
                "completed": out_cmp,
                "offsides": out_off,
                "out_of_bounds": out_out,
                "intercepted": out_int,
                "blocked": out_blk,
            }

            # add to empty list
            mylist.append(mydict)

        # assign list to appropriate team
        if team_id == id_x:
            players_passing_stats_x = mylist.copy()
        else:
            players_passing_stats_y = mylist.copy()

    return players_passing_stats_x, players_passing_stats_y
