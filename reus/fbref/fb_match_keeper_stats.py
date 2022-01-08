from .fb_match_metadata import fb_match_metadata

def fb_match_keeper_stats(pageSoup):
    """
    Extracts goalkeeping stats for each keeper in a given match that includes StatsBomb data
    
    Parameters:
    pageSoup (html document): bs4 object of a match

    Returns:
    list: goalkeeping stats of home team keeper
    list: goalkeeping stats of away team keeper
    """

    # Get team ids
    metadata = fb_match_metadata(pageSoup)[0]
    id_x = metadata.get('id_x')
    id_y = metadata.get('id_y')

    # Loop through both teams
    for team_id in [id_x, id_y]:
        # generate empty list for each team
        mylist = []
        # generate html id
        id_ = 'keeper_stats_' + team_id

        # find goalkeeping object
        stats_keeper = pageSoup.find('table', {'id' : id_})
        stats_keeper = stats_keeper.find_all('tr')

        # iterate through each keeper and store metrics
        for row in stats_keeper[2:]:
            th = row.find('th')
            name = th['csk']
            player_id = th.find('a', href=True)['href'].split('/')[3]

            nation = row.find('td', {'data-stat' : 'nationality'}).text
            age = row.find('td', {'data-stat' : 'age'}).text.split('-')
            age = int(age[0]) + int(age[1]) / 365
            minutes = row.find('td', {'data-stat' : 'minutes'}).text
            shots_against = row.find('td', {'data-stat' : 'shots_on_target_against'}).text
            goals_allowed = row.find('td', {'data-stat' : 'goals_against_gk'}).text
            saves = row.find('td', {'data-stat' : 'saves'}).text
            save_pct = row.find('td', {'data-stat' : 'save_pct'}).text
            psxg = row.find('td', {'data-stat' : 'psxg_gk'}).text
            launched_completed = row.find('td', {'data-stat' : 'passes_completed_launched_gk'}).text
            launched_attempted = row.find('td', {'data-stat' : 'passes_launched_gk'}).text
            launched_acc = row.find('td', {'data-stat' : 'passes_pct_launched_gk'}).text
            passes_attempted = row.find('td', {'data-stat' : 'passes_gk'}).text
            throws_attempted = row.find('td', {'data-stat' : 'passes_throws_gk'}).text
            pct_lauched = row.find('td', {'data-stat' : 'pct_passes_launched_gk'}).text
            passes_avg_length = row.find('td', {'data-stat' : 'passes_length_avg_gk'}).text
            gk_attempted = row.find('td', {'data-stat' : 'goal_kicks'}).text
            gk_pct_launched = row.find('td', {'data-stat' : 'pct_goal_kicks_launched'}).text
            gk_avg_length = row.find('td', {'data-stat' : 'goal_kick_length_avg'}).text
            crosses_faced = row.find('td', {'data-stat' : 'crosses_gk'}).text
            crosses_stopped = row.find('td', {'data-stat' : 'crosses_stopped_gk'}).text
            crosses_stopped_pct = row.find('td', {'data-stat' : 'crosses_stopped_pct_gk'}).text
            defensive_actions = row.find('td', {'data-stat' : 'def_actions_outside_pen_area_gk'}).text
            defensive_actions_avg_distance = row.find('td', {'data-stat' : 'avg_distance_def_actions_gk'}).text

            # generate dictionary for team
            mydict = {
                'player_id' : player_id,
                'name' : name,
                'nation' : nation,
                'age' : age,
                'minutes' : minutes,
                'shots_against' : shots_against,
                'goals_allowed' : goals_allowed,
                'saves' : saves,
                'saves_pct' : save_pct,
                'psxg' : psxg,
                'launched_completed' : launched_completed,
                'launched_attempted' : launched_attempted,
                'launched_accuracy' : launched_acc,
                'passes_attempted' : passes_attempted,
                'throws_attempted' : throws_attempted,
                'pct_launched' : pct_lauched,
                'passes_avg_length' : passes_avg_length,
                'gk_attempted' : gk_attempted,
                'gk_pct_launched' : gk_pct_launched,
                'gk_avg_length' : gk_avg_length,
                'crosses_faced' : crosses_faced,
                'crosses_stopped' : crosses_stopped,
                'crosses_stopped_pct' : crosses_stopped_pct,
                'defensive_actions' : defensive_actions,
                'defensive_actions_avg_distance' : defensive_actions_avg_distance}
            
            # add to empty list
            mylist.append(mydict)

        # assign list to appropriate team
        if team_id == id_x:
            keeper_stats_x = mylist.copy()
        else:
            keeper_stats_y = mylist.copy()


    return keeper_stats_x, keeper_stats_y