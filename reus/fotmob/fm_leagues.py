import pandas as pd


def fm_leagues(
    ccode: str = None, country: str = None, league_id: str = None, name: str = None
) -> pd.DataFrame:
    """Returns a dataframe of league information

    Args:
        ccode (str): country code of a league. Defaults to None.
        country (str): country of a league. Defaults to None.
        league_id (str): league id of a league. Defaults to None.
        name (str): name of a league. Defaults to None.

    Returns:
        dataframe: league information
    """

    # fix url to github
    df = pd.read_csv(
        "https://raw.githubusercontent.com/ian-shepherd/reus_data/main/raw-data/fotmob_leagues.csv",
        encoding="latin-1",
    )

    # Country code
    if ccode is None:
        ccode = df.ccode.unique()
    elif not isinstance(ccode, list):
        ccode = [ccode]

    df = df[df.ccode.isin(ccode)]

    # Country
    if country is None:
        country = df.country.unique()
    elif not isinstance(country, list):
        country = [country]

    df = df[df.country.isin(country)]

    # League ID
    if league_id is None:
        league_id = df.id.unique()
    elif not isinstance(league_id, list):
        league_id = [league_id]

    df = df[df.id.isin(league_id)]

    # Name
    if name is None:
        name = df.name.unique()
    elif not isinstance(name, list):
        name = [name]

    df = df[df.name.isin(name)]

    return df
