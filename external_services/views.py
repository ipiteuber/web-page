from django.shortcuts import render
from .steam import get_steam_game_players
from django.contrib.auth.decorators import login_required

# Create your views here.

def steam_stats_view(request):
    games = {
        "CS2": get_steam_game_players(730), 
        "Marvel Rivals": get_steam_game_players(2767030),
        "Overwatch": get_steam_game_players(2357570),
    }
    return render(request, 'external_services/steam_stats.html', {'games': games})

@login_required
def calendly_embed(request):
    return render(request, "external_services/calendly_embed.html")