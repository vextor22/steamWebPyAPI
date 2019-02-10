import sys
import requests
import SteamAPI
import random
import os

from secret_steam_key import *


random.seed(os.urandom(4))

steamConn = SteamAPI.SteamAPI(steam_key)
steamID = sys.argv[1]
try:
    int(steamID)    
except:
    steamID = steamConn.getPlayerID(steamID)


#get username
player = steamConn.getPlayerSummary(steamID)
print("Username: ", player.name)

#gather user's list of owned games into list of (id, playtime)
games = steamConn.getOwnedGames(steamID)['response']['games']


gameList = []
for game in games:
    gameList.append((game['appid'],game['playtime_forever']))
gameListSorted = sorted(gameList, key=lambda x: x[1])

#get list of all games and organize into map of id -> name
appJson = steamConn.getAppList()
apps = appJson['applist']['apps']
appDetails = {}
for app in apps:
    appDetails[app['appid']] = app['name']

for game in gameListSorted:
    print("Game Name: %s, playtime: % 6.2f" % (appDetails[game[0]],float(game[1])/60))

randomGame = random.choices(gameListSorted)[0]
print("Random Game Name: %s, playtime: % 6.2f" % (appDetails[randomGame[0]],float(randomGame[1])/60))
