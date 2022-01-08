def tm_player_transfers(pageSoup):
    """
    Extracts player transfer information

    Parameters:
    pageSoup (html document): bs4 object of player referenced in url

    Returns:
    list: player transfers
    """

    # Find transfer object
    transfer_data = pageSoup.find('div', {'data-viewport' : 'Transferhistorie'})
    table = transfer_data.find('table')
    tbody = table.find('tbody')

    # Find rows
    rows = tbody.find_all('tr')

    # Generate empty list
    mylist = []

    # iterate through each transfer and store attributes
    for row in rows:

        # extract teams
        teams = row.find_all('td', {'class' : 'no-border-rechts vereinswappen'})
        left = teams[0].find('img', alt=True)['alt']
        joined = teams[1].find('img', alt=True)['alt']

        # extract raw market value and fee
        mv = row.find('td', {'class' : 'zelle-mw'}).text
        fee = row.find('td', {'class' : 'zelle-abloese'}).text

        # extract currency
        currency = mv[0]

        # base of market value and fee
        mv_mult = 1000000 if mv[-1] == 'm' else 1000
        fee_mult = 1000000 if fee[-1] == 'm' else 1000

        # cleanup extraneous text in fee variable and determine transfer type
        if fee.lower() == "end of loan":
            transfer_type = "End of Loan"
            fee = fee.lower().replace('end of loan', '0')
        elif fee.lower() == "loan transfer":
            transfer_type = "Loan"
            fee = fee.lower().replace('loan transfer', '0')
        elif "loan fee:" in fee.lower():
            transfer_type = "Loan"
            fee = fee.lower().replace('loan fee:', '')
        elif "loan" in fee.lower():
            transfer_type = "Loan"
            fee = fee.lower().replace('loan', '')
        elif fee.lower() == "free transfer":
            transfer_type = "Free Transfer"
            fee = fee.lower().replace('free transfer', '0')
        elif fee == "-":
            transfer_type = "Youth"
            fee = fee.replace('-', '0')
        elif fee == "?":
            transfer_type = "Transfer"
            fee = fee.replace('?', '0')
        else:
            transfer_type = 'Transfer'
        
        # no market value
        mv = mv.replace('-', '0')

        # excess text
        substring = ['Loan fee:', '€', '£', '$', 'm', 'Th.', 'â\u201a¬']
        for s in substring:
            mv = mv.replace(s, '')
            fee = fee.replace(s, '')

        # generate dictionary for each transfer
        mydict = {'left' : left,
                  'joined' : joined,
                  'type' : transfer_type,
                  'currency' : currency,
                  'market_value' : float(mv.strip()) * mv_mult,
                  'fee' : float(fee.strip()) * fee_mult}

        # append dictionary to list
        mylist.append(mydict)

    return mylist