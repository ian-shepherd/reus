def tm_player_injury_scraper(pageSoup) -> list:
    """Helper function extracts player injury history

    Args:
        pageSoup (bs4): bs4 object of player page referenced in url

    Returns:
        list: player injuries
    """

    # find table
    table = pageSoup.find("table")
    tbody = table.find("tbody")

    # Find rows
    rows = tbody.find_all("tr")

    # Generate empty list
    mylist = []

    # iterate through each injury and store attributes
    for row in rows:
        dates = row.find_all("td", {"class": "zentriert"})
        season = dates[0].text
        injury = row.find("td", {"class": "hauptlink"}).text
        start = dates[1].text
        end = dates[2].text
        days = row.find("td", {"class": "rechts"}).text

        # error handling for current injuries
        try:
            games_missed = row.find(
                "td", {"class": "rechts hauptlink wappen_verletzung"}
            ).text
        except AttributeError:
            games_missed = row.find(
                "td", {"class": "rechts hauptlink wappen_verletzung bg_rot_20"}
            ).text

        # generate dictionary for each transfer
        mydict = {
            "season": season,
            "injury": injury,
            "start": start,
            "end": end,
            "days": days,
            "games_missed": games_missed.replace("-", "0"),
        }

        # append dictionary to list
        mylist.append(mydict)

    return mylist


def tm_format_currency(value: str) -> float:
    """Helper function to convert values from string to float values

    Args:
        value (str): raw value of fee or market value

    Returns:
        float: converted value
    """

    # Remove currency
    currencies = ["€", "£", "$"]
    for c in currencies:
        value = value.replace(c, "")

    # Determine multiplier
    mult = 1000000 if value[-1] == "m" else 1000

    # Convert to float
    value = float(value.replace("k", "").replace("m", "").strip()) * mult

    return value
