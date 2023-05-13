# from ...reus.util import get_page_soup
from ..util import get_page_soup
from .fb_team_player_summary_stats import fb_team_player_summary_stats
from .fb_team_player_keeper_stats import fb_team_player_keeper_stats
from .fb_team_player_advanced_keeper_stats import fb_team_player_advanced_keeper_stats
from .fb_team_player_shooting_stats import fb_team_player_shooting_stats
from .fb_team_player_passing_stats import fb_team_player_passing_stats
from .fb_team_player_passing_type_stats import fb_team_player_passing_type_stats
from .fb_team_player_goal_sca_stats import fb_team_player_goal_sca_stats
from .fb_team_player_defensive_actions_stats import (
    fb_team_player_defensive_actions_stats,
)
from .fb_team_player_possession_stats import fb_team_player_possession_stats
from .fb_team_player_playing_time_stats import fb_team_player_playing_time_stats
from .fb_team_player_misc_stats import fb_team_player_misc_stats
from bs4 import BeautifulSoup


def fb_team_player_data(url: str, html_file: BeautifulSoup = None) -> tuple:
    """Extracts statistics of each player for a given team. This includes summary, shooting, passing,
    defensive, possession, possession, playing time, and goalkeeping stats

    Args:
        url (str): path of fbref team page
        html_file (BeautifulSoup, optional): pageSoup html file. Defaults to None.

    Returns:
        tuple: player stats
            list: summary stats of players
            list: goalkeeping stats of players
            list: advanced goalkeeping stats of players
            list: shooting stats of players
            list: passing stats of players
            list: passing type stats of players
            list: goal and sca stats of players
            list: defensive stats of players
            list: possession stats of players
            list: playing time stats of players
            list: miscellaneous stats of players

    """

    if html_file is None:
        page = "https://fbref.com" + url
        pageSoup = get_page_soup(page)
    else:
        pageSoup = html_file

    summary_stats = fb_team_player_summary_stats(pageSoup)
    keeper_stats = fb_team_player_keeper_stats(pageSoup)
    advanced_keeper_stats = fb_team_player_advanced_keeper_stats(pageSoup)
    shooting_stats = fb_team_player_shooting_stats(pageSoup)
    passing_stats = fb_team_player_passing_stats(pageSoup)
    passing_type_stats = fb_team_player_passing_type_stats(pageSoup)
    goal_sca_stats = fb_team_player_goal_sca_stats(pageSoup)
    defensive_stats = fb_team_player_defensive_actions_stats(pageSoup)
    possession_stats = fb_team_player_possession_stats(pageSoup)
    playing_time_stats = fb_team_player_playing_time_stats(pageSoup)
    misc_stats = fb_team_player_misc_stats(pageSoup)

    player = (
        summary_stats,
        keeper_stats,
        advanced_keeper_stats,
        shooting_stats,
        passing_stats,
        passing_type_stats,
        goal_sca_stats,
        defensive_stats,
        possession_stats,
        playing_time_stats,
        misc_stats,
    )

    return player
