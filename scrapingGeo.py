# FIRSTLY INSTALL THE REQUIRED PACKAGES USING THE COMMANDS GIVEN BELOW
# pip install bs4

from bs4 import BeautifulSoup as bs
import json
import requests


def saveJson(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)


def fetchHtmlAndParse(url):
    html = requests.get(url)
    return bs(html.content, 'html.parser')


def removeUnicode(text):
    return text.encode('ascii', 'ignore').decode().replace('\"', '')


def fetchAndFormatArticlesData(urls):
    articles = []

    for article in urls:
        bsObj = fetchHtmlAndParse(article)
        temp = {
            'title': '', 'image': '', 'date': '', 'data': ''
        }

        for     content in bsObj.find('h1'):
            temp['title'] = removeUnicode(content.text)

        for date in bsObj.find_all('p', class_='post-date-time'):
            temp['date'] = date.text.replace('\n', '')

        for source in bsObj.find_all('div', class_='medium-insert-images ui-sortable'):
            if(source.img.get('src') != None):
                temp['image'] = source.img.get('src')

        for content in bsObj.find_all('p', class_=''):
            if (content.text != None):
                temp['data'] = temp['data'] + removeUnicode(content.text)

        articles.append(temp)

    return articles


def fetchLinksLatestNewsGEO(url):
    bsObj = fetchHtmlAndParse(url)
    links = []

    for link in bsObj.find_all('div', class_='list'):
        if (link.a.get('href') != None):
            links.append(link.a.get('href'))

    return links


def fetchLinksGEO(url):
    bsObj = fetchHtmlAndParse(url)
    links = []

    for link in bsObj.find_all('div', class_='heading'):
        if(link.a.get('href') != None):
            links.append(link.a.get('href'))

    return links


def main():
    geoURL = 'https://geo.tv/'
    geoLatestNewsURL = 'https://www.geo.tv/latest-news/'

    saveJson(fetchAndFormatArticlesData(
        fetchLinksLatestNewsGEO(geoLatestNewsURL)), 'latestNewsGEO.json')

    saveJson(fetchAndFormatArticlesData(
        fetchLinksGEO(geoURL)), 'GEO.json')


main()
