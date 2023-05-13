from ..util import get_page_soup_headers


def tm_player_transfers(pageSoup=None, url: str = None) -> list:
    """Extracts player transfer information

    Args:
        pageSoup (bs4, optional): bs4 object of player page referenced in url. Defaults to None.
        url (str, optional): path of transfermarkt player page. Defaults to None.

    Returns:
        list: player transfers
    """

    assert (
        pageSoup is not None or url is not None
    ), "Either pageSoup or url must be provided"

    if pageSoup is None:
        pageSoup = get_page_soup_headers(url)

    # Find transfer object
    transfer_data = pageSoup.find("div", {"data-viewport": "Transferhistorie"})
    table = transfer_data.find_all("div", {"class": "tm-player-transfer-history-grid"})

    # Generate empty list
    mylist = []

    # iterate through each transfer and store attributes
    # for row in rows:
    for row in table[1:-1]:
        # extract teams
        left = row.find(
            "div", {"class": "tm-player-transfer-history-grid__old-club"}
        ).text.strip()
        joined = row.find(
            "div", {"class": "tm-player-transfer-history-grid__new-club"}
        ).text.strip()

        # extract raw market value and fee
        mv = row.find(
            "div", {"class": "tm-player-transfer-history-grid__market-value"}
        ).text.strip()
        fee = row.find(
            "div", {"class": "tm-player-transfer-history-grid__fee"}
        ).text.strip()

        # extract currency
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
        substring = ["Loan fee:", "€", "£", "$", "m", "Th.", "â\u201a¬"]
        for s in substring:
            mv = mv.replace(s, "")
            fee = fee.replace(s, "")

        # generate dictionary for each transfer
        mydict = {
            "left": left,
            "joined": joined,
            "type": transfer_type,
            "currency": currency,
            "market_value": float(mv.strip()) * mv_mult,
            "fee": float(fee.strip()) * fee_mult,
        }

        # append dictionary to list
        mylist.append(mydict)

    return mylist
