from ..util import get_page_soup


def fb_team_defensive_actions_stats(pageSoup=None, url: str = None) -> list:
    """Extracts defensive action stats for each team in a given league

    Args:
        pageSoup (bs4, optional): bs4 object of a team. Defaults to None.
        url (str, optional): path of fbref team page. Defaults to None.

    Returns:
        tuple: defensive actions stats for home and away team players
            list: defensive actions stats for each team
            list: defensive actions stats against each team
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
        id_ = "stats_squads_defense_" + side

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

            # tackles
            tackles_attempted = row.find("td", {"data-stat": "tackles"}).text
            tackles_successful = row.find("td", {"data-stat": "tackles_won"}).text
            tackles_defensive_third = row.find(
                "td", {"data-stat": "tackles_def_3rd"}
            ).text
            tackles_middle_third = row.find("td", {"data-stat": "tackles_mid_3rd"}).text
            tackles_attacking_third = row.find(
                "td", {"data-stat": "tackles_att_3rd"}
            ).text

            # challenges
            challenges_successful = row.find(
                "td", {"data-stat": "challenge_tackles"}
            ).text
            challenges_attempted = row.find("td", {"data-stat": "challenges"}).text
            challenge_success_rate = row.find(
                "td", {"data-stat": "challenge_tackles_pct"}
            ).text
            if challenge_success_rate == "":
                challenge_success_rate = None
            challenges_lost = row.find("td", {"data-stat": "challenges_lost"}).text

            # blocks
            blocks = row.find("td", {"data-stat": "blocks"}).text
            blocked_shots = row.find("td", {"data-stat": "blocked_shots"}).text
            blocked_passes = row.find("td", {"data-stat": "blocked_passes"}).text

            # other
            interceptions = row.find("td", {"data-stat": "interceptions"}).text
            tkl_int = row.find("td", {"data-stat": "tackles_interceptions"}).text
            clearances = row.find("td", {"data-stat": "clearances"}).text
            errors = row.find("td", {"data-stat": "errors"}).text

            # generate dictionary for team
            mydict = {
                "team_id": team_id,
                "team": team,
                "num_players": num_players,
                "matches": matches,
                "tackles_attempted": tackles_attempted,
                "tackles_successful": tackles_successful,
                "tackles_defensive_third": tackles_defensive_third,
                "tackles_middle_third": tackles_middle_third,
                "tackles_attacking_third": tackles_attacking_third,
                "challenges_successful": challenges_successful,
                "challenges_attempted": challenges_attempted,
                "challenge_success_rate": challenge_success_rate,
                "challenges_lost": challenges_lost,
                "blocks": blocks,
                "blocked_shots": blocked_shots,
                "blocked_passes": blocked_passes,
                "interceptions": interceptions,
                "tkl_int": tkl_int,
                "clearances": clearances,
                "errors": errors,
            }

            # add to empty list
            mylist.append(mydict)

        # assign list to appropriate team
        if side == "for":
            defensive_actions_stats_for = mylist.copy()
        else:
            defensive_actions_stats_against = mylist.copy()

    return defensive_actions_stats_for, defensive_actions_stats_against
