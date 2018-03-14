import sys
import requests
import SteamAPI

steamID = sys.argv[1]


steamConn = SteamAPI.SteamAPI()

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
resp = requests.get('http://api.steampowered.com/ISteamApps/GetAppList/v0002/')
apps = resp.json()['applist']['apps']
appDetails = {}
for app in apps:
    appDetails[app['appid']] = app['name']

for game in gameListSorted:
    print("Game Name: %s, playtime: %s" % (appDetails[game[0]],float(game[1])/60))
