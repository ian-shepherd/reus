Fbref
======

Complete list of all football reference functions

Match functions
---------------

.. py:function:: .fbref.fb_match_data(url: str, save_html: bool = False, html_file: BeautifulSoup = None) -> tuple

   Extracts metadata and statistics for a given match that include Opta data. This includes summary match statistics for each team, summary stats for away team, passing, defensive, possession and goalkeeping stats

   :param url: path of fbref match page
   :type url: str
   :param save_html: whether to save html file of match page. Defaults to False.
   :type save_html: bool
   :param html_file: pageSoup html file of match page. Defaults to None.
   :type html_file: BeautifulSoup or None
   :return: match data and BeautifulSoup file of match page (optional)
   :rtype: (dict, dict, dict, list, dict, list, list, list, list, list, list, list, list, list, list, list, list, list, list, list, BeautifulSoup) or (dict, dict, dict, list, dict,
      list, list, list, list, list, list, list, list, list, list, list, list, list, list, list, BeautifulSoup)
   
.. py:function:: .fbref.fb_match_defensive_actions_stats(pageSoup=None, url: str = None) -> tuple

   Extracts defensive action stats for each player in a given match that includes advanced data

   :param pageSoup: bs4 object of a match. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref match page. Defaults to None.
   :type url: str or None
   :return: (defensive stats for home team players, defensive stats for away team players)
   :rtype: (list, list)
   
.. py:function:: .fbref.fb_match_keeper_stats(pageSoup=None, url: str = None) -> tuple

   Extracts goalkeeping stats for each keeper in a given match that includes advanced data

   :param pageSoup: bs4 object of a match. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref match page. Defaults to None.
   :type url: str or None
   :return: (keeper stats for home team players, keeper stats for away team players)
   :rtype: (list, list)
   
.. py:function:: .fbref.fb_match_lineups(pageSoup=None, url: str = None) -> dict

   Extracts matchday squad information (formation, starters, bench) for a given match

   :param pageSoup: bs4 object of a match. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref match page. Defaults to None.
   :type url: str or None
   :return: squad information
   :rtype: dict

.. py:function:: .fbref.fb_match_metadata(pageSoup=None, url: str = None) -> tuple

   Extracts general info (teams, managers, captains, date, time, venue, attendance, score, xG) for a given match

   :param pageSoup: bs4 object of a match. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref match page. Defaults to None.
   :type url: str or None
   :return: (metadata, officials)
   :rtype: (dict, dict)
   
.. py:function:: .fbref.fb_match_misc_stats(pageSoup=None, url: str = None) -> tuple

   Extracts miscellaneous stats for each player in a given match that includes advanced data

   :param pageSoup: bs4 object of a match. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref match page. Defaults to None.
   :type url: str or None
   :return: (miscellaneous stats for home team players, miscellaneous stats for away team players)
   :rtype: (list, list)
   
.. py:function:: .fbref.fb_match_passing_stats(pageSoup=None, url: str = None) -> tuple

   Extracts passing stats for each player in a given match that includes advanced data

   :param pageSoup: bs4 object of a match. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref match page. Defaults to None.
   :type url: str or None
   :return: (passing stats for home team players, passing stats for away team players)
   :rtype: (list, list)

.. py:function:: .fbref.fb_match_passing_type_stats(pageSoup=None, url: str = None) -> tuple

   Extracts passing type stats for each player in a given match that includes advanced data

   :param pageSoup: bs4 object of a match. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref match page. Defaults to None.
   :type url: str or None
   :return: (passing type stats for home team players, passing type stats for away team players)
   :rtype: (list, list)

.. py:function:: .fbref.fb_match_possession_stats(pageSoup=None, url: str = None) -> tuple

   Extracts possession stats for each player in a given match that includes advanced data

   :param pageSoup: bs4 object of a match. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref match page. Defaults to None.
   :type url: str or None
   :return: (possession stats for home team players, possession stats for away team players)
   :rtype: (list, list)

