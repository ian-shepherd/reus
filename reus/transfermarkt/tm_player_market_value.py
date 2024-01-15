import json
import re

from ..util import fetch_api_data


def tm_player_market_value(json_file: json = None, player_id: str = None) -> list:
    """Extracts date, team, and market value from market value chart

    Args:
        json_file (json, optional): json file of player market value history. Defaults to None.
        player_id (str, optional): transfermarkt player id. Defaults to None.

    Returns:
        list: market value of player by date
    """

    assert (
        json_file is not None or player_id is not None
    ), "Either json_file or player_id must be specified"

    if json_file is not None:
        data = json_file
    else:
        data = fetch_api_data(
            f"https://www.transfermarkt.us/ceapi/marketValueDevelopment/graph/{player_id}"
        )

    # Get market values object
    market_values = data["list"]

    # generate empty list
    mylist = []

    # iterate through each data point and store attributes
    for m in market_values:
        date = m.get("datum_mw").replace("'", "")
        team = m.get("verein")
        age = m.get("age")
        mw = m.get("mw")
        currency = mw[0]
        mult = 1000000 if mw[-1] == "m" else 1000
        # keep only numbers and period
        value = float(re.sub("[^0-9.]", "", mw)) * mult

        # generate dictionary for each point
        mydict = {
            "date": date,
            "team": team,
            "age": age,
            "currency": currency,
            "value": value,
        }

        # append dictionary to list
        mylist.append(mydict)

    return mylist
