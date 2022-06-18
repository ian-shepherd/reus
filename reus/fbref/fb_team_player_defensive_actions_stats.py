from ..util import get_page_soup


def fb_team_player_defensive_actions_stats(pageSoup=None, url: str = None):
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

        tkl = row.find("td", {"data-stat": "tackles"}).text
        tklW = row.find("td", {"data-stat": "tackles_won"}).text
        tkl_def = row.find("td", {"data-stat": "tackles_def_3rd"}).text
        tkl_mid = row.find("td", {"data-stat": "tackles_mid_3rd"}).text
        tkl_att = row.find("td", {"data-stat": "tackles_att_3rd"}).text

        drb_tkl = row.find("td", {"data-stat": "dribble_tackles"}).text
        drb_att = row.find("td", {"data-stat": "dribbles_vs"}).text
        drb_pct = row.find("td", {"data-stat": "dribble_tackles_pct"}).text
        drb_past = row.find("td", {"data-stat": "dribbled_past"}).text

        press = row.find("td", {"data-stat": "pressures"}).text
        press_succ = row.find("td", {"data-stat": "pressure_regains"}).text
        press_pct = row.find("td", {"data-stat": "pressure_regain_pct"}).text
        press_def = row.find("td", {"data-stat": "pressures_def_3rd"}).text
        press_mid = row.find("td", {"data-stat": "pressures_mid_3rd"}).text
        press_att = row.find("td", {"data-stat": "pressures_att_3rd"}).text

        blk = row.find("td", {"data-stat": "blocks"}).text
        blk_shots = row.find("td", {"data-stat": "blocked_shots"}).text
        blk_sv = row.find("td", {"data-stat": "blocked_shots_saves"}).text
        blk_pass = row.find("td", {"data-stat": "blocked_passes"}).text

        interceptions = row.find("td", {"data-stat": "interceptions"}).text
        tkl_int = row.find("td", {"data-stat": "tackles_interceptions"}).text
        clr = row.find("td", {"data-stat": "clearances"}).text
        err = row.find("td", {"data-stat": "errors"}).text

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
            "tackles": tkl,
            "tackles_won": tklW,
            "tackles_defensive_third": tkl_def,
            "tackles_middle_third": tkl_mid,
            "tackles_attacking_third": tkl_att,
            "dribble_tackles": drb_tkl,
            "dribble_tackles_attempted": drb_att,
            "dribble_pct": drb_pct,
            "dribbled_past": drb_past,
            "pressures": press,
            "pressures_successful": press_succ,
            "pressure_pct": press_pct,
            "pressures_defensive_third": press_def,
            "pressures_middle_third": press_mid,
            "pressures_attacking_third": press_att,
            "blocks": blk,
            "blocked_shots": blk_shots,
            "blocked_shots_on_target": blk_sv,
            "blocked_passes": blk_pass,
            "interceptions": interceptions,
            "tkl_int": tkl_int,
            "clearances": clr,
            "errors": err,
            "match_logs": match_logs,
        }

        # add to empty list
        mylist.append(mydict)

    return mylist
