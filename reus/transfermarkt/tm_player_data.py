from ..util import get_page_soup_headers
from .tm_player_metadata import tm_player_metadata
from .tm_player_market_value import tm_player_market_value
from .tm_player_transfers import tm_player_transfers


def tm_player_data(url: str, currency="EUR"):
    """Extracts metadata, market value history, and transfer history for a given player based on EUR, GBP, or USD currency.

    Args:
        url (str): path of transfermarkt player page
        currency (str): desired currency to return for values. Defaults to EUR.

    Returns:
        tuple: player data
            dict: player metadata
            list: historical market values
            list: transfer history
    """

    assert currency in [
        "EUR",
        "GBP",
        "USD",
    ], "Select a valid currency of EUR, GBP, or USD"

    # Determine url
    match currency:
        case "EUR":
            domain = "https://www.transfermarkt.com"
        case "GBP":
            domain = "https://www.transfermarkt.co.uk"
        case "USD":
            domain = "https://www.transfermarkt.us"

    page = "".join((domain, url))
    pageSoup = get_page_soup_headers(page)

    metadata = tm_player_metadata(pageSoup)
    market_value = tm_player_market_value(pageSoup)
    transfers = tm_player_transfers(pageSoup)

    player = (metadata, market_value, transfers)

    return player
