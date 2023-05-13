import re
from ..util import get_page_soup_headers


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
    # name
    try:
        full_name = (
            player_data.find("span", text="Name in home country:")
            .find_next("span")
            .text.strip()
        )
    except AttributeError:
        try:
            full_name = (
                player_data.find("span", text="Full name:")
                .find_next("span")
                .text.strip()
            )
        except AttributeError:
            full_name = None

    # birth date
    try:
        birth_date = (
            player_data.find("span", text="Date of birth:")
            .find_next("span")
            .text.strip()
        )
        birth_date = birth_date.replace(" Happy Birthday", "")
    except AttributeError:
        birth_date = None

    # birth place
    try:
        birth_place = (
            player_data.find("span", text="Place of birth:")
            .find_next("span")
            .text.strip()
        )
    except AttributeError:
        birth_place = None

    # birth country
    try:
        birth_country = (
            player_data.find("span", text="Place of birth:")
            .find_next("span")
            .find("img")["title"]
        )
    except AttributeError:
        birth_country = None

    # age
    try:
        age = player_data.find("span", text="Age:").find_next("span").text.strip()
    except AttributeError:
        age = None

    # height
    try:
        height = player_data.find("span", text="Height:").find_next("span").text.strip()
        height = height.replace(",", ".").replace("m", "").strip()
    except AttributeError:
        height = None

    # nationality
    try:
        nationality = (
            player_data.find("span", text="Citizenship:").find_next("span").text.strip()
        )
        nationality = re.split(r"\s{2,}", nationality)
    except AttributeError:
        nationality = None

    # position
    try:
        position = (
            player_data.find("span", text="Position:").find_next("span").text.strip()
        )
    except AttributeError:
        position = None

    # foot
    try:
        foot = player_data.find("span", text="Foot:").find_next("span").text.strip()
    except AttributeError:
        foot = None

    # agent
    try:
        agent = (
            player_data.find("span", text="Player agent:")
            .find_next("span")
            .text.strip()
        )
    except AttributeError:
        agent = None

    # outfitter
    try:
        outfitter = (
            player_data.find("span", text="Outfitter:").find_next("span").text.strip()
        )
    except AttributeError:
        outfitter = None

    # social media
    try:
        socialTwitter = (
            pageSoup.find("span", text="Social-Media:")
            .find_next("span")
            .find("a", title="Twitter")["href"]
        )
    except AttributeError:
        socialTwitter = None
    except TypeError:
        socialTwitter = None

    try:
        socialFacebook = (
            pageSoup.find("span", text="Social-Media:")
            .find_next("span")
            .find("a", title="Facebook")["href"]
        )
    except AttributeError:
        socialFacebook = None
    except TypeError:
        socialFacebook = None

    try:
        socialInstagram = (
            pageSoup.find("span", text="Social-Media:")
            .find_next("span")
            .find("a", title="Instagram")["href"]
        )
    except AttributeError:
        socialInstagram = None
    except TypeError:
        socialInstagram = None

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
    try:
        pos_alt1 = position_data.find("dt", text="Other position:").find_next("dd").text
    except AttributeError:
        pos_alt1 = None

    try:
        pos_alt2 = position_data.find("dd", text=pos_alt1).find_next("dd").text
    except AttributeError:
        pos_alt2 = None

    # club
    club = pageSoup.find("div", {"class": "data-header__box--big"})
    club = club.find("img", alt=True)["alt"]

    try:
        joined = pageSoup.find("span", text="Joined:")
        joined = joined.find_next("span").text.strip()
    except AttributeError:
        joined = None

    # contract expiration
    try:
        contracted = pageSoup.find("span", text="Contract expires:")
        contracted = contracted.find_next("span").text.strip()
    except AttributeError:
        contracted = None

    # date of last contract extension
    try:
        extension = (
            player_data.find("span", text="Date of last contract extension:")
            .find_next("span")
            .text.strip()
        )
    except AttributeError:
        extension = None

    # market value
    try:
        # value = pageSoup.find("div", {"class": "dataMarktwert"}).text
        # updated = re.search("(?<=update: ).*$", value).group()
        # value = value.split(" ")[0].strip()
        value = (
            pageSoup.find("div", {"class": "data-header__box--small"}).find("a").text
        )
        value = value.split("Last update: ")
        updated = value[1]
        value = value[0]
        currency = value[0]
        mult = 1000000 if value[-1] == "m" else 1000
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
        "full_name": full_name,
        "born": birth_date,
        "birth_place": birth_place,
        "birth_country": birth_country,
        "age": age,
        "height": height,
        "nationality": nationality[0],
        "position": position,
        "position_main": position_main,
        "position_alt1": pos_alt1,
        "position_alt2": pos_alt2,
        "foot": foot,
        "agent": agent,
        "outfitter": outfitter,
        "social_twitter": socialTwitter,
        "social_facebook": socialFacebook,
        "social_instagram": socialInstagram,
        "club": club,
        "joined": joined,
        "contracted": contracted,
        "extension": extension,
        "currency": currency,
        "mv": value,
        "update": updated,
    }

    return mydict
