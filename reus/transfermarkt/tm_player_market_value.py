import re

from ..util import get_page_soup_headers


def tm_player_market_value(pageSoup=None, url: str = None) -> list:
    """Extracts date, team, and market value from highchart

    Args:
        pageSoup (bs4, optional): bs4 object of player market value page referenced in url. Defaults to None.
        url (str, optional): path of transfermarkt player market value page. Defaults to None.

    Returns:
        list: market value of player by date
    """

    assert (
        pageSoup is not None or url is not None
    ), "Either pageSoup or url must be provided"

    if pageSoup is None:
        pageSoup = get_page_soup_headers(url)

    # Extract currency
    value = pageSoup.find("div", {"class": "data-header__box--small"}).find("a").text
    value = value.split("Last update: ")[0]
    currency = value[0]

    # Find hicharts script object
    script = pageSoup.find("script", text=re.compile("Highcharts.Chart")).string

    # string pattern
    pattern = re.compile("'datum_mw':(.*?),'x'")
    date = re.findall(pattern, script)
    pattern = re.compile("'verein':(.*?),'age'")
    team = re.findall(pattern, script)
    pattern = re.compile("'y':(.*?),'verein'")
    value = re.findall(pattern, script)

    # generate empty list
    mylist = []

    # iterate through each data point and store attributes
    for i in range(len(date)):
        # generate dictionary for each point
        mydict = {
            "date": date[i].replace("\\x20", " ").replace("'", ""),
            "team": team[i]
            .replace("\\x20", " ")
            .replace("\\u00E9", "\u00E9")
            .replace("'", ""),
            "currency": currency,
            "value": value[i].replace("\\x20", " "),
        }

        # append dictionary to list
        mylist.append(mydict)

    return mylist


# TODO: updaated documentation
