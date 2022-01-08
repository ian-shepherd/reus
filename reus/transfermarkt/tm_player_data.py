from ..util import get_page_soup
from .tm_player_metadata import tm_player_metadata
from .tm_player_market_value import tm_player_market_value
from .tm_player_transfers import tm_player_transfers

def tm_player_data(url, currency='EUR'):
    """
    Extracts metadata, market value history, and transfer history for a given player
    
    Parameters:
    url (string): path of transfermarkt player
    currency (string): desired currency to return for values

    Returns:
    dict: player metadata
    list: market value of player by date
    list: player transfers
    """

    # Determine url    
    match currency:
        case 'EUR':
            domain = 'https://www.transfermarkt.com'
        case 'GBP':
            domain = 'https://www.transfermarkt.co.uk'
        case 'USD':
            domain = 'https://www.transfermarkt.us'


    page = ''.join((domain, url))
    pageSoup = get_page_soup(page)

    metadata = tm_player_metadata(pageSoup)
    market_value = tm_player_market_value(pageSoup)
    transfers = tm_player_transfers(pageSoup)

    player = (metadata,
              market_value,
              transfers)

    return player