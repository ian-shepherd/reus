import pandas as pd
import numpy as np


def generate_standings(
    df: pd.DataFrame, matches: str = "All", xG: bool = False
) -> pd.DataFrame:
    """Returns a dataframe of league standings from given match results. \n
    xPts are calculated using the xGD of each match.

    Args:
        df (pd.DataFrame): dataframe of match results
        matches (str, optional): type of matches to include in standings. Defaults to "All". \n
            "All": all matches \n
            "Home": only home matches \n
            "Away": only away matches
        xG (bool, optional): whether to include expected calculations. Defaults to False.

    Returns:
        dataframe: league standings
    """

    assert matches in [
        "All",
        "Home",
        "Away",
    ], "matches must be one of 'All', 'Home', or 'Away'"

    # subset data
    cols = ["team_x", "team_y", "score_x", "score_y", "date"]
    if "xg_x" in df.columns:
        cols += ["xg_x", "xg_y"]

    df = df.loc[:, cols]

    # generate home results
    home = df.loc[:, ["team_x", "score_x", "score_y", "xg_x", "xg_y", "date"]].rename(
        columns={
            "team_x": "Team",
            "score_x": "GF",
            "score_y": "GA",
            "xg_x": "xG",
            "xg_y": "xGA",
        }
    )
    away = df.loc[:, ["team_y", "score_y", "score_x", "xg_y", "xg_x", "date"]].rename(
        columns={
            "team_y": "Team",
            "score_y": "GF",
            "score_x": "GA",
            "xg_y": "xG",
            "xg_x": "xGA",
        }
    )
    if matches == "All":
        df = pd.concat([home, away])
    elif matches == "Home":
        df = home
    elif matches == "Away":
        df = away

    # generate matches playerd
    df["MP"] = 1

    # generate points
    df["Pts"] = np.where(df.GF > df.GA, 3, np.where(df.GF == df.GA, 1, 0))

    # goal difference
    df["GD"] = df.GF - df.GA

    # generate expected sections
    if xG:
        df["xGD"] = df.xG - df.xGA
        # https://theshortfuse.sbnation.com/2017/11/15/16655916/how-to-calculate-xpoints-analysis-stats-xg
        df["xPts"] = pd.cut(
            df.xGD,
            bins=[-10, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 10],
            labels=[0.1, 0.3, 0.5, 0.7, 1.5, 2.0, 2.3, 2.7],
        ).astype(float)

    else:
        df["xG"] = None
        df["xGA"] = None
        df["xGD"] = None
        df["xPts"] = None

    # generate wins, draws, losses
    df["W"] = np.where(df.GF > df.GA, 1, 0)
    df["D"] = np.where(df.GF == df.GA, 1, 0)
    df["L"] = np.where(df.GF < df.GA, 1, 0)

    # Last 5 matches
    last_5 = df.sort_values(by="date", ascending=False).groupby("Team").head(5)
    last_5["result"] = last_5[["W", "D", "L"]].idxmax(axis=1)
    last_5 = last_5.groupby("Team")["result"].apply("".join).reset_index()

    # generate table
    df = (
        df.groupby("Team")
        .agg(
            {
                "MP": "sum",
                "W": "sum",
                "D": "sum",
                "L": "sum",
                "GF": "sum",
                "GA": "sum",
                "GD": "sum",
                "Pts": "sum",
                "xG": "sum",
                "xGA": "sum",
                "xGD": "sum",
                "xPts": "sum",
            }
        )
        .reset_index()
    )

    # per match stats
    df["Pts/MP"] = round(df.Pts / df.MP, 2)
    if xG:
        df["xGD/90"] = round(df.xGD / df.MP, 2)

    # generate form
    df["Form"] = last_5.result

    # order table
    df = df.sort_values(by=["Pts", "GD", "GF"], ascending=False).reset_index(drop=True)
    df.reset_index(inplace=True)
    df.rename(columns={"index": "Pos"}, inplace=True)
    df["Pos"] += 1

    # remove unnecessary columns
    if xG:
        pass
    else:
        df.drop(columns=["xG", "xGA", "xGD", "xPts"], inplace=True)

    return df
