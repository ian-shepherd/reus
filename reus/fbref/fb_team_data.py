# from ...reus.util import get_page_soup
from ..util import get_page_soup
from .fb_team_summary_stats import fb_team_summary_stats
from .fb_team_keeper_stats import fb_team_keeper_stats
from .fb_team_advanced_keeper_stats import fb_team_advanced_keeper_stats
from .fb_team_shooting_stats import fb_team_shooting_stats
from .fb_team_passing_stats import fb_team_passing_stats
from .fb_team_passing_type_stats import fb_team_passing_type_stats
from .fb_team_goal_sca_stats import fb_team_goal_sca_stats
from .fb_team_defensive_actions_stats import (
    fb_team_defensive_actions_stats,
)
from .fb_team_possession_stats import fb_team_possession_stats
from .fb_team_playing_time_stats import fb_team_playing_time_stats
from .fb_team_misc_stats import fb_team_misc_stats
from bs4 import BeautifulSoup


def fb_team_data(url: str, html_file: BeautifulSoup = None) -> tuple:
    """Extracts statistics of each team. This includes summary, shooting, passing,
    defensive, possession, possession, playing time, and goalkeeping stats

    Args:
        url (str): path of fbref stats page
        html_file (BeautifulSoup, optional): pageSoup html file. Defaults to None.

    Returns:
        tuple: player stats
            list: summary stats for team
            list: summary stats against team
            list: keeper stats for team
            list: keeper stats against team
            list: advanced keeper stats for team
            list: advanced keeper stats against team
            list: shooting stats for team
            list: shooting stats against team
            list: passing stats for team
            list: passing stats against team
            list: passing type stats for team
            list: passing type stats against team
            list: goal and sca stats for team
            list: goal and sca stats against team
            list: defensive stats for team
            list: defensive stats against team
            list: possession stats for team
            list: possession stats against team
            list: playing time stats for team
            list: playing time stats against team
            list: miscellaneous stats for team
            list: miscellaneous stats against team
    """

    if html_file is None:
        page = "https://fbref.com" + url
        pageSoup = get_page_soup(page)
    else:
        pageSoup = html_file

    summary_stats_for, summary_stats_against = fb_team_summary_stats(pageSoup)
    keeper_stats_for, keeper_stats_against = fb_team_keeper_stats(pageSoup)
    (
        advanced_keeper_stats_for,
        advanced_keeper_stats_against,
    ) = fb_team_advanced_keeper_stats(pageSoup)
    shooting_stats_for, shooting_stats_against = fb_team_shooting_stats(pageSoup)
    passing_stats_for, passing_stats_against = fb_team_passing_stats(pageSoup)
    passing_type_stats_for, passing_type_stats_against = fb_team_passing_type_stats(
        pageSoup
    )
    goal_sca_stats_for, goal_sca_stats_against = fb_team_goal_sca_stats(pageSoup)
    defensive_stats_for, defensive_stats_against = fb_team_defensive_actions_stats(
        pageSoup
    )
    possession_stats_for, possession_stats_against = fb_team_possession_stats(pageSoup)
    playing_time_stats_for, playing_time_stats_against = fb_team_playing_time_stats(
        pageSoup
    )
    misc_stats_for, misc_stats_against = fb_team_misc_stats(pageSoup)

    team = (
        summary_stats_for,
        summary_stats_against,
        keeper_stats_for,
        keeper_stats_against,
        advanced_keeper_stats_for,
        advanced_keeper_stats_against,
        shooting_stats_for,
        shooting_stats_against,
        passing_stats_for,
        passing_stats_against,
        passing_type_stats_for,
        passing_type_stats_against,
        goal_sca_stats_for,
        goal_sca_stats_against,
        defensive_stats_for,
        defensive_stats_against,
        possession_stats_for,
        possession_stats_against,
        playing_time_stats_for,
        playing_time_stats_against,
        misc_stats_for,
        misc_stats_against,
    )

    return team
