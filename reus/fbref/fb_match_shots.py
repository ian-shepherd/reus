from ..util import get_page_soup


def fb_match_shots(pageSoup=None, url: str = None) -> list:
    """Extracts shots for a given match that includes Opta data

    Args:
        pageSoup (bs4, optional): bs4 object of a match. Defaults to None.
        url (str, optional): path of fbref match page. Defaults to None.

    Returns:
        list: shots for the match
    """

    assert (
        pageSoup is not None or url is not None
    ), "Either pageSoup or url must be provided"

    if pageSoup is None:
        pageSoup = get_page_soup(url)

    # Find shots object
    table = pageSoup.find("table", {"id": "shots_all"})
    try:
        shots = table.find("tbody")
    except AttributeError:
        return None
    shots = shots.find_all("tr")

    # generate empty list
    shotList = []

    # iterate through each shot and store attributes
    for row in shots:
        # skip spacers
        if row["class"][0] == "spacer":
            continue

        # generate empty dictionary
        mydict = {}

        # general
        minute = row.find("th", {"data-stat": "minute"}).text
        if minute == "":
            minute = None
        player_id = row.find("a", href=True)["href"].split("/")[3]
        name = row.find("a", href=True).text
        team_id = (
            row.find("td", {"data-stat": "team"})
            .find("a", href=True)["href"]
            .split("/")[3]
        )
        team_name = row.find("td", {"data-stat": "team"}).find("a", href=True).text
        xG = row.find("td", {"data-stat": "xg_shot"}).text
        if xG == "":
            xG = None
        psxg = row.find("td", {"data-stat": "psxg_shot"}).text
        if psxg == "":
            psxg = None
        outcome = row.find("td", {"data-stat": "outcome"}).text
        distance = row.find("td", {"data-stat": "distance"}).text
        body_part = row.find("td", {"data-stat": "body_part"}).text
        notes = row.find("td", {"data-stat": "notes"}).text

        # sca 1
        try:
            sca_player1 = (
                row.find("td", {"data-stat": "sca_1_player"})
                .find("a", href=True)["href"]
                .split("/")[3]
            )
            sca_player1_name = row.find("td", {"data-stat": "sca_1_player"}).text
            sca_player1_event = row.find("td", {"data-stat": "sca_1_type"}).text
        except TypeError:
            sca_player1 = None
            sca_player1_name = None
            sca_player1_event = None

        # sca 2
        try:
            sca_player2 = (
                row.find("td", {"data-stat": "sca_2_player"})
                .find("a", href=True)["href"]
                .split("/")[3]
            )
            sca_player2_name = row.find("td", {"data-stat": "sca_2_player"}).text
            sca_player2_event = row.find("td", {"data-stat": "sca_2_type"}).text
        except TypeError:
            sca_player2 = None
            sca_player2_name = None
            sca_player2_event = None

        mydict = {
            "minute": minute,
            "player_id": player_id,
            "name": name,
            "team_id": team_id,
            "team_name": team_name,
            "xG": xG,
            "psxg": psxg,
            "outcome": outcome,
            "distance": distance,
            "body_part": body_part,
            "notes": notes,
            "sca_player1": sca_player1,
            "sca_player1_name": sca_player1_name,
            "sca_player1_event": sca_player1_event,
            "sca_player2": sca_player2,
            "sca_player2_name": sca_player2_name,
            "sca_player2_event": sca_player2_event,
        }

        shotList.append(mydict)

    return shotList
