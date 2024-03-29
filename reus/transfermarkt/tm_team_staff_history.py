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
    team_id = int(float(filtered_df.transfermarkt.iloc[0]))

    return club, team_id


def _get_role_id(role):
    role_dict = {
        "Academy Goalkeeping cooridnator": 144,
        "Academy Manager": 67,
        "Academy Staff": 139,
        "Advisor": 118,
        "Advisor of management": 102,
        "Assistant Manager": 2,
        "Board Member": 39,
        "Caretaker Manager": 10,
        "Chairman": 28,
        "Chief Analyst": 16,
        "Chief Executive Officer": 25,
        "Chief Instructor": 127,
        "Chief Scout": 53,
        "Club Doctor": 19,
        "Club representative": 149,
        "Conditioning Coach": 11,
        "Development Coach": 187,
        "Developer International Relations": 148,
        "Director": 188,
        "Director of Finance": 81,
        "Director of Football": 13,
        "Director of Marketing and Sales": 57,
        "Fitness Coach": 22,
        "Goalkeeping Coach": 3,
        "Goalkeeping Co-oridnator": 65,
        "Head of Academy Coaching": 106,
        "Head of Media and Communication": 179,
        "Head of Medical": 46,
        "Head of Methodology": 185,
        "Head of Scouting": 90,
        "Head of Youth Scouting": 140,
        "Honorary President": 86,
        "Kit Manager": 20,
        "Loan Player Manager": 158,
        "Manager": 1,
        "Marketing Staff": 44,
        "Marketing/Management": 83,
        "Match Analyst": 146,
        "Masseur": 45,
        "Media Officer": 92,
        "Media worker": 131,
        "Member of administrative board": 59,
        "Medical Director Physiotherapy": 180,
        "Nutritionist": 130,
        "Owner": 105,
        "Photographer": 151,
        "Physiotherapist": 12,
        "President": 17,
        "Scout": 7,
        "Sponsoring": 56,
        "Sporting Director": 54,
        "Sports Scientist": 71,
        "Sports Technologies Coordinator": 183,
        "Staff of the Office": 111,
        "Technical Coach": 38,
        "Team Manager": 55,
        "Vice-Chairman": 28,
        "Vice-President": 27,
        "Video Analyst": 70,
        "Youth Chief Scout": 167,
        "Youth Coach": 104,
        "Youth Scout": 166,
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
        role (str, optional): role of staff member. Defaults to None.

    Returns:
        list: team role staff history
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
        url = f"https://www.transfermarkt.us/{club}/mitarbeiterhistorie/verein/{team_id}/personalie_id/{role_id}"

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
