from .fb_match_metadata import fb_match_metadata
from ..util import get_page_soup


def _extract_text(row, data_stat):
    element = row.find("td", {"data-stat": data_stat})
    return element.text


def _extract_keepers(row):
    th = row.find("th")

    # general
    try:
        name = th.text
    except AttributeError:
        name = th["csk"]

    player_id = th.find("a", href=True)["href"].split("/")[3]
    nation = _extract_text(row, "nationality")
    age = _extract_text(row, "age").split("-")
    try:
        age = int(age[0]) + int(age[1]) / 365
    except ValueError:
        age = None
    minutes = _extract_text(row, "minutes")

    # shot stopping
    shots_against = _extract_text(row, "gk_shots_on_target_against")
    goals_allowed = _extract_text(row, "gk_goals_against")
    saves = _extract_text(row, "gk_saves")
    save_pct = row.find("td", {"data-stat": "gk_save_pct"}).text
    if save_pct == "":
        save_pct = None
    psxg = _extract_text(row, "gk_psxg")

    # launched
    launched_completed = _extract_text(row, "gk_passes_completed_launched")
    launched_attempted = _extract_text(row, "gk_passes_launched")
    launched_accuracy = row.find("td", {"data-stat": "gk_passes_pct_launched"}).text
    if launched_accuracy == "":
        launched_accuracy = None

    # passes
    passes_attempted = _extract_text(row, "gk_passes")
    throws_attempted = _extract_text(row, "gk_passes_throws")
    pct_launched = _extract_text(row, "gk_pct_passes_launched")
    passes_avg_length = _extract_text(row, "gk_passes_length_avg")

    # goal kicks
    gk_attempted = _extract_text(row, "gk_goal_kicks")
    gk_pct_launched = _extract_text(row, "gk_pct_goal_kicks_launched")
    gk_avg_length = _extract_text(row, "gk_goal_kick_length_avg")

    # crosses
    crosses_faced = _extract_text(row, "gk_crosses")
    crosses_stopped = _extract_text(row, "gk_crosses_stopped")
    crosses_stopped_pct = _extract_text(row, "gk_crosses_stopped_pct")

    # sweeper
    defensive_actions = _extract_text(row, "gk_def_actions_outside_pen_area")
    defensive_actions_avg_distance = _extract_text(row, "gk_avg_distance_def_actions")

    # generate dictionary for team
    mydict = {
        "player_id": player_id,
        "name": name,
        "nation": nation,
        "age": age,
        "minutes": minutes,
        "shots_against": shots_against,
        "goals_allowed": goals_allowed,
        "saves": saves,
        "save_pct": save_pct,
        "psxg": psxg,
        "launched_completed": launched_completed,
        "launched_attempted": launched_attempted,
        "launched_accuracy": launched_accuracy,
        "passes_attempted": passes_attempted,
        "throws_attempted": throws_attempted,
        "pct_launched": pct_launched,
        "passes_avg_length": passes_avg_length,
        "gk_attempted": gk_attempted,
        "gk_pct_launched": gk_pct_launched,
        "gk_avg_length": gk_avg_length,
        "crosses_faced": crosses_faced,
        "crosses_stopped": crosses_stopped,
        "crosses_stopped_pct": crosses_stopped_pct,
        "defensive_actions": defensive_actions,
        "defensive_actions_avg_distance": defensive_actions_avg_distance,
    }

    return mydict


def _extract_teams(pageSoup, team_id):
    # generate empty list for each team
    mylist = []
    # generate html id
    id_ = "keeper_stats_" + team_id

    # find goalkeeping object
    stats_keeper = pageSoup.find("table", {"id": id_})
    stats_keeper = stats_keeper.find_all("tr")

    # iterate through each keeper and store metrics
    for row in stats_keeper[2:]:
        mydict = _extract_keepers(row)

        # add to empty list
        mylist.append(mydict)

    return mylist


def fb_match_keeper_stats(pageSoup=None, url: str = None) -> tuple:
    """Extracts goalkeeping stats for each keeper in a given match that includes advanced data

    Args:
        pageSoup (bs4, optional): bs4 object of a match. Defaults to None.
        url (str, optional): path of fbref match page. Defaults to None.

    Returns:
        tuple: goalkeeping stats for home and away team
            list: goalkeeping stats for home team players
            list: goalkeeping stats for away team players
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
        mylist = _extract_teams(pageSoup, team_id)

        # assign list to appropriate team
        if team_id == id_x:
            keeper_stats_x = mylist.copy()
        else:
            keeper_stats_y = mylist.copy()

    return keeper_stats_x, keeper_stats_y
