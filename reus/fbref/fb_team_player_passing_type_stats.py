from ..util import get_page_soup


def fb_team_player_passing_type_stats(pageSoup=None, url: str = None) -> list:
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
        minutes_90 = row.find("td", {"data-stat": "minutes_90s"}).text
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
            "90s": minutes_90,
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
            "match_logs": match_logs,
        }

        # add to empty list
        mylist.append(mydict)

    return mylist
