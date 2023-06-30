import pandas as pd


def fm_leagues(
    competition_type: str = None,
    competition_name: str = None,
    ccode: str = None,
    country: str = None,
    gender: str = None,
    league_id: str = None,
    league_url: str = None,
) -> pd.DataFrame:
    """Returns a dataframe of league information

    Args:
        competition_type (str or list, optional): type of competition. Defaults to None. \n
            'Domestic Leagues - 1st Tier' \n
            'Domestic Leagues - 2nd Tier' \n
            'Domestic Leagues - 3rd Tier and Lower' \n
            'Domestic Cups' \n
            'Domestic Youth Leagues' \n
            'Club International Cups' \n
            'National Team Competitions' \n
            'National Team Qualification'
        competition_name (str): name of a league. Defaults to None.
        ccode (str): country code of a league. Defaults to None.
        country (str): country of a league. Defaults to None.
        gender (str or list, optional): gender of competition. Defaults to None. \n
            'M' \n
            'W'
        league_id (str): league id of a league. Defaults to None.
        league_url (str): league url of a league. Defaults to None.

    Returns:
        dataframe: league information
    """

    # fix url to github
    df = pd.read_csv(
        "https://raw.githubusercontent.com/ian-shepherd/reus_data/main/raw-data/fotmob_leagues.csv",
        encoding="latin-1",
    )

    # Competition type
    if competition_type is None:
        competition_type = df.competition_type.unique()
    elif not isinstance(competition_type, list):
        competition_type = [competition_type]

    df = df[df.competition_type.isin(competition_type)]

    # Competition name
    if competition_name is None:
        competition_name = df.competition_name.unique()
    elif not isinstance(competition_name, list):
        competition_name = [competition_name]

    df = df[df.competition_name.isin(competition_name)]

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

    # Gender
    if gender is None:
        gender = df.gender.unique()
    elif not isinstance(gender, list):
        gender = [gender]

    df = df[df.gender.isin(gender)]

    # League ID
    if league_id is None:
        league_id = df.id.unique()
    elif not isinstance(league_id, list):
        league_id = [league_id]

    df = df[df.id.isin(league_id)]

    # League URL
    if league_url is None:
        league_url = df.league_url.unique()
    elif not isinstance(league_url, list):
        league_url = [league_url]

    df = df[df.league_url.isin(league_url)]

    return df
