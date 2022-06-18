from ..util import get_page_soup


def fb_team_player_passing_type_stats(pageSoup=None, url: str = None):
    """Extracts passing type stats for each player in a given team

    Args:
        pageSoup (bs4, optional): bs4 object of a team. Defaults to None.
        url (str, optional): path of fbref team page. Defaults to None.

    Returns:
        list: passing type stats for each player
    """

    assert (
        pageSoup is not None or url is not None
    ), "Either pageSoup or url must be provided"

    if pageSoup is None:
        pageSoup = get_page_soup(url)

    # Find table object
    div = pageSoup.find("div", {"id": "all_stats_passing_types"})
    if div is None:
        return None

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
        minutes_90 = row.find("td", {"data-stat": "minutes_90s"}).text

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
            "90s": minutes_90,
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
            "match_logs": match_logs,
        }

        # add to empty list
        mylist.append(mydict)

    return mylist
