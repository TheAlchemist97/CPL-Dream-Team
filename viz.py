import csv
import matplotlib.pyplot as plt

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

# Open the CSV file again to read the attributes for the top scorers
with open('C:/CPL/cpl_player.csv') as f:
    reader = csv.DictReader(f)
    top_scorer_data = None
    second_top_scorer_data = None
    for row in reader:
        if row['firstName'] + ' ' + row['lastName'] == top_scorers[0]:
            top_scorer_data = row
        elif row['firstName'] + ' ' + row['lastName'] == top_scorers[1]:
            second_top_scorer_data = row

# Create a bar graph for the top scorer
x_labels = ['Goals', 'Penalties', 'Expected Goals']
top_scorer_values = [int(top_scorer_data['Goal']), int(top_scorer_data['PenGoal']), float(top_scorer_data['ExpG'])]

fig, ax = plt.subplots()
ax.bar(x_labels, top_scorer_values, color = 'red')
ax.set_ylabel('Value')
ax.set_title('Top Scorer: ' + top_scorers[0])
plt.show()

# Create a bar graph for the second top scorer
second_top_scorer_values = [int(second_top_scorer_data['Goal']), int(second_top_scorer_data['PenGoal']), float(second_top_scorer_data['ExpG'])]

fig, ax = plt.subplots()
ax.bar(x_labels, second_top_scorer_values, color = 'blue')
ax.set_ylabel('Value')
ax.set_title('Second Top Scorer: ' + top_scorers[1])
plt.show()

import csv
import matplotlib.pyplot as plt

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

# Open the CSV file again to read the attributes for the top left midfielder
with open('C:/CPL/cpl_player.csv') as f:
    reader = csv.DictReader(f)
    top_left_midfielder_data = None
    for row in reader:
        if row['firstName'] + ' ' + row['lastName'] == top_left_midfielders[0]:
            top_left_midfielder_data = row

# Create a bar graph for the top left midfielder
x_labels = ['Assists', 'Exp. Assists', 'Chances Created']
top_left_midfielder_values = [int(top_left_midfielder_data['Ast']), float(top_left_midfielder_data['ExpA']), int(top_left_midfielder_data['Chance'])]

fig, ax = plt.subplots()
ax.bar(x_labels, top_left_midfielder_values, color='blue')
ax.set_ylabel('Value')
ax.set_title('Top Left Midfielder: ' + top_left_midfielders[0])
plt.show()

import csv
import matplotlib.pyplot as plt

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

