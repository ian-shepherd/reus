from .util import tm_player_injury_scraper
from ..util import get_page_soup


def tm_player_injury(pageSoup):
    """
    Extracts player injury history and equipped to handle players with multiple pages of injuries

    Parameters:
    pageSoup (html document): bs4 object of player referenced in url

    Returns:
    list: player injuries
    """

    # Determine if multiple pages present    
    injuryPages = len(pageSoup.find_all('li', {'class' : 'tm-pagination__list-item'}))

    # Execute one time using helper function
    if injuryPages == 0:
        injuries = tm_player_injury_scraper(pageSoup)

    # Multiple pages of injuries
    else:
        # execute 1st page
        injuries = tm_player_injury_scraper(pageSoup)

        # iterate over each subsequent page
        for p in range(1, injuryPages-2):

            # generate url for next page
            page = pageSoup.find('meta', {'property' : "og:url"})['content']
            page = "/".join((page, "page", str(p+1)))

            # return page soup for next page
            pageSoup = get_page_soup(page)

            # Extract injuries for next page and add to current list
            injuries_ = tm_player_injury_scraper(pageSoup)
            injuries.extend(injuries_)


    return injuries