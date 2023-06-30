from ..util import get_page_soup


def _get_current_stat(row):
    if row == "Possession":
        return "possession"
    elif row == "Passing Accuracy":
        return "passing"
    elif row == "Shots on Target":
        return "shooting"
    elif row == "Saves":
        return "saves"
    elif row == "Cards":
        return "cards"


def _extract_percentage_stat(row):
    stat = row.find_all("div")
    stat_x = stat[0].find_all("div")[0].text.split()
    stat_success_x = stat_x[0]
    stat_attempted_x = stat_x[2]
    stat_accuracy_x = stat_x[4].replace("%", "")

    stat_y = stat[5].find_all("div")[0].text.split()
    stat_accuracy_y = stat_y[0].replace("%", "")
    stat_success_y = stat_y[2]
    stat_attempted_y = stat_y[4]

    return (
        stat_success_x,
        stat_attempted_x,
        stat_accuracy_x,
        stat_success_y,
        stat_attempted_y,
        stat_accuracy_y,
        None,
    )


def _extract_save_stat(row):
    goalkeeping = row.find_all("div")
    goalkeeping_x = goalkeeping[0].find_all("div")[0].text.split()
    if goalkeeping_x[0] == "of":
        saves_x = "0"
        saves_attempted_x = goalkeeping_x[1]
        save_rate_x = "0"
    else:
        saves_x = goalkeeping_x[0]
        saves_attempted_x = goalkeeping_x[2]
        save_rate_x = goalkeeping_x[4].replace("%", "")
    goalkeeping_y = goalkeeping[5].find_all("div")[0].text.split()
    if goalkeeping_y[2] == "of":
        saves_y = "0"
        saves_attempted_y = goalkeeping_y[3]
        save_rate_y = "0"
    else:
        saves_y = goalkeeping_y[2]
        saves_attempted_y = goalkeeping_y[4]
        save_rate_y = goalkeeping_y[0].replace("%", "")

    return (
        saves_x,
        saves_attempted_x,
        save_rate_x,
        saves_y,
        saves_attempted_y,
        save_rate_y,
        None,
    )


def _extract_cards(row):
    cards = row.find_all("div")
    cards_x = cards[0]
    yellow_cards_x = len(cards_x.find_all("span", {"class": "yellow_card"}))
    red_cards_x = len(cards_x.find_all("span", {"class": "red_card"}))
    cards_y = cards[5]
    yellow_cards_y = len(cards_y.find_all("span", {"class": "yellow_card"}))
    red_cards_y = len(cards_y.find_all("span", {"class": "red_card"}))

    return (
        yellow_cards_x,
        red_cards_x,
        yellow_cards_y,
        red_cards_y,
        None,
    )


def _extract_extra_stats(div):
    stat_x = div.findPrevious("div").text
    stat_y = div.findNext("div").text

    return stat_x, stat_y


