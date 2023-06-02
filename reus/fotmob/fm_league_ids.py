import pandas as pd


def fm_league_ids(
    competition_type: str = None,
    competition_name: str = None,
    ccode: str = None,
    country: str = None,
    gender: str = None,
) -> pd.Series:
    """Returns a series of league ids

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
        competition_name (str or list, optional): name of competition. Defaults to None.
        ccode (str or list, optional): country code of competition. Defaults to None.
        country (str or list, optional): country of competition. Defaults to None.
        gender (str or list, optional): gender of competition. Defaults to None. \n
            'M' \n
            'W'

    Returns:
        series: league ids
    """

    df = pd.read_csv(
        "https://raw.githubusercontent.com/ian-shepherd/reus_data/main/raw-data/fotmob_leagues.csv",
        keep_default_na=False,
        encoding_errors="ignore",
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

    return df.id
