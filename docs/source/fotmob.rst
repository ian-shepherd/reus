Fotmob
======

Complete list of all fotmob functions

Functions
---------

.. py:function:: .fotmob.fm_league_matches(league_id: str, json_file: json = None) -> pd.DataFrame:

    Returns matches of a given league

    :param league_id: id of a league
    :type league_id: str
    :param json_file: season of a league. Use / divider for leagues over 2 calendar years. Defaults to None.
    :type json_file: json or None
    :return: league matches
    :rtype: dataframe

.. py:function:: .fotmob.fm_league_table(league_id: str, season: str = None, matches="All", json_file: json = None) -> dict:

    Returns standing of a given league

    :param league_id: id of a league
    :type league_id: str
    :param season: season of a league. Use / divider for leagues over 2 calendar years. Defaults to None.
    :type season: str or None
    :param matches: type of matches to include in standings. Defaults to "All".
    
        - ``All``
        - ``Home``
        - ``Away``
        - ``Form``
    
    :type matches: str
    :param json_file: json file of league page. Defaults to None.
    :type json_file: json or None
    :return: league standings
    :rtype: dict

.. py:function:: .fotmob.fm_leagues(competition_type: str = None, competition_name: str = None, ccode: str = None, country: str = None, gender: str = None, league_id: str = None, league_url: str = None) -> pd.DataFrame

    Returns a dataframe of league information

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
    :param ccode: country code of a league. Defaults to None.
    :type ccode: str or None
    :param country: country of a league. Defaults to None.
    :param gender: gender of competition. Defaults to None.

      - ``M``
      - ``W``
      
    :type gender: str, list, or None
    :type country: str or None
    :param league_id: league id of a league. Defaults to None.
    :type league_id: str or None
    :param league_url: url of a league. Defaults to None.
    :type league_url: str or None
    :return: league information
    :rtype: dataframe

.. py:function:: .fotmob.fm_match_data(match_id: str, save_json: bool = False, json_file: json = None) -> tuple

    Returns metadata and match data for a given match id

    :param match_id: id of a match
    :type match_id: str
    :param save_json: whether to save json of match page. Defaults to False.
    :type save_json: bool
    :param json_file: json file of match page. Defaults to None.
    :type json_file: json or None
    :return: match data and json of match page (optional)
    :rtype: (dict, list, dict, list, list, list, list, list, list, list, json) or (dict, list, dict, list, list, list, list, list, list, list)

.. py:function:: .fotmob.fm_match_ids(match_date: str, ccode: str = None, name: str = None, league_id: str = None) -> list

    Returns a list of match ids for a given date

    :param match_date: date of matches in format YYYYMMDD
    :type match_date: str
    :param ccode: country code of a league. Defaults to None.
    :type ccode: str or None
    :param name: name of a league. Defaults to None.
    :type name: str or None
    :param league_id: league id of a league. Defaults to None.
    :type league_id: str or None
    :return: match ids
    :rtype: list
    

