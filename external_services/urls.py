from django.urls import path
from .views import steam_stats_view, calendly_embed

urlpatterns = [
    path('steam/', steam_stats_view, name='steam_stats'),
    path('calendly/', calendly_embed, name='calendly'),
]