.. py:function:: .fbref.fb_match_shots(pageSoup=None, url: str = None) -> list

   Extracts shots for a given match that includes Opta data

   :param pageSoup: bs4 object of a match. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref match page. Defaults to None.
   :type url: str or None
   :return: shots for the match
   :rtype: list[dict]
   
.. py:function:: .fbref.fb_match_summary_stats(pageSoup=None, url: str = None) -> tuple

   Extracts summary statistics for each player in a given match that includes advanced data

   :param pageSoup: bs4 object of a match. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref match page. Defaults to None.
   :type url: str or None
   :return: (summary stats for home team players, summary stats for away team players)
   :rtype: (list, list)

.. py:function:: .fbref.fb_match_summary(pageSoup=None, url: str = None) -> list

   Extracts events (goals, bookings, and substitutions) from match summary for a given match

   :param pageSoup: bs4 object of a match. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref match page. Defaults to None.
   :type url: str or None
   :return: events
   :rtype: list[dict]

.. py:function:: .fbref.fb_match_team_stats(pageSoup=None, url: str = None) -> dict

   Extracts summary stats for each team in a given match

   :param pageSoup: bs4 object of a match. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref match page. Defaults to None.
   :type url: str or None
   :return: summary statistics for each team
   :rtype: dict

 
League functions
----------------

.. py:function:: .fbref.fb_league_table(url: str) -> list

   Returns a list of league table and basic information in a season

   :param url: url of a season
   :type url: str
   :return: league table
   :rtype: list[dict]

.. py:function:: .fbref.fb_match_urls(url: str) -> list

   Returns a list of urls for matches in a season

   :param url: url of a season
   :type url: str
   :return: match urls for given season
   :rtype: list[str]

.. py:function:: .fbref.fb_season_fixture_urls(competition_type: str = None, competition_name: str = None, country: str = None, gender: str = None, governing_body: str = None, tier: str = None, season_end_year: int = None, advanced: str = None) -> pd.Series

   Returns a series of urls for fixture section of a season

   :param competition_type: type of competition. Defaults to None.
      
      - ``Domestic Leagues - 1st Tier``
      - ``Domestic Leagues - 2nd Tier``
      - ``Domestic Leagues - 3rd Tier and Lower``
      - ``Domestic Cups``
      - ``Domestic Youth Leagues``
      - ``Club International Cups``
      - ``National Team Competitions``
      - ``National Team Qualification``

   :type competition_type: str, list, or None
   :param competition_name: name of competition. Defaults to None.
   :type competition_name: str, list, or None
   :param country: country of competition. Defaults to None.
   :type country: str, list, or None
   :param gender: gender of competition. Defaults to None.

      - ``M``
      - ``W``
      
   :type gender: str, list, or None
   :param governing_body: governing body of competition. Defaults to None.

      - ``AFC``
      - ``CAF``
      - ``CONMEBOL``
      - ``CONCACAF``
      - ``OFC``
      - ``UEFA``
      - ``FIFA``

   :type governing_body: str, list, or None
   :param tier: tier of competition. Defaults to None.
   :type tier: str, list, or None

      - ``1st``
      - ``2nd``
      - ``3rd``
      - ``4th``
      - ``5th``
      - ``Youth``

   :param season_end: year at end of competition. Defaults to None.
   :type season_end: int, list, or None
   :param advanced: flag for if advanced data is available. Defaults to None.

      - ``Y``
      - ``N``

   :type advanced: str, list, or None
   :return: season fixture urls
   :rtype: series

