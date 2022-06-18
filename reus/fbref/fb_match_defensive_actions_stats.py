from .fb_match_metadata import fb_match_metadata
from ..util import get_page_soup


def fb_match_defensive_actions_stats(pageSoup=None, url: str = None):
    """Extracts defensive stats for each player in a given match that includes StatsBomb data

    Args:
        pageSoup (bs4, optional): bs4 object of a match. Defaults to None.
        url (str, optional): path of fbref match page. Defaults to None.

    Returns:
        tuple: defensive stats for home and away team players
            list: defensive stats for home team players
            list: defensive stats for away team players
    """

    assert (
        pageSoup is not None or url is not None
    ), "Either pageSoup or url must be provided"

    if pageSoup is None:
        pageSoup = get_page_soup(url)

    # Get team ids
    metadata = fb_match_metadata(pageSoup)[0]
    id_x = metadata.get("id_x")
    id_y = metadata.get("id_y")

    # Loop through both teams
    for team_id in [id_x, id_y]:
        # generate empty list for each team
        mylist = []
        # generate html id
        id_ = "stats_" + team_id + "_defense"

        # find defensive actions object
        stats_players = pageSoup.find("table", {"id": id_})
        stats_players = stats_players.find_all("tr")

        # iterate through each player and store metrics
        for row in stats_players[2:-1]:
            th = row.find("th")
            player_id = th.find("a", href=True)["href"].split("/")[3]

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

            # generate dictionary for team
            mydict = {
                "player_id": player_id,
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
            }

            # add to empty list
            mylist.append(mydict)

        # assign list to appropriate team
        if team_id == id_x:
            defensive_stats_x = mylist.copy()
        else:
            defensive_stats_y = mylist.copy()

    return defensive_stats_x, defensive_stats_y


if __name__ == "__main__":
    url = "/en/matches/c2e426c8/Leicester-City-Watford-November-28-2021-Premier-League"
    page = "https://fbref.com" + url
    # from util_placeholder import get_page_soup

    # pageSoup = get_page_soup(page)
    # stats_x, stats_y = fb_match_defensive_actions_stats(pageSoup)

    stats_x, stats_y = fb_match_defensive_actions_stats(url=page)
    print(stats_x)
