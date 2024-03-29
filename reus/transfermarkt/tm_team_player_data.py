import pandas as pd

from ..util import get_page_soup_headers
from .util import tm_format_currency


def _get_team_id_and_club(team_id, club):
    df = pd.read_csv(
        "https://raw.githubusercontent.com/ian-shepherd/reus_data/main/raw-data/team_translations.csv",
        keep_default_na=False,
    )
    filter_condition = (
        (df.fbref_name == club)
        | (df.transfermarkt_name == club)  # noqa: W503
        | (df.transfermarkt_link == club)  # noqa: W503
        | (df.fcpython == club)  # noqa: W503
        | (df.fivethirtyeight == club)  # noqa: W503
    )
    filtered_df = df[filter_condition]
    club = filtered_df.transfermarkt_link.iloc[0]
    team_id = int(float(filtered_df.transfermarkt.iloc[0]))

    return club, team_id


def _extract_player_metadata(row, num, adj):
    # extract basic info
    player_table = row.find("table")
    url = player_table.find("a", href=True)["href"]
    name = player_table.find("img")["alt"]
    pos = player_table.find_all("tr")[1].text.strip()

    # extract birth day and age
    data = row.find_all("td", {"class": "zentriert"})
    birth = data[1].text.strip()
    birth = birth.split("(")
    birth_date = birth[0].strip()
    age = birth[1].replace(")", "").strip()

    # extract nation
    nation = data[2].find("img")["alt"]

    # extract height
    try:
        height = data[-5 + adj].text.strip()
        height = height.replace(",", ".").replace("m", "").strip()
    except TypeError:
        height = None

    # extract foot
    try:
        foot = data[-4 + adj].text.strip()
        foot = None if foot == "-" else foot
    except TypeError:
        foot = None

    # extract joined date
    try:
        joined = data[-3 + adj].text.strip()
        joined = None if joined == "-" else joined
    except TypeError:
        joined = None

    # extract signing information
    signed_from, signed_from_url, signed_value = _extract_signing_info(data, adj)

    # extract contracted
    if adj == 1:
        contracted = None
    else:
        try:
            contracted = data[-1].text.strip()
        except TypeError:
            contracted = None

    # extract market value
    try:
        mv = row.find("td", {"class": "rechts hauptlink"}).text
        currency = mv[0]
        mv = tm_format_currency(mv)
    except (AttributeError, ValueError, ValueError):
        mv = 0
        currency = None

    # generate dictionary for each player
    mydict = {
        "name": name,
        "url": url,
        "number": num,
        "position": pos,
        "birth_date": birth_date,
        "age": age,
        "nation": nation,
        "height": height,
        "foot": foot,
        "joined": joined,
        "signed_from": signed_from,
        "signed_from_url": signed_from_url,
        "fee": signed_value,
        "currency": currency,
        "contracted": contracted,
        "market_value": mv,
    }

    return mydict


def _extract_signing_info(data, adj):
    try:
        signed_from = data[-2 + adj].find("img")["alt"]
        signed_from_url = data[-2 + adj].find("a", href=True)["href"]
        signed_value = data[-2 + adj].find("a")["title"].split()[-1]
        signed_value = signed_value.replace("-", "0").replace("transfer", "0")
        if signed_value == "?":
            signed_value = "unknown"
        else:
            signed_value = tm_format_currency(signed_value)
    except TypeError:
        signed_from = None
        signed_from_url = None
        signed_value = None

    return signed_from, signed_from_url, signed_value


def tm_team_player_data(
    club: str,
    season: str,
    domain: str = "us",
    team_id: int = None,
    transfermarkt_name: bool = False,
) -> list:
    """Extracts basic player information for each player in a squad including basic player information,
    market value, and contract expiration

    Args:
        club (str): club name
        season (str): year at start of season
        domain (str, optional): domain to use for transfermarkt. Defaults to "us".
        team_id (int, optional): transfermarkt team id. Defaults to None.
        transfermarkt_name (bool, optional): if True, club is a transfermarkt name. Defaults to False.

    Returns:
        list: squad players
    """

    if team_id is None and transfermarkt_name is False:
        club, team_id = _get_team_id_and_club(team_id, club)

    # Generate url
    try:
        page = f"https://www.transfermarkt.{domain}/{club}/kader/verein/{str(team_id)}/saison_id/{season}/plus/1"
    except IndexError:
        print("This team does not exist, please confirm spelling")
        exit()

    pageSoup = get_page_soup_headers(page)

    # Find table object
    table = pageSoup.find("table", {"class": "items"})
    tbody = table.find("tbody")

    # Previous season column adjustment
    col_name = table.find_all("th")[-2].text
    if col_name == "Signed from":
        adj = 1
    else:
        adj = 0

    # Find rows
    rows = tbody.find_all("tr")

    # Generate empty list
    mylist = []

    # iterate through each transfer and store attributes
    for row in rows:
        # check if valid row
        try:
            num = row.find("div", {"class": "rn_nummer"}).text
        except AttributeError:
            continue

        mydict = _extract_player_metadata(row, num, adj)

        # append dictionary to list
        mylist.append(mydict)

    return mylist
