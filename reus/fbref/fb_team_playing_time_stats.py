from ..util import get_page_soup


def fb_team_playing_time_stats(pageSoup=None, url: str = None) -> list:
    """Extracts playing time stats for each team

    Args:
        pageSoup (bs4, optional): bs4 object of a team. Defaults to None.
        url (str, optional): path of fbref team page. Defaults to None.

    Returns:
        tuple: playing time stats for home and away team players
            list: playing time stats for each team
            list: playing time stats against each team
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
        id_ = "stats_squads_playing_time_" + side

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

            # playing time
            matches = row.find("td", {"data-stat": "games"}).text
            minutes = row.find("td", {"data-stat": "minutes"}).text

            # starts
            starts = row.find("td", {"data-stat": "games_starts"}).text
            minutes_per_start = row.find("td", {"data-stat": "minutes_per_start"}).text
            full_90 = row.find("td", {"data-stat": "games_complete"}).text

            # subs
            subs = row.find("td", {"data-stat": "games_subs"}).text
            minutes_per_sub = row.find("td", {"data-stat": "minutes_per_sub"}).text
            unused_sub = row.find("td", {"data-stat": "unused_subs"}).text

            # Team Success
            ppm = row.find("td", {"data-stat": "points_per_game"}).text
            goals = row.find("td", {"data-stat": "on_goals_for"}).text
            goals_allowed = row.find("td", {"data-stat": "on_goals_against"}).text
            plus_minus = row.find("td", {"data-stat": "plus_minus"}).text
            plus_minus_p90 = row.find("td", {"data-stat": "plus_minus_per90"}).text

            # Team Success (xG)
            try:
                xG = row.find("td", {"data-stat": "on_xg_for"}).text
                xGA = row.find("td", {"data-stat": "on_xg_against"}).text
                xG_plus_minus = row.find("td", {"data-stat": "xg_plus_minus"}).text
                xG_plus_minus_p90 = row.find(
                    "td", {"data-stat": "xg_plus_minus_per90"}
                ).text
            except AttributeError:
                xG = xGA = xG_plus_minus = xG_plus_minus_p90 = None

            # generate dictionary for team
            mydict = {
                "team_id": team_id,
                "team": team,
                "num_players": num_players,
                "matches": matches,
                "minutes": minutes,
                "starts": starts,
                "minutes_per_start": minutes_per_start,
                "full_90": full_90,
                "subs": subs,
                "minutes_per_sub": minutes_per_sub,
                "unused_sub": unused_sub,
                "ppm": ppm,
                "goals": goals,
                "goals_allowed": goals_allowed,
                "plus_minus": plus_minus,
                "plus_minus_p90": plus_minus_p90,
                "xG": xG,
                "xGA": xGA,
                "xG_plus_minus": xG_plus_minus,
                "xG_plus_minus_p90": xG_plus_minus_p90,
            }

            # add to empty list
            mylist.append(mydict)

        # assign list to appropriate team
        if side == "for":
            playing_time_stats_for = mylist.copy()
        else:
            playing_time_stats_against = mylist.copy()

    return playing_time_stats_for, playing_time_stats_against
