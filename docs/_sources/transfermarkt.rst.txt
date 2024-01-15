Transfermarkt
=============

Complete list of all transfermarkt functions

Player functions
----------------

.. py:function:: .transfermarkt.tm_player_data(url: str, html_file: BeautifulSoup = None, json_file_mv: json = None, json_file_transfers: json = None, save_files: bool = False) -> tuple

   Extracts metadata, market value history, and transfer history for a given player

   :param url: path of transfermarkt player page
   :type url: str
   :param html_file: pageSoup html file of profile page. Defaults to None.
   :type html_file: BeautifulSoup or None
   :param json_file_mv: json file of player market value history. Defaults to None.
   :type json_file_mv: json or None
   :param json_file_transfers: json file of player transfer history. Defaults to None.
   :type json_file_transfers: json or None
   :param save_files: whether to save html and json files. Defaults to False.
   :type save_files: bool
   :return: player metadata, historical market values, transfer history, BeautifulSoup file of player page (optional), json file of market value history (optional), and json file of transfer history (optional)
   :rtype: (dict, list, list, BeautifulSoup, json, json) or (dict, list, list)

.. py:function:: .transfermarkt.tm_player_injury(pageSoup) -> list

   Extracts player injury history and equipped to handle players with multiple pages of injuries

   :param pageSoup: bs4 object of injury page for player referenced in url
   :type pageSoup: bs4
   :return: player injuries
   :rtype: list
 
.. py:function:: .transfermarkt.tm_player_market_value(json_file: json = None, player_id: str = None) -> list

   Extracts date, team, and market value from highchart

   :param json_file: json file of player market value history. Defaults to None.
   :type json_file: json or None
   :param player_id: transfermarkt player id. Defaults to None.
   :type player_id: str or None
   :return: market value of player by date
   :rtype: list
 
.. py:function:: .transfermarkt.tm_player_metadata(pageSoup=None, url: str = None) -> dict:

   Extracts general player information (biographical, club, contract, market value, and miscellaneous)

   :param pageSoup: bs4 object of player page referenced in url. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of transfermarkt player page. Defaults to None.
   :type url: str or None
   :return: player metadata
   :rtype: dict
   
.. py:function:: .transfermarkt.tm_player_transfers(json_file: json = None, player_id: str = None) -> list

   Extracts player transfer information

   :param json_file: json file of player transfer history. Defaults to None.
   :type json_file: json or None
   :param player_id: transfermarkt player id. Defaults to None.
   :type player_id: str or None
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

.. py:function:: .transfermarkt.tm_team_staff(club: str = None, team_id: int = None, pageSoup = None, url: str = None) -> list

   Extracts team staff information

   :param club: club name
   :type club: str
   :param team_id: transfermarkt team id. Defaults to None.
   :type team_id: int
   :param pageSoup: bs4 object of staff page for team referenced in url. Defaults to None.
   :type pageSoup: bs4
   :param url: path of transfermarkt staff page. Defaults to None.
   :type url: str
   :return: team staff
   :rtype: list  

.. py:function:: .transfermarkt.tm_team_staff_history(club: str = None, team_id: int = None, pageSoup = None, url: str = None, role: str = None) -> list

   Extracts historical team staff information for a given role

   :param club: club name
   :type club: str
   :param team_id: transfermarkt team id. Defaults to None.
   :type team_id: int
   :param pageSoup: bs4 object of staff page for team referenced in url. Defaults to None.
   :type pageSoup: bs4
   :param url: path of transfermarkt staff page. Defaults to None.
   :type url: str
   :param role: role of staff member. Defaults to None.
   :type role: str
   :return: team role staff history
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
