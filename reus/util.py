import requests
from bs4 import BeautifulSoup


def get_page_soup(url: str, save_html: bool = False) -> BeautifulSoup:
    """Returns html of a given url

    Args:
        url (str): The URL to fetch the HTML from.
        save_html (bool): Whether to save the HTML content or not.

    Returns:
        bs4: pageSoup
    """

    pageTree = requests.get(url)
    pageSoup = BeautifulSoup(pageTree.content, "html.parser")

    if save_html:
        return pageSoup, pageTree.content
    else:
        return pageSoup


def get_page_soup_headers(url: str, save_html: bool = False) -> BeautifulSoup:
    """Returns html of a given url

    Args:
        url (str): The URL to fetch the HTML from.
        save_html (bool): Whether to save the HTML content or not.

    Returns:
        bs4: pageSoup
    """

    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"  # noqa: E501
    headers = {"User-Agent": USER_AGENT}

    pageTree = requests.get(url, headers=headers)
    pageSoup = BeautifulSoup(pageTree.content, "html.parser")

    if save_html:
        return pageSoup, pageTree.content
    else:
        return pageSoup
