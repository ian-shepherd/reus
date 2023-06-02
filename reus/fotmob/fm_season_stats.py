import requests
from .fm_season_stat_leaders import fm_season_stat_leaders
import pandas as pd
import json


def fm_season_stats(
    league_id: str,
    team_or_player: str,
    stat_name: str,
    url: str = None,
    json_file: json = None,
) -> pd.DataFrame:
    """Returns complete list of stat leaders of a given league

    Args:
        league_id (str): id of a league
        team_or_player (str): 'teams' or 'players'
        stat_name (str, optional): name of stat. See documentation for list of available stats. Defaults to None.
        url (str, optional): url of stat leaders. Defaults to None.
        json_file (json, optional): json file of stat data. Defaults to None.

    Returns:
        dataframe: stat leaders
    """

    assert team_or_player in [
        "teams",
        "players",
    ], "team_or_player must be one of 'teams' or 'players'"

    if url is None and json_file is None:
        leaders = fm_season_stat_leaders(league_id, team_or_player, stat_name)
        url = leaders["all_url"].iloc[0]

        response = requests.get(url)
        data = response.json()
    else:
        data = json_file

    data = data.get("TopLists")
    df = pd.DataFrame(data[0])

    expanded_df = pd.json_normalize(df.StatList)

    df = pd.concat([df, expanded_df], axis=1)
    df.drop(
        columns=[
            "StatList",
            "LocalizedTitleId",
            "LocalizedSubtitleId",
            "StatFormat",
            "SubstatFormat",
            "StatDecimals",
            "SubstatDecimals",
            "StatLocation",
            "Category",
            "LocalizedCategoryId",
        ],
        inplace=True,
    )

    return df
