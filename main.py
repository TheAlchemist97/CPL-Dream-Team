import csv

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import chardet
import io
from io import open

with open("C:/CPL/cpl_player.csv", "rb") as f:
    result = chardet.detect(f.read())

df = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])
print(df)

most_goals = df["Goal"].max()
top_scorer = df.loc[df["Goal"] == most_goals, "firstName"].values[0]

# Print the top scorer name
print(f" {top_scorer} and {most_goals}")

def find_top_scorers():
    with open('C:/CPL/cpl_player.csv') as f:
        reader = csv.DictReader(f)
        top_scorer = None
        top_score = 0
        second_top_scorer = None
        second_top_score = 0
        for row in reader:
            if row['Position'] == 'Centre Forward':
                goals = int(row['Goal'])
                penalties = int(row['PenGoal'])
                expected = float(row['ExpG'])
                score = goals + penalties - expected
                if score > top_score:
                    second_top_score = top_score
                    second_top_scorer = top_scorer
                    top_scorer = row['firstName'] + ' ' + row['lastName']
                    top_score = score
                elif score > second_top_score:
                    second_top_score = score
                    second_top_scorer = row['firstName'] + ' ' + row['lastName']
        return [top_scorer, second_top_scorer]

top_scorers = find_top_scorers()
print(top_scorers)

def find_top_left_midfielders(num_players):
    with open('C:/CPL/cpl_player.csv', newline='') as f:
        reader = csv.DictReader(f)
        players = []
        for row in reader:
            if row['Position'] == 'Left Midfielder':
                assists = int(row['Ast'])
                exp_assists = float(row['ExpA'])
                chances_created = int(row['Chance'])
                score = assists * 2 + exp_assists + chances_created * 0.5
                players.append((row['firstName'] + ' ' + row['lastName'], score))
        players.sort(key=lambda x: x[1], reverse=True)
        top_players = [player[0] for player in players[:num_players]]
        return top_players

top_left_midfielders = find_top_left_midfielders(1)
print(top_left_midfielders)


def find_top_centre_attacking_midfielders(num_players):
    with open('C:/CPL/cpl_player.csv', newline='') as f:
        reader = csv.DictReader(f)
        players = []
        for row in reader:
            if row['Position'] == 'Centre Attacking Midfielder':
                goals = int(row['Goal'])
                assists = float(row['Ast'])
                chances_created = int(row['Chance'])
                score = goals * 2 + assists + chances_created * 0.5
                players.append((row['firstName'] + ' ' + row['lastName'], score))
        players.sort(key=lambda x: x[1], reverse=True)
        top_players = [player[0] for player in players[:num_players]]
        return top_players

top_centre_attacking_midfielders = find_top_centre_attacking_midfielders(1)
print(top_centre_attacking_midfielders)

def find_top_defensive_midfielder(num_players):
    with open('C:/CPL/cpl_player.csv', newline='') as f:
        reader = csv.DictReader(f)
        players = []
        for row in reader:
            if row['Position'] == 'Defensive Midfielder':
                assists = int(row['Ast'])
                successful_tackles = int(row['SucflTkls'])
                interceptions = int(row['Int'])
                score = assists + successful_tackles * 2 + interceptions * 0.5
                players.append((row['firstName'] + ' ' + row['lastName'], score))
        players.sort(key=lambda x: x[1], reverse=True)
        top_players = [player[0] for player in players[:num_players]]
        return top_players

top_defensive_midfielders = find_top_defensive_midfielder(1)
print(top_defensive_midfielders)

def find_right_midfielders(num_players):
    with open('C:/CPL/cpl_player.csv', newline='') as f:
        reader = csv.DictReader(f)
        players = []
        for row in reader:
            if row['Position'] == 'Right Midfielder':
                assists = int(row['Ast'])
                exp_assists = float(row['ExpA'])
                chances_created = int(row['Chance'])
                score = assists * 2 + exp_assists + chances_created * 0.5
                players.append((row['firstName'] + ' ' + row['lastName'], score))
        players.sort(key=lambda x: x[1], reverse=True)
        top_players = [player[0] for player in players[:num_players]]
        return top_players

