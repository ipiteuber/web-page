from django.conf import settings
import requests

def get_steam_game_players(appid):
    api_key = settings.STEAM_API_KEY
    url = f"http://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid={appid}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['response'].get('player_count', 0)
    return 0
