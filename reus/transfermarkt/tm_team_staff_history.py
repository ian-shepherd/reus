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


def _get_role_id(role):
    # TODO: order by number or alphabetical
    # TODO: check missing (Man City)
    role_dict = {
        "Manager": 1,
        "Caretaker Manager": 10,
        "Assistant Manager": 2,
        "Goalkeeping Coach": 3,
        "Conditioning Coach": 11,
        "Fitness Coach": 22,
        "Technical Coach": 38,
        "Chief Analyst": 16,
        "Youth Coach": 104,
        "Head of Academy Coaching": 106,
        "Video Analyst": 70,
        "Match Analyst": 146,
        "Director of Football": 13,
        "Sporting Director": 54,
        "Team Manager": 55,
        "Academy Manager": 67,
        "Chief Executive Officer": 25,
        "Advisor of management": 102,
        "Director": 188,
        "Chairman": 28,
        "Board Member": 39,
        "Owner": 105,
        "Chief Scout": 53,
        "Head of Scouting": 90,
        "Scout": 7,
        "Youth Chief Scout": 167,
        "Youth Scout": 166,
        "Head of Youth Scouting": 140,
        "Head of Medical": 46,
        "Club Doctor": 19,
        "Physiotherapist": 12,
        "Sports Scientist": 71,
        "Masseur": 45,
        "Medical Director Physiotherapy": 180,
        "Marketing Staff": 44,
        "Media Officer": 92,
        "Media worker": 131,
        "Sponsoring": 56,
        "Head of Media and Communication": 179,
        "Photographer": 151,
        "Kit Manager": 20,
        "Club representative": 149,
        "Director of Finance": 81,
        "Advisor": 118,
        "Loan Player Manager": 158,
        "President": 17,
        "Vice-President": 27,
        "Vice-Chairman": 28,
        "Member of administrative board": 59,
        "Marketing/Management": 83,
        "Director of Marketing and Sales": 57,
        "Honorary President": 86,
        "Nutritionist": 130,
        "Academy Staff": 139,
        "Chief Instructor": 127,
        "Development Coach": 187,
        "Academy Goalkeeping cooridnator": 144,
        "Goalkeeping Co-oridnator": 65,
    }

    role_id = role_dict[role]

    return role_id


def tm_team_staff_history(
    club: str = None,
    team_id: int = None,
    pageSoup=None,
    url: str = None,
    role: str = None,
) -> list:
    """Extracts historical team staff information for a given role

    Args:
        club (str, optional): club name. Defaults to None.
        team_id (int, optional): transfermarkt team id. Defaults to None.
        pageSoup (bs4, optional): bs4 object of staff page for team referenced in url. Defaults to None.
        url (str, optional): path of transfermarkt team staff page. Defaults to None.

    Returns:
        list: team staff history
    """

    assert (
        pageSoup is not None
        or url is not None  # noqa: W503
        or (club is not None and team_id is not None and role is not None)  # noqa: W503
    ), "Either pageSoup, url, or club, team_id, and role must be provided"

    if url is None and pageSoup is None:
        # Determine team id and club name
        club, team_id = _get_team_id_and_club(team_id, club)

        # Generate url
        role_id = _get_role_id(role)
        url = f"https://www.transfermarkt.com/{club}/mitarbeiter/verein/{team_id}/personalie_id/{role_id}"

        # Get page soup
        pageSoup = get_page_soup_headers(url)

    # Find table
    table = pageSoup.find_all("table")[1]
    tbody = table.find("tbody")

    # Find rows
    rows = tbody.find_all("tr")

    # Generate empty list
    mylist = []

    # iterate through each row
    for row in rows:
        # check if valid row
        try:
            row["class"] not in ["odd", "even"]
        except KeyError:
            continue

        # Store attributes
        name = row.find("img")["alt"]
        url = row.find("a")["href"]

        dob = row.find("td").find_all("td")[2].text
        cells = row.find_all("td", {"class": "zentriert"})

        # Error handling for no nation
        try:
            nation = cells[0].find("img")["alt"]
        except TypeError:
            nation = None

        appointed = cells[1].text
        left = cells[2].text
        time_in_post = row.find("td", {"class": "rechts"}).text

        # Error handling for non managers
        try:
            matches = cells[3].text
        except IndexError:
            matches = None
        try:
            ppg = cells[4].text
        except IndexError:
            ppg = None

        # Generate dictionary for each staff member
        mydict = {
            "name": name,
            "url": url,
            "dob": dob,
            "nation": nation,
            "appointed": appointed,
            "left": left,
            "time_in_post": time_in_post,
            "matches": matches,
            "ppg": ppg,
        }

        # Append dictionary to list
        mylist.append(mydict)

    return mylist
