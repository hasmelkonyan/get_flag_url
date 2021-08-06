import json
from bs4 import BeautifulSoup as BS
import requests
import re

HEAD_URL = "https://restcountries.eu/rest/v2/name/"

def getFlag(country_name):
    country_url = f"{HEAD_URL + country_name}"
    res = requests.get(country_url)
    html_page = res.content
    soup = BS(html_page, 'html.parser')
    text = soup.findAll(text=True)
    new_json = json.dumps(text)

    flag_url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', new_json)
    print(flag_url)


getFlag("uk")