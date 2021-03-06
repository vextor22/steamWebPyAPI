## Steam webAPI

The Steam webAPI is a reasonably documented API offered to Steam account holders. It provides user data including: owned games, play-time statistics and friends.

The goal of this Python package is to provide a thin layer of abstraction for interacting with this API from a Python application.

---

## To Install:

Installing the package is straighforward, the package installs Requests as a dependency:

`pip install https://github.com/vextor22/steamWebPyAPI/tarball/master`

And to uninstall:

`pip uninstall SteamAPI`

---

## Usage:

Unfortunately I have some difficult wrapping my head around packages apparently, and the import is a little cumbersome.

An example (Steam API key must be protected, do not include it inline with code that will be in a public repo):

```python
import sys
import SteamAPI

//steam key from protected location
from secret_steam_key import *

steamID = sys.argv[1]

//Initialize connecter object
steamConn = SteamAPI.SteamAPI(steam_key)

#get username
player = steamConn.getPlayerSummary(steamID)
print("Username: ", player.name)
```