.. py:function:: .fotmob.fm_season_stat_leaders(league_id: str, team_or_player: str, stat_name: list, season: str = None, json_file: json = None) -> pd.DataFrame:

    Returns top 3 stat leaders of a given league

    :param league_id: id of a league
    :type league_id: str
    :param team_or_player: whether to return team or player stat leaders. Defaults to "player".
    
        - ``player``
        - ``team``

    :type team_or_player: str
    :param stat_name: name of stats.

        Player stats:

        - ``Accurate long balls per 90``
        - ``Accurate passes per 90``
        - ``Assists``
        - ``Big chances created``
        - ``Big chances missed``
        - ``Blocks per 90``
        - ``Chances created``
        - ``Clean sheets``
        - ``Clearances per 90``
        - ``Expected assist (xA)``
        - ``Expected assist (xA) per 90``
        - ``Expected goals (xG)``
        - ``Expected goals (xG) per 90``
        - ``Expected goals on target (xGOT)``
        - ``FotMob rating``
        - ``Fouls committed per 90``
        - ``Goals + Assists``
        - ``Goals conceded per 90``
        - ``Goals per 90``
        - ``Goals prevented``
        - ``Interceptions per 90``
        - ``Penalties conceded``
        - ``Penalties won``
        - ``Possession won final 3rd per 90``
        - ``Red cards``
        - ``Save percentage``
        - ``Saves per 90``
        - ``Shots on target per 90``
        - ``Shots per 90``
        - ``Successful dribbles per 90``
        - ``Successful tackles per 90``
        - ``Top scorer``
        - ``xG + xA per 90``
        - ``Yellow cards``

        Team stats:

        - ``Accurate crosses per match``
        - ``Accurate long balls per match``
        - ``Accurate passes per match``
        - ``Average possession``
        - ``Big chances``
        - ``Big chances missed``
        - ``Clean sheets``
        - ``Clearances per match``
        - ``Expected goals``
        - ``FotMob rating``
        - ``Fouls per match``
        - ``Goals conceded per match``
        - ``Goals per match``
        - ``Interceptions per match``
        - ``Penalties awarded``
        - ``Penalties conceded``
        - ``Possession won final 3rd per match``
        - ``Red cards``
        - ``Saves per match``
        - ``Shots on target per match``
        - ``Successful tackles per match``
        - ``xG conceded``
        - ``Yellow cards``

    :type stat_name: list
    :param season: season of a league. Use / divider for leagues over 2 calendar years. Defaults to None.
    :type season: str or None
    :param json_file: json file of stat data. Defaults to None.
    :type json_file: json or None
    :return: stat leaders
    :rtype: dataframe

.. py:function:: .fotmob.fm_season_stats(league_id: str, team_or_player: str, stat_name: list, season: str = None, json_file: json = None) -> pd.DataFrame:

    Returns complete list of stat leaders of a given league

    :param league_id: id of a league
    :type league_id: str
    :param team_or_player: whether to return team or player stat leaders. Defaults to "player".
    
        - ``player``
        - ``team``

    :type team_or_player: str
    :param stat_name: name of stats.

        Player stats:

        - ``Accurate long balls per 90``
        - ``Accurate passes per 90``
        - ``Assists``
        - ``Big chances created``
        - ``Big chances missed``
        - ``Blocks per 90``
        - ``Chances created``
        - ``Clean sheets``
        - ``Clearances per 90``
        - ``Expected assist (xA)``
        - ``Expected assist (xA) per 90``
        - ``Expected goals (xG)``
        - ``Expected goals (xG) per 90``
        - ``Expected goals on target (xGOT)``
        - ``FotMob rating``
        - ``Fouls committed per 90``
        - ``Goals + Assists``
        - ``Goals conceded per 90``
        - ``Goals per 90``
        - ``Goals prevented``
        - ``Interceptions per 90``
        - ``Penalties conceded``
        - ``Penalties won``
        - ``Possession won final 3rd per 90``
        - ``Red cards``
        - ``Save percentage``
        - ``Saves per 90``
        - ``Shots on target per 90``
        - ``Shots per 90``
        - ``Successful dribbles per 90``
        - ``Successful tackles per 90``
        - ``Top scorer``
        - ``xG + xA per 90``
        - ``Yellow cards``

        Team stats:

        - ``Accurate crosses per match``
        - ``Accurate long balls per match``
        - ``Accurate passes per match``
        - ``Average possession``
        - ``Big chances created``
        - ``Big chances missed``
        - ``Clean sheets``
        - ``Clearances per match``
        - ``Expected goals``
        - ``FotMob rating``
        - ``Fouls per match``
        - ``Goals conceded per match``
        - ``Goals per match``
        - ``Interceptions per match``
        - ``Penalties awarded``
        - ``Penalties conceded``
        - ``Possession won final 3rd per match``
        - ``Red cards``
        - ``Saves per match``
        - ``Shots on target per match``
        - ``Successful tackles per match``
        - ``xG conceded``
        - ``Yellow cards``

    :type stat_name: list
    :param season: season of a league. Use / divider for leagues over 2 calendar years. Defaults to None.
    :type season: str or None
    :param json_file: json file of stat data. Defaults to None.
    :type json_file: json or None
    :return: stat leaders
    :rtype: dataframe

