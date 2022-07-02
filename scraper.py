import requests
from bs4 import BeautifulSoup
import pandas as pd
from IPython.display import display

players = []
positions = []
age = []
team = []
games_played = []
PPG = []

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

for row in table.tbody.find_all('tr'):
    columns = row.find_all('td')

    if (columns != []):
        players.append(columns[0].text.strip())
        positions.append(columns[1].text.strip())
        age.append(columns[2].text.strip())
        team.append(columns[3].text.strip())
        games_played.append(columns[4].text.strip())
        PPG.append(columns[28].text.strip()) 

df = pd.DataFrame( {
    'Name': players,
    'Positon': positions,
    'Age': age,
    'Team': team,
    'GP': games_played,
    'PPG': PPG
})

display(df)
        


