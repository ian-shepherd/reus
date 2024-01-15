import pandas as pd

from ..util import get_page_soup_headers


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
    team_id = int(filtered_df.transfermarkt.iloc[0])

    return club, team_id


def tm_team_staff(
    club: str = None,
    team_id: int = None,
    pageSoup=None,
    url: str = None,
) -> list:
    """Extracts team staff information

    Args:
        club (str, optional): club name. Defaults to None.
        team_id (int, optional): transfermarkt team id. Defaults to None.
        pageSoup (bs4, optional): bs4 object of staff page for team referenced in url. Defaults to None.
        url (str, optional): path of transfermarkt team staff page. Defaults to None.

    Returns:
        list: team staff
    """

    assert (
        pageSoup is not None
        or url is not None  # noqa: W503
        or (club is not None and team_id is not None)  # noqa: W503
    ), "Either pageSoup, url, or club and team_id must be provided"

    if url is None:
        # Determine team id and club name
        club, team_id = _get_team_id_and_club(team_id, club)

        # Generate url
        url = f"https://www.transfermarkt.us/{club}/mitarbeiter/verein/{team_id}"

    if pageSoup is None:
        pageSoup = get_page_soup_headers(url)

    # Find tables
    table = pageSoup.find_all("table")

    # Generate empty list
    mylist = []

    # Iterate through each table
    for table in pageSoup.find_all("table"):
        # Find rows
        rows = table.find_all("tr")

        # Iterate through each row
        for row in rows:
            # Check if valid row
            if len(row.find_all("td")) < 9:
                continue

            # Store attributes
            name = row.find("a").text
            url = row.find("a").get("href")
            role = row.find_all("td")[3].text
            cells = row.find_all("td", {"class": "zentriert"})
            age = cells[0].text

            # Error handling for no nation
            try:
                nation = cells[1].find("img")["title"]
            except TypeError:
                nation = None

            appointed = cells[2].text
            contracted = cells[3].text.strip()

            # Error handling for no last club or url
            try:
                last_club = cells[4].find("a")["title"]
            except TypeError:
                last_club = None
            try:
                last_club_url = cells[4].find("a")["href"]
            except TypeError:
                last_club_url = None

            # Generate dictionary for each staff member
            mydict = {
                "name": name,
                "url": url,
                "role": role,
                "age": age,
                "nation": nation,
                "appointed": appointed,
                "contracted": contracted,
                "last_club": last_club,
                "last_club_url": last_club_url,
            }

            # Append dictionary to list
            mylist.append(mydict)

    return mylist
