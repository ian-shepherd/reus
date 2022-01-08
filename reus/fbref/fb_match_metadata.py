def fb_match_metadata(pageSoup):
    """
    Extracts general information (teams, managers, captains, date, time, venue, attendance, score, xG) for a given match
    
    Parameters:
    pageSoup (html document): bs4 object of a match

    Returns:
    dict: metadata information
    dict: match officials
    """

    # Extract url
    url = pageSoup.find('meta', {'property' : "og:url"})['content']
    url = url.replace('https://fbref.com', '')
    
    # Find scorebox object
    scorebox = pageSoup.find('div', {'class' : 'scorebox'})
    teams = scorebox.find_all('div', {'itemprop' : 'performer'})
    
    # extract team id and name
    id_x = teams[0].find('a', href=True)['href'].split('/')[3]
    id_y = teams[1].find('a', href=True)['href'].split('/')[3]
    team_x = teams[0].find('a', href=True).text
    team_y = teams[1].find('a', href=True).text
    
    # extract scores
    scores = pageSoup.find_all('div', {'class' : 'scores'})
    score_x = scores[0].find('div', {'class' : 'score'}).text
    # error handling for non-xG
    try:
        xg_x = scores[0].find('div', {'class' : 'score_xg'}).text
    except AttributeError:
        xg_x = None
    score_y = scores[1].find('div', {'class' : 'score'}).text
    # error handling for non-xG
    try:
        xg_y = scores[1].find('div', {'class' : 'score_xg'}).text
    except AttributeError:
        xg_y = None
    
    # extract managers and captains
    managers = pageSoup.find_all('div', {'class' : 'datapoint'})
    manager_x = managers[0].text.replace('Manager: ', '')
    manager_y = managers[2].text.replace('Manager: ', '')
    captain_x = managers[1].find('a', href=True)['href']
    captain_y = managers[3].find('a', href=True)['href']

    # Find match information object
    scorebox_meta = pageSoup.find('div', {'class' : 'scorebox_meta'})

    # extract date and time information
    datetime = scorebox_meta.find('span', {'class' : 'venuetime'})
    date = datetime['data-venue-date']
    kickoff = datetime['data-venue-time']

    # extract attendance, venue, and official information
    scorebox_meta_ = scorebox_meta.find_all('div')
    if scorebox_meta_[4].text.startswith('Attendance:'):
        attendance = scorebox_meta_[4].text
        attendance = attendance.replace("Attendance: ", "")
        attendance = attendance.replace(",", "")
        venue = scorebox_meta_[5].text.replace('Venue: ', '')
        officials = scorebox_meta_[6].find_all('small')[1].text.split('\xa0· ')
    else:
        attendance = 0
        venue = scorebox_meta_[4].text.replace('Venue: ', '')
        officials = scorebox_meta_[5].find_all('small')[1].text.split('\xa0· ')
    

    # generate dictionary for general metadata
    matadict = {'url' : url,
                'match_id' : url.split('/')[3],
                'id_x' : id_x,
                'id_y' : id_y,
                'team_x' : team_x,
                'team_y' : team_y,
                'score_x' : score_x,
                'score_y' : score_y,
                'xg_x' : xg_x,
                'xg_y' : xg_y,
                'manager_x' : manager_x,
                'manager_y' : manager_y,
                'captain_x' : captain_x,
                'captain_id_x' : captain_x.split('/')[3],
                'captain_y' : captain_y,
                'captain_id_y' : captain_y.split('/')[3],
                'date' : date,
                'kickoff' : kickoff,
                'attendance' : attendance,
                'venue' : venue}
    
    # extract officials
    referee = officials[0].replace(" (Referee)", "")
    ar1 = officials[1].replace(" (AR1)", "")
    ar2 = officials[2].replace(" (AR2)", "")
    fourth = officials[3].replace(" (4th)", "")
    var = (officials[4].replace(" (VAR)", "") if len(officials) > 4 else None)

    # generate dictionary for officials
    officialsdict = {'referee' : referee,
                     'ar1' : ar1,
                     'ar2' : ar2,
                     'fourth' : fourth,
                     'var' :var}

    return matadict, officialsdict