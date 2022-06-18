Transfermarkt
=============

Complete list of all transfermarkt functions

Player functions
----------------

.. py:function:: .transfermarkt.tm_player_data(url: str, currency="EUR")

   Extracts metadata, market value history, and transfer history for a given player based on EUR, GBP, or USD currency.

   :param url: path of transfermarkt player page
   :type url: str
   :param currency: desired currency to return for values. Defaults to EUR.
   :type currency: str
   :return: player metadata, historical market values, transfer history
   :rtype: (dict, list, list)

.. py:function:: .transfermarkt.tm_player_injury(pageSoup)

   Extracts player injury history and equipped to handle players with multiple pages of injuries

   :param pageSoup: bs4 object of injury page for player referenced in url
   :type pageSoup: bs4
   :return: player injuries
   :rtype: list
 
.. py:function:: .transfermarkt.tm_player_market_value(pageSoup)

   Extracts date, team, and market value from highchart

   :param pageSoup: bs4 object of player page referenced in url
   :type pageSoup: bs4
   :return: market value of player by date
   :rtype: list
 
.. py:function:: .transfermarkt.tm_player_metadata(pageSoup)

   Extracts general player information (biographical, club, contract, market value, and miscellaneous)

   :param pageSoup: bs4 object of player page referenced in url
   :type pageSoup: bs4
   :return: player metadata
   :rtype: dict
   
.. py:function:: .transfermarkt.tm_player_transfers(pageSoup)

   Extracts player transfer information

   :param pageSoup: bs4 object of player page referenced in url
   :type pageSoup: bs4
   :return: player transfers
   :rtype: list 


Team functions
--------------  

.. py:function:: .transfermarkt.tm_team_player_urls(club: str, season: str, currency="EUR")

   Extracts basic player information for each player in a squad including basic player information, market value, and contract expiration

   :param club: club name
   :type club: str
   :param season: year at start of season
   :type season: str or int
   :param currency: desired currency to return for values. Defaults to EUR.
   :type currency: str
   :return: squad players
   :rtype: list 

.. py:function:: .transfermarkt.tm_team_transfers(club: str, season, position_group="All", main_position="All", window="All", currency="EUR")

   Extracts player transfer information

   :param club: club name
   :type club: str
   :param season: year at start of season
   :type season: str or int
   :param position_group: position group to filter by. Defaults to All.
   :type position_group: str
   :param main_position: main position to filter by. Defaults to All.
   :type main_position: str
   :param window: transfer window to filter by. Defaults to All.
   :type window: str
   :param currency: desired currency to return for values. Defaults to EUR.
   :type currency: str
   :return: team transfers
   :rtype: list 
  
  
Helper functions
----------------
   
.. py:function:: .transfermarkt.tm_player_injury_scraper(pageSoup)

   Helper function extracts player injury history

   :param pageSoup: bs4 object of player page referenced in url
   :type pageSoup: bs4
   :return: player injuries for specific page
   :rtype: list    
   
.. py:function:: .transfermarkt.tm_format_currency(value: str)

   Helper function to convert values from string to float values

   :param value: raw value of fee or market value
   :type value: str
   :return: converted value
   :rtype: float    
