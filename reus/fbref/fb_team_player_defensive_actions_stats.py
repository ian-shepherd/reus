from ..util import get_page_soup


def fb_team_player_defensive_actions_stats(pageSoup=None, url: str = None) -> list:
    """Extracts defensive action stats for each player in a given team

    Args:
        pageSoup (bs4, optional): bs4 object of a team. Defaults to None.
        url (str, optional): path of fbref team page. Defaults to None.

    Returns:
        list: defensive stats for each player
    """

    assert (
        pageSoup is not None or url is not None
    ), "Either pageSoup or url must be provided"

    if pageSoup is None:
        pageSoup = get_page_soup(url)

    # Find table object
    div = pageSoup.find("div", {"id": "all_stats_defense"})
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

        # tackles
        tackles_attempted = row.find("td", {"data-stat": "tackles"}).text
        tackles_successful = row.find("td", {"data-stat": "tackles_won"}).text
        tackles_defensive_third = row.find("td", {"data-stat": "tackles_def_3rd"}).text
        tackles_middle_third = row.find("td", {"data-stat": "tackles_mid_3rd"}).text
        tackles_attacking_third = row.find("td", {"data-stat": "tackles_att_3rd"}).text

        # challenges
        challenges_successful = row.find("td", {"data-stat": "challenge_tackles"}).text
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
            "match_logs": match_logs,
        }

        # add to empty list
        mylist.append(mydict)

    return mylist
