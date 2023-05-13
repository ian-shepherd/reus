import re
from ..util import get_page_soup


def fb_match_metadata(pageSoup=None, url: str = None) -> tuple:
    """Extracts general information (teams, managers, captains, date, time, venue, attendance, score, xG) for a given match

    Args:
        pageSoup (bs4, optional): bs4 object of a match. Defaults to None.
        url (str, optional): path of fbref match page. Defaults to None.

    Returns:
        tuple: metadata and officials
            dict: metadata information
            dict: match officials
    """

    assert (
        pageSoup is not None or url is not None
    ), "Either pageSoup or url must be provided"

    if pageSoup is None:
        pageSoup = get_page_soup(url)

    # Extract url
    url = pageSoup.find("meta", {"property": "og:url"})["content"]
    url = url.replace("https://fbref.com", "")
    match_id = url.split("/")[3]

    # Find scorebox object
    scorebox = pageSoup.find("div", {"class": "scorebox"})
    # teams = scorebox.find_all("div", {"itemprop": "performer"})
    teams = scorebox.find_all("strong")

    # extract team id and name
    team_idx = []
    for i in range(len(teams)):
        if teams[i].find("a", href=True) is not None and "squad" in teams[i].find(
            "a", href=True
        ).get("href"):
            team_idx.append(i)
    id_x = teams[team_idx[0]].find("a", href=True)["href"].split("/")[3]
    id_y = teams[team_idx[1]].find("a", href=True)["href"].split("/")[3]
    team_x = teams[team_idx[0]].find("a", href=True).text
    team_y = teams[team_idx[1]].find("a", href=True).text

    # extract scores
    scores = pageSoup.find_all("div", {"class": "scores"})
    score_x = scores[0].find("div", {"class": "score"}).text
    score_y = scores[1].find("div", {"class": "score"}).text
    # error handling for non-xG
    try:
        xg_x = scores[0].find("div", {"class": "score_xg"}).text
    except AttributeError:
        xg_x = None
    try:
        xg_y = scores[1].find("div", {"class": "score_xg"}).text
    except AttributeError:
        xg_y = None

    # extract managers and captains
    managers = pageSoup.find_all("div", {"class": "datapoint"})
    manager_x = None
    manager_y = None
    captain_x = None
    captain_y = None
    captain_url_x = None
    captain_url_y = None
    captain_id_x = None
    captain_id_y = None
    managerOrder = []
    for m in managers:
        if "Manager: " in m.text:
            managerOrder.append("Manager")
        elif "Captain: " in m.text:
            managerOrder.append("Captain")
    if managerOrder == ["Manager", "Captain", "Manager", "Captain"]:
        manager_x = managers[0].text.replace("Manager: ", "")
        manager_y = managers[2].text.replace("Manager: ", "")
        captain_x = managers[1].find("a", href=True).text
        captain_y = managers[3].find("a", href=True).text
        captain_url_x = managers[1].find("a", href=True)["href"]
        captain_url_y = managers[3].find("a", href=True)["href"]
        captain_id_x = captain_url_x.split("/")[3]
        captain_id_y = captain_url_y.split("/")[3]
    elif managerOrder == ["Manager", "Captain", "Captain"]:
        manager_x = managers[0].text.replace("Manager: ", "")
        captain_x = managers[1].find("a", href=True).text
        captain_y = managers[2].find("a", href=True).text
        captain_url_x = managers[1].find("a", href=True)["href"]
        captain_url_y = managers[2].find("a", href=True)["href"]
        captain_id_x = captain_url_x.split("/")[3]
        captain_id_y = captain_url_y.split("/")[3]
    elif managerOrder == ["Captain", "Manager", "Captain"]:
        manager_y = managers[1].text.replace("Manager: ", "")
        captain_x = managers[0].find("a", href=True).text
        captain_y = managers[2].find("a", href=True).text
        captain_url_x = managers[0].find("a", href=True)["href"]
        captain_url_y = managers[2].find("a", href=True)["href"]
        captain_id_x = captain_url_x.split("/")[3]
        captain_id_y = captain_url_y.split("/")[3]
    elif managerOrder == ["Manager", "Captain", "Manager"]:
        manager_x = managers[0].text.replace("Manager: ", "")
        manager_y = managers[2].text.replace("Manager: ", "")
        captain_x = managers[1].find("a", href=True).text
        captain_url_x = managers[1].find("a", href=True)["href"]
        captain_id_x = captain_url_x.split("/")[3]
    elif managerOrder == ["Manager", "Manager", "Captain"]:
        manager_x = managers[0].text.replace("Manager: ", "")
        manager_y = managers[1].text.replace("Manager: ", "")
        captain_y = managers[2].find("a", href=True).text
        captain_url_y = managers[2].find("a", href=True)["href"]
        captain_id_y = captain_url_y.split("/")[3]
    elif managerOrder == ["Manager", "Manager"]:
        manager_x = managers[0].text.replace("Manager: ", "")
        manager_y = managers[1].text.replace("Manager: ", "")
    elif managerOrder == ["Captain", "Captain"]:
        captain_x = managers[0].find("a", href=True).text
        captain_y = managers[1].find("a", href=True).text
        captain_url_x = managers[0].find("a", href=True)["href"]
        captain_url_y = managers[1].find("a", href=True)["href"]
        captain_id_x = captain_url_x.split("/")[3]
        captain_id_y = captain_url_y.split("/")[3]

    # Find match information object
    scorebox_meta = pageSoup.find("div", {"class": "scorebox_meta"})

    # extract date and time information
    datetime = scorebox_meta.find("span", {"class": "venuetime"})
    date = datetime["data-venue-date"]
    kickoff = datetime["data-venue-time"]
    league_info = pageSoup.find("div", {"id": "content"})
    league_id = league_info.find("a", href=True)["href"].split("/")[3]
    league = league_info.find("a", href=True).text
    matchweek = (
        re.search(r"\(([^)]+)", league_info.text).group(1).replace("Matchweek ", "")
    )

    # extract attendance, venue, and official information
    scorebox_meta_ = scorebox_meta.find_all("div")
    attendance = None
    venue = None
    officials = None
    notes = None
    for i in list(scorebox_meta_):
        if "Attendance:" in i.text:
            attendance = i.text.replace("Attendance: ", "").replace(",", "")
        elif "Venue:" in i.text:
            venue = i.text.replace("Venue: ", "")
        elif "Officials:" in i.text:
            officials = i.find_all("small")[1].text.split("\xa0· ")
            for j in officials:
                officials[officials.index(j)] = j.replace("\xa0", " ")
        elif "Match awarded to " in i.text:
            notes = i.text

    # generate dictionary for general metadata
    metadict = {
        "match_id": match_id,
        "url": url,
        "date": date,
        "kickoff": kickoff,
        "venue": venue,
        "attendance": attendance,
        "league_id": league_id,
        "league": league,
        "id_x": id_x,
        "team_x": team_x,
        "id_y": id_y,
        "team_y": team_y,
        "manager_x": manager_x,
        "manager_y": manager_y,
        "captain_x": captain_x,
        "captain_url_x": captain_url_x,
        "captain_id_x": captain_id_x,
        "captain_y": captain_y,
        "captain_url_y": captain_url_y,
        "captain_id_y": captain_id_y,
        "score_x": score_x,
        "score_y": score_y,
        "xg_x": xg_x,
        "xg_y": xg_y,
        "matchweek": matchweek,
        "notes": notes,
    }

    # extract officials
    referee = officials[0].replace(" (Referee)", "")
    ar1 = officials[1].replace(" (AR1)", "") if len(officials) > 1 else None
    ar2 = officials[2].replace(" (AR2)", "") if len(officials) > 2 else None
    fourth = officials[3].replace(" (4th)", "") if len(officials) > 3 else None
    var = officials[4].replace(" (VAR)", "") if len(officials) > 4 else None

    # generate dictionary for officials
    officialsdict = {
        "referee": referee,
        "ar1": ar1,
        "ar2": ar2,
        "fourth": fourth,
        "var": var,
    }

    return metadict, officialsdict
