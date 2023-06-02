import json
from urllib.request import urlopen
import pandas as pd


def fm_league_matches(league_id: str, json_file: json = None) -> pd.DataFrame:
    """Returns matches of a given league

    Args:
        league_id (str): id of a league
        json_file (json, optional): json file of match data. Defaults to None.

    Returns:
        dataframe: league matches
    """

    if json_file is None:
        url = f"https://www.fotmob.com/api/leagues?id={league_id}"

        response = urlopen(url)
        data = json.loads(response.read())
    else:
        data = json_file

    df = pd.DataFrame(data["matches"]["allMatches"])

    # teams
    df["id_x"] = df["home"].apply(lambda x: x.get("id"))
    df["team_x"] = df["home"].apply(lambda x: x.get("name"))
    df["id_y"] = df["away"].apply(lambda x: x.get("id"))
    df["team_y"] = df["away"].apply(lambda x: x.get("name"))

    # status
    df["utcTime"] = pd.to_datetime(df["status"].apply(lambda x: x.get("utcTime")))
    df["started"] = df["status"].apply(lambda x: x.get("started"))
    df["finished"] = df["status"].apply(lambda x: x.get("finished"))
    df["scoreStr"] = df["status"].apply(lambda x: x.get("scoreStr"))

    df.drop(columns=["home", "away", "status"], inplace=True)

    return df
