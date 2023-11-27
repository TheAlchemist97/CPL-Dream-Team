import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import chardet
import io
from io import open

with open("C:/CPL/cpl_player.csv", "rb") as f:
    result = chardet.detect(f.read())

#####################################################Forwards###########################################################
#Centre_Forward

#Goals
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
centre_forwards = data[data['Position'] == 'Centre Forward']

# Create a bar chart visualization of goals scored
sns.barplot(x='firstName', y='Goal', data=centre_forwards)
plt.xlabel('Centre Forwards')
plt.ylabel('Goals Scored')
plt.title('Goals scored by Centre Forwards')
plt.xticks(rotation=90)
plt.show()

#Penalties
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
centre_forwards = data[data['Position'] == 'Centre Forward']

# Create a bar chart visualization of goals scored
sns.barplot(x='firstName', y='PenGoal', data=centre_forwards)
plt.xlabel('Centre Forwards')
plt.ylabel('Penalties Scored')
plt.title('Penalties scored by Centre Forwards')
plt.xticks(rotation=90)
plt.show()

#Expected Goals
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
centre_forwards = data[data['Position'] == 'Centre Forward']

# Create a bar chart visualization of goals scored
sns.barplot(x='firstName', y='ExpG', data=centre_forwards)
plt.xlabel('Centre Forwards')
plt.ylabel('Expected Goals')
plt.title('Expected Goals by Centre Forwards')
plt.xticks(rotation=90)
plt.show()

######################################################Midfielders######################################################

#Left_Midfielder

#Assists
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
left_midfielder = data[data['Position'] == 'Left Midfielder']

# Create a bar chart visualization of goals scored
sns.pointplot(x='firstName', y='Ast', data=left_midfielder)
plt.xlabel('Left Midfielders')
plt.ylabel('Assists')
plt.title('Assists by Left Midfielders')
plt.xticks(rotation=90)
plt.show()

#Expected_Assists
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
left_midfielder = data[data['Position'] == 'Left Midfielder']

# Create a bar chart visualization of goals scored
sns.pointplot(x='firstName', y='ExpA', data=left_midfielder)
plt.xlabel('Left Midfielders')
plt.ylabel('Expected Assists')
plt.title('Expected Assists by Left Midfielders')
plt.xticks(rotation=90)
plt.show()

#Chances_Created
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
left_midfielder = data[data['Position'] == 'Left Midfielder']

# Create a bar chart visualization of goals scored
sns.pointplot(x='firstName', y='Chance', data=left_midfielder)
plt.xlabel('Left Midfielders')
plt.ylabel('Chances')
plt.title('Chances Created by Left Midfielders')
plt.xticks(rotation=90)
plt.show()

#Centre_Attacking_Midfielder

#Goals
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
centre_attacking_midfielder = data[data['Position'] == 'Centre Attacking Midfielder']

# Create a bar chart visualization of goals scored
sns.barplot(x='firstName', y='Goal', data=centre_attacking_midfielder)
plt.xlabel('Centre Attacking Midfielder')
plt.ylabel('Goals Scored')
plt.title('Goals by Centre Attacking Midfielder')
plt.xticks(rotation=90)
plt.show()

#Assists
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
centre_attacking_midfielder = data[data['Position'] == 'Centre Attacking Midfielder']

# Create a bar chart visualization of goals scored
sns.barplot(x='firstName', y='Ast', data=centre_attacking_midfielder)
plt.xlabel('Centre Attacking Midfielder')
plt.ylabel('Assists')
plt.title('Assists by Centre Attacking Midfielder')
plt.xticks(rotation=90)
plt.show()

#Chances_Created
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
centre_attacking_midfielder = data[data['Position'] == 'Centre Attacking Midfielder']

# Create a bar chart visualization of goals scored
sns.barplot(x='firstName', y='Chance', data=centre_attacking_midfielder)
plt.xlabel('Centre Attacking Midfielder')
plt.ylabel('Chances Created')
plt.title('Chances Created by Centre Attacking Midfielders')
plt.xticks(rotation=90)
plt.show()

