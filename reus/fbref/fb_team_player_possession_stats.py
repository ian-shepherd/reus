from ..util import get_page_soup


def fb_team_player_possession_stats(pageSoup=None, url: str = None) -> list:
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

        # touches
        touches = row.find("td", {"data-stat": "touches"}).text
        touches_def_pen_area = row.find(
            "td", {"data-stat": "touches_def_pen_area"}
        ).text
        touches_def_3rd = row.find("td", {"data-stat": "touches_def_3rd"}).text
        touches_mid_3rd = row.find("td", {"data-stat": "touches_mid_3rd"}).text
        touches_att_3rd = row.find("td", {"data-stat": "touches_att_3rd"}).text
        touches_att_pen_area = row.find(
            "td", {"data-stat": "touches_att_pen_area"}
        ).text
        touches_live = row.find("td", {"data-stat": "touches_live_ball"}).text

        # take ons
        dribble_attempt = row.find("td", {"data-stat": "take_ons"}).text
        dribble_success = row.find("td", {"data-stat": "take_ons_won"}).text
        dribble_success_pct = row.find("td", {"data-stat": "take_ons_won_pct"}).text
        if dribble_success_pct == "":
            dribble_success_pct = None
        dribble_tackled = row.find("td", {"data-stat": "take_ons_tackled"}).text
        dribble_tackled_pct = row.find("td", {"data-stat": "take_ons_tackled_pct"}).text

        # carries
        carries = row.find("td", {"data-stat": "carries"}).text
        carries_total_distance = row.find("td", {"data-stat": "carries_distance"}).text
        carries_progressive_distance = row.find(
            "td", {"data-stat": "carries_progressive_distance"}
        ).text
        progressive_carries = row.find("td", {"data-stat": "progressive_carries"}).text
        carries_into_final_third = row.find(
            "td", {"data-stat": "carries_into_final_third"}
        ).text
        carries_into_penalty_area = row.find(
            "td", {"data-stat": "carries_into_penalty_area"}
        ).text
        miscontrols = row.find("td", {"data-stat": "miscontrols"}).text
        dispossessed = row.find("td", {"data-stat": "dispossessed"}).text

        # receiving
        passes_received = row.find("td", {"data-stat": "passes_received"}).text
        progressive_passes_received = row.find(
            "td", {"data-stat": "progressive_passes_received"}
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
            "touches": touches,
            "touches_def_pen_area": touches_def_pen_area,
            "touches_def_3rd": touches_def_3rd,
            "touches_mid_3rd": touches_mid_3rd,
            "touches_att_3rd": touches_att_3rd,
            "touches_att_pen_area": touches_att_pen_area,
            "touches_live": touches_live,
            "dribble_attempt": dribble_attempt,
            "dribble_success": dribble_success,
            "dribble_success_pct": dribble_success_pct,
            "dribble_tackled": dribble_tackled,
            "dribble_tackled_pct": dribble_tackled_pct,
            "carries": carries,
            "carry_total_distance": carries_total_distance,
            "carry_progressive_distance": carries_progressive_distance,
            "progressive_carries": progressive_carries,
            "carries_into_final_third": carries_into_final_third,
            "carries_into_penalty_area": carries_into_penalty_area,
            "miscontrols": miscontrols,
            "dispossessed": dispossessed,
            "passes_received": passes_received,
            "progressive_passes_received": progressive_passes_received,
            "match_logs": match_logs,
        }

        # add to empty list
        mylist.append(mydict)

    return mylist
