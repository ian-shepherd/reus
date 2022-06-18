from ..util import get_page_soup


def fb_match_shots(pageSoup=None, url: str = None):
    """Extracts shots for a given match that includes StatsBomb data

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
    shots = table.find("tbody")
    shots = shots.find_all("tr")

    # generate empty list
    shotList = []

    # iterate through each shot and store attributes
    for row in shots:

        # generate empty dictionary
        mydict = {}

        # error handling for empty minutes
        mins = row.find("th", {"data-stat": "minute"}).text
        if mins == "":
            continue

        player_id = row.find("a", href=True)["href"].split("/")[3]
        team_id = (
            row.find("td", {"data-stat": "squad"})
            .find("a", href=True)["href"]
            .split("/")[3]
        )
        outcome = row.find("td", {"data-stat": "outcome"}).text
        distance = row.find("td", {"data-stat": "distance"}).text
        body_part = row.find("td", {"data-stat": "body_part"}).text
        notes = row.find("td", {"data-stat": "notes"}).text

        # error handling for no sca_player1
        try:
            sca_player1 = (
                row.find("td", {"data-stat": "sca_1_player"})
                .find("a", href=True)["href"]
                .split("/")[3]
            )
            sca_player1_event = row.find("td", {"data-stat": "sca_1_type"}).text
        except TypeError:
            sca_player1 = None
            sca_player1_event = None

        # error handling for no sca_player2
        try:
            sca_player2 = (
                row.find("td", {"data-stat": "sca_2_player"})
                .find("a", href=True)["href"]
                .split("/")[3]
            )
            sca_player2_event = row.find("td", {"data-stat": "sca_2_type"}).text
        except TypeError:
            sca_player2 = None
            sca_player2_event = None

        # generate dictionary for each shot
        mydict["minute"] = mins
        mydict["player"] = player_id
        mydict["team_id"] = team_id
        mydict["outcome"] = outcome
        mydict["distance"] = distance
        mydict["body_part"] = body_part
        mydict["notes"] = notes
        mydict["sca_player1"] = sca_player1
        mydict["sca_player1_event"] = sca_player1_event
        mydict["sca_player2"] = sca_player2
        mydict["sca_player2_event"] = sca_player2_event

        # append dictionary to list
        shotList.append(mydict)

    return shotList
