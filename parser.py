import requests
from bs4 import BeautifulSoup
import json
import pprint
import re
from contextlib import contextmanager


class Article:
    def __init__(self, name):
        self.name = name

    def getArticleStuff(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        content = soup.find('div', class_='body')
        return content

poteplenie = Article('n+1 article')

# print(poteplenie.getArticleStuff('https://nplus1.ru/news/2020/01/29/warm-arctic'))





class Source:
    def __init__(self, name):
        self.name = name

#    def getTitles(self, url):


    def getLinks(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        links = []

        links.append({
            'name': self.name
        })

        for link in soup.findAll('a', attrs={'href': re.compile("")}):
            # links.update({re.sub('\s+', ' ', link.text.strip().replace(u'\xa0', u' ').replace('\n', ' ')): (link.get('href') if 'http' in link.get('href') else self.name + link.get('href'))})
                                # delete multiple spaces               replace symbols                replace \n to space     add domain to relative links

            title = re.sub('/s+', ' ', link.text.strip().replace(u'\xa0', u' ').replace('\n', ' '))
            address = link.get('href') if 'http' in link.get('href') else self.name + link.get('href')

            if 'tut.by' in url:
                if len(title) > 2 and '/news/' in address:
                    links.append({
                        'title': title,
                        'url': address
                    })
            elif len(title) > 2:
                links.append({
                    'title': title,
                    'url': address
                })

        return links


class tutLinks(Source):
    def getLinks(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        links = []

        links.append({
            'name': self.name
        })
        for link in soup.findAll('a', attrs={'href': re.compile("")}):

            title = re.sub('/s+', ' ', link.text.strip().replace(u'\xa0', u' ').replace('\n', ' '))
            address = link.get('href') if 'http' in link.get('href') else self.name + link.get('href')

            if len(title) > 2 and '/news/' in address:
                links.append({
                    'title': title,
                    'url': address
                })
        return links


tut = tutLinks('https://tut.by')
pprint.pprint(tut.getLinks('https://tut.by'))

nPlusOne = Source('https://nplus1.ru')
esquire = Source('https://esquire.ru')
# tut = Source('https://tut.by')

#pprint.pprint(nPlusOne.getLinks('https://nplus1.ru/'))
# pprint.pprint(esquire.getLinks('https://esquire.ru'))
# pprint.pprint(tut.getLinks('https://tut.by'))



