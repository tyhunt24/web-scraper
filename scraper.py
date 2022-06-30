import requests
from bs4 import BeautifulSoup
import pandas 

#gets the page that we are going to scrape
page = requests.get("https://www.basketball-reference.com/leagues/NBA_2022_per_game.html")

#creates a beatiful soup object that takes content to scrape and the correct parser
soup = BeautifulSoup(page.content, "html.parser")

#table classes to have
# for table in soup.find_all('table'):
#     print(table.get('class'))

#get the table that we want
tables = soup.find_all('table')
table = soup.find('table', class_="stats_table")
a = []

for row in table.tbody.find_all('tr'):
    columns = row.find_all('td')
    for i in columns:
        print(i.text)



