from ..util import get_page_soup


def fb_team_player_passing_stats(pageSoup=None, url: str = None):
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

        cmp = row.find("td", {"data-stat": "passes_completed"}).text
        att = row.find("td", {"data-stat": "passes"}).text
        acc = row.find("td", {"data-stat": "passes_pct"}).text
        totdist = row.find("td", {"data-stat": "passes_total_distance"}).text
        prgdist = row.find("td", {"data-stat": "passes_progressive_distance"}).text

        short_cmp = row.find("td", {"data-stat": "passes_completed_short"}).text
        short_att = row.find("td", {"data-stat": "passes_short"}).text
        short_acc = row.find("td", {"data-stat": "passes_pct_short"}).text

        med_cmp = row.find("td", {"data-stat": "passes_completed_medium"}).text
        med_att = row.find("td", {"data-stat": "passes_medium"}).text
        med_acc = row.find("td", {"data-stat": "passes_pct_medium"}).text

        long_cmp = row.find("td", {"data-stat": "passes_completed_long"}).text
        long_att = row.find("td", {"data-stat": "passes_long"}).text
        long_acc = row.find("td", {"data-stat": "passes_pct_long"}).text

        ast = row.find("td", {"data-stat": "assists"}).text
        xA = row.find("td", {"data-stat": "xa"}).text
        ast_xA = row.find("td", {"data-stat": "xa_net"}).text
        key_passes = row.find("td", {"data-stat": "assisted_shots"}).text
        final_third = row.find("td", {"data-stat": "passes_into_final_third"}).text
        ppa = row.find("td", {"data-stat": "passes_into_penalty_area"}).text
        crs_ppa = row.find("td", {"data-stat": "crosses_into_penalty_area"}).text
        prog = row.find("td", {"data-stat": "progressive_passes"}).text

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
            "completed": cmp,
            "attempted": att,
            "accuracy": acc,
            "total_distance": totdist,
            "progressive_distance": prgdist,
            "short_completed": short_cmp,
            "short_attempted": short_att,
            "short_accuracy": short_acc,
            "medium_completed": med_cmp,
            "medium_attempted": med_att,
            "medium_accuracy": med_acc,
            "long_completed": long_cmp,
            "long_attempted": long_att,
            "long_accuracy": long_acc,
            "assists": ast,
            "xA": xA,
            "assists_minus_xA": ast_xA,
            "key_passes": key_passes,
            "into_final_third": final_third,
            "into_penalty_area": ppa,
            "crosses_into_penalty_area": crs_ppa,
            "progressive_passes": prog,
            "match_logs": match_logs,
        }

        # add to empty list
        mylist.append(mydict)

    return mylist
