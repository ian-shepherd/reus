import json
import time

from bs4 import BeautifulSoup

from ..util import fetch_api_data, get_page_soup_headers
from .tm_player_market_value import tm_player_market_value
from .tm_player_metadata import tm_player_metadata
from .tm_player_transfers import tm_player_transfers


def tm_player_data(
    url: str,
    html_file: BeautifulSoup = None,
    json_file_mv: json = None,
    json_file_transfers: json = None,
    save_files: bool = False,
) -> tuple:
    """Extracts metadata, market value history, and transfer history for a given player

    Args:
        url (str): path of transfermarkt player page
        html_file (BeautifulSoup, optional): pageSoup html file of profile page. Defaults to None.
        json_file_mv (dict, optional): json file of market value history. Defaults to None.
        json_file_transfers (dict, optional): json file of player transfer history. Defaults to None.
        save_files (bool, optional): whether to save html and json files. Defaults to False.

    Returns:
        tuple: player data
            dict: player metadata
            list: historical market values
            list: transfer history
            BeautifulSoup: html file (if save_files=True)
            json: json file of market values (if save_files=True)
            json: json file of transfers (if save_files=True)
    """

    player_id = url.split("/")[-1]

    # Metadata
    if html_file is None:
        page = "https://www.transfermarkt.us" + url
        # mv_page = page.replace("profil", "marktwertverlauf")

        if save_files:
            pageSoup, pageContents = get_page_soup_headers(page, save_html=save_files)
            time.sleep(4)
            # pageSoup2, pageContents2 = get_page_soup_headers(
            #     mv_page, save_html=save_html
            # )
        else:
            pageSoup = get_page_soup_headers(page)
            time.sleep(4)
            # pageSoup2 = get_page_soup_headers(mv_page)

    else:
        pageSoup = html_file
        # mv_page = "https://www.transfermarkt.us" + url.replace(
        #     "profil", "marktwertverlauf"
        # )
        # pageSoup2 = get_page_soup_headers(mv_page)

    # Market Value History
    if json_file_mv is None:
        data = fetch_api_data(
            f"https://www.transfermarkt.us/ceapi/marketValueDevelopment/graph/{player_id}"
        )
        time.sleep(4)
    else:
        data = json_file_mv

    # Transfer History
    if json_file_transfers is None:
        data2 = fetch_api_data(
            f"https://www.transfermarkt.us/ceapi/transferHistory/list/{player_id}"
        )
        time.sleep(4)
    else:
        data2 = json_file_transfers

    metadata = tm_player_metadata(pageSoup=pageSoup)
    # market_value = tm_player_market_value(pageSoup2)
    market_value = tm_player_market_value(json_file=data)
    # transfers = tm_player_transfers(pageSoup=pageSoup)
    # transfers = None
    transfers = tm_player_transfers(json_file=data2)

    player = (
        (metadata, market_value, transfers, pageContents, data, data2)
        if save_files
        else (metadata, market_value, transfers)
    )

    return player
