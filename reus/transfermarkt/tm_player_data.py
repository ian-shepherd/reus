from ..util import get_page_soup_headers
from .tm_player_metadata import tm_player_metadata
from .tm_player_market_value import tm_player_market_value
from .tm_player_transfers import tm_player_transfers
from bs4 import BeautifulSoup


def tm_player_data(
    url: str, save_html: bool = False, html_file: BeautifulSoup = None
) -> tuple:
    """Extracts metadata, market value history, and transfer history for a given player

    Args:
        url (str): path of transfermarkt player page
        save_html (bool, optional): whether to save html file. Defaults to False.
        html_file (BeautifulSoup, optional): pageSoup html file. Defaults to None.

    Returns:
        tuple: player data
            dict: player metadata
            list: historical market values
            list: transfer history
            BeautifulSoup: html file (if save_html=True)
    """

    if html_file is None:
        page = "https://www.transfermarkt.us" + url
        if save_html:
            pageSoup, pageContents = get_page_soup_headers(page, save_html=save_html)
        else:
            pageSoup = get_page_soup_headers(page)
    else:
        pageSoup = html_file

    metadata = tm_player_metadata(pageSoup)
    market_value = tm_player_market_value(pageSoup)
    transfers = tm_player_transfers(pageSoup)

    player = (
        (metadata, market_value, transfers, pageContents)
        if save_html
        else (metadata, market_value, transfers)
    )

    return player
