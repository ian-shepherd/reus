import requests
from bs4 import BeautifulSoup

def get_page_soup(url):
    """
    Returns html of a given url
    
    Parameters:
    url (string): complete url

    Returns:
    html: pageSoup
    """


    headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

    pageTree = requests.get(url, headers=headers)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

    return pageSoup