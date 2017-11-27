
from django.db import models

import importlib.machinery, os, math, random

path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')

machine_path = os.path.join(path, 'machine_model.py')
board_path = os.path.join(path, 'ttt_board.py')

mod_machine = importlib.machinery.SourceFileLoader('machine_player', machine_path)
mod_board = importlib.machinery.SourceFileLoader('ttt_board', board_path)

machine = mod_machine.load_module('machine_player')
board = mod_board.load_module('ttt_board')


# Create your models here.


def heads_or_tails():
    choices = ["heads", "tails"]
    coin = random.choice(choices)
    return coin

def whose_go(num, player_1, player_2, coin):

    if coin == "heads":
        if num % 2 != 0:
            player = player_1
            symbol = "X"
        else:
            player = player_2
            symbol = "0"
    else:
        if num % 2 != 0:
            player = player_2
            symbol = "X"
        else:
            player = player_1
            symbol = "0"

    num += 1

    return(num, player, symbol)

def pos_to_list(position):
    position = list(map(lambda a: int(a), position))

    return position

def check_board(position, game, player):
    while True:
        position = pos_to_list(position)

        if game.board[position[0]][position[1]] == ".":
            break
        else:
            position = input(str(player) + " enter another position: ").split(" ")
            position = pos_to_list(position)
    return(position)

def end_of_game(player, message, win, machine_player):
    print(str(player) + message)
    if machine_player != False:
        machine_player.machine_win()

    if input("Play again? Enter y for yes: ") == "y":
        main()


def win_lose_draw(player, num, board, symbol, machine_player=False):
    if board.win_check(symbol) == "win":
        message = " you've WON!!!"
        end_of_game(player, message, True, machine_player)
        game_over = True

    elif num == 10:
        message = " no one won :( it's a draw"
        end_of_game(player, message, False, machine_player)
        game_over = True

    else:
        game_over = False

    return(game_over)


def main():
    new_board = board.TicTacToe()
    new_board.print_board()
    player_1 = input("Player 1 please enter your name: ")
    machine_or_man = input("Would you like to play another human of play a machine?? H/M")
    if machine_or_man == "H":
        player_2 = input("Player 2 please enter your name: ")
        machine_player = False
    else:
        player_2 = "Machine"
        machine_player = machine.MachinePlayer()

    num = 1
    coin_toss = heads_or_tails()
    print(coin_toss)

    while True:
        num, player, symbol = whose_go(num, player_1, player_2, coin_toss)
        if player == "Machine":
            position = machine_player.choose_option(new_board.free_spaces)


        else:
            position = input(str(player) + " enter a position: ").split(" ")
            position = check_board(position, new_board, player)
        new_board.receive_input(position, symbol)
        new_board.print_board()

        print(num)

        game_over = win_lose_draw(player, num, new_board, symbol, machine_player)
        if game_over == False:
            continue
        elif game_over == True:
            break

    quit()
