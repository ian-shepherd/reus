from ..util import get_page_soup


def fb_team_keeper_stats(pageSoup=None, url: str = None) -> list:
    """Extracts keeper stats for each team in a given league

    Args:
        pageSoup (bs4, optional): bs4 object of a team. Defaults to None.
        url (str, optional): path of fbref team page. Defaults to None.

    Returns:
        tuple: keeper stats for home and away team players
            list: keeper stats for each team
            list: keeper stats against each team
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
        id_ = "stats_squads_keeper_" + side

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
            matches = row.find("td", {"data-stat": "gk_games"}).text
            starts = row.find("td", {"data-stat": "gk_games_starts"}).text
            minutes = row.find("td", {"data-stat": "gk_minutes"}).text
            minutes_90 = row.find("td", {"data-stat": "minutes_90s"}).text

            # performance
            goals_allowed = row.find("td", {"data-stat": "gk_goals_against"}).text
            goals_allowed_p90 = row.find(
                "td", {"data-stat": "gk_goals_against_per90"}
            ).text
            shots_against = row.find(
                "td", {"data-stat": "gk_shots_on_target_against"}
            ).text
            saves = row.find("td", {"data-stat": "gk_saves"}).text
            save_pct = row.find("td", {"data-stat": "gk_save_pct"}).text
            wins = row.find("td", {"data-stat": "gk_wins"}).text
            draws = row.find("td", {"data-stat": "gk_ties"}).text
            losses = row.find("td", {"data-stat": "gk_losses"}).text
            clean_sheets = row.find("td", {"data-stat": "gk_clean_sheets"}).text
            cleen_sheet_pct = row.find("td", {"data-stat": "gk_clean_sheets_pct"}).text

            # penalty kicks
            pk_against = row.find("td", {"data-stat": "gk_pens_att"}).text
            pk_allowed = row.find("td", {"data-stat": "gk_pens_allowed"}).text
            pk_saves = row.find("td", {"data-stat": "gk_pens_saved"}).text
            pk_missed = row.find("td", {"data-stat": "gk_pens_missed"}).text
            pk_save_pct = row.find("td", {"data-stat": "gk_pens_save_pct"}).text

            # generate dictionary for team
            mydict = {
                "team_id": team_id,
                "team": team,
                "num_players": num_players,
                "matches": matches,
                "starts": starts,
                "minutes": minutes,
                "90s": minutes_90,
                "goals_allowed": goals_allowed,
                "goals_allowed_p90": goals_allowed_p90,
                "shots_against": shots_against,
                "saves": saves,
                "saves_pct": save_pct,
                "wins": wins,
                "draws": draws,
                "losses": losses,
                "clean_sheets": clean_sheets,
                "clean_sheets_pct": cleen_sheet_pct,
                "pk_against": pk_against,
                "pk_allowed": pk_allowed,
                "pk_saves": pk_saves,
                "pk_missed": pk_missed,
                "pk_save_pct": pk_save_pct,
            }

            # add to empty list
            mylist.append(mydict)

        # assign list to appropriate team
        if side == "for":
            keeper_stats_for = mylist.copy()
        else:
            keeper_stats_against = mylist.copy()

    return keeper_stats_for, keeper_stats_against
