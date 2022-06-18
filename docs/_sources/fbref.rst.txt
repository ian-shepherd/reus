Fbref
======

Complete list of all football reference functions

Match functions
---------------
.. py:function:: .fbref.fb_match_data(url: str)

   Extracts metadata and statistics for a given match that includes StatsBomb data. This includes summary match statistics for each team, summary stats for away team, passing, defensive, possession and goalkeeping stats

   :param url: path of fbref match page
   :type url: str
   :return: match data
   :rtype: tuple
   
.. py:function:: .fbref.fb_match_defensive_actions_stats(pageSoup=None, url: str = None)

   Extracts defensive stats for each player in a given match that includes StatsBomb data

   :param pageSoup: bs4 object of a match. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref match page. Defaults to None.
   :type url: str or None
   :return: defensive stats for home and away team players
   :rtype: (list, list)
   
.. py:function:: .fbref.fb_match_keeper_stats(pageSoup=None, url: str = None)

   Extracts goalkeeping stats for each keeper in a given match that includes StatsBomb data

   :param pageSoup: bs4 object of a match. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref match page. Defaults to None.
   :type url: str or None
   :return: goalkeeping stats for home and away team players
   :rtype: (list, list)   
   
.. py:function:: .fbref.fb_match_lineups(pageSoup=None, url: str = None)

   Extracts matchday squad information (formation, starters, bench) for a given match

   :param pageSoup: bs4 object of a match. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref match page. Defaults to None.
   :type url: str or None
   :return: squad information
   :rtype: dict   

.. py:function:: .fbref.fb_match_metadata(pageSoup=None, url: str = None)

   Extracts general information (teams, managers, captains, date, time, venue, attendance, score, xG) for a given match

   :param pageSoup: bs4 object of a match. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref match page. Defaults to None.
   :type url: str or None
   :return: (metadata, officials)
   :rtype: (dict, dict)
   
.. py:function:: .fbref.fb_match_misc_stats(pageSoup=None, url: str = None)

   Extracts miscellaneous stats for each player in a given match that includes StatsBomb data

   :param pageSoup: bs4 object of a match. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref match page. Defaults to None.
   :type url: str or None
   :return: miscellaneous stats for home and away team players
   :rtype: (list, list)   
   
.. py:function:: .fbref.fb_match_passing_stats(pageSoup=None, url: str = None)

   Extracts passing stats for each player in a given match that includes StatsBomb data

   :param pageSoup: bs4 object of a match. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref match page. Defaults to None.
   :type url: str or None
   :return: passing stats for home and away team players
   :rtype: (list, list)

.. py:function:: .fbref.fb_match_passing_type_stats(pageSoup=None, url: str = None)

   Extracts passing type stats for each player in a given match that includes StatsBomb data

   :param pageSoup: bs4 object of a match. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref match page. Defaults to None.
   :type url: str or None
   :return: passing type stats for home and away team players
   :rtype: (list, list)

.. py:function:: .fbref.fb_match_possession_stats(pageSoup=None, url: str = None)

   Extracts possession stats for each player in a given match that includes StatsBomb data

   :param pageSoup: bs4 object of a match. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref match page. Defaults to None.
   :type url: str or None
   :return: possession stats for home and away team players
   :rtype: (list, list)

.. py:function:: .fbref.fb_match_shots(pageSoup=None, url: str = None)

   Extracts shots for a given match that includes StatsBomb data

   :param pageSoup: bs4 object of a match. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref match page. Defaults to None.
   :type url: str or None
   :return: shots for the match
   :rtype: list[str]
   
.. py:function:: .fbref.fb_match_summary(pageSoup)

   Extracts events (goals, bookings, and substitutions) from match summary for a given match

   :param pageSoup: bs4 object of a match. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref match page. Defaults to None.
   :type url: str or None
   :return: events
   :rtype: list[str]

.. py:function:: .fbref.fb_match_summary_stats(pageSoup=None, url: str = None)

   Extracts summary statistics for each player in a given match that includes StatsBomb data

   :param pageSoup: bs4 object of a match. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref match page. Defaults to None.
   :type url: str or None
   :return: summary stats for home and away team players
   :rtype: (list, list)
   
.. py:function:: .fbref.fb_match_team_stats(pageSoup=None, url: str = None)

   Extracts summary stats for each team in a given match

   :param pageSoup: bs4 object of a match. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref match page. Defaults to None.
   :type url: str or None
   :return: summary statistics for each team
   :rtype: dict

 
League functions
----------------

.. py:function:: .fbref.fb_league_table(url: str)

   Returns a list of league table and basic information in a season

   :param url: url of a season
   :type url: str
   :return: league table
   :rtype: list[dict]

