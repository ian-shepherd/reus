from ..util import get_page_soup


def fb_team_shooting_stats(pageSoup=None, url: str = None) -> list:
    """Extracts shooting stats for each team in a given league

    Args:
        pageSoup (bs4, optional): bs4 object of a team. Defaults to None.
        url (str, optional): path of fbref team page. Defaults to None.

    Returns:
        tuple: shooting stats for home and away team players
            list: shooting stats for each team
            list: shooting stats against each team
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
        id_ = "stats_squads_shooting_" + side

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

            # standard
            goals = row.find("td", {"data-stat": "goals"}).text
            shots = row.find("td", {"data-stat": "shots"}).text
            shots_on_target = row.find("td", {"data-stat": "shots_on_target"}).text
            shots_on_target_per = row.find(
                "td", {"data-stat": "shots_on_target_pct"}
            ).text
            shots_p90 = row.find("td", {"data-stat": "shots_per90"}).text
            shots_on_target_p90 = row.find(
                "td", {"data-stat": "shots_on_target_per90"}
            ).text
            goals_per_shot = row.find("td", {"data-stat": "goals_per_shot"}).text
            goals_per_sot = row.find(
                "td", {"data-stat": "goals_per_shot_on_target"}
            ).text
            try:
                dist = row.find("td", {"data-stat": "average_shot_distance"}).text
                fk = row.find("td", {"data-stat": "shots_free_kicks"}).text
            except AttributeError:
                dist = fk = None
            pk = row.find("td", {"data-stat": "pens_made"}).text
            pk_attempted = row.find("td", {"data-stat": "pens_att"}).text

            # expected
            try:
                xG = row.find("td", {"data-stat": "xg"}).text
                npxG = row.find("td", {"data-stat": "npxg"}).text
                npxG_per_shot = row.find("td", {"data-stat": "npxg_per_shot"}).text
                goals_xG = row.find("td", {"data-stat": "xg_net"}).text
                npg_xG = row.find("td", {"data-stat": "npxg_net"}).text
            except AttributeError:
                xG = npxG = npxG_per_shot = goals_xG = npg_xG = None

            # generate dictionary for team
            mydict = {
                "team_id": team_id,
                "team": team,
                "num_players": num_players,
                "matches": matches,
                "goals": goals,
                "shots": shots,
                "shots_on_target": shots_on_target,
                "shots_on_target%": shots_on_target_per,
                "shots_p90": shots_p90,
                "shots_on_target_p90": shots_on_target_p90,
                "goals_per_shot": goals_per_shot,
                "goals_per_shot_on_target": goals_per_sot,
                "avg_distance": dist,
                "free_kicks": fk,
                "pk": pk,
                "pk_attempted": pk_attempted,
                "xG": xG,
                "npxG": npxG,
                "npxG_per_shot": npxG_per_shot,
                "goals_minus_xG": goals_xG,
                "npg_minus_xG": npg_xG,
            }

            # add to empty list
            mylist.append(mydict)

        # assign list to appropriate team
        if side == "for":
            shooting_stats_for = mylist.copy()
        else:
            shooting_stats_against = mylist.copy()

    return shooting_stats_for, shooting_stats_against
