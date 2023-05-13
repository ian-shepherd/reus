from ..util import get_page_soup


def fb_team_possession_stats(pageSoup=None, url: str = None) -> list:
    """Extracts possession stats for each team in a given league

    Args:
        pageSoup (bs4, optional): bs4 object of a team. Defaults to None.
        url (str, optional): path of fbref team page. Defaults to None.

    Returns:
        tuple: possession stats for home and away team players
            list: possession stats for each team
            list: possession stats against each team
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
        id_ = "stats_squads_possession_" + side

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
            dribble_tackled_pct = row.find(
                "td", {"data-stat": "take_ons_tackled_pct"}
            ).text

            # carries
            carries = row.find("td", {"data-stat": "carries"}).text
            carries_total_distance = row.find(
                "td", {"data-stat": "carries_distance"}
            ).text
            carries_progressive_distance = row.find(
                "td", {"data-stat": "carries_progressive_distance"}
            ).text
            progressive_carries = row.find(
                "td", {"data-stat": "progressive_carries"}
            ).text
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

            # generate dictionary for team
            mydict = {
                "team_id": team_id,
                "team": team,
                "num_players": num_players,
                "matches": matches,
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
            }

            # add to empty list
            mylist.append(mydict)

        # assign list to appropriate team
        if side == "for":
            possession_stats_for = mylist.copy()
        else:
            possession_stats_against = mylist.copy()

    return possession_stats_for, possession_stats_against
