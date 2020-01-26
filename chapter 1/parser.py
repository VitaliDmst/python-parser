import requests
from bs4 import BeautifulSoup
import json
import pprint



def getTitles(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    titleByClass = soup.findAll(class_='title')
    linksByClass = soup.findAll(class_='title', href=True)
    result = {}
    for i in range(1, len(titleByClass)):
        # print(titleByClass[i].text)
        # print(linksByClass[i])
        result[f"article{i}"] = titleByClass[i].text
        result[f"url {i}"] = titleByClass[i]

        # result[f"url {i}"] = titleByClass[i]
    return result

pprint.pprint(getTitles('https://esquire.ru/'))


