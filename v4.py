import requests
from bs4 import BeautifulSoup
import json
import pprint
import re
import random


class Source:

    def __init__(self, name, url):
        self.name = name
        self.url = url

    def getLinks(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        articles_list = []

        for link in soup.findAll('a', attrs={'href': re.compile("")}):
            title = re.sub('/s+', ' ', link.text.strip().replace(u'\xa0', u' ').replace('\n', ' '))
            address = link.get('href') if 'http' in link.get('href') else self.url + link.get('href')
                                                    # if links absolyte remove self url part

            if len(title) > 2:
                articles_list.append({
                    'title': title,
                    'url': address
                })


        list_styles = ['list-group-item-secondary', 'list-group-item-success', 'list-group-item-danger', 'list-group-item-warning', 'list-group-item-info', 'list-group-item-dark']
        html_list = """  <div class="col-xl-4">
                            <ul class="list-group">
              <li class="list-group-item">{}</li>""".format(self.name)

        for i in range(len(articles_list)):

            html_list += """
                <li class="list-group-item {} slide-up"><a href="{}">{}</a></li>
            """.format(random.choice(list_styles), articles_list[i]['url'], articles_list[i]['title'])

        return html_list + "</ul></div>"

    def createPage(self):

        page_head = """
        <!doctype html>
        <html lang="en">
        <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        
        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        
        <title>Hello, world!</title>
        <script src="https://unpkg.com/scrollreveal@4.0.0/dist/scrollreveal.min.js"></script>
        </head>
        <body>
        <div class="container-fluid">
        <div class="row">

        """.format(self.name)

        page_bottom = """
        </div>
        </div>
<script>
var slideUp = {
    distance: 1000,
    interval: 200,
    origin: 'bottom'
};</script>

<script>
ScrollReveal().reveal('.slide-up', slideUp);
</script>
        </body>
        </html>
        """

        html_page = page_head + tut.getLinks('https://tut.by') + esquire.getLinks('https://esquire.ru') + nplus1.getLinks('https://nplus1.ru') + page_bottom

        return html_page

nplus1 = Source('Nplus1', 'https://nplus1.ru')
tut = Source('tut.by', 'https://tut.by')
esquire = Source('esquire.ru', 'https://esquire.ru')

print(tut.createPage())
