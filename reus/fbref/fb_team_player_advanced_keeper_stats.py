from ..util import get_page_soup


def fb_team_player_advanced_keeper_stats(pageSoup=None, url: str = None) -> list:
    """Extracts advanced keeper stats for each player in a given team

    Args:
        pageSoup (bs4, optional): bs4 object of a team. Defaults to None.
        url (str, optional): path of fbref team page. Defaults to None.

    Returns:
        list: goalkeeper stats for each player
    """

    assert (
        pageSoup is not None or url is not None
    ), "Either pageSoup or url must be provided"

    if pageSoup is None:
        pageSoup = get_page_soup(url)

    # Find table object
    div = pageSoup.find("div", {"id": "all_stats_keeper_adv"})
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

        # goals
        goals_allowed = row.find("td", {"data-stat": "gk_goals_against"}).text
        pk_allowed = row.find("td", {"data-stat": "gk_pens_allowed"}).text
        fk_allowed = row.find("td", {"data-stat": "gk_free_kick_goals_against"}).text
        corner_allowed = row.find(
            "td", {"data-stat": "gk_corner_kick_goals_against"}
        ).text
        own_goals = row.find("td", {"data-stat": "gk_own_goals_against"}).text

        # expected
        psxg = row.find("td", {"data-stat": "gk_psxg"}).text
        psxg_per_sot = row.find(
            "td", {"data-stat": "gk_psnpxg_per_shot_on_target_against"}
        ).text
        psxg_g = row.find("td", {"data-stat": "gk_psxg_net"}).text
        psxg_g_p90 = row.find("td", {"data-stat": "gk_psxg_net_per90"}).text

        # launched
        launched_completed = row.find(
            "td", {"data-stat": "gk_passes_completed_launched"}
        ).text
        launched_attempted = row.find("td", {"data-stat": "gk_passes_launched"}).text
        launched_acc = row.find("td", {"data-stat": "gk_passes_pct_launched"}).text

        # passes
        passes_attempted = row.find("td", {"data-stat": "gk_passes"}).text
        throws_attempted = row.find("td", {"data-stat": "gk_passes_throws"}).text
        pct_lauched = row.find("td", {"data-stat": "gk_pct_passes_launched"}).text
        passes_avg_length = row.find("td", {"data-stat": "gk_passes_length_avg"}).text

        # goal kicks
        gk_attempted = row.find("td", {"data-stat": "gk_goal_kicks"}).text
        gk_pct_launched = row.find(
            "td", {"data-stat": "gk_pct_goal_kicks_launched"}
        ).text
        gk_avg_length = row.find("td", {"data-stat": "gk_goal_kick_length_avg"}).text

        # crosses
        crosses_faced = row.find("td", {"data-stat": "gk_crosses"}).text
        crosses_stopped = row.find("td", {"data-stat": "gk_crosses_stopped"}).text
        crosses_stopped_pct = row.find(
            "td", {"data-stat": "gk_crosses_stopped_pct"}
        ).text

        # sweeper
        defensive_actions = row.find(
            "td", {"data-stat": "gk_def_actions_outside_pen_area"}
        ).text
        defensive_actions_p90 = row.find(
            "td", {"data-stat": "gk_def_actions_outside_pen_area_per90"}
        ).text
        defensive_actions_avg_distance = row.find(
            "td", {"data-stat": "gk_avg_distance_def_actions"}
        ).text

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
            "goals_allowed": goals_allowed,
            "pk_allowed": pk_allowed,
            "fk_allowed": fk_allowed,
            "corner_allowed": corner_allowed,
            "own_goals": own_goals,
            "psxg": psxg,
            "psxg_per_shot_on_target": psxg_per_sot,
            "psxg_minus_ga": psxg_g,
            "psxg_minus_ga_p90": psxg_g_p90,
            "launched_completed": launched_completed,
            "launched_attempted": launched_attempted,
            "launched_accuracy": launched_acc,
            "passes_attempted": passes_attempted,
            "throws_attempted": throws_attempted,
            "pct_launched": pct_lauched,
            "passes_avg_length": passes_avg_length,
            "gk_attempted": gk_attempted,
            "gk_pct_launched": gk_pct_launched,
            "gk_avg_length": gk_avg_length,
            "crosses_faced": crosses_faced,
            "crosses_stopped": crosses_stopped,
            "crosses_stopped_pct": crosses_stopped_pct,
            "defensive_actions": defensive_actions,
            "defensive_actions_p90": defensive_actions_p90,
            "defensive_actions_avg_distance": defensive_actions_avg_distance,
            "match_logs": match_logs,
        }

        # add to empty list
        mylist.append(mydict)

    return mylist
