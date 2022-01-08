Functions
=========

Complete list of all functions of reus package


General helper
--------------

.. py:function:: .fbref.get_page_soup(url)

   Returns html of a given url

   :param url: complete url
   :type url: str
   :return: pageSoup
   :rtype: bs4 object



Fbref
-----
Functions to extract football reference data

Match functions
###############
.. py:function:: .fbref.fb_match_data(url)

   Extracts metadata and statistics for a given match that includes StatsBomb data

   :param str url: path of fbref match
   :return: match data
   :rtype: tuple
   
.. py:function:: .fbref.fb_match_defensive_actions_stats(pageSoup)

   Extracts defensive stats for each player in a given match that includes StatsBomb data

   :param pageSoup: html document of a match
   :type pageSoup: bs4
   :return: defensive stats for home and away team
   :rtype: (list, list)
   
.. py:function:: .fbref.fb_match_keeper_stats(pageSoup)

   Extracts goalkeeping stats for each keeper in a given match that includes StatsBomb data

   :param pageSoup: html document of a match
   :type pageSoup: bs4
   :return: goalkeeping stats for home and away team
   :rtype: (list, list)   
   
.. py:function:: .fbref.fb_match_lineups(pageSoup)

   Extracts matchday squad information (formation, starters, bench) for a given match

   :param pageSoup: html document of a match
   :type pageSoup: bs4
   :return: squad information
   :rtype: dict   

.. py:function:: .fbref.fb_match_metadata(pageSoup)

   Extracts general information (teams, managers, captains, date, time, venue, attendance, score, xG) for a given match

   :param pageSoup: html document of a match
   :type pageSoup: bs4
   :return: (metadata, officials)
   :rtype: (dict, dict)
   
.. py:function:: .fbref.fb_match_misc_stats(pageSoup)

   Extracts miscellaneous stats for each player in a given match that includes StatsBomb data

   :param pageSoup: html document of a match
   :type pageSoup: bs4
   :return: miscellaneous stats for home and away team
   :rtype: (list, list)   
   
.. py:function:: .fbref.fb_match_passing_stats(pageSoup)

   Extracts passing stats for each player in a given match that includes StatsBomb data

   :param pageSoup: html document of a match
   :type pageSoup: bs4
   :return: passing stats for home and away team
   :rtype: (list, list)

.. py:function:: .fbref.fb_match_passing_type_stats(pageSoup)

   Extracts passing type stats for each player in a given match that includes StatsBomb data

   :param pageSoup: html document of a match
   :type pageSoup: bs4
   :return: passing type stats for home and away team
   :rtype: (list, list)

.. py:function:: .fbref.fb_match_possession_stats(pageSoup)

   Extracts possession stats for each player in a given match that includes StatsBomb data

   :param pageSoup: html document of a match
   :type pageSoup: bs4
   :return: possession stats for home and away team
   :rtype: (list, list)

.. py:function:: .fbref.fb_match_shots(pageSoup)

   Extracts shots for a given match that includes StatsBomb data

   :param pageSoup: html document of a match
   :type pageSoup: bs4
   :return: shots for the match
   :rtype: list[str]
   
.. py:function:: .fbref.fb_match_summary(pageSoup)

   Extracts events (goals, bookings, and substitutions) from match summary for a given match

   :param pageSoup: html document of a match
   :type pageSoup: bs4
   :return: events
   :rtype: list[str]

.. py:function:: .fbref.fb_match_summary_stats(pageSoup)

   Extracts summary statistics for each player in a given match that includes StatsBomb data

   :param pageSoup: html document of a match
   :type pageSoup: bs4
   :return: summary stats for home and away team
   :rtype: (list, list)
   
.. py:function:: .fbref.fb_match_team_stats(pageSoup)

   Extracts summary stats for each team in a given match

   :param pageSoup: html document of a match
   :type pageSoup: bs4
   :return: summary statistics for each team
   :rtype: dict

 
League functions
################

.. py:function:: .fbref.fb_league_table(url)

   Returns a list of league table and basic information in a season

   :param url: url of a season
   :type url: str
   :return: league table
   :rtype: list[str]

