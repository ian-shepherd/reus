import pandas as pd


def fb_season_fixture_urls(
    competition_type: str = None,
    competition_name: str = None,
    country: str = None,
    gender: str = None,
    governing_body: str = None,
    tier: str = None,
    season_end_year: int = None,
    advanced: str = None,
) -> pd.Series:
    """Returns a series of urls for fixture section of a season

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
        country (str or list, optional): country of competition. Defaults to None.
        gender (str or list, optional): gender of competition. Defaults to None.
            'M' \n
            'W'
        governing_body (str or list, optional): governing body of competition. Defaults to None. \n
            'AFC' \n
            'CAF' \n
            'CONMEBOL' \n
            'CONCACAF' \n
            'OFC' \n
            'UEFA' \n
            'FIFA' \n
            ''
        tier (str or list, optional): tier of competition. Defaults to None. \n
            '1st' \n
            '2nd' \n
            '3rd' \n
            '4th' \n
            '5th' \n
            'Youth' \n
            ''
        season_end_year (int or list, optional): year at end of competition. Defaults to None.
        advanced (str or list, optional): flag for if advanced data is available. Defaults to None. \n
            'Y' \n
            'N'

    Returns:
        series: season fixture urls
    """

    df = pd.read_csv(
        "https://raw.githubusercontent.com/ian-shepherd/reus_data/main/raw-data/all_competitions.csv",
        keep_default_na=False,
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

    # Governing body
    if governing_body is None:
        governing_body = df.governing_body.unique()
    elif not isinstance(governing_body, list):
        governing_body = [governing_body]

    df = df[df.governing_body.isin(governing_body)]

    # Tier
    if tier is None:
        tier = df.tier.unique()
    elif not isinstance(tier, list):
        tier = [tier]

    df = df[df.tier.isin(tier)]

    # Season end
    if season_end_year is None:
        season_end_year = df.season_end_year.unique()
    elif not isinstance(season_end_year, list):
        season_end_year = [season_end_year]

    df = df[df.season_end_year.isin(season_end_year)]

    # Advanced stats
    if advanced is None:
        advanced = df.advanced.unique()
    elif not isinstance(advanced, list):
        advanced = [advanced]

    df = df[df.advanced.isin(advanced)]

    return df["fixtures_url"]
