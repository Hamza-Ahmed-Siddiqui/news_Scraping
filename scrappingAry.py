# FIRSTLY INSTALL THE REQUIRED PACKAGES USING THE COMMANDS GIVEN BELOW
# pip install bs4 24378.979

from bs4 import BeautifulSoup as bs
import json
import requests

S = "Imran Khan"

def saveJson(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)


def fetchHtmlAndParse(url):
    html = requests.get(url)
    return bs(html.content, 'html.parser')


def removeUnicode(text):
    return text.encode('ascii', 'ignore').decode().replace('\"', '')
