from ..util import get_page_soup


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
        if i.text == "Possession":
            currentStat = "possession"
            continue
        elif i.text == "Passing Accuracy":
            currentStat = "passing"
            continue
        elif i.text == "Shots on Target":
            currentStat = "shooting"
            continue
        elif i.text == "Saves":
            currentStat = "saves"
            continue
        elif i.text == "Cards":
            currentStat = "cards"
            continue

        if currentStat == "possession":
            possession = i.find_all("strong")
            possession_x = possession[0].text.replace("%", "")
            possession_y = possession[1].text.replace("%", "")
            currentStat = None
            continue
        elif currentStat == "passing":
            passing = i.find_all("div")
            passing_x = passing[0].find_all("div")[0].text.split()
            passes_completed_x = passing_x[0]
            passes_attempted_x = passing_x[2]
            passing_accuracy_x = passing_x[4].replace("%", "")
            passing_y = passing[5].find_all("div")[0].text.split()
            passing_accuracy_y = passing_y[0].replace("%", "")
            passes_completed_y = passing_y[2]
            passes_attempted_y = passing_y[4]
            currentStat = None
            continue
        elif currentStat == "shooting":
            shooting = i.find_all("div")
            shooting_x = shooting[0].find_all("div")[0].text.split()
            shots_target_x = shooting_x[0]
            shots_taken_x = shooting_x[2]
            shot_accuracy_x = shooting_x[4].replace("%", "")
            shooting_y = shooting[5].find_all("div")[0].text.split()
            shot_accuracy_y = shooting_y[0].replace("%", "")
            shots_target_y = shooting_y[2]
            shots_taken_y = shooting_y[4]
            currentStat = None
            continue
        elif currentStat == "saves":
            goalkeeping = i.find_all("div")
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
            currentStat = None
            continue
        elif currentStat == "cards":
            cards = i.find_all("div")
            cards_x = cards[0]
            yellow_cards_x = len(cards_x.find_all("span", {"class": "yellow_card"}))
            red_cards_x = len(cards_x.find_all("span", {"class": "red_card"}))
            cards_y = cards[5]
            yellow_cards_y = len(cards_y.find_all("span", {"class": "yellow_card"}))
            red_cards_y = len(cards_y.find_all("span", {"class": "red_card"}))
            currentStat = None
            continue

    # Extra stats
    extra = pageSoup.find("div", {"id": "team_stats_extra"})
    extraTable = extra.find_all("div")

    fouls_x = fouls_y = None
    corners_x = corners_y = None
    crosses_x = crosses_y = None
    touches_x = touches_y = None
    tackles_x = tackles_y = None
    interceptions_x = interceptions_y = None
    aerials_won_x = aerials_won_y = None
    clearances_x = clearances_y = None
    offsides_x = offsides_y = None
    goal_kicks_x = goal_kicks_y = None
    throw_ins_x = throw_ins_y = None
    long_balls_x = long_balls_y = None

    for div in extraTable:
        if div.text == "Fouls":
            fouls_x = div.findPrevious("div").text
            fouls_y = div.findNext("div").text
        elif div.text == "Corners":
            corners_x = div.findPrevious("div").text
            corners_y = div.findNext("div").text
        elif div.text == "Crosses":
            crosses_x = div.findPrevious("div").text
            crosses_y = div.findNext("div").text
        elif div.text == "Touches":
            touches_x = div.findPrevious("div").text
            touches_y = div.findNext("div").text
        elif div.text == "Tackles":
            tackles_x = div.findPrevious("div").text
            tackles_y = div.findNext("div").text
        elif div.text == "Interceptions":
            interceptions_x = div.findPrevious("div").text
            interceptions_y = div.findNext("div").text
        elif div.text == "Aerials Won":
            aerials_won_x = div.findPrevious("div").text
            aerials_won_y = div.findNext("div").text
        elif div.text == "Clearances":
            clearances_x = div.findPrevious("div").text
            clearances_y = div.findNext("div").text
        elif div.text == "Offsides":
            offsides_x = div.findPrevious("div").text
            offsides_y = div.findNext("div").text
        elif div.text == "Goal Kicks":
            goal_kicks_x = div.findPrevious("div").text
            goal_kicks_y = div.findNext("div").text
        elif div.text == "Throw Ins":
            throw_ins_x = div.findPrevious("div").text
            throw_ins_y = div.findNext("div").text
        elif div.text == "Long Balls":
            long_balls_x = div.findPrevious("div").text
            long_balls_y = div.findNext("div").text

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
        "fouls_x": fouls_x,
        "fouls_y": fouls_y,
        "corners_x": corners_x,
        "corners_y": corners_y,
        "crosses_x": crosses_x,
        "crosses_y": crosses_y,
        "touches_x": touches_x,
        "touches_y": touches_y,
        "tackles_x": tackles_x,
        "tackles_y": tackles_y,
        "interceptions_x": interceptions_x,
        "interceptions_y": interceptions_y,
        "aerials_won_x": aerials_won_x,
        "aerials_won_y": aerials_won_y,
        "clearances_x": clearances_x,
        "clearances_y": clearances_y,
        "offsides_x": offsides_x,
        "offsides_y": offsides_y,
        "goal_kicks_x": goal_kicks_x,
        "goal_kicks_y": goal_kicks_y,
        "throw_ins_x": throw_ins_x,
        "throw_ins_y": throw_ins_y,
        "long_balls_x": long_balls_x,
        "long_balls_y": long_balls_y,
    }

    return mydict
