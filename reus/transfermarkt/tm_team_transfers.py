from ..util import get_page_soup
from .util import tm_format_currency
import pandas as pd

def tm_team_transfers(club, season, position_group='All', main_position='All', window='All', currency='EUR'):
    """
    Extracts basic player information for each player in a squad including basic player information, market value, and contract expiration

    Parameters:
    club (string): club name
    season (string or int): year at start of season
    position_group (string): positional group
    main_position (string): main position
    window (string): transfer window
    currency (string): desired currency to return for values    

    Returns:
    list: team transfers
    """

    # Validate variables
    assert position_group in ['All', 'Goalkeepers', 'Defenders', 'Midfielders', 'Strikers'], 'Select a valid position group'
    assert main_position in ['All', 'Goalkeeper', 'Sweeper', 'Centre-Back', 'Left-Back', 'Right-Back',
                             'Defensive Midfield', 'Central Midfield', 'Right Midfield', 'Left Midfield', 'Attacking Midfield',
                             'Left Winger', 'Right Winger', 'Second Striker', 'Centre-Forward'], 'Select a valid main position'
    assert window in ['All', 'Summer', 'Winter'], 'Select a valid transfer window'

    # Lookup team name
    df = pd.read_csv('https://raw.githubusercontent.com/ian-shepherd/reus_data/main/raw-data/team_translations.csv', keep_default_na=False)
    df = df[(df.fbref_name==club) | (df.transfermarkt_name==club) | \
        (df.transfermarkt_link==club) | (df.fcpython==club) | \
        (df.fivethirtyeight==club)]

    season = str(season)

    # Determine domain    
    match currency:
        case 'EUR':
            domain = 'https://www.transfermarkt.com'
            signed_currency = '€'
        case 'GBP':
            domain = 'https://www.transfermarkt.co.uk'
            signed_currency = '£'
        case 'USD':
            domain = 'https://www.transfermarkt.us'
            signed_currency = '$'
    
    # Determine position group subdirectory
    match position_group:
        case 'All':
            pos_group_subdir = ''
        case 'Goalkeepers':
            pos_group_subdir = 'Torwart'
        case 'Defenders':
            pos_group_subdir = 'Abwehr'
        case 'Midfielders':
            pos_group_subdir = 'Mittelfeld'
        case 'Strikers':
            pos_group_subdir = 'Sturm'

    # Determine position subdirectory
    match main_position:
        case 'All':
            pos_subdir = '0'
        case 'Goalkeeper':
            pos_subdir = '1'
        case 'Sweeper':
            pos_subdir = '2'
        case 'Centre-Back':
            pos_subdir = '3'
        case 'Left-Back':
            pos_subdir = '4'
        case 'Right-Back':
            pos_subdir = '5'
        case 'Defensive Midfield':
            pos_subdir = '6'
        case 'Central Midfield':
            pos_subdir = '7'
        case 'Right Midfield':
            pos_subdir = '8'
        case 'Left Midfield':
            pos_subdir = '9'
        case 'Attacking Midfield':
            pos_subdir = '10'
        case 'Left Winger':
            pos_subdir = '11'
        case 'Right Winger':
            pos_subdir = '12'
        case 'Second Striker':
            pos_subdir = '13'
        case 'Centre-Forward':
            pos_subdir = '14'
        
    # Determine transfer window subdirectory
    match window:
        case 'All':
            window_subdir = ''
        case 'Summer':
            window_subdir = 's'
        case 'Winter':
            window_subdir = 'w'
    
    # Generate url
    try:
        subdir = '/'.join(("saison_id", season, "pos", pos_group_subdir, "detailpos", pos_subdir, "w_s", window_subdir, "plus/1#zugaenge"))
        page = '/'.join((domain, df.transfermarkt_link.iloc[0], "transfers/verein", str(df.transfermarkt.iloc[0]), subdir))
    except IndexError:
        print('This team does not exist, please confirm spelling')
        exit()


    pageSoup = get_page_soup(page)

    # Find table objects
    tables = pageSoup.find_all('table', {'class' : 'items'})

    # Error handling for no transfers or non-conducive position combinations
    assert len(tables) > 0, 'Confirm that you have entered a valid combination of positions and that there are transfers'

    if len(tables) == 2:
        table_arrivals, table_departures = tables
    elif len(tables) == 1:
        if pageSoup.find('span', {'class' : 'empty'}).find_previous('h2').text.strip() == 'Arrivals':
            table_arrivals = None
            table_departures = tables[0]
        elif pageSoup.find('span', {'class' : 'empty'}).find_previous('h2').text.strip() == 'Departures':
            table_arrivals = tables[0]
            table_departures = None
    

    # Generate empty list
    mylist = []

    # iterate over arrivals and departures    
    for table in [table_arrivals, table_departures]:
        
        # error handling for no transfers
        try:
            tbody = table.find('tbody')
        except AttributeError:
            continue

        # determine transfer direction
        if table == table_arrivals:
            direction = 'arrival'
        else:
            direction = 'departure'
    
        # find rows
        rows = tbody.find_all('tr')

        # iterate through each transfer and store attributes
        for row in rows:

            # check if valid row
            try:
                row_ = row['class'] not in ['odd', 'even']
            except KeyError:
                continue
            
            # row classes
            hauptlink_class = row.find_all('td', {'class' : 'hauptlink'})
            signing_class = row.find_all('img', {'class' : 'flaggenrahmen'})[-1]

            # extract basic info
            url = row.find('a', href=True)['href']
            name = row.find('img')['alt']
            pos = row.find('td', {'class' : 'hauptlink'}).find_next('td').text.strip()
            age = row.find('td', {'class' : 'zentriert'}).text.strip()
            nation = row.find_all('td', {'class' : 'zentriert'})[1].find('img')['alt']

            # transfer info
            mv = row.find('td', {'class' : 'rechts'}).text.strip()
            transfer_club = hauptlink_class[1].text.strip()
            try:
                transfer_club_url = hauptlink_class[1].find('a', href=True)['href']
            except TypeError:
                transfer_club_url = None
            transfer_league = signing_class.find_next('a', href=True).text
            transfer_league_url = signing_class.find_next('a', href=True)['href']
            transfer_country = signing_class['alt']
            signed_value = hauptlink_class[-1].text

            # value cleaning
            if "End of loan" in signed_value:
                transfer_type = 'End of loan'
                signed_value = '0'
            elif 'Loan' in signed_value:
                transfer_type = 'Loan'
                signed_value = signed_value.replace('Loan', '').replace('fee:', '').strip()
            elif 'loan transfer' in signed_value:
                transfer_type = 'Loan'
                signed_value = '0'
            elif 'free transfer' in signed_value:
                transfer_type = 'free transfer'
                signed_value = '0'
            else:
                signed_value = signed_value.replace('-','0')
                transfer_type = 'Transfer'

            # generate dictionary for each player
            mydict = {'direction' : direction,
                      'transfer_type' : transfer_type,
                      'name' : name,
                      'url' : url,
                      'position' : pos,
                      'age' : age,
                      'nation' : nation,
                      'transfer_club' : transfer_club,
                      'transfer_club_url' : transfer_club_url,
                      'transfer_league' : transfer_league,
                      'transfer_league_url' : transfer_league_url,
                      'transfer_country' : transfer_country,
                      'currency' : signed_currency,
                      'fee' : tm_format_currency(signed_value),
                      'market_value' : tm_format_currency(mv)}
            
            # append dictionary to list
            mylist.append(mydict)

    return mylist