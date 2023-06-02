import json
from urllib.request import urlopen
import pandas as pd


def fm_season_stat_leaders(
    league_id: str, team_or_player: str, stat_name: list, json_file: json = None
) -> pd.DataFrame:
    """Returns top 3 stat leaders of a given league

    Args:
        league_id (str): id of a league
        team_or_player (str): 'teams' or 'players'
        stat_name (list): name of stats. See documentation for list of available stats.
        json_file (json, optional): json file of stat data. Defaults to None.

    Returns:
        dataframe: stat leaders
    """

    assert team_or_player in [
        "teams",
        "players",
    ], "team_or_player must be one of 'teams' or 'players'"

    if isinstance(stat_name, str):
        stat_name = [stat_name]

    if json_file is None:
        url = f"https://www.fotmob.com/api/leagues?id={league_id}"

        response = urlopen(url)
        data = json.loads(response.read())
    else:
        data = json_file

    data = data["stats"][team_or_player]  # [stat_name]
    data = [d for d in data if d.get("header") in stat_name]

    df = pd.DataFrame(data[0].get("topThree"))
    df["stat_name"] = data[0].get("header")
    df["all_url"] = data[0].get("fetchAllUrl")
    df = df.loc[:, ["stat_name", "id", "name", "teamName", "value", "all_url"]]
    for d in data[1:]:
        df_ = pd.DataFrame(d.get("topThree"))
        df_["stat_name"] = d.get("header")
        df_["all_url"] = d.get("fetchAllUrl")
        df = pd.concat([df, df_], join="inner", ignore_index=True)

    if team_or_player == "teams":
        df.drop(columns=["teamName"], inplace=True)

    return df