def fb_match_team_stats(pageSoup=None, url: str = None) -> dict:
    """Extracts summary stats for each team in a given match

    Args:
        pageSoup (bs4, optional): bs4 object of a match. Defaults to None.
        url (str, optional): path of fbref match page. Defaults to None.

    Returns:
        dict: summary statistics for each team
    """

    assert (
        pageSoup is not None or url is not None
    ), "Either pageSoup or url must be provided"

    if pageSoup is None:
        pageSoup = get_page_soup(url)

    # Find team stats object
    stats = pageSoup.find("div", {"id": "team_stats"})
    statsTable = stats.find("table").find_all("tr")

    # Baseline stats
    possession_x = None
    possession_y = None
    passes_completed_x = None
    passes_attempted_x = None
    passing_accuracy_x = None
    passes_completed_y = None
    passes_attempted_y = None
    passing_accuracy_y = None
    shots_target_x = None
    shots_taken_x = None
    shot_accuracy_x = None
    shots_target_y = None
    shots_taken_y = None
    shot_accuracy_y = None
    saves_x = None
    saves_attempted_x = None
    save_rate_x = None
    saves_y = None
    saves_attempted_y = None
    save_rate_y = None
    yellow_cards_x = None
    red_cards_x = None
    yellow_cards_y = None
    red_cards_y = None

    currentStat = None
    for i in statsTable[1:]:
        if i.text in [
            "Possession",
            "Passing Accuracy",
            "Shots on Target",
            "Saves",
            "Cards",
        ]:
            currentStat = _get_current_stat(i.text)
            continue

        if currentStat == "possession":
            possession = i.find_all("strong")
            possession_x = possession[0].text.replace("%", "")
            possession_y = possession[1].text.replace("%", "")
            currentStat = None
            continue
        elif currentStat == "passing":
            (
                passes_completed_x,
                passes_attempted_x,
                passing_accuracy_x,
                passes_completed_y,
                passes_attempted_y,
                passing_accuracy_y,
                currentStat,
            ) = _extract_percentage_stat(i)

            continue
        elif currentStat == "shooting":
            (
                shots_target_x,
                shots_taken_x,
                shot_accuracy_x,
                shots_target_y,
                shots_taken_y,
                shot_accuracy_y,
                currentStat,
            ) = _extract_percentage_stat(i)

            continue
        elif currentStat == "saves":
            (
                saves_x,
                saves_attempted_x,
                save_rate_x,
                saves_y,
                saves_attempted_y,
                save_rate_y,
                currentStat,
            ) = _extract_save_stat(i)
            continue
        elif currentStat == "cards":
            (
                yellow_cards_x,
                red_cards_x,
                yellow_cards_y,
                red_cards_y,
                currentStat,
            ) = _extract_cards(i)
            continue

    # Extra stats
    extra = pageSoup.find("div", {"id": "team_stats_extra"})
    extraTable = extra.find_all("div")

    fouls_x = fouls_y = None  # noqa: F841
    corners_x = corners_y = None  # noqa: F841
    crosses_x = crosses_y = None  # noqa: F841
    touches_x = touches_y = None  # noqa: F841
    tackles_x = tackles_y = None  # noqa: F841
    interceptions_x = interceptions_y = None  # noqa: F841
    aerials_won_x = aerials_won_y = None  # noqa: F841
    clearances_x = clearances_y = None  # noqa: F841
    offsides_x = offsides_y = None  # noqa: F841
    goal_kicks_x = goal_kicks_y = None  # noqa: F841
    throw_ins_x = throw_ins_y = None  # noqa: F841
    long_balls_x = long_balls_y = None  # noqa: F841

    extra_stats_mapping = {
        "Fouls": ("fouls_x", "fouls_y"),
        "Corners": ("corners_x", "corners_y"),
        "Crosses": ("crosses_x", "crosses_y"),
        "Touches": ("touches_x", "touches_y"),
        "Tackles": ("tackles_x", "tackles_y"),
        "Interceptions": ("interceptions_x", "interceptions_y"),
        "Aerials Won": ("aerials_won_x", "aerials_won_y"),
        "Clearances": ("clearances_x", "clearances_y"),
        "Offsides": ("offsides_x", "offsides_y"),
        "Goal Kicks": ("goal_kicks_x", "goal_kicks_y"),
        "Throw Ins": ("throw_ins_x", "throw_ins_y"),
        "Long Balls": ("long_balls_x", "long_balls_y"),
    }

    # generate dictionary
    mydict = {
        "possession_x": possession_x,
        "possession_y": possession_y,
        "passes_completed_x": passes_completed_x,
        "passes_attempted_x": passes_attempted_x,
        "passing_accuracy_x": passing_accuracy_x,
        "passes_completed_y": passes_completed_y,
        "passes_attempted_y": passes_attempted_y,
        "passing_accuracy_y": passing_accuracy_y,
        "shots_on_target_x": shots_target_x,
        "shots_taken_x": shots_taken_x,
        "shot_accuracy_x": shot_accuracy_x,
        "shots_on_target_y": shots_target_y,
        "shots_taken_y": shots_taken_y,
        "shot_accuracy_y": shot_accuracy_y,
        "saves_x": saves_x,
        "shots_faced_x": saves_attempted_x,
        "save_rate_x": save_rate_x,
        "saves_y": saves_y,
        "shots_faced_y": saves_attempted_y,
        "save_rate_y": save_rate_y,
        "yellow_cards_x": yellow_cards_x,
        "red_cards_x": red_cards_x,
        "yellow_cards_y": yellow_cards_y,
        "red_cards_y": red_cards_y,
    }

    for div in extraTable:
        stat_name = div.text
        if stat_name in extra_stats_mapping:
            vars_x, vars_y = _extract_extra_stats(div)
            for i, key in enumerate(extra_stats_mapping[stat_name]):
                mydict[key] = vars_x if i == 0 else vars_y

    return mydict
