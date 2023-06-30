import pandas as pd


def fb_season_urls(
    competition_type: str = None,
    competition_name: str = None,
    country: str = None,
    gender: str = None,
    governing_body: str = None,
    tier: str = None,
    season_end_year: int = None,
    advanced: str = None,
) -> pd.Series:
    """Returns a series of urls for overview section of a season

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
        series: season urls
    """

    df = pd.read_csv(
        "https://raw.githubusercontent.com/ian-shepherd/reus_data/main/raw-data/all_competitions.csv",
        keep_default_na=False,
    )

    filters = {
        "competition_type": competition_type,
        "competition_name": competition_name,
        "country": country,
        "gender": gender,
        "governing_body": governing_body,
        "tier": tier,
        "season_end_year": season_end_year,
        "advanced": advanced,
    }

    for column, value in filters.items():
        if value is not None:
            if not isinstance(value, list):
                value = [value]
            df = df[df[column].isin(value)]

    return df["seasons_urls"]
