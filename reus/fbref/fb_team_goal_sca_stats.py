from ..util import get_page_soup


def fb_team_goal_sca_stats(pageSoup=None, url: str = None) -> list:
    """Extracts shot and goal creating actions stats for each team in a given league

    Args:
        pageSoup (bs4, optional): bs4 object of a team. Defaults to None.
        url (str, optional): path of fbref team page. Defaults to None.

    Returns:
        tuple: possession stats for home and away team players
            list: shot and goal creating stats for each team
            list: shot and goal creating stats against each team
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
        id_ = "stats_squads_gca_" + side

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

            # generate dictionary for team
            mydict = {
                "team_id": team_id,
                "team": team,
                "num_players": num_players,
                "matches": matches,
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
            }

            # add to empty list
            mylist.append(mydict)

        # assign list to appropriate team
        if side == "for":
            goal_sca_stats_for = mylist.copy()
        else:
            goal_sca_stats_against = mylist.copy()

    return goal_sca_stats_for, goal_sca_stats_against
