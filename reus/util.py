import requests
from bs4 import BeautifulSoup


def get_page_soup(url: str):
    """Returns html of a given url

    Args:
        url (str): _description_

    Returns:
        bs4: pageSoup
    """

    pageTree = requests.get(url)
    pageSoup = BeautifulSoup(pageTree.content, "html.parser")

    return pageSoup


def get_page_soup_headers(url: str):
    """Returns html of a given url

    Args:
        url (str): _description_

    Returns:
        bs4: pageSoup
    """

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }

    pageTree = requests.get(url, headers=headers)
    pageSoup = BeautifulSoup(pageTree.content, "html.parser")

    return pageSoup
