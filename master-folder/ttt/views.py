from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return render(request, 'ttt/index.html')

def play_game(request):
    return render(request, 'ttt/play_game.html')

def new_game(request):
    return render(request, 'ttt/new_game.html', {
        'new_player' : request.POST.get('player_name', '')})