.. py:function:: .fbref.fb_season_urls(competition_type: str = None, competition_name: str = None, country: str = None, gender: str = None, governing_body: str = None, tier: str = None, season_end_year: int = None, advanced: str = None) -> pd.Series

   Returns a series of urls for overview section of a season

   :param competition_type: type of competition. Defaults to None.
      
      - ``Domestic Leagues - 1st Tier``
      - ``Domestic Leagues - 2nd Tier``
      - ``Domestic Leagues - 3rd Tier and Lower``
      - ``Domestic Cups``
      - ``Domestic Youth Leagues``
      - ``Club International Cups``
      - ``National Team Competitions``
      - ``National Team Qualification``

   :type competition_type: str, list, or None
   :param competition_name: name of competition. Defaults to None.
   :type competition_name: str, list, or None
   :param country: country of competition. Defaults to None.
   :type country: str, list, or None
   :param gender: gender of competition. Defaults to None.

      - ``M``
      - ``W``
      
   :type gender: str, list, or None
   :param governing_body: governing body of competition. Defaults to None.

      - ``AFC``
      - ``CAF``
      - ``CONMEBOL``
      - ``CONCACAF``
      - ``OFC``
      - ``UEFA``
      - ``FIFA``

   :type governing_body: str, list, or None
   :param tier: tier of competition. Defaults to None.
   :type tier: str, list, or None

      - ``1st``
      - ``2nd``
      - ``3rd``
      - ``4th``
      - ``5th``
      - ``Youth``

   :param season_end: year at end of competition. Defaults to None.
   :type season_end: int, list, or None
   :param advanced: flag for if advanced data is available. Defaults to None.

      - ``Y``
      - ``N``

   :type advanced: str, list, or None
   :return: season fixture urls
   :rtype: series

.. py:function:: .fbref.fb_team_advanced_keeper_stats(pageSoup=None, url: str = None) -> list

   Extracts advanced keeper stats for each team in a given league

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: (advanced keeper stats for each team, advanced keeper stats against each team)
   :rtype: (list, list)
   
.. py:function:: .fbref.fb_team_data(url: str, html_file: BeautifulSoup = None) -> tuple

   Extracts statistics of each team. This includes summary, shooting, passing, defensive, possession, possession, playing time, and goalkeeping stats

   :param url: path of fbref stats page
   :type url: str
   :param html_file: pageSoup html file of fbref stats page. Defaults to None.
   :type html_file: BeautifulSoup or None
   :return: team data
   :rtype: (list, list, list, list, list, list, list, list, list, list, list, list, list, list, list, list, list, list, list, list, list, list)

.. py:function:: .fbref.fb_team_defensive_actions_stats(pageSoup=None, url: str = None) -> tuple

   Extracts defensive action stats for each team in a given league

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: (defensive action stats for each team, defensive action stats against each team)
   :rtype: (list, list)

.. py:function:: .fbref.fb_team_goal_sca_stats(pageSoup=None, url: str = None) -> tuple

   Extracts shot and goal creating actions stats for each team in a given league

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: (shot and goal creating actions stats for each team, shot and goal creating actions stats against each team)
   :rtype: (list, list)


.. py:function:: .fbref.fb_team_keeper_stats(pageSoup=None, url: str = None) -> tuple

   Extracts keeper stats for each team in a given league

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: (keeper stats for each team, keeper stats against each team)
   :rtype: (list, list)


.. py:function:: .fbref.fb_team_misc_stats(pageSoup=None, url: str = None) -> tuple

   Extracts miscellaneous stats for each team in a given league

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: (miscellaneous stats for each team, miscellaneous stats against each team)
   :rtype: (list, list)


.. py:function:: .fbref.fb_team_passing_stats(pageSoup=None, url: str = None) -> tuple

   Extracts passing stats for each team in a given league

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: (passing stats for each team, passing stats against each team)
   :rtype: (list, list)

.. py:function:: .fbref.fb_team_passing_type_stats(pageSoup=None, url: str = None) -> tuple

   Extracts passing type stats for each team in a given league

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: (passing type stats for each team, passing type stats against each team)
   :rtype: (list, list)

.. py:function:: .fbref.fb_team_playing_time_stats(pageSoup=None, url: str = None) -> tuple

   Extracts playing time stats for each team in a given league

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: (playing time stats for each team, playing time stats against each team)
   :rtype: (list, list)

.. py:function:: .fbref.fb_team_possession_stats(pageSoup=None, url: str = None) -> tuple

   Extracts possession stats for each team in a given league

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: (possession stats for each team, possession stats against each team)
   :rtype: (list, list)

