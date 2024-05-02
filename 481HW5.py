import requests as req
from bs4 import BeautifulSoup as bs

#Ex 0:
def github() -> str:
    """
   This code would give you a link to my GitHub Repository page!
    """

    return "https://github.com/zixuan28/ECON481_HWs/blob/main/481HW5.py"

#Ex 1:
def scrape_code(url: str) -> str:
    """
    This function scrapes code from a given URL and returns all the code found as a single string.
    """
    web = req.get(url)
    soup = bs(web.text, 'html.parser')
    codes = [x.text for x in soup.find_all('code', {'class': 'sourceCode python'})]
    for code in codes:
        print(code)
    
    return None
