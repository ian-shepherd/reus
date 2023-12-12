import time

from bs4 import BeautifulSoup

from ..util import get_page_soup_headers
from .tm_player_market_value import tm_player_market_value
from .tm_player_metadata import tm_player_metadata
from .tm_player_transfers import tm_player_transfers


def tm_player_data(
    url: str, save_html: bool = False, html_file: BeautifulSoup = None
) -> tuple:
    """Extracts metadata, market value history, and transfer history for a given player

    Args:
        url (str): path of transfermarkt player page
        save_html (bool, optional): whether to save html file. Defaults to False.
        html_file (BeautifulSoup, optional): pageSoup html file of profile page. Defaults to None.

    Returns:
        tuple: player data
            dict: player metadata
            list: historical market values
            list: transfer history
            BeautifulSoup: html file (if save_html=True)
    """

    if html_file is None:
        page = "https://www.transfermarkt.us" + url
        mv_page = page.replace("profil", "marktwertverlauf")

        if save_html:
            pageSoup, pageContents = get_page_soup_headers(page, save_html=save_html)
            time.sleep(4)
            pageSoup2, pageContents2 = get_page_soup_headers(
                mv_page, save_html=save_html
            )
        else:
            pageSoup = get_page_soup_headers(page)
            time.sleep(4)
            pageSoup2 = get_page_soup_headers(mv_page)
    else:
        pageSoup = html_file
        mv_page = "https://www.transfermarkt.us" + url.replace(
            "profil", "marktwertverlauf"
        )
        pageSoup2 = get_page_soup_headers(mv_page)

    metadata = tm_player_metadata(pageSoup)
    market_value = tm_player_market_value(pageSoup2)
    transfers = tm_player_transfers(pageSoup)

    player = (
        (metadata, market_value, transfers, pageContents, pageContents2)
        if save_html
        else (metadata, market_value, transfers)
    )

    return player


# TODO: updaated documentation
