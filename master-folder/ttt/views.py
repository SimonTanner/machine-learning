from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from ttt.lib.game import Game

import importlib.machinery, os, time, json

'''path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')

game_path = os.path.join(path, 'game.py')
play_path = os.path.join(path, 'play.py')

mod_game = importlib.machinery.SourceFileLoader('new_game', game_path)
mod_play = importlib.machinery.SourceFileLoader('play', play_path)

new_game = mod_game.load_module('new_game')
play = mod_play.load_module('play')'''

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
        message = 'Play'
        if game.whose_turn == game.machine_player:
            game.take_turn()

        return render(request, 'ttt/new_game.html', {
        'new_player' : player_name,
        'current_player' : game.whose_turn,
        'choice_1' : game.board.board['1'],
        'choice_2' : game.board.board['2'],
        'choice_3' : game.board.board['3'],
        'choice_4' : game.board.board['4'],
        'choice_5' : game.board.board['5'],
        'choice_6' : game.board.board['6'],
        'choice_7' : game.board.board['7'],
        'choice_8' : game.board.board['8'],
        'choice_9' : game.board.board['9'],
        'message' : message})
    else:
        if game.whose_turn == game.player_name:
            choice = request.POST.get('choice', '')
            time.sleep(2)
            message = game.take_turn(int(choice))
            return render(request, 'ttt/new_game.html', {
            'new_player' : player_name,
            'current_player' : game.whose_turn,
            'choice_1' : game.board.board['1'],
            'choice_2' : game.board.board['2'],
            'choice_3' : game.board.board['3'],
            'choice_4' : game.board.board['4'],
            'choice_5' : game.board.board['5'],
            'choice_6' : game.board.board['6'],
            'choice_7' : game.board.board['7'],
            'choice_8' : game.board.board['8'],
            'choice_9' : game.board.board['9'],
            'message' : message}
            )
        else:
            message = game.take_turn()
            time.sleep(2)
            return render(request, 'ttt/new_game.html', {
            'new_player' : player_name,
            'current_player' : game.whose_turn,
            'choice_1' : game.board.board['1'],
            'choice_2' : game.board.board['2'],
            'choice_3' : game.board.board['3'],
            'choice_4' : game.board.board['4'],
            'choice_5' : game.board.board['5'],
            'choice_6' : game.board.board['6'],
            'choice_7' : game.board.board['7'],
            'choice_8' : game.board.board['8'],
            'choice_9' : game.board.board['9'],
            'message' : message}
            )
