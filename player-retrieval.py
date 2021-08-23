!pip install sportsreference #install the sportsreference libraries so that colab can access it. Sometimes it times out so might have to run this bloack again
!pip install sportsipy #same as above, installs the library, each houses different information, but both are needed
from sportsipy.nba.teams import Teams #allows us to get team abbreviations, necessary to get all of the player data
from sportsreference.nba.roster import Roster #with the team abbreviations, we get the player data housed in each roster
from sportsipy.nba.roster import Player #once we have all of the player ID's we use this to get specific data for each player
import pandas as pd #to show the data in a dataframe so we can export it to an excel file

teams=[] 
playerid=[]
playername=[]
for team in Teams():
  teams.append(team.abbreviation) #this allows us to get the abbreviation of each team in a list
for i in teams:
  for player in Roster(i, year = '2021').players: #this takes each abbreviation and returns that teams 2021 roster
    playerid.append(player.player_id) #within that roster, we get each player's ID and put that into a list
for i in playerid:
  playername.append(Player(i).name) #with the player ID we get everything so now we start by just getting their name to match with their ID
FGM = [] 
FGA = [] 
TPM=[]
TPA=[]
THRPM = [] 
THRPA = [] 
FTM = [] 
FTA = [] 
ORB = [] 
DRB = [] 
AST = [] 
STL = [] 
BLK = [] 
TOV = [] 
PF = []
MP = []
G = []
GS = []
for i in playerid:
  try:
    a=((Player(i)('2020-21').field_goals/Player(i)('2020-21').minutes_played)*36) 
  except TypeError: #this and the following cells go through each player ID and return a stat (per 36 minutes via my calculation)
    a=0 #need the try/except method for the cases where a player doesnt have that stat. The library holds it as a nonetype, but we need it as a 0, so this passes over the cases of a nonetype and puts a 0 in its place
  FGM.append(a)
for i in playerid:
  try:
    b=((Player(i)('2020-21').field_goal_attempts/Player(i)('2020-21').minutes_played)*36)
  except TypeError:
    b=0
  FGA.append(b)
for i in playerid:
  try:
    r=((Player(i)('2020-21').two_pointers/Player(i)('2020-21').minutes_played)*36)
  except TypeError:
    r=0
  TPM.append(r)
for i in playerid:
  try:
    s=((Player(i)('2020-21').two_point_attempts/Player(i)('2020-21').minutes_played)*36)
  except TypeError:
    s=0
  TPA.append(s)
for i in playerid:
  try:
    c=((Player(i)('2020-21').three_pointers/Player(i)('2020-21').minutes_played)*36)
  except TypeError:
    c=0
  THRPM.append(c)
for i in playerid:
  try:
    e=((Player(i)('2020-21').three_point_attempts/Player(i)('2020-21').minutes_played)*36)
  except TypeError:
    e=0
  THRPA.append(e)
for i in playerid:
  try:
    f=((Player(i)('2020-21').free_throws/Player(i)('2020-21').minutes_played)*36)
  except TypeError:
    f=0
  FTM.append(f)
for i in playerid:
  try:
    g=((Player(i)('2020-21').free_throw_attempts/Player(i)('2020-21').minutes_played)*36)
  except TypeError:
    g=0
  FTA.append(g)
for i in playerid:
  try:
    h=((Player(i)('2020-21').offensive_rebounds/Player(i)('2020-21').minutes_played)*36)
  except TypeError:
    h=0
  ORB.append(h)
for i in playerid:
  try:
    j=((Player(i)('2020-21').defensive_rebounds/Player(i)('2020-21').minutes_played)*36)
  except TypeError:
    j=0
  DRB.append(j)
for i in playerid:
  try:
    k=((Player(i)('2020-21').assists/Player(i)('2020-21').minutes_played)*36)
  except TypeError:
    k=0
  AST.append(k)
for i in playerid:
  try:
    l=((Player(i)('2020-21').steals/Player(i)('2020-21').minutes_played)*36)
  except TypeError:
    l=0
  STL.append(l)
for i in playerid:
  try:
    m=((Player(i)('2020-21').blocks/Player(i)('2020-21').minutes_played)*36)
  except TypeError:
    m=0
  BLK.append(m)
for i in playerid:
  try:
    n=((Player(i)('2020-21').turnovers/Player(i)('2020-21').minutes_played)*36)
  except TypeError:
    n=0
  TOV.append(n)
for i in playerid:
  try:
    t=((Player(i)('2020-21').personal_fouls/Player(i)('2020-21').minutes_played)*36)
  except TypeError:
    t=0
  PF.append(t)
for i in playerid:
  try:
    o=(Player(i)('2020-21').minutes_played)
  except TypeError:
    o=0
  MP.append(o)
for i in playerid:
  try:
    p=(Player(i)('2020-21').games_played)
  except TypeError:
    p=0
  G.append(p)
for i in playerid:
  try:
    q=(Player(i)('2020-21').games_started)
  except TypeError:
    q=0
  GS.append(q)

d = {'Player Name': playername, #This creates a dataframe with each stat I pulled, so that this can be made into an excel file
     'Player ID': playerid, 
     'FGM': FGM, 
     'FGA': FGA, 
     '2PM': TPM,
     '2PA': TPA,
     '3PM': THRPM, 
     '3PA': THRPA, 
     'FTM': FTM, 
     'FTA': FTA, 
     'ORB': ORB, 
     'DRB': DRB,
     'AST': AST,
     'STL': STL,
     'BLK': BLK,
     'TOV': TOV,
     'PF': PF,
     'MP': MP,
     'GP': G,
     'GS': GS}
df= pd.DataFrame(data = d)
df.insert(20, 'Game Started %', round((df['GS']/df['GP'])*100),2)#this creates a calculated column to see the % of games started
Starter=[]
for i in df['Game Started %']:
  if i>=75:
   Starter.append('Yes')
  else:
    Starter.append('No')
df.insert(21,'Starter',Starter) #the for loop and this column sets up our output variable, a player is a starter if they started 75% or more of their games played
df1 = df.sort_values(by=['Player Name'], ascending=True) #for ease, the dataframe is sorted in alphabetical order
df2 = df1.style.set_caption('2021 NBA Player Stats Per 36 Minutes')

df2.to_excel('2020PlayerDataPer36Min.xlsx', index = False, header=True) #this converts the dataframe into an excel file, which actually gets stored in the colab notebook

from google.colab import files #sometimes colab loses the file, so this is to find the saved dataset I created and bring it back in
uploaded = files.upload()

dfl=pd.read_excel('2020PlayerDataPer36Min.xlsx', index_col=0) #this is to read the data in the excel file I created and put it back in a DataFrame
df1=dfl.drop(['FGM','FGA','Player ID', 'MP','GP','GS','Game Started %'], axis=1)#this is dropping unnecessary columns that wont be included in the logisitc regression
df1.head(10)

df2=pd.get_dummies(df1)  #this is to turn my Starter column into a dummy variable and it will end up being the output variable
df3=df2.drop(['Starter_No'], axis=1)
df4=df3.rename(columns={"Starter_Yes": "Starter"})
df4.head(10)