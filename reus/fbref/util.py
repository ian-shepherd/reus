from typing import List

import bs4


def extract_stat(attribute, pattern):
    th = attribute.find("th")
    if pattern == "date":
        return th.text
    elif pattern == "url":
        return th.find("a", href=True)["href"]
    else:
        return attribute.find("td", {"data-stat": pattern}).text


def match_log_iterator(rows: List[bs4.Tag], attributes: list) -> list:
    mylist = []

    for row in rows:
        mydict = {}
        if row.get("class") is not None:
            continue
        if row.find("td", {"data-stat": "bench_explain"}) is not None:
            for attribute in attributes[:10]:
                att = extract_stat(attribute=row, pattern=attribute)
                mydict[attribute] = att
        else:
            for attribute in attributes:
                att = extract_stat(attribute=row, pattern=attribute)
                mydict[attribute] = att
        mylist.append(mydict)

    return mylist