.. py:function:: .fbref.fb_team_shooting_stats(pageSoup=None, url: str = None) -> tuple

   Extracts shooting stats for each team in a given league

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: (shooting stats for each team, shooting stats against each team)
   :rtype: (list, list)

.. py:function:: .fbref.fb_team_summary_stats(pageSoup=None, url: str = None) -> tuple

   Extracts summary stats for each team in a given league

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: (summary stats for each team, summary stats against each team)
   :rtype: (list, list)


Player functions
----------------

.. py:function:: .fbref.fb_player_scouting_report(pageSoup=None, url: str = None, player_url: str = None, comp_league: str = None, position_comp: str = "Primary") -> dict

   Extracts scouting report for a given player

   :param pageSoup: bs4 object of a player's scouting report. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref scouting report page. Defaults to None.
   :type url: str or None
   :param player_url: path of fbref player page. Defaults to None.
   :type player_url: str or None
   :param comp_league: name of comparison league. Defaults to None.
   :type comp_league: str or None
   :param position_comp: primary or secondary position. Defaults to "Primary".
   :type position_comp: str
   :return: complete scouting report for a player
   :rtype: dict

.. py:function:: .fbref.fb_player_match_logs_data(season_end: str, player_id: str) -> dict

   Extracts scouting report for a given player

   :param season_end: ending year of a season
   :type season_end: str
   :param player_id: unique identifier for a player
   :type player_id: str
   :return: match logs for a player in a given season
   :rtype: dict[list]
  
.. py:function:: .fbref.fb_player_match_logs_defensive_actions(pageSoup=None, season_end: str = None, player_id: str = None) -> dict

   Retrieves a players defensive actions match log for a given season

   :param pageSoup: bs4 object of a players defensive actions match log page. Defaults to None.
   :type pageSoup: bs4 or None
   :param season_end: ending year of a season
   :type season_end: str
   :param player_id: unique identifier for a player
   :type player_id: str
   :return: defensive actions match log for a player in a given season
   :rtype: list

.. py:function:: .fbref.fb_player_match_logs_gca_sca(pageSoup=None, season_end: str = None, player_id: str = None) -> dict

   Retrieves a players goal and shot creating actions match log for a given season

   :param pageSoup: bs4 object of a players goal and shot creating actions match log page. Defaults to None.
   :type pageSoup: bs4 or None
   :param season_end: ending year of a season
   :type season_end: str
   :param player_id: unique identifier for a player
   :type player_id: str
   :return: goal and shot creating actions match log for a player in a given season
   :rtype: list

.. py:function:: .fbref.fb_player_match_logs_misc(pageSoup=None, season_end: str = None, player_id: str = None) -> dict

   Retrieves a players miscellaneous match log for a given season

   :param pageSoup: bs4 object of a players miscellaneous match log page. Defaults to None.
   :type pageSoup: bs4 or None
   :param season_end: ending year of a season
   :type season_end: str
   :param player_id: unique identifier for a player
   :type player_id: str
   :return: miscellaneous match log for a player in a given season
   :rtype: list

.. py:function:: .fbref.fb_player_match_logs_passing(pageSoup=None, season_end: str = None, player_id: str = None) -> dict

   Retrieves a players passing match log for a given season

   :param pageSoup: bs4 object of a players passing match log page. Defaults to None.
   :type pageSoup: bs4 or None
   :param season_end: ending year of a season
   :type season_end: str
   :param player_id: unique identifier for a player
   :type player_id: str
   :return: passing match log for a player in a given season
   :rtype: list

.. py:function:: .fbref.fb_player_match_logs_passing_types(pageSoup=None, season_end: str = None, player_id: str = None) -> dict

   Retrieves a players passing type match log for a given season

   :param pageSoup: bs4 object of a players passing type match log page. Defaults to None.
   :type pageSoup: bs4 or None
   :param season_end: ending year of a season
   :type season_end: str
   :param player_id: unique identifier for a player
   :type player_id: str
   :return: passing type match log for a player in a given season
   :rtype: list

