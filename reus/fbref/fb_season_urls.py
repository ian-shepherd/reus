import pandas as pd


def fb_season_urls(
    competition_type: str = None,
    competition_name: str = None,
    country: str = None,
    gender: str = None,
    governing_body: str = None,
    tier: str = None,
    season_end_year: str = None,
    stats_bomb: str = None,
):
    """Returns a series of urls for overview section of a season

    Args:
        competition_type (str or list, optional): type of competition. Defaults to None.
        competition_name (str or list, optional): name of competition. Defaults to None.
        country (str or list, optional): country of competition. Defaults to None.
        gender (str or list, optional): gender of competition. Defaults to None.
        governing_body (str or list, optional): governing body of competition. Defaults to None.
        tier (str or list, optional): tier of competition. Defaults to None.
        season_end_year (str or list, optional): year at end of competition. Defaults to None.
        stats_bomb (str or list, optional): flag for if statsbomb data is available. Defaults to None.

    Returns:
        series: season urls
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

    # Stats bomb
    if stats_bomb is None:
        stats_bomb = df.stats_bomb.unique()
    elif not isinstance(stats_bomb, list):
        stats_bomb = [stats_bomb]

    df = df[df.stats_bomb.isin(stats_bomb)]

    return df["seasons_urls"]
