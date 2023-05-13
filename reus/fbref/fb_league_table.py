from ..util import get_page_soup


def fb_league_table(url: str) -> list:
    """Returns a list of league table and basic information in a season

    Args:
        url (str): url of a season

    Returns:
        list: league table
    """

    pageSoup = get_page_soup(url)

    # Find table object
    table = pageSoup.find("table")
    tbody = table.find("tbody")
    rows = tbody.find_all("tr")

    # Generate empty list
    mylist = []

    # iterate through each team and store attributes
    for row in rows:
        rank = row.find("th", {"data-stat": "rank"}).text
        team = row.find("td", {"data-stat": "team"}).text.strip()
        team_id = (
            row.find("td", {"data-stat": "team"})
            .find("a", href=True)["href"]
            .split("/")[3]
        )
        matches = row.find("td", {"data-stat": "games"}).text
        wins = row.find("td", {"data-stat": "wins"}).text
        draws = row.find("td", {"data-stat": "ties"}).text
        losses = row.find("td", {"data-stat": "losses"}).text
        goals = row.find("td", {"data-stat": "goals_for"}).text
        goals_allowed = row.find("td", {"data-stat": "goals_against"}).text
        goal_differential = row.find("td", {"data-stat": "goal_diff"}).text
        points = row.find("td", {"data-stat": "points"}).text
        ppg = row.find("td", {"data-stat": "points_avg"}).text
        try:
            xG = row.find("td", {"data-stat": "xg_for"}).text
            xGA = row.find("td", {"data-stat": "xg_against"}).text
            xGD = float(row.find("td", {"data-stat": "xg_diff"}).text)
            xGDp90 = float(row.find("td", {"data-stat": "xg_diff_per90"}).text)
        except AttributeError:
            xG = xGA = xGD = xGDp90 = None
        last_5_ = row.find("td", {"data-stat": "last_5"})
        last_5 = ""
        for t in last_5_.find_all("div", {"class": "poptip"}):
            last_5 += t.text
        avg_attendance = row.find("td", {"data-stat": "attendance_per_g"}).text
        top_scorer = row.find("td", {"data-stat": "top_team_scorers"}).text
        goalkeeper = row.find("td", {"data-stat": "top_keeper"}).text
        notes = row.find("td", {"data-stat": "notes"}).text

        # generate dictionary for each player
        mydict = {
            "rank": rank,
            "team": team,
            "team_id": team_id,
            "matches": matches,
            "wins": wins,
            "draws": draws,
            "losses": losses,
            "G": goals,
            "GA": goals_allowed,
            "GD": goal_differential,
            "Points": points,
            "Pts/MP": ppg,
            "xG": xG,
            "xGA": xGA,
            "xGD": xGD,
            "xGD/90": xGDp90,
            "last_5": last_5,
            "avg_attendance": avg_attendance,
            "top_scorer": top_scorer,
            "goalkeeper": goalkeeper,
            "notes": notes,
        }

        # append dictionary to list
        mylist.append(mydict)

    return mylist
