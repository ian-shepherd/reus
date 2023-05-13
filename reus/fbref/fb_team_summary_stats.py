from ..util import get_page_soup


def fb_team_summary_stats(pageSoup=None, url: str = None) -> list:
    """Extracts summary stats for each team in a given league

    Args:
        pageSoup (bs4, optional): bs4 object of a team. Defaults to None.
        url (str, optional): path of fbref team page. Defaults to None.

    Returns:
        tuple: summary stats for home and away team players
            list: summary stats for each team
            list: summary stats against each team
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
        id_ = "stats_squads_standard_" + side

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

            # performance
            goals = row.find("td", {"data-stat": "goals"}).text
            assists = row.find("td", {"data-stat": "assists"}).text
            g_a = row.find("td", {"data-stat": "goals_assists"}).text
            npg = row.find("td", {"data-stat": "goals_pens"}).text
            pk = row.find("td", {"data-stat": "pens_made"}).text
            pk_attempted = row.find("td", {"data-stat": "pens_att"}).text
            card_yellow = row.find("td", {"data-stat": "cards_yellow"}).text
            card_red = row.find("td", {"data-stat": "cards_red"}).text

            # expected
            try:
                xG = row.find("td", {"data-stat": "xg"}).text
                npxG = row.find("td", {"data-stat": "npxg"}).text
                xAG = row.find("td", {"data-stat": "xg_assist"}).text
                npxg_xga = row.find("td", {"data-stat": "npxg_xg_assist"}).text
            except AttributeError:
                xG = npxG = xAG = npxg_xga

            # progression
            progressive_carries = row.find(
                "td", {"data-stat": "progressive_carries"}
            ).text
            progressive_passes = row.find(
                "td", {"data-stat": "progressive_passes"}
            ).text

            # performance per 90 minutes
            goalp90 = row.find("td", {"data-stat": "goals_per90"}).text
            assistsp90 = row.find("td", {"data-stat": "assists_per90"}).text
            g_ap90 = row.find("td", {"data-stat": "goals_assists_per90"}).text
            npgp90 = row.find("td", {"data-stat": "goals_pens_per90"}).text
            npg_ap90 = row.find("td", {"data-stat": "goals_assists_pens_per90"}).text

            # expected per 90 minutes
            try:
                xGp90 = row.find("td", {"data-stat": "xg_per90"}).text
                xAGp90 = row.find("td", {"data-stat": "xg_assist_per90"}).text
                xG_xAGp90 = row.find("td", {"data-stat": "xg_xg_assist_per90"}).text
                npxGp90 = row.find("td", {"data-stat": "npxg_per90"}).text
                npxG_xAGp90 = row.find("td", {"data-stat": "npxg_xg_assist_per90"}).text
            except AttributeError:
                xGp90 = xAGp90 = xG_xAGp90 = npxGp90 = npxG_xAGp90 = None

            # generate dictionary for team
            mydict = {
                "team_id": team_id,
                "team": team,
                "num_players": num_players,
                "matches": matches,
                "goals": goals,
                "assists": assists,
                "goals+assists": g_a,
                "npg": npg,
                "pk": pk,
                "pk_attempted": pk_attempted,
                "card_yellow": card_yellow,
                "card_red": card_red,
                "xG": xG,
                "npxG": npxG,
                "xAG": xAG,
                "npxG+xA": npxg_xga,
                "progressive_carries": progressive_carries,
                "progressive_passes": progressive_passes,
                "goals_p90": goalp90,
                "assists_p90": assistsp90,
                "goals+assists_p90": g_ap90,
                "npg_p90": npgp90,
                "npg+assists_p90": npg_ap90,
                "xG_p90": xGp90,
                "xAG_p90": xAGp90,
                "xG+xAGp90": xG_xAGp90,
                "npxG_p90": npxGp90,
                "npxG+xAG_p90": npxG_xAGp90,
            }

            # add to empty list
            mylist.append(mydict)

        # assign list to appropriate team
        if side == "for":
            summary_stats_for = mylist.copy()
        else:
            summary_stats_against = mylist.copy()

    return summary_stats_for, summary_stats_against
