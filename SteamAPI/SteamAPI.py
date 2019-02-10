import requests

class SteamAPI(object):

    class PlayerSummary(object):
        def __init__(self, playerSummary):
            self.json = playerSummary.json()
            #extract player name from summary json
            for result in self.json:
                for player in self.json[result]['players']:
                    self.name = player['personaname']
    def __init__(self, key):
        self.steam_key = key

    def getPlayerID(self, steamID):
        query ='http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=%s&vanityurl=%s'
        response = requests.get(query % (self.steam_key, steamID))
        print(response)
        rJson = response.json()['response']
        if rJson['success'] == 1:
            print(rJson['steamid'])
            return rJson['steamid']
        return None
    def getPlayerSummary(self, steamID):
        query ='http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=%s&steamids=%s'
        response = requests.get(query % (self.steam_key, steamID))
        playerObject = SteamAPI.PlayerSummary(response)
        return playerObject
    def getOwnedGames(self, steamID):
        query = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=%s&steamid=%s&format=json'
        resp = requests.get(query % (self.steam_key, steamID))
        return resp.json()
    def getAppList(self):
        query = 'http://api.steampowered.com/ISteamApps/GetAppList/v0002/'
        return requests.get(query).json()
