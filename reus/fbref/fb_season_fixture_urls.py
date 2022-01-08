import pandas as pd

def fb_season_fixture_urls(country, season_end, gender="M", competition_type="Domestic Leagues - 1st Tier"):
    """
    Returns a series of urls for fixture section a season
    
    Parameters:
    country (string or list): country of league
    season_end (string or list): year at end of season
    gender (string or list): gender of league
    competition_type (string or list): type of competition

    Returns:
    series: season fixture urls
    """

    if not isinstance(country, list):
        country = [country]

    if not isinstance(season_end, list):
        season_end = [season_end]

    if not isinstance(gender, list):
        gender = [gender]

    if not isinstance(competition_type, list):
        competition_type = [competition_type]

    df = pd.read_csv('https://raw.githubusercontent.com/ian-shepherd/reus_data/main/raw-data/all_competitions.csv', keep_default_na=False)
    df = df[df.country.isin(country) & df.season_end_year.isin(season_end) & df.gender.isin(gender) & df.competition_type.isin(competition_type)]
    
    return df['fixtures_url']