from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from ttt.lib.game import Game
from ttt.lib.play import play

choices = {'choice_1': 1}

def index(request):
    return render(request, 'ttt/index.html')

def play_game(request):
    return render(request, 'ttt/play_game.html')

def new_game(request):
    global player_name, game
    if request.POST.get('player_name', ''):
        player_name = request.POST.get('player_name', '')
        game = Game(player_name)
        return render(request, 'ttt/new_game.html', {
        'new_player' : request.POST.get('player_name', '')})
    else:
        return render(request, 'ttt/new_game.html', {
        'new_player' : player_name,
        'choice' : request.POST.get('choice', ''),
        'choice_1_1' : 6}
        )
