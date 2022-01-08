import re

def tm_player_market_value(pageSoup):
    """
    Extracts date, team, and market value from highchart

    Parameters:
    pageSoup (html document): bs4 object of player referenced in url

    Returns:
    list: market value of player by date
    """

    # Extract currency
    currency = pageSoup.find('div', {'class' : 'zeile-oben'}).find('div', {'class' : 'right-td'}).text.strip()[0]

    # Find hicharts script object
    script = pageSoup.find("script", text=re.compile("Highcharts.Chart")).string

    # string pattern
    pattern = re.compile("'datum_mw':(.*?),'x'")
    date = re.findall(pattern, script)
    pattern = re.compile("'verein':(.*?),'age'")
    team = re.findall(pattern, script)
    pattern = re.compile("'y':(.*?),'verein'")
    value = re.findall(pattern, script)

    # generate empty list
    mylist = []

    # iterate through each data point and store attributes
    for i in range(len(date)):
        
        # generate dictionary for each point
        mydict = {'date' : date[i].replace('\\x20', ' ').replace("'", ""),
                  'team' : team[i].replace('\\x20', ' ').replace('\\u00E9', '\u00E9').replace("'", ""),
                  'currency' : currency,
                  'value' : value[i].replace('\\x20', ' ')}
        
        # append dictionary to list
        mylist.append(mydict)

    return mylist