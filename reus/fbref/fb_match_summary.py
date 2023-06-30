from ..util import get_page_soup


def _extract_event_type(event, divs):
    # goal and shootout handling
    if divs[2]["class"][1] == "own_goal":
        event = "Own Goal"
    elif event.startswith("Goal"):
        event = "Goal"
    elif divs[2]["class"][1] == "penalty_shootout_goal":
        event = "Goal (shootout)"
    elif divs[2]["class"][1] == "penalty_shootout_miss":
        event = "Miss (shootout)"
    elif divs[2]["class"][1] == "penalty_goal":
        event = "Goal (penalty)"
    elif divs[2]["class"][1] == "penalty_miss":
        event = "Miss (penalty)"

    return event


def _extract_event_player(event, divs):
    try:
        event_player1 = divs[3].find("a", href=True)["href"]
    except (AttributeError, TypeError):
        return None, None

    if event in ["Goal (penalty)", "Own Goal", "Goal (shootout)"]:
        event_player2 = None
    else:
        try:
            event_player2 = divs[3].find("small").find("a", href=True)["href"]
        except (AttributeError, TypeError):
            event_player2 = None

    return event_player1, event_player2


def fb_match_summary(pageSoup=None, url: str = None) -> list:
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
        event = _extract_event_type(event, divs)

        score_x, score_y = map(int, score.split(":"))

        # determine score before goal
        if event in ["Goal", "Own Goal", "Goal (shootout)", "Goal (penalty)"]:
            if team == "x":
                score_x -= 1
                score_pre = f"{score_x}:{score_y}"
            else:
                score_y -= 1
                score_pre = f"{score_x}:{score_y}"
        else:
            score_pre = score

        # extract primary and secondary (if applicable)
        event_player1, event_player2 = _extract_event_player(event, divs)
        if event_player1 is None:
            continue

        # generate dictionary for each event
        mydict = {
            "team": team,
            "minute": mins,
            "event": event,
            "score_pre": score_pre,
            "score_post": score,
            "player1": event_player1,
            "player2": event_player2,
        }

        # append event dictionary to list
        eventList.append(mydict)

    return eventList