with open('C:/CPL/cpl_player.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['firstName'] + ' ' + row['lastName'] == top_centre_attacking_midfielders[0]:
            goals = int(row['Goal'])
            assists = float(row['Ast'])
            chances_created = int(row['Chance'])
            break

fig, ax = plt.subplots(figsize=(8, 4))

attributes = ['Goals', 'Assists', 'Chances Created']
values = [goals, assists, chances_created]

ax.barh(attributes, values, color='purple')
ax.set_title('Top Centre Attacking Midfielder: ' + top_centre_attacking_midfielders[0])

plt.show()

import csv
import matplotlib.pyplot as plt

def find_top_defensive_midfielder(num_players):
    with open('C:/CPL/cpl_player.csv', newline='') as f:
        reader = csv.DictReader(f)
        players = []
        for row in reader:
            if row['Position'] == 'Defensive Midfielder':
                assists = int(row['Ast'])
                successful_tackles = int(row['SucflTkls'])
                interceptions = int(row['Int'])
                score = assists + successful_tackles + interceptions
                players.append((row['firstName'] + ' ' + row['lastName'], score))
        players.sort(key=lambda x: x[1], reverse=True)
        top_players = [player[0] for player in players[:num_players]]
        return top_players

top_defensive_midfielders = find_top_defensive_midfielder(1)
print(top_defensive_midfielders)

# Get data for the top defensive midfielder
with open('C:/CPL/cpl_player.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['firstName'] + ' ' + row['lastName'] == top_defensive_midfielders[0]:
            assists = int(row['Ast'])
            successful_tackles = int(row['SucflTkls'])
            interceptions = int(row['Int'])
            break

# Plot the data in a bar graph
labels = ['Assists', 'Successful Tackles', 'Interceptions']
values = [assists, successful_tackles, interceptions]
plt.bar(labels, values, color=['red', 'green', 'blue'])
plt.title('Top Defensive Midfielder: ' + top_defensive_midfielders[0])
plt.xlabel('Attributes')
plt.ylabel('Value')
plt.show()

import csv
import matplotlib.pyplot as plt

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

# Get the attributes of the top right midfielder
with open('C:/CPL/cpl_player.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['firstName'] + ' ' + row['lastName'] == top_right_midfielders[0]:
            goals = int(row['Goal'])
            assists = int(row['Ast'])
            exp_assists = float(row['ExpA'])



# Create a bar chart for the attributes
attributes = ['Goals', 'Assists', 'Expected Assists']
values = [goals, assists, exp_assists]

plt.bar(attributes, values)
plt.title('Top Right Midfielder: ' + top_right_midfielders[0])
plt.show()

import matplotlib.pyplot as plt

def find_left_back(num_players):
    with open('C:/CPL/cpl_player.csv', newline='') as f:
        reader = csv.DictReader(f)
        players = []
        for row in reader:
            if row['Position'] == 'Left Back':
                interceptions = int(row['Int'])
                successful_tackles = int(row['SucflTkls'])
                clean_sheets = int(row['CleanSheet'])
                score = interceptions + successful_tackles + clean_sheets
                players.append((row['firstName'] + ' ' + row['lastName'], score))
        players.sort(key=lambda x: x[1], reverse=True)
        top_players = [player[0] for player in players[:num_players]]
        return top_players

top_left_backs = find_left_back(1)

with open('C:/CPL/cpl_player.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['firstName'] + ' ' + row['lastName'] == top_left_backs[0]:
            interceptions = int(row['Int'])
            successful_tackles = int(row['SucflTkls'])
            clean_sheets = int(row['CleanSheet'])
            break

attributes = ['Interceptions', 'Successful Tackles', 'Clean Sheets']
values = [interceptions, successful_tackles, clean_sheets]

plt.bar(attributes, values)
plt.title('Top Left Back: ' + top_left_backs[0])
plt.show()

import csv
import matplotlib.pyplot as plt

def find_left_centre_back(num_players):
    with open('C:/CPL/cpl_player.csv', newline='') as f:
        reader = csv.DictReader(f)
        players = []
        for row in reader:
            if row['Position'] == 'Left Centre Back':
                interceptions = int(row['Int'])
                successful_tackles = int(row['SucflTkls'])
                clean_sheets = int(row['CleanSheet'])
                score = interceptions + successful_tackles + clean_sheets
                players.append((row['firstName'] + ' ' + row['lastName'], score))
        players.sort(key=lambda x: x[1], reverse=True)
        top_players = [player[0] for player in players[:num_players]]
        return top_players, players[0][1]

top_left_centre_backs, score = find_left_centre_back(1)
print(top_left_centre_backs)

plt.bar(['Interceptions', 'Successful Tackles', 'Clean Sheets'], [int(row['Int']), int(row['SucflTkls']), int(row['CleanSheet'])])
plt.title('Top Left Centre Back: ' + str(top_left_centre_backs))
plt.show()

import csv
import matplotlib.pyplot as plt

def find_right_centre_back(num_players):
    with open('C:/CPL/cpl_player.csv', newline='') as f:
        reader = csv.DictReader(f)
        players = []
        for row in reader:
            if row['Position'] == 'Right Centre Back':
                interceptions = int(row['Int'])
                successful_tackles = int(row['SucflTkls'])
                clean_sheets = int(row['CleanSheet'])
                score = interceptions + successful_tackles + clean_sheets
                players.append((row['firstName'] + ' ' + row['lastName'], score))
        players.sort(key=lambda x: x[1], reverse=True)
        top_players = [player[0] for player in players[:num_players]]
        return top_players

top_right_centre_backs = find_right_centre_back(1)
print(top_right_centre_backs)

with open('C:/CPL/cpl_player.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['firstName'] + ' ' + row['lastName'] == top_right_centre_backs[0]:
            interceptions = int(row['Int'])
            successful_tackles = int(row['SucflTkls'])
            clean_sheets = int(row['CleanSheet'])
            break

attributes = ['Interceptions', 'Successful Tackles', 'Clean Sheets']
values = [interceptions, successful_tackles, clean_sheets]

plt.bar(attributes, values)
plt.title('Top Right Centre Back: ' + top_right_centre_backs[0])
plt.xlabel('Attributes')
plt.ylabel('Values')
plt.show()

import csv
import matplotlib.pyplot as plt

def find_right_back(num_players):
    with open('C:/CPL/cpl_player.csv', newline='') as f:
        reader = csv.DictReader(f)
        players = []
        for row in reader:
            if row['Position'] == 'Right Back':
                interceptions = int(row['Int'])
                successful_tackles = int(row['SucflTkls'])
                clean_sheets = int(row['CleanSheet'])
                score = interceptions + successful_tackles + clean_sheets
                players.append((row['firstName'] + ' ' + row['lastName'], score))
        players.sort(key=lambda x: x[1], reverse=True)
        top_players = [player[0] for player in players[:num_players]]
        return top_players

top_right_backs = find_right_back(1)

with open('C:/CPL/cpl_player.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['firstName'] + ' ' + row['lastName'] == top_right_backs[0]:
            interceptions = int(row['Int'])
            successful_tackles = int(row['SucflTkls'])
            clean_sheets = int(row['CleanSheet'])
            break

labels = ['Interceptions', 'Successful Tackles', 'Clean Sheets']
values = [interceptions, successful_tackles, clean_sheets]

fig, ax = plt.subplots()
ax.barh(labels, values)
ax.set_title('Top Right Back: ' + top_right_backs[0])
ax.set_xlabel('Value')
ax.set_ylabel('Attribute')

plt.show()

import csv
import matplotlib.pyplot as plt
def find_top_goalkeeper(num_players):
    with open('C:/CPL/cpl_player.csv', newline='') as f:
        reader = csv.DictReader(f)
        players = []
        for row in reader:
            if row['Position'] == 'Goalkeeper':
                saves = int(row['Saves'])
                clean_sheets = int(row['CleanSheet'])
                score = saves + clean_sheets
                players.append((row['firstName'] + ' ' + row['lastName'], score))
        players.sort(key=lambda x: x[1], reverse=True)
        top_players = [player[0] for player in players[:num_players]]
        return top_players

top_goalkeepers = find_top_goalkeeper(1)
print(top_goalkeepers)

def visualize_goalkeeper_attributes(name):
    with open('C:/CPL/cpl_player.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['firstName'] + ' ' + row['lastName'] == name:
                saves = int(row['Saves'])
                clean_sheets = int(row['CleanSheet'])
                break

    attributes = ['Saves', 'Clean Sheets']
    values = [saves, clean_sheets]

    fig = plt.figure(figsize=(5, 5))

    # Create a bar chart
    plt.bar(attributes, values)

    # Add labels and title
    plt.xlabel('Attributes')
    plt.ylabel('Values')
    plt.title('Top Goalkeeper: ' + name)

    # Show the plot
    plt.show()

top_goalkeepers = find_top_goalkeeper(1)
visualize_goalkeeper_attributes(top_goalkeepers[0])