#Defensive_Midfielder

#Assists
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
defensive_midfielder = data[data['Position'] == 'Defensive Midfielder']

# Create a bar chart visualization of goals scored
sns.pointplot(x='firstName', y='Ast', data=defensive_midfielder)
plt.xlabel('Defensive Midfielder')
plt.ylabel('Assists')
plt.title('Assists by Defensive Midfielder')
plt.xticks(rotation=90)
plt.show()

#Successful_Tackles
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
defensive_midfielder = data[data['Position'] == 'Defensive Midfielder']

# Create a bar chart visualization of goals scored
sns.pointplot(x='firstName', y='SucflTkls', data=defensive_midfielder)
plt.xlabel('Defensive Midfielder')
plt.ylabel('Successful Tackles')
plt.title('Successful Tackles by Defensive Midfielder')
plt.xticks(rotation=90)
plt.show()

#Interceptions
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
defensive_midfielder = data[data['Position'] == 'Defensive Midfielder']

# Create a bar chart visualization of goals scored
sns.pointplot(x='firstName', y='Int', data=defensive_midfielder)
plt.xlabel('Defensive Midfielder')
plt.ylabel('Interceptions')
plt.title('Interceptions by Defensive Midfielder')
plt.xticks(rotation=90)
plt.show()

#Right_Midfielder

#Assists
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
right_midfielder = data[data['Position'] == 'Right Midfielder']

# Create a bar chart visualization of goals scored
sns.barplot(x='firstName', y='Ast', data=right_midfielder)
plt.xlabel('Right Midfielder')
plt.ylabel('Assists')
plt.title('Assists by Right Midfielder')
plt.xticks(rotation=90)
plt.show()

#ExpA
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
right_midfielder = data[data['Position'] == 'Right Midfielder']

# Create a bar chart visualization of goals scored
sns.barplot(x='firstName', y='ExpA', data=right_midfielder)
plt.xlabel('Right Midfielder')
plt.ylabel('Expected Assists')
plt.title('Expected Assists by Right Midfielder')
plt.xticks(rotation=90)
plt.show()

#Chances_Created
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
right_midfielder = data[data['Position'] == 'Right Midfielder']

# Create a bar chart visualization of goals scored
sns.barplot(x='firstName', y='Chance', data=right_midfielder)
plt.xlabel('Right Midfielder')
plt.ylabel('Chance Created')
plt.title('Chances Created by Right Midfielder')
plt.xticks(rotation=90)
plt.show()

########################################################Defenders######################################################

#Left_Back

#Interceptions
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
left_back = data[data['Position'] == 'Left Back']

# Create a bar chart visualization of goals scored
sns.pointplot(x='firstName', y='Int', data=left_back)
plt.xlabel('Left Back')
plt.ylabel('Interceptions')
plt.title('Interceptions by Left Back')
plt.xticks(rotation=90)
plt.show()

#Successful_Tackles
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
left_back = data[data['Position'] == 'Left Back']

# Create a bar chart visualization of goals scored
sns.pointplot(x='firstName', y='SucflTkls', data=left_back)
plt.xlabel('Left Back')
plt.ylabel('Successful Tackles')
plt.title('Successful Tackles by Left Back')
plt.xticks(rotation=90)
plt.show()

#Successful_Duels
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
left_back = data[data['Position'] == 'Left Back']

# Create a bar chart visualization of goals scored
sns.pointplot(x='firstName', y='SucflDuels', data=left_back)
plt.xlabel('Left Back')
plt.ylabel('Successful Duels')
plt.title('Successful Duels by Left Back')
plt.xticks(rotation=90)
plt.show()

#Left_Centre_Back

#Interceptions
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
left_centre_back = data[data['Position'] == 'Left Centre Back']

# Create a bar chart visualization of goals scored
sns.barplot(x='firstName', y='Int', data=left_centre_back)
plt.xlabel('Left Centre Back')
plt.ylabel('Int')
plt.title('Interceptions by Left Centre Back')
plt.xticks(rotation=90)
plt.show()

