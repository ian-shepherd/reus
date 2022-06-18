from ..util import get_page_soup


def fb_team_player_possession_stats(pageSoup=None, url: str = None):
    """Extracts possession stats for each player in a given team

    Args:
        pageSoup (bs4, optional): bs4 object of a team. Defaults to None.
        url (str, optional): path of fbref team page. Defaults to None.

    Returns:
        list: possession stats for each player
    """

    assert (
        pageSoup is not None or url is not None
    ), "Either pageSoup or url must be provided"

    assert (
        pageSoup is not None or url is not None
    ), "Either pageSoup or url must be provided"

    if pageSoup is None:
        pageSoup = get_page_soup(url)

    # Find table object
    div = pageSoup.find("div", {"id": "all_stats_possession"})
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

        touches = row.find("td", {"data-stat": "touches"}).text
        touches_def_pen = row.find("td", {"data-stat": "touches_def_pen_area"}).text
        touches_def = row.find("td", {"data-stat": "touches_def_3rd"}).text
        touches_mid = row.find("td", {"data-stat": "touches_mid_3rd"}).text
        touches_att = row.find("td", {"data-stat": "touches_att_3rd"}).text
        touches_att_pen = row.find("td", {"data-stat": "touches_att_pen_area"}).text
        touches_live = row.find("td", {"data-stat": "touches_live_ball"}).text

        dribble_success = row.find("td", {"data-stat": "dribbles_completed"}).text
        dribble_attempted = row.find("td", {"data-stat": "dribbles"}).text
        dribble_pct = row.find("td", {"data-stat": "dribbles_completed_pct"}).text
        dribble_past = row.find("td", {"data-stat": "players_dribbled_past"}).text
        dribble_meg = row.find("td", {"data-stat": "nutmegs"}).text

        carries = row.find("td", {"data-stat": "carries"}).text
        carries_dist = row.find("td", {"data-stat": "carry_distance"}).text
        carries_prg_dist = row.find(
            "td", {"data-stat": "carry_progressive_distance"}
        ).text
        carries_prg = row.find("td", {"data-stat": "progressive_carries"}).text
        carries_final_third = row.find(
            "td", {"data-stat": "carries_into_final_third"}
        ).text
        carries_pa = row.find("td", {"data-stat": "carries_into_penalty_area"}).text
        miscon = row.find("td", {"data-stat": "miscontrols"}).text
        dispos = row.find("td", {"data-stat": "dispossessed"}).text

        passes_targeted = row.find("td", {"data-stat": "pass_targets"}).text
        passes_received = row.find("td", {"data-stat": "passes_received"}).text
        passes_received_pct = row.find("td", {"data-stat": "passes_received_pct"}).text
        passes_received_prg = row.find(
            "td", {"data-stat": "progressive_passes_received"}
        ).text

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
            "touches": touches,
            "touches_defensive_pen": touches_def_pen,
            "touches_defensive_third": touches_def,
            "touches_middle_third": touches_mid,
            "touches_attacking_third": touches_att,
            "touches_attacking_pen": touches_att_pen,
            "touches_live": touches_live,
            "dribbles_successful": dribble_success,
            "dribbles_attempted": dribble_attempted,
            "dribble_pct": dribble_pct,
            "dribbled_past": dribble_past,
            "dribble_megs": dribble_meg,
            "carries": carries,
            "carry_distance": carries_dist,
            "carry_progressive_distance": carries_prg_dist,
            "carries_progressive": carries_prg,
            "carries_into_final_third": carries_final_third,
            "carries_into_penalty_area": carries_pa,
            "miscontrols": miscon,
            "dispossessed": dispos,
            "passes_targeted": passes_targeted,
            "passes_received": passes_received,
            "passes_received_pct": passes_received_pct,
            "passes_received_progressive": passes_received_prg,
            "match_logs": match_logs,
        }

        # add to empty list
        mylist.append(mydict)

    return mylist
