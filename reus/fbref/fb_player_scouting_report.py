import time

import bs4

from ..util import get_page_soup


def _get_scouting_url(player_url: str, comp_league: str) -> bs4.BeautifulSoup:
    pageSoup = get_page_soup(player_url)

    scouting_links = pageSoup.find(
        "p", {"class": "listhead"}, string="Scouting Report"
    ).find_next_sibling("ul")

    if comp_league is None:
        url = scouting_links.find("a").get("href")
    else:
        for link in scouting_links.find_all("a"):
            if comp_league == link.string:
                url = link.get("href")
                break

    if url is None:
        raise ValueError("No scouting report found for the given league")

    url = "https://fbref.com" + url

    return url


def _extract_stats(pageSoup: bs4.BeautifulSoup, position_comp: str) -> dict:
    if position_comp == "Primary":
        comp_span = pageSoup.find_all(
            "span", {"data-label": "Complete Scouting Report"}
        )[0]
    elif position_comp == "Secondary":
        comp_span = pageSoup.find_all(
            "span", {"data-label": "Complete Scouting Report"}
        )[1]
    id_ = comp_span.get("id").split("_")[2]
    id_ = f"div_scout_full_{id_}"

    stats = pageSoup.find("div", {"id": id_})
    table = stats.find("table")
    rows = table.find_all("tr")

    stats_dict = {}
    stat_group = "tmp"
    mydict = {}
    for row in rows:
        th = row.find("th", {"class": "over_header"})
        if th is not None:
            stats_dict[stat_group] = mydict
            stat_group = th.string
            mydict = {}
        else:
            stat_name = row.find("th", {"data-stat": True}).string
            if stat_name == "Statistic" or stat_name == " ":
                continue

            try:
                stat_val = row.find("td")["csk"]
                stat_percentile = int(row.find_all("td")[1]["csk"])
                mydict[stat_name] = {"value": stat_val, "percentile": stat_percentile}
            except KeyError:
                continue

    stats_dict[stat_group] = mydict
    stats_dict.pop("tmp", None)

    return stats_dict


def fb_player_scouting_report(
    pageSoup=None,
    url: str = None,
    player_url: str = None,
    comp_league: str = None,
    position_comp: str = "Primary",
) -> dict:
    """Extracts scouting report for a given player

    Args:
        pageSoup (bs4, optional): bs4 object of a player's scouting report. Defaults to None.
        url (str, optional): path of fbref scouting report page. Defaults to None.
        player_url (str, optional): path of fbref player page. Defaults to None.
        comp_league (str, optional): name of comparison league. Defaults to None.
        position_comp (str, optional): primary or secondary position. Defaults to "Primary".

    Returns:
        dict: complete scouting report for a player
    """

    assert (
        pageSoup is not None or url is not None or player_url is not None
    ), "One of pageSoup, url, or player_url must be provided"

    assert position_comp in [
        "Primary",
        "Secondary",
    ], "position_comp must be one of 'Primary', 'Secondary', or None"

    if pageSoup is not None:
        pass
    elif url is not None:
        pageSoup = get_page_soup(url)
    elif player_url is not None:
        url = _get_scouting_url(player_url, comp_league)
        time.sleep(4)
        pageSoup = get_page_soup(url)

    if position_comp is None:
        position_comp = "Primary"

    stats_dict = _extract_stats(pageSoup, position_comp)

    return stats_dict