#Successful_Tackles
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
left_centre_back = data[data['Position'] == 'Left Centre Back']

# Create a bar chart visualization of goals scored
sns.barplot(x='firstName', y='SucflTkls', data=left_centre_back)
plt.xlabel('Left Centre Back')
plt.ylabel('Successful Tackles')
plt.title('Successful Tackles by Left Centre Back')
plt.xticks(rotation=90)
plt.show()

#Clearance
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
left_centre_back = data[data['Position'] == 'Left Centre Back']

# Create a bar chart visualization of goals scored
sns.barplot(x='firstName', y='Clrnce', data=left_centre_back)
plt.xlabel('Left Centre Back')
plt.ylabel('Clearance')
plt.title('Clearance by Left Centre Back')
plt.xticks(rotation=90)
plt.show()

#Right_Centre_Back

#Interceptions
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
right_centre_back = data[data['Position'] == 'Right Centre Back']

# Create a bar chart visualization of goals scored
sns.barplot(x='firstName', y='Int', data=right_centre_back)
plt.xlabel('Right Centre Back')
plt.ylabel('Int')
plt.title('Interceptions by Right Centre Back')
plt.xticks(rotation=90)
plt.show()

#Successful_Tackles
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
right_centre_back = data[data['Position'] == 'Right Centre Back']

# Create a bar chart visualization of goals scored
sns.barplot(x='firstName', y='SucflTkls', data=right_centre_back)
plt.xlabel('Right Centre Back')
plt.ylabel('Successful Tackles')
plt.title('Successful Tackles by Right Centre Back')
plt.xticks(rotation=90)
plt.show()

#Clearance
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
right_centre_back = data[data['Position'] == 'Right Centre Back']

# Create a bar chart visualization of goals scored
sns.barplot(x='firstName', y='Clrnce', data=right_centre_back)
plt.xlabel('Right Centre Back')
plt.ylabel('Clearance')
plt.title('Clearance by Right Centre Back')
plt.xticks(rotation=90)
plt.show()

#Right_Back

#Interceptions
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
right_back = data[data['Position'] == 'Right Back']

# Create a bar chart visualization of goals scored
sns.pointplot(x='firstName', y='Int', data=right_back)
plt.xlabel('Right Back')
plt.ylabel('Interceptions')
plt.title('Interceptions by Right Back')
plt.xticks(rotation=90)
plt.show()

#Successful_Tackles
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
right_back = data[data['Position'] == 'Right Back']

# Create a bar chart visualization of goals scored
sns.pointplot(x='firstName', y='SucflTkls', data=right_back)
plt.xlabel('Right Back')
plt.ylabel('Successful Tackles')
plt.title('Successful Tackles by Right Back')
plt.xticks(rotation=90)
plt.show()

#Successful_Duels
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
right_back = data[data['Position'] == 'Right Back']

# Create a bar chart visualization of goals scored
sns.pointplot(x='firstName', y='SucflDuels', data=right_back)
plt.xlabel('Right Back')
plt.ylabel('Successful Duels')
plt.title('Successful Duels by Right Back')
plt.xticks(rotation=90)
plt.show()


##################################################Goalkeeper############################################################

#Saves
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
goalkeeper = data[data['Position'] == 'Goalkeeper']

# Create a bar chart visualization of goals scored
sns.barplot(x='firstName', y='Saves', data=goalkeeper)
plt.xlabel('Goalkeeper')
plt.ylabel('Saves')
plt.title('Saves by Goalkeeper')
plt.xticks(rotation=90)
plt.show()

#CleanSheet
data = pd.read_csv("C:/CPL/cpl_player.csv", encoding=result["encoding"])

# Filter data for centre forwards
goalkeeper = data[data['Position'] == 'Goalkeeper']

# Create a bar chart visualization of goals scored
sns.barplot(x='firstName', y='CleanSheet', data=goalkeeper)
plt.xlabel('Goalkeeper')
plt.ylabel('CleanSheet')
plt.title('CleanSheet by Goalkeeper')
plt.xticks(rotation=90)
plt.show()