top_right_midfielders = find_right_midfielders(1)
print(top_right_midfielders)

def find_left_back(num_players):
    with open('C:/CPL/cpl_player.csv', newline='') as f:
        reader = csv.DictReader(f)
        players = []
        for row in reader:
            if row['Position'] == 'Left Back':
                interceptions = int(row['Int'])
                successful_tackles = int(row['SucflTkls'])
                successful_duels = int(row['SucflDuels'])
                score = interceptions * 2 + successful_tackles * 0.5 + successful_duels
                players.append((row['firstName'] + ' ' + row['lastName'], score))
        players.sort(key=lambda x: x[1], reverse=True)
        top_players = [player[0] for player in players[:num_players]]
        return top_players

top_left_backs = find_left_back(1)
print(top_left_backs)

def find_left_centre_back(num_players):
    with open('C:/CPL/cpl_player.csv', newline='') as f:
        reader = csv.DictReader(f)
        players = []
        for row in reader:
            if row['Position'] == 'Left Centre Back':
                interceptions = int(row['Int'])
                successful_tackles = int(row['SucflTkls'])
                clearance = int(row['Clrnce'])
                score = interceptions + successful_tackles * 2 + clearance * 3
                players.append((row['firstName'] + ' ' + row['lastName'], score))
        players.sort(key=lambda x: x[1], reverse=True)
        top_players = [player[0] for player in players[:num_players]]
        return top_players

top_left_centre_backs = find_left_centre_back(1)
print(top_left_centre_backs)

def find_right_centre_back(num_players):
    with open('C:/CPL/cpl_player.csv', newline='') as f:
        reader = csv.DictReader(f)
        players = []
        for row in reader:
            if row['Position'] == 'Right Centre Back':
                interceptions = int(row['Int'])
                successful_tackles = int(row['SucflTkls'])
                clearance = int(row['Clrnce'])
                score = interceptions + successful_tackles * 2 + clearance * 3
                players.append((row['firstName'] + ' ' + row['lastName'], score))
        players.sort(key=lambda x: x[1], reverse=True)
        top_players = [player[0] for player in players[:num_players]]
        return top_players

top_right_centre_backs = find_right_centre_back(1)
print(top_right_centre_backs)

def find_right_back(num_players):
    with open('C:/CPL/cpl_player.csv', newline='') as f:
        reader = csv.DictReader(f)
        players = []
        for row in reader:
            if row['Position'] == 'Right Back':
                interceptions = int(row['Int'])
                successful_tackles = int(row['SucflTkls'])
                successful_duels = int(row['SucflDuels'])
                score = interceptions * 2 + successful_tackles * 0.5 + successful_duels
                players.append((row['firstName'] + ' ' + row['lastName'], score))
        players.sort(key=lambda x: x[1], reverse=True)
        top_players = [player[0] for player in players[:num_players]]
        return top_players

top_right_backs = find_right_back(1)
print(top_right_backs)

def find_top_goalkeeper(num_players):
    with open('C:/CPL/cpl_player.csv', newline='') as f:
        reader = csv.DictReader(f)
        players = []
        for row in reader:
            if row['Position'] == 'Goalkeeper':
                saves = int(row['Saves'])
                clean_sheets = int(row['CleanSheet'])
                score = saves * 2 + clean_sheets * 3
                players.append((row['firstName'] + ' ' + row['lastName'], score))
        players.sort(key=lambda x: x[1], reverse=True)
        top_players = [player[0] for player in players[:num_players]]
        return top_players

top_goalkeepers = find_top_goalkeeper(1)
print(top_goalkeepers)

import PIL
from PIL import Image
with Image.open("C:\CPL\Dream Team.jpeg") as img:
    img.show()


