.. py:function:: .fbref.fb_match_urls(pageSoup)

   Returns a list of urls for matches in a season

   :param pageSoup: url of a season
   :type pageSoup: bs4
   :return: match urls for given season
   :rtype: list[str]

.. py:function:: .fbref.fb_season_fixture_urls(country, season_end, gender="M", competition_type="Domestic Leagues - 1st Tier")

   Returns a series of urls for fixture section a season

   :param country: country of league
   :type country: str or list
   :param season_end: year at end of season
   :type season_end: str or list
   :param gender: gender of league
   :type gender: str or list
   :param competition_type: html document of a match
   :type competition_type: str or list
   :return: season fixture urls
   :rtype: series

.. py:function:: .fbref.fb_season_urls(country, season_end, gender="M", competition_type="Domestic Leagues - 1st Tier")

   Returns a series of urls for overview section a season

   :param country: country of league
   :type country: str or list
   :param season_end: year at end of season
   :type season_end: str or list
   :param gender: gender of league
   :type gender: str or list
   :param competition_type: html document of a match
   :type competition_type: str or list
   :return: season urls
   :rtype: series
   
Transfermarkt
-------------
Functions to extract transfermarkt data

Player functions
################

.. py:function:: .transfermarkt.tm_player_data(url, currency='EUR')

   Extracts metadata, market value history, and transfer history for a given player

   :param url: path of transfermarkt player
   :type url: str
   :param currency: desired currency to return for values
   :type currency: str
   :return: (player metadata, market value history, player transfers)
   :rtype: (dict, list, list)

.. py:function:: .transfermarkt.tm_player_injury(pageSoup)

   Extracts player injury history and equipped to handle players with multiple pages of injuries

   :param pageSoup: html document of a player injury page
   :type pageSoup: bs4
   :return: player injuries
   :rtype: list
 
.. py:function:: .transfermarkt.tm_player_market_value(pageSoup)

   Extracts date, team, and market value from highchart

   :param pageSoup: html document of a player
   :type pageSoup: bs4
   :return: market value of player by date
   :rtype: list
 
.. py:function:: .transfermarkt.tm_player_metadata(pageSoup)

   Extracts general player information (biographical, club, contract, market value, and miscellaneous)

   :param pageSoup: html document of a player
   :type pageSoup: bs4
   :return: player metadata
   :rtype: dict
   
.. py:function:: .transfermarkt.tm_player_transfers(pageSoup)

   Extracts player transfer information

   :param pageSoup: html document of a player
   :type pageSoup: bs4
   :return: player transfers
   :rtype: list 


Team functions
##############   

.. py:function:: .transfermarkt.tm_team_player_urls(club, season, currency='EUR')

   Extracts basic player information for each player in a squad including basic player information, market value, and contract expiration

   :param club: club name
   :type club: str
   :param season: year at start of season
   :type season: str or int
   :param currency: desired currency to return for values
   :type currency: str
   :return: squad players
   :rtype: list 

.. py:function:: .transfermarkt.tm_team_transfers(club, season, position_group='All', main_position='All', window='All', currency='EUR')

   Extracts player transfer information

   :param club: club name
   :type club: str
   :param season: year at start of season
   :type season: str or int
   :param position_group: positional group
   :type position_group: str
   :param main_position: main position
   :type main_position: str
   :param window: transfer window
   :type window: str
   :param currency: desired currency to return for values
   :type currency: str
   :return: team transfers
   :rtype: list 
  
  
Helper functions
################
   
.. py:function:: .transfermarkt.tm_player_injury_scraper(pageSoup)

   Helper function extracts player injury history

   :param pageSoup: html document of a player injury page
   :type pageSoup: bs4
   :return: player injuries for specific page
   :rtype: list    
   
.. py:function:: .transfermarkt.tm_format_currency(value)

   Helper function to convert values from string to float values

   :param value: raw value of fee or market value
   :type value: str
   :return: converted value
   :rtype: float    
