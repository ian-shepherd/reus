import re

from ..util import get_page_soup_headers


def _extract_text(attribute, tag, pattern, cat="text"):
    try:
        val = attribute.find(tag, text=pattern).find_next(tag)
        if cat == "text":
            return val.text.strip()
        else:
            return val.find("img")["title"]
    except AttributeError:
        return None


def _extract_social_media(pageSoup, tag, pattern):
    try:
        val = (
            pageSoup.find(tag, text="Social-Media:")
            .find_next(tag)
            .find("a", title=pattern)["href"]
        )
        return val
    except (AttributeError, TypeError):
        return None


def _extract_positions(pageSoup, position):
    # position - primary
    try:
        position_data = pageSoup.find("div", {"class": "detail-position__box"})
        position_main = (
            position_data.find("dt", text="Main position:").find_next("dd").text.strip()
        )
    except AttributeError:
        try:
            position_main = position.split(" - ")[-1].strip()
        except AttributeError:
            position_main = None

    # position - alternate
    position_data = pageSoup.find("div", {"class": "detail-position__box"})
    try:
        pos_alt1 = position_data.find("dt", text="Other position:").find_next("dd").text
    except AttributeError:
        pos_alt1 = None

    try:
        pos_alt2 = position_data.find("dd", text=pos_alt1).find_next("dd").text
    except AttributeError:
        pos_alt2 = None

    return position_main, pos_alt1, pos_alt2


def _reorder_dict(mydict):
    order = [
        "id",
        "name",
        "url",
        "headshot_url",
        "full_name",
        "born",
        "birth_place",
        "birth_country",
        "age",
        "height",
        "nationality",
        "position",
        "position_main",
        "position_alt1",
        "position_alt2",
        "foot",
        "agent",
        "outfitter",
        "social_twitter",
        "social_facebook",
        "social_instagram",
        "club",
        "joined",
        "contracted",
        "extension",
        "currency",
        "mv",
        "update",
    ]
    return {k: mydict[k] for k in order}


def tm_player_metadata(pageSoup=None, url: str = None) -> dict:
    #
    """Extracts general player information (biographical, club, contract, market value, and miscellaneous)

    Args:
        pageSoup (bs4, optional): bs4 object of player page referenced in url. Defaults to None.
        url (str, optional): path of transfermarkt player page. Defaults to None.

    Returns:
        dict: player metadata
    """

    assert (
        pageSoup is not None or url is not None
    ), "Either pageSoup or url must be provided"

    if pageSoup is None:
        pageSoup = get_page_soup_headers(url)

    # Extract url
    url = pageSoup.find("meta", {"property": "og:url"})["content"]

    # Find data object
    player_data = pageSoup.find("div", {"data-viewport": "Steckbrief"})
    headshot_url = pageSoup.find("div", {"class": "modal-trigger"}).find("img")["src"]

    # Extract data and error handling
    attributes = {
        "full_name": ["Name in home country:", "Full name:"],
        "born": ["Date of birth:", "Date of birth/Age:"],
        "birth_place": ["Place of birth:"],
        "birth_country": ["Place of birth:", "img"],
        "height": ["Height:"],
        "nationality": ["Citizenship:"],
        "position": ["Position:"],
        "foot": ["Foot:"],
        "agent": ["Player agent:"],
        "outfitter": ["Outfitter:"],
    }

    player_info = {}

    for attr, patterns in attributes.items():
        cat = "img" if patterns[-1] == "img" else "text"
        for pattern in patterns:
            value = _extract_text(player_data, "span", pattern, cat)
            player_info[attr] = value
            if value is not None:
                if attr == "born":
                    value = value.replace(" Happy Birthday", "")
                    # keep everything within parenthesis
                    age = re.findall(r"\(.*\)", value)[0]
                    player_info["age"] = age.replace("(", "").replace(")", "")
                    # remove everything after parenthesis
                    value = re.sub(r"\(.*\)", "", value).strip()
                elif attr == "height":
                    value = value.replace(",", ".").replace("m", "").strip()
                elif attr == "nationality":
                    value = re.split(r"\s{2,}", value)[0]

                player_info[attr] = value
                break

    # social media
    social_attributes = {
        "social_twitter": "Twitter",
        "social_facebook": "Facebook",
        "social_instagram": "Instagram",
    }

    for attr, pattern in social_attributes.items():
        value = _extract_social_media(pageSoup, "span", pattern)
        player_info[attr] = value

    position_main, pos_alt1, pos_alt2 = _extract_positions(
        pageSoup, player_info["position"]
    )

    # club
    club = pageSoup.find("div", {"class": "data-header__box--big"})
    club = club.find("img", alt=True)["alt"]

    meta_attributes = {
        "joined": "Joined:",
        "contracted": "Contract expires:",
        "extension": "Date of last contract extension:",
    }

    for attr, pattern in meta_attributes.items():
        value = _extract_text(pageSoup, "span", pattern)
        player_info[attr] = value

    # market value
    try:
        value = (
            pageSoup.find("div", {"class": "data-header__box--small"}).find("a").text
        )
        value = value.split("Last update: ")
        updated = value[1]
        value = value[0]
        currency = value[0]
        mult = 1000000 if value.strip()[-1] == "m" else 1000
        value = float(value[1:].replace("Th.", "").replace("m", "").strip()) * mult
    except AttributeError:
        value = None
        updated = None
        currency = None

    # url path, player_id, and name
    id_ = url.split("/")[-1]
    name = url.split("/")[-4]
    url = "/".join((name, "profil/spieler", id_))

    # Generate dictionary and store attributes
    mydict = {
        "id": id_,
        "name": name,
        "url": "/" + url.split("/")[-4] + "/profil/spieler/" + url.split("/")[-1],
        "headshot_url": headshot_url,
        "position_main": position_main,
        "position_alt1": pos_alt1,
        "position_alt2": pos_alt2,
        "club": club,
        "currency": currency,
        "mv": value,
        "update": updated,
        **player_info,
    }

    mydict = _reorder_dict(mydict)

    return mydict
