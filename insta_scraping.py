# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 13:54:20 2021

@author: Kossi Eloi Fabius DEFLY
"""

import requests
from bs4 import BeautifulSoup
import json
import cloudscraper

scraper = cloudscraper.create_scraper()

url = "https://www.instagram.com/explore/tags/jacqueschiracdeces/"

response = scraper.get(url)
soup = BeautifulSoup(response.text, 'lxml')

scripts = soup.findAll('script', {'type': 'text/javascript'})[3]
clean_data = str(scripts).replace(';</script>', '').replace('<script type="text/javascript">window._sharedData = ', '')

jsondata = json.loads(clean_data)

data = jsondata['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['edges'][1]['node']

data_text = data['edge_media_to_caption']['edges'][0]['node']['text']
data_image = data['display_url']
data_comments_link = 'https://www.instagram.com/p/' + data['shortcode']

comments = scraper.get(data_comments_link)
soup2 = BeautifulSoup(comments.text, 'lxml')
script = soup2.findAll('script', {'type': 'text/javascript'})[3]

print("----------------------------------")
"""print(data_comments_link, data_image, data_text)"""
print(script)
print("----------------------------------")