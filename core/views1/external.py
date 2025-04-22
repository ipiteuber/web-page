import requests
from django.shortcuts import render

def random_advice(request):
    r = requests.get('https://api.adviceslip.com/advice')
    slip = r.json().get('slip', {})
    return render(request, 'external/advice.html', {'advice': slip.get('advice')})
