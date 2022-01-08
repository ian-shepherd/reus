from ..util import get_page_soup

def fb_match_urls(url):
    """
    Returns a list of urls for matches in a season
    
    Parameters:
    url (string): url of a season

    Returns:
    list: match urls for given season
    """

    pageSoup = get_page_soup(url)
    table = pageSoup.find('table')
    tbody = table.find('tbody')
    tr = tbody.find_all('tr')

    match_urls = []
    for row in tr:
        # error handling for matches with no data yet
        try:
            if 'matches' in row.find_all('a', href=True)[2]['href']:
                match_urls.append(row.find_all('a', href=True)[2]['href'])
        except IndexError:
            continue
    
    return match_urls