.. py:function:: .fbref.fb_player_match_logs_possession(pageSoup=None, season_end: str = None, player_id: str = None) -> dict

   Retrieves a players possession match log for a given season

   :param pageSoup: bs4 object of a players possession match log page. Defaults to None.
   :type pageSoup: bs4 or None
   :param season_end: ending year of a season
   :type season_end: str
   :param player_id: unique identifier for a player
   :type player_id: str
   :return: possession match log for a player in a given season
   :rtype: list

.. py:function:: .fbref.fb_player_match_logs_summary(pageSoup=None, season_end: str = None, player_id: str = None) -> dict

   Retrieves a players summary match log for a given season

   :param pageSoup: bs4 object of a players summary match log page. Defaults to None.
   :type pageSoup: bs4 or None
   :param season_end: ending year of a season
   :type season_end: str
   :param player_id: unique identifier for a player
   :type player_id: str
   :return: summary match log for a player in a given season
   :rtype: list
  

Team functions
--------------

.. py:function:: .fbref.fb_team_player_advanced_keeper_stats(pageSoup=None, url: str = None) -> list

   Extracts advanced keeper stats for each player in a given team

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: goalkeeper stats for each player
   :rtype: list[dict]
   
.. py:function:: .fbref.fb_team_player_data(url: str, html_file: BeautifulSoup = None) -> tuple

   Extracts statistics of each player for a given team. This includes summary, passing, defensive, possession, possession, playing time, and goalkeeping stats

   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :param html_file: pageSoup html file of fbref team page. Defaults to None.
   :type html_file: BeautifulSoup or None
   :return: player stats
   :rtype: (list, list, list, list, list, list, list, list, list, list, list)

.. py:function:: .fbref.fb_team_player_defensive_actions_stats(pageSoup=None, url: str = None) -> list

   Extracts defensive action stats for each player in a given team

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: defensive stats for each player
   :rtype: list[dict]
   
.. py:function:: .fbref.fb_team_player_goal_sca_stats(pageSoup=None, url: str = None) -> list

   Extracts shot and goal creating actions for each player in a given team

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: shot and goal creating actions for each player
   :rtype: list[dict]


.. py:function:: .fbref.fb_team_player_keeper_stats(pageSoup=None, url: str = None) -> list

   Extracts basic keeper stats for each player in a given team

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: goalkeeper stats for each player
   :rtype: list[dict]
   
.. py:function:: .fbref.fb_team_player_misc_stats(pageSoup=None, url: str = None) -> list

   Extracts miscellaneous stats for rach player in a given team

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: miscellaneous stats for each player
   :rtype: list[dict]


.. py:function:: .fbref.fb_team_player_passing_stats(pageSoup=None, url: str = None) -> list

   Extracts passing stats for each player in a given team

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: passing stats for each player
   :rtype: list[dict]
   
.. py:function:: .fbref.fb_team_player_passing_type_stats(pageSoup=None, url: str = None) -> list

   Extracts passing type stats for each player in a given team

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: passing type stats for each player
   :rtype: list[dict]


.. py:function:: .fbref.fb_team_player_playing_time_stats(pageSoup=None, url: str = None) -> list

   Extracts playing time stats for each player in a given team

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: playing time for each player
   :rtype: list[dict]
   
.. py:function:: .fbref.fb_team_player_possession_stats(pageSoup=None, url: str = None) -> list

   Extracts possession stats for each player in a given team

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: possession stats for each player
   :rtype: list[dict]


.. py:function:: .fbref.fb_team_player_shooting_stats(pageSoup=None, url: str = None) -> list

   Extracts shooting stats for each player in a given team

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: shooting stats for each player
   :rtype: list[dict]
   
.. py:function:: .fbref.fb_team_player_summary_stats(pageSoup=None, url: str = None) -> list

  Extracts summary stats for each player in a given team

   :param pageSoup: bs4 object of a team. Defaults to None.
   :type pageSoup: bs4 or None
   :param url: path of fbref team page. Defaults to None.
   :type url: str or None
   :return: summary stats for each player
   :rtype: list[dict]
