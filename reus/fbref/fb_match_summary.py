from ..util import get_page_soup


def fb_match_summary(pageSoup=None, url: str = None):
    """Extracts events (goals, bookings, and substitutions) from match summary for a given match

    Args:
        pageSoup (bs4, optional): bs4 object of a match. Defaults to None.
        url (str, optional): path of fbref match page. Defaults to None.

    Returns:
        list: match events
    """

    assert (
        pageSoup is not None or url is not None
    ), "Either pageSoup or url must be provided"

    if pageSoup is None:
        pageSoup = get_page_soup(url)

    # Find events object
    summary = pageSoup.find("div", {"id": "events_wrap"})
    events = summary.find_all("div", {"class": ["event a", "event b"]})

    # generate empty list
    eventList = []

    # iterate through each event
    for eve in events:

        # generate dictionary for each event
        mydict = {}

        # determine team
        if eve["class"][1] == "a":
            team = "x"
        else:
            team = "y"

        divs = eve.find_all("div")

        mins = divs[0].text.split("\u2019")[0].strip()
        score = divs[0].find("small").text
        event = divs[5].text.split("—")[1].strip()

        # goal and shootout handling
        if divs[2]["class"][1] == "own_goal":
            event = "Own Goal"
        elif event.startswith("Goal"):
            event = "Goal"
        elif divs[2]["class"][1] == "penalty_shootout_goal":
            event = "Goal (shootout)"
        elif divs[2]["class"][1] == "penalty_shootout_miss":
            event = "Miss (shootout)"

        # determine score before goal
        if event in ["Goal", "Own Goal", "Goal (shootout)"]:
            score_x, score_y = score.split(":")
            if team == "x":
                score_x = int(score_x) - 1
                score_pre = str(score_x) + ":" + score_y
            else:
                score_y = int(score_y) - 1
                score_pre = score_x + ":" + str(score_y)
        else:
            score_pre = score

        score_post = score

        # extra primary and secondary (if applicable)
        event_player1 = divs[3].find("a", href=True)["href"]
        try:
            event_player2 = divs[3].find("small").find("a", href=True)["href"]
        except AttributeError:
            event_player2 = None

        # generate dictionary for each event
        mydict["team"] = team
        mydict["minute"] = mins
        mydict["event"] = event
        mydict["score_pre"] = score_pre
        mydict["score_post"] = score_post
        mydict["player1"] = event_player1
        mydict["player2"] = event_player2

        # append event dictionary to list
        eventList.append(mydict)

    return eventList
