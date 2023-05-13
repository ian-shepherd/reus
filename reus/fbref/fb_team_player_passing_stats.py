from ..util import get_page_soup


def fb_team_player_passing_stats(pageSoup=None, url: str = None) -> list:
    """Extracts passing stats for each player in a given team

    Args:
        pageSoup (bs4, optional): bs4 object of a team. Defaults to None.
        url (str, optional): path of fbref team page. Defaults to None.

    Returns:
        list: passing stats for each player
    """

    assert (
        pageSoup is not None or url is not None
    ), "Either pageSoup or url must be provided"

    if pageSoup is None:
        pageSoup = get_page_soup(url)

    # Find table object
    div = pageSoup.find("div", {"id": "all_stats_passing"})
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

        # total
        passes_completed = row.find("td", {"data-stat": "passes_completed"}).text
        passes_attempted = row.find("td", {"data-stat": "passes"}).text
        pass_accuracy = row.find("td", {"data-stat": "passes_pct"}).text
        if pass_accuracy == "":
            pass_accuracy = None
        total_distance = row.find("td", {"data-stat": "passes_total_distance"}).text
        progressive_distance = row.find(
            "td", {"data-stat": "passes_progressive_distance"}
        ).text

        # short
        short_passes_completed = row.find(
            "td", {"data-stat": "passes_completed_short"}
        ).text
        short_passes_attempted = row.find("td", {"data-stat": "passes_short"}).text
        short_pass_accuracy = row.find("td", {"data-stat": "passes_pct_short"}).text
        if short_pass_accuracy == "":
            short_pass_accuracy = None

        # medium
        medium_passes_completed = row.find(
            "td", {"data-stat": "passes_completed_medium"}
        ).text
        medium_passes_attempted = row.find("td", {"data-stat": "passes_medium"}).text
        medium_pass_accuracy = row.find("td", {"data-stat": "passes_pct_medium"}).text
        if medium_pass_accuracy == "":
            medium_pass_accuracy = None

        # long
        long_passes_completed = row.find(
            "td", {"data-stat": "passes_completed_long"}
        ).text
        long_passes_attempted = row.find("td", {"data-stat": "passes_long"}).text
        long_pass_accuracy = row.find("td", {"data-stat": "passes_pct_long"}).text
        if long_pass_accuracy == "":
            long_pass_accuracy = None

        # other
        assists = row.find("td", {"data-stat": "assists"}).text
        xg_assist = row.find("td", {"data-stat": "xg_assist"}).text
        xA = row.find("td", {"data-stat": "pass_xa"}).text
        xg_assist_net = row.find("td", {"data-stat": "xg_assist_net"}).text
        key_passes = row.find("td", {"data-stat": "assisted_shots"}).text
        passes_into_final_third = row.find(
            "td", {"data-stat": "passes_into_final_third"}
        ).text
        passes_into_penalty_area = row.find(
            "td", {"data-stat": "passes_into_penalty_area"}
        ).text
        crosses_into_penalty_area = row.find(
            "td", {"data-stat": "crosses_into_penalty_area"}
        ).text
        progressive_passes = row.find("td", {"data-stat": "progressive_passes"}).text

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
            "passes_completed": passes_completed,
            "passes_attempted": passes_attempted,
            "pass_accuracy": pass_accuracy,
            "total_distance": total_distance,
            "progressive_distance": progressive_distance,
            "short_passes_completed": short_passes_completed,
            "short_passes_attempted": short_passes_attempted,
            "short_pass_accuracy": short_pass_accuracy,
            "medium_passes_completed": medium_passes_completed,
            "medium_passes_attempted": medium_passes_attempted,
            "medium_pass_accuracy": medium_pass_accuracy,
            "long_passes_completed": long_passes_completed,
            "long_passes_attempted": long_passes_attempted,
            "long_pass_accuracy": long_pass_accuracy,
            "assists": assists,
            "xg_assist": xg_assist,
            "xA": xA,
            "xg_assist_net": xg_assist_net,
            "key_passes": key_passes,
            "passes_into_final_third": passes_into_final_third,
            "passes_into_penalty_area": passes_into_penalty_area,
            "crosses_into_penalty_area": crosses_into_penalty_area,
            "progressive_passes": progressive_passes,
            "match_logs": match_logs,
        }

        # add to empty list
        mylist.append(mydict)

    return mylist
