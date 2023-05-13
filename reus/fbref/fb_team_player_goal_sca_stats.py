from ..util import get_page_soup


def fb_team_player_goal_sca_stats(pageSoup=None, url: str = None) -> list:
    """Extracts shot and goal creating actions for each player in a given team

    Args:
        pageSoup (bs4, optional): bs4 object of a team. Defaults to None.
        url (str, optional): path of fbref team page. Defaults to None.

    Returns:
        list: shot and goal creating actions for each player
    """

    assert (
        pageSoup is not None or url is not None
    ), "Either pageSoup or url must be provided"

    if pageSoup is None:
        pageSoup = get_page_soup(url)

    # Find table object
    div = pageSoup.find("div", {"id": "all_stats_gca"})
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

        # sca
        shot_creating_actions = row.find("td", {"data-stat": "sca"}).text
        shot_creating_actions_p90 = row.find("td", {"data-stat": "sca_per90"}).text

        # sca types
        sca_pass_live = row.find("td", {"data-stat": "sca_passes_live"}).text
        sca_pass_dead = row.find("td", {"data-stat": "sca_passes_dead"}).text
        sca_take_on = row.find("td", {"data-stat": "sca_take_ons"}).text
        sca_shot = row.find("td", {"data-stat": "sca_shots"}).text
        sca_foul = row.find("td", {"data-stat": "sca_fouled"}).text
        sca_defense = row.find("td", {"data-stat": "sca_defense"}).text

        # gca
        goal_creating_actions = row.find("td", {"data-stat": "gca"}).text
        goal_creating_actions_p90 = row.find("td", {"data-stat": "gca_per90"}).text

        # gca types
        gca_pass_live = row.find("td", {"data-stat": "gca_passes_live"}).text
        gca_pass_dead = row.find("td", {"data-stat": "gca_passes_dead"}).text
        gca_take_on = row.find("td", {"data-stat": "gca_take_ons"}).text
        gca_shot = row.find("td", {"data-stat": "gca_shots"}).text
        gca_foul = row.find("td", {"data-stat": "gca_fouled"}).text
        gca_defense = row.find("td", {"data-stat": "gca_defense"}).text

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
            "shot_creating_actions": shot_creating_actions,
            "shot_creating_actions_p90": shot_creating_actions_p90,
            "sca_pass_live": sca_pass_live,
            "sca_pass_dead": sca_pass_dead,
            "sca_take_on": sca_take_on,
            "sca_shot": sca_shot,
            "sca_foul": sca_foul,
            "sca_defensive_action": sca_defense,
            "goal_creating_actions": goal_creating_actions,
            "goal_creating_actions_p90": goal_creating_actions_p90,
            "gca_pass_live": gca_pass_live,
            "gca_pass_dead": gca_pass_dead,
            "gca_take_on": gca_take_on,
            "gca_shot": gca_shot,
            "gca_foul": gca_foul,
            "gca_defensive_action": gca_defense,
            "match_logs": match_logs,
        }

        # add to empty list
        mylist.append(mydict)

    return mylist
