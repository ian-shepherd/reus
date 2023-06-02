import json
from urllib.request import urlopen
import pandas as pd


def fm_league_table(league_id: str, matches="All", json_file: json = None) -> dict:
    """Returns standing of a given league

    Args:
        league_id (str): id of a league
        matches (str, optional): type of matches to include in standings. Defaults to "All". \n
            'All' \n
            'Home' \n
            'Away' \n
            'Form'
        json_file (json, optional): json file of league page. Defaults to None.

    Returns:
        dictionary: league standings
    """

    assert matches in [
        "All",
        "Home",
        "Away",
        "Form",
    ], "matches must be one of 'All', 'Home', 'Away', or 'Form'"

    if json_file is None:
        url = f"https://www.fotmob.com/api/leagues?id={league_id}"

        response = urlopen(url)
        data = json.loads(response.read())
    else:
        data = json_file

    mydict = {}
    try:
        name = data["table"][0]["data"]["leagueName"]
        mydict[name] = pd.DataFrame(data["table"][0]["data"]["table"][matches.lower()])
    except KeyError:
        for i in range(len(data["table"][0]["data"]["tables"])):
            name = data["table"][0]["data"]["tables"][i]["leagueName"]
            mydict[name] = pd.DataFrame(
                (data["table"][0]["data"]["tables"][i]["table"][matches.lower()])
            )

    return mydict
