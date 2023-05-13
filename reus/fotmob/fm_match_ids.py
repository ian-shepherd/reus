import json
from urllib.request import urlopen


def fm_match_ids(
    match_date: str,
    ccode: str = None,
    name: str = None,
    league_id: int = None,
) -> list:
    """Returns a list of match ids for a given date

    Args:
        match_date (str): date of matches in format YYYY-MM-DD
        ccode (str): country code of a league. Defaults to None.
        name (str): name of a league. Defaults to None.
        league_id (int): league id of a league. Defaults to None.

    Returns:
        list: match ids
    """

    if not isinstance(ccode, list):
        ccode = [ccode]

    if not isinstance(name, list):
        name = [name]

    if not isinstance(league_id, list):
        league_id = [league_id]

    url = f"https://www.fotmob.com/api/matches?date={match_date}"

    response = urlopen(url)
    data = json.loads(response.read())

    myList = []
    for league in data.get("leagues"):
        if ccode != [None] and not league.get("ccode") in ccode:
            continue

        if name != [None] and not league.get("name") in name:
            continue

        if league_id != [None] and not league.get("primaryId") in league_id:
            continue

        for match in league.get("matches"):
            myList.append(match.get("id"))

    return myList
