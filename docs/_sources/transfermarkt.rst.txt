Transfermarkt
=============

Complete list of all transfermarkt functions

Player functions
----------------

.. py:function:: .transfermarkt.tm_player_data(url: str, save_html: bool = False, html_file: BeautifulSoup = None) -> tuple

   Extracts metadata, market value history, and transfer history for a given player

   :param url: path of transfermarkt player page
   :type url: str
   :param save_html: whether to save html file. Defaults to False.
   :type currency: bool
   :param html_file: pageSoup html file. Defaults to None.
   :type html_file: BeautifulSoup or None
   :return: player metadata, historical market values, transfer history, and BeautifulSoup file of player page (optional)
   :rtype: (dict, list, list, BeautifulSoup) or (dict, list, list)

.. py:function:: .transfermarkt.tm_player_injury(pageSoup) -> list

   Extracts player injury history and equipped to handle players with multiple pages of injuries

   :param pageSoup: bs4 object of injury page for player referenced in url
   :type pageSoup: bs4
   :return: player injuries
   :rtype: list
 
.. py:function:: .transfermarkt.tm_player_market_value(pageSoup=None, url: str = None) -> list

   Extracts date, team, and market value from highchart

   :param pageSoup: bs4 object of player page referenced in url. Defaults to None.
   :type pageSoup: bs4
   :param url: path of transfermarkt player page. Defaults to None.
   :type url: str
   :return: market value of player by date
   :rtype: list
 
.. py:function:: .transfermarkt.tm_player_metadata(pageSoup=None, url: str = None) -> dict:

   Extracts general player information (biographical, club, contract, market value, and miscellaneous)

   :param pageSoup: bs4 object of player page referenced in url. Defaults to None.
   :type pageSoup: bs4
   :param url: path of transfermarkt player page. Defaults to None.
   :type url: str
   :return: player metadata
   :rtype: dict
   
.. py:function:: .transfermarkt.tm_player_transfers(pageSoup=None, url: str = None) -> list:

   Extracts player transfer information

   :param pageSoup: bs4 object of player page referenced in url. Defaults to None.
   :type pageSoup: bs4
   :param url: path of transfermarkt player page. Defaults to None.
   :type url: str
   :return: player transfers
   :rtype: list 


Team functions
--------------  

.. py:function:: .transfermarkt.tm_team_transfers(club: str, season: str, domain: str = "us", position_group="All", main_position="All", window="All", team_id: int = None, transfermarkt_name: bool = False) -> list

   Extracts player transfer information

   :param club: club name
   :type club: str
   :param season: year at start of season
   :type season: str or int
   :param domain: domain to use for transfermarkt. Defaults to us.
   :type domain: str
   :param position_group: position group to filter by. Defaults to All.
   :type position_group: str
   :param main_position: main position to filter by. Defaults to All.
   :type main_position: str
   :param window: transfer window to filter by. Defaults to All.
   :type window: str
   :param team_id: transfermarkt team id. Defaults to None.
   :type team_id: int
   :param transfermarkt_name: if True, club is a transfermarkt name. Defaults to False.
   :type transfermarkt_name: bool
   :return: team transfers
   :rtype: list 

.. py:function:: .transfermarkt.tm_team_player_data(club: str, season: str, domain: str = "us", team_id: int = None, transfermarkt_name: bool = False) -> list

   Extracts basic player information for each player in a squad including basic player information, market value, and contract expiration

   :param club: club name
   :type club: str
   :param season: year at start of season
   :type season: str or int
   :param domain: domain to use for transfermarkt. Defaults to us.
   :type domain: str
   :param team_id: transfermarkt team id. Defaults to None.
   :type team_id: int
   :param transfermarkt_name: if True, club is a transfermarkt name. Defaults to False.
   :type transfermarkt_name: bool
   :return: squad players
   :rtype: list  
  
Helper functions
----------------
   
.. py:function:: .transfermarkt.tm_player_injury_scraper(pageSoup) -> list

   Helper function extracts player injury history

   :param pageSoup: bs4 object of player page referenced in url
   :type pageSoup: bs4
   :return: player injuries for specific page
   :rtype: list
   
.. py:function:: .transfermarkt.tm_format_currency(value: str) -> float

   Helper function to convert values from string to float values

   :param value: raw value of fee or market value
   :type value: str
   :return: converted value
   :rtype: float
