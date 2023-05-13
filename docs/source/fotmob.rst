Fotmob
======

Complete list of all fotmob functions

Functions
---------
.. py:function:: .fotmob.fm_leagues(ccode: str = None, country: str = None, league_id: str = None, name: str = None) -> pd.DataFrame

    Returns a dataframe of league information

    :param ccode: country code of a league. Defaults to None.
    :type ccode: str or None
    :param country: country of a league. Defaults to None.
    :type country: str or None
    :param league_id: league id of a league. Defaults to None.
    :type league_id: str or None
    :param name: name of a league. Defaults to None.
    :type name: str or None
    :return: league information
    :rtype: dataframe

.. py:function:: .fotmob.fm_match_data(match_id: str) -> tuple

    Returns metadata and match data for a given match id

    :param match_id: id of a match
    :type match_id: str
    :return: match data and json of match page (optional)
    :rtype: (dict, list, list, list, list, list, list, json) or (dict, list, list, list, list, list, list)

.. py:function:: .fotmob.fm_match_ids(match_date: str, ccode: str = None, name: str = None, league_id: str = None) -> list

    Returns a list of match ids for a given date

    :param match_date: date of matches in format YYYY-MM-DD
    :type match_date: str
    :param ccode: country code of a league. Defaults to None.
    :type ccode: str or None
    :param name: name of a league. Defaults to None.
    :type name: str or None
    :param league_id: league id of a league. Defaults to None.
    :type league_id: str or None
    :return: match ids
    :rtype: list
    

