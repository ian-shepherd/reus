import json

from ..util import fetch_api_data


def tm_player_transfers(json_file: json = None, player_id: str = None) -> list:
    """Extracts player transfer information

    Args:
        json_file (json, optional): json file of player transfer history. Defaults to None.
        player_id (str, optional): transfermarkt player id. Defaults to None.

    Returns:
        list: player transfers
    """

    assert (
        json_file is not None or player_id is not None
    ), "Either json_file or player_id must be specified"

    if json_file is not None:
        data = json_file
    else:
        data = fetch_api_data(
            f"https://www.transfermarkt.us/ceapi/transferHistory/list/{player_id}"
        )

    # Get market values object
    transfers = data["transfers"]

    # generate empty list
    mylist = []

    # iterate through each data point and store attributes
    for t in transfers:
        date = t.get("date")
        left = t.get("from")["clubName"]
        left_url = t.get("from")["href"]
        joined = t.get("to")["clubName"]
        joined_url = t.get("to")["href"]

        mv = t.get("marketValue")
        fee = t.get("fee")
        currency = mv[0]

        # base of market value and fee
        mv_mult = 1000000 if mv[-1] == "m" else 1000
        fee_mult = 1000000 if fee[-1] == "m" else 1000

        # cleanup extraneous text in fee variable and determine transfer type
        if fee.lower() == "end of loan":
            transfer_type = "End of Loan"
            fee = fee.lower().replace("end of loan", "0")
        elif fee.lower() == "loan transfer":
            transfer_type = "Loan"
            fee = fee.lower().replace("loan transfer", "0")
        elif "loan fee:" in fee.lower():
            transfer_type = "Loan"
            fee = fee.lower().replace("loan fee:", "")
        elif "loan" in fee.lower():
            transfer_type = "Loan"
            fee = fee.lower().replace("loan", "")
        elif fee.lower() == "free transfer":
            transfer_type = "Free Transfer"
            fee = fee.lower().replace("free transfer", "0")
        elif fee == "-":
            transfer_type = "Youth"
            fee = fee.replace("-", "0")
        elif fee == "?":
            transfer_type = "Transfer"
            fee = fee.replace("?", "0")
        else:
            transfer_type = "Transfer"

        # no market value
        mv = mv.replace("-", "0")

        # excess text
        substring = ["Loan fee:", "€", "£", "$", "m", "Th.", "k", "â\u201a¬"]
        for s in substring:
            mv = mv.replace(s, "")
            fee = fee.replace(s, "")

        mydict = {
            "date": date,
            "left": left,
            "left_url": left_url,
            "joined": joined,
            "joined_url": joined_url,
            "type": transfer_type,
            "currency": currency,
            "market_value": float(mv.strip()) * mv_mult,
            "fee": float(fee.strip()) * fee_mult,
        }
        mylist.append(mydict)

    return mylist
