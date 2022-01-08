def fb_match_team_stats(pageSoup):
    """
    Extracts summary stats for each team in a given match
    
    Parameters:
    pageSoup (html document): bs4 object of a match

    Returns:
    dict: summary statistics for each team
    """

    # Find team stats object
    stats = pageSoup.find('div', {'id' : 'team_stats'})
    statsTable = stats.find('table').find_all('tr')

    # Error handling for missing metrics
    try:
        possession = statsTable[2].find_all('strong')
        possession_x = int(possession[0].text.replace('%', '')) / 100
        possession_y = int(possession[1].text.replace('%', '')) / 100
    except IndexError:
        possession_x = possession_y = None

    try:
        passing = statsTable[4].find_all('div')
        passing_x = passing[0].find_all('div')[0].text.split()
        passing_completed_x = passing_x[0]
        passing_attempted_x = passing_x[2]
        passing_accuracy_x = int(passing_x[4].replace('%', '')) / 100
        passing_y = passing[5].find_all('div')[0].text.split()
        passing_accuracy_y = int(passing_y[0].replace('%', '')) / 100
        passing_completed_y = passing_y[2]
        passing_attempted_y = passing_y[4]
    except IndexError:
        passing_completed_x = passing_completed_y = None
        passing_attempted_x = passing_attempted_y = None
        passing_accuracy_x = passing_accuracy_y = None

    try:
        shots = statsTable[6].find_all('div')
        shots_x = shots[0].find_all('div')[0].text.split()
        shots_target_x = shots_x[0]
        shots_taken_x = shots_x[2]
        shots_accuracy_x = int(shots_x[4].replace('%', '')) / 100
        shots_y = shots[5].find_all('div')[0].text.split()
        shots_accuracy_y = int(shots_y[0].replace('%', '')) / 100
        shots_target_y = shots_y[2]
        shots_taken_y = shots_y[4]
    except IndexError:
        shots_target_x = shots_target_y = None
        shots_taken_x = shots_taken_y = None
        shots_accuracy_x = shots_accuracy_y = None
        

    try:
        saves = statsTable[8].find_all('div')
        saves_x = saves[0].find_all('div')[0].text.split()
        saves_completed_x = saves_x[0]
        saves_attempted_x = saves_x[2]
        saves_rate_x = int(saves_x[4].replace('%', '')) / 100
        saves_y = saves[5].find_all('div')[0].text.split()
        saves_rate_y = int(saves_y[0].replace('%', '')) / 100
        saves_completed_y = saves_y[2]
        saves_attempted_y = saves_y[4]
    except IndexError:
        saves_completed_x = saves_completed_y = None
        saves_attempted_x = saves_attempted_y = None
        saves_rate_x = saves_rate_y = None


    extra = pageSoup.find('div', {'id' : 'team_stats_extra'})
    extraTable = extra.find_all('div')

    # Error handling for missing statistics
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
        if div.text == 'Fouls':
            fouls_x = div.findPrevious('div').text
            fouls_y = div.findNext('div').text
        elif div.text == 'Corners':
            corners_x = div.findPrevious('div').text
            corners_y = div.findNext('div').text
        elif div.text == 'Crosses':
            crosses_x = div.findPrevious('div').text
            crosses_y = div.findNext('div').text
        elif div.text == 'Touches':
            touches_x = div.findPrevious('div').text
            touches_y = div.findNext('div').text
        elif div.text == 'Tackles':
            tackles_x = div.findPrevious('div').text
            tackles_y = div.findNext('div').text
        elif div.text == 'Interceptions':
            interceptions_x = div.findPrevious('div').text
            interceptions_y = div.findNext('div').text
        elif div.text == 'Aerials Won':
            aerials_won_x = div.findPrevious('div').text
            aerials_won_y = div.findNext('div').text
        elif div.text == 'Clearances':
            clearances_x = div.findPrevious('div').text
            clearances_y = div.findNext('div').text
        elif div.text == 'Offsides':
            offsides_x = div.findPrevious('div').text
            offsides_y = div.findNext('div').text
        elif div.text == 'Goal Kicks':
            goal_kicks_x = div.findPrevious('div').text
            goal_kicks_y = div.findNext('div').text
        elif div.text == 'Throw Ins':
            throw_ins_x = div.findPrevious('div').text
            throw_ins_y = div.findNext('div').text
        elif div.text == 'Long Balls':
            long_balls_x = div.findPrevious('div').text
            long_balls_y = div.findNext('div').text

    # generate dictionary
    mydict = {'possession_x' : possession_x,
              'possession_y' : possession_y,
              'passes_completed_x' : passing_completed_x,
              'passes_attempted_x' : passing_attempted_x,
              'passsing_accuracy_x' : passing_accuracy_x,
              'passes_completed_y' : passing_completed_y,
              'passes_attempted_y' : passing_attempted_y,
              'passsing_accuracy_y' : passing_accuracy_y,
              'shots_on_target_x' : shots_target_x,
              'shots_taken_x' : shots_taken_x,
              'shot_accuracy_x' : shots_accuracy_x,
              'shots_on_target_y' : shots_target_y,
              'shots_taken_y' : shots_taken_y,
              'shot_accuracy_y' : shots_accuracy_y,
              'saves_x' : saves_completed_x,
              'shots_faced_x' : saves_attempted_x,
              'save_rate_x' : saves_rate_x,
              'saves_y' : saves_completed_y,
              'shots_faced_y' : saves_attempted_y,
              'save_rate_y' : saves_rate_y,
              'fouls_x' : fouls_x,
              'fouls_y' : fouls_y,
              'corners_x' : corners_x,
              'corners_y' : corners_y,
              'crosses_x' : crosses_x,
              'crosses_y' : crosses_y,
              'touches_x' : touches_x,
              'touches_y' : touches_y,
              'tackles_x' : tackles_x,
              'tackles_y' : tackles_y,
              'interceptions_x' : interceptions_x,
              'interceptions_y' : interceptions_y,
              'aerials_won_x' : aerials_won_x,
              'aerials_won_y' : aerials_won_y,
              'clearances_x' : clearances_x,
              'clearances_y' : clearances_y,
              'offsides_x' : offsides_x,
              'offsides_y' : offsides_y,
              'goal_kicks_x' : goal_kicks_x,
              'goal_kicks_y' : goal_kicks_y,
              'throw_ins_x' : throw_ins_x,
              'throw_ins_y' : throw_ins_y,
              'long_balls_x' : long_balls_x,
              'long_balls_y' : long_balls_y}

    return mydict