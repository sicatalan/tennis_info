from urllib import request
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re


link = "https://www.atptour.com/es/rankings/singles"
page = requests.get(link)
soup = BeautifulSoup(page.text, "html.parser")


print(soup.prettify())