.. py:function:: .fbref.fb_match_urls(url: str)

   Returns a list of urls for matches in a season

   :param url: url of a season
   :type url: str
   :return: match urls for given season
   :rtype: list[str]

.. py:function:: .fbref.fb_season_fixture_urls(competition_type: str = None, competition_name: str = None, country: str = None, gender: str = None, governing_body: str = None, tier: str = None, season_end_year: int = None, stats_bomb: str = None)

   Returns a series of urls for fixture section of a season

   :param competition_type: type of competition. Defaults to None.
   :type competition_type: str, list, or None
   :param competition_name: name of competition. Defaults to None.
   :type competition_name: str, list, or None
   :param country: country of competition. Defaults to None.
   :type country: str, list, or None
   :param gender: gender of competition. Defaults to None.
   :type gender: str, list, or None
   :param governing_body: governing body of competition. Defaults to None.
   :type governing_body: str, list, or None
   :param tier: tier of competition. Defaults to None.
   :type tier: str, list, or None
   :param season_end: year at end of competition. Defaults to None.
   :type season_end: int, list, or None
   :param stats_bomb: flag for if statsbomb data is available. Defaults to None.
   :type stats_bomb: str, list, or None
   :return: season fixture urls
   :rtype: series

.. py:function:: .fbref.fb_season_urls(competition_type: str = None, competition_name: str = None, country: str = None, gender: str = None, governing_body: str = None, tier: str = None, season_end_year: int = None, stats_bomb: str = None)

   Returns a series of urls for overview section of a season

   :param competition_type: type of competition. Defaults to None.
   :type competition_type: str, list, or None
   :param competition_name: name of competition. Defaults to None.
   :type competition_name: str, list, or None
   :param country: country of competition. Defaults to None.
   :type country: str, list, or None
   :param gender: gender of competition. Defaults to None.
   :type gender: str, list, or None
   :param governing_body: governing body of competition. Defaults to None.
   :type governing_body: str, list, or None
   :param tier: tier of competition. Defaults to None.
   :type tier: str, list, or None
   :param season_end: year at end of competition. Defaults to None.
   :type season_end: int, list, or None
   :param stats_bomb: flag for if statsbomb data is available. Defaults to None.
   :type stats_bomb: str, list, or None
   :return: season urls
   :rtype: series


Team functions
--------------

.. py:function:: .fbref.fb_team_player_advanced_keeper_stats(pageSoup=None, url: str = None)

   Extracts advanced keeper stats for each player in a given team

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: goalkeeper stats for each player
   :rtype: list[dict]
   
.. py:function:: .fbref.fb_team_player_data(url: str)

   Extracts statistics of each player for a given team. This includes summary, passing, defensive, possession, possession, playing time, and goalkeeping stats

   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: player stats
   :rtype: tuple

.. py:function:: .fbref.fb_team_player_defensive_actions_stats(pageSoup=None, url: str = None)

   Extracts defensive action stats for each player in a given team

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: defensive stats for each player
   :rtype: list[dict]
   
.. py:function:: .fbref.fb_team_player_goal_sca_stats(pageSoup=None, url: str = None)

   Extracts shot and goal creating actions for each player in a given team

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: shot and goal creating actions for each player
   :rtype: list[dict]


.. py:function:: .fbref.fb_team_player_keeper_stats(pageSoup=None, url: str = None)

   Extracts basic keeper stats for each player in a given team

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: goalkeeper stats for each player
   :rtype: list[dict]
   
.. py:function:: .fbref.fb_team_player_misc_stats(pageSoup=None, url: str = None)

   Extracts miscellaneous stats for rach player in a given team

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: miscellaneous stats for each player
   :rtype: list[dict]


.. py:function:: .fbref.fb_team_player_passing_stats(pageSoup=None, url: str = None)

   Extracts passing stats for each player in a given team

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: passing stats for each player
   :rtype: list[dict]
   
.. py:function:: .fbref.fb_team_player_passing_type_stats(pageSoup=None, url: str = None)

   Extracts passing type stats for each player in a given team

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: passing type stats for each player
   :rtype: list[dict]


.. py:function:: .fbref.fb_team_player_playing_time_stats(pageSoup=None, url: str = None)

   Extracts playing time stats for each player in a given team

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: playing time for each player
   :rtype: list[dict]
   
.. py:function:: .fbref.fb_team_player_possession_stats(pageSoup=None, url: str = None)

   Extracts possession stats for each player in a given team

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: possession stats for each player
   :rtype: list[dict]


.. py:function:: .fbref.fb_team_player_shooting_stats(pageSoup=None, url: str = None)

   Extracts shooting stats for each player in a given team

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: shooting stats for each player
   :rtype: list[dict]
   
.. py:function:: .fbref.fb_team_player_summary_stats(pageSoup=None, url: str = None)

  Extracts summary stats for each player in a given team

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: summary stats for each player
   :rtype: list[dict]
