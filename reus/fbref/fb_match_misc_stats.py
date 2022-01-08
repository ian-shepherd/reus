from .fb_match_metadata import fb_match_metadata

def fb_match_misc_stats(pageSoup):
    """
    Extracts miscellaneous stats for each player in a given match that includes StatsBomb data
    
    Parameters:
    pageSoup (html document): bs4 object of a match

    Returns:
    list: miscellaneous stats of home team players
    list: miscellaneous stats of away team players
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
        id_ = 'stats_' + team_id + '_misc'

        # find miscellaneous stats object
        stats_players = pageSoup.find('table', {'id' : id_})
        stats_players = stats_players.find_all('tr')

        # iterate through each player and store metrics
        for row in stats_players[2:-1]:
            th = row.find('th')
            player_id = th.find('a', href=True)['href'].split('/')[3]

            crdY = row.find('td', {'data-stat' : 'cards_yellow'}).text
            crdR = row.find('td', {'data-stat' : 'cards_red'}).text
            crdY2 = row.find('td', {'data-stat' : 'cards_yellow_red'}).text
            fls = row.find('td', {'data-stat' : 'fouls'}).text
            fld = row.find('td', {'data-stat' : 'fouled'}).text
            off = row.find('td', {'data-stat' : 'offsides'}).text
            crs = row.find('td', {'data-stat' : 'crosses'}).text
            interceptions = row.find('td', {'data-stat' : 'interceptions'}).text
            tklW = row.find('td', {'data-stat' : 'tackles_won'}).text
            pk_won = row.find('td', {'data-stat' : 'pens_won'}).text
            pk_con = row.find('td', {'data-stat' : 'pens_conceded'}).text
            og = row.find('td', {'data-stat' : 'own_goals'}).text
            recov = row.find('td', {'data-stat' : 'ball_recoveries'}).text
            aerial_won = row.find('td', {'data-stat' : 'aerials_won'}).text
            aerial_lost = row.find('td', {'data-stat' : 'aerials_lost'}).text
            aerial_pct = row.find('td', {'data-stat' : 'aerials_won_pct'}).text
            
            # generate dictionary for team
            mydict = {
                'player_id' : player_id,
                'cards_yellow' : crdY,
                'cards_red' : crdR,
                'cards_second_yellow' : crdY2,
                'fouls' : fls,
                'fouled' : fld,
                'offsides' : off,
                'crosses' : crs,
                'interceptions' : interceptions,
                'tackles_won' : tklW,
                'pk_won' : pk_won,
                'pk_con' : pk_con,
                'own_goals' : og,
                'recoveries' : recov,
                'aerials_won' : aerial_won,
                'aerials_lost' : aerial_lost,
                'aerials_pct' : aerial_pct}
            
            # add to empty list
            mylist.append(mydict)

        # assign list to appropriate team
        if team_id == id_x:
            players_misc_stats_x = mylist.copy()
        else:
            players_misc_stats_y = mylist.copy()

    return players_misc_stats_x, players_misc_stats_y