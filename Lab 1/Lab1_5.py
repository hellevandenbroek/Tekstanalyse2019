#!/usr/bin/env python3

from lxml import html
import requests

page = requests.get('https://www.ntnu.edu/vacancies')
tree = html.fromstring(page.content)

all = tree.xpath('//div[@class="vacancies"]/h3/a/text()')

dates = ""
titles = ""
for stilling in all:
    titles += stilling[1:stilling.index(' - ')]
    dates += stilling[stilling.index(': '):len(stilling)]
    titles += '\n'
    dates += '\n'


print("Number of vacancies: ", len(all))
print(titles)
print(dates)

