from ..util import get_page_soup


def fb_team_passing_type_stats(pageSoup=None, url: str = None) -> list:
    """Extracts passing type stats for each team in a given league

    Args:
        pageSoup (bs4, optional): bs4 object of a team. Defaults to None.
        url (str, optional): path of fbref team page. Defaults to None.

    Returns:
        tuple: passing type stats for home and away team players
            list: passing type stats for each team
            list: passing type stats against each team
    """

    assert (
        pageSoup is not None or url is not None
    ), "Either pageSoup or url must be provided"

    if pageSoup is None:
        pageSoup = get_page_soup(url)

    for side in ["for", "against"]:
        # generate empty list for each team
        mylist = []
        # generate html id
        id_ = "stats_squads_passing_types_" + side

        # find goalkeeping object
        stats = pageSoup.find("table", {"id": id_})
        stats = stats.find_all("tr")

        # iteratre through each team and store metrics
        for row in stats[2:]:
            th = row.find("th")
            # general
            team = th.find("a", {"href": True}).text.strip()
            team_id = th.find("a", {"href": True})["href"].split("/")[3]
            num_players = row.find("td", {"data-stat": "players_used"}).text
            matches = row.find("td", {"data-stat": "minutes_90s"}).text
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

            # generate dictionary for team
            mydict = {
                "team_id": team_id,
                "team": team,
                "num_players": num_players,
                "matches": matches,
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

            # add to empty list
            mylist.append(mydict)

        # assign list to appropriate team
        if side == "for":
            passing_type_stats_for = mylist.copy()
        else:
            passing_type_stats_against = mylist.copy()

    return passing_type_stats_for, passing_type_stats_against
