from .fb_match_metadata import fb_match_metadata

def fb_match_passing_stats(pageSoup):
    """
    Extracts passing stats for each player in a given match that includes StatsBomb data
    
    Parameters:
    pageSoup (html document): bs4 object of a match

    Returns:
    list: passing stats of home team players
    list: passing stats of away team players
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
        id_ = 'stats_' + team_id + '_passing'

        # find passing object
        stats_players = pageSoup.find('table', {'id' : id_})
        stats_players = stats_players.find_all('tr')

        # iterate through each player and store metrics
        for row in stats_players[2:-1]:
            th = row.find('th')
            player_id = th.find('a', href=True)['href'].split('/')[3]

            cmp = row.find('td', {'data-stat' : 'passes_completed'}).text
            att = row.find('td', {'data-stat' : 'passes'}).text
            acc = row.find('td', {'data-stat' : 'passes_pct'}).text
            totdist = row.find('td', {'data-stat' : 'passes_total_distance'}).text
            prgdist = row.find('td', {'data-stat' : 'passes_progressive_distance'}).text
            short_cmp = row.find('td', {'data-stat' : 'passes_completed_short'}).text
            short_att = row.find('td', {'data-stat' : 'passes_short'}).text
            short_acc = row.find('td', {'data-stat' : 'passes_pct_short'}).text
            med_cmp = row.find('td', {'data-stat' : 'passes_completed_medium'}).text
            med_att = row.find('td', {'data-stat' : 'passes_medium'}).text
            med_acc = row.find('td', {'data-stat' : 'passes_pct_medium'}).text
            long_cmp = row.find('td', {'data-stat' : 'passes_completed_long'}).text
            long_att = row.find('td', {'data-stat' : 'passes_long'}).text
            long_acc = row.find('td', {'data-stat' : 'passes_pct_long'}).text
            ast = row.find('td', {'data-stat' : 'assists'}).text
            xA = row.find('td', {'data-stat' : 'xa'}).text
            key_passes = row.find('td', {'data-stat' : 'assisted_shots'}).text
            final_third = row.find('td', {'data-stat' : 'passes_into_final_third'}).text
            ppa = row.find('td', {'data-stat' : 'passes_into_penalty_area'}).text
            crs_ppa = row.find('td', {'data-stat' : 'crosses_into_penalty_area'}).text
            prog = row.find('td', {'data-stat' : 'progressive_passes'}).text

            mydict = {
                'player_id' : player_id,
                'completed' : cmp,
                'attempted' : att,
                'accuracy' : acc,
                'total_distance' : totdist,
                'progressive_distance' : prgdist,
                'short_completed' : short_cmp,
                'short_attempted' : short_att,
                'short_accuracy' : short_acc,
                'medium_completed' : med_cmp,
                'medium_attempted' : med_att,
                'medium_accuracy' : med_acc,
                'long_completed' : long_cmp,
                'long_attempted' : long_att,
                'long_accuracy' : long_acc,
                'assists' : ast,
                'xA' : xA,
                'key_passes' : key_passes,
                'into_final_third' : final_third,
                'into_penalty_area' : ppa,
                'crosses_into_penalty_area' : crs_ppa,
                'progressive_passes' : prog}
            
            # add to empty list
            mylist.append(mydict)

        # assign list to appropriate team
        if team_id == id_x:
            players_passing_stats_x = mylist.copy()
        else:
            players_passing_stats_y = mylist.copy()


    return players_passing_stats_x, players_passing_stats_y