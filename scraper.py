import requests
from bs4 import BeautifulSoup
import pandas 
import os

#gets the page that we are going to scrape
page = requests.get("https://www.basketball-reference.com/leagues/NBA_2022_per_game.html")

#creates a beatiful soup object that takes content to scrape and the correct parser
soup = BeautifulSoup(page.content, "html.parser")

#print(soup.prettify())

#find my element by table and classname
table = soup.find('table', class_="stats_table")
rows = table.find_all('tr')




