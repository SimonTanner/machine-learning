from lib.ttt_board import TicTacToe
from lib.machine_model import MachinePlayer
import random

class Game():

    def __init__(self, player_name, x_or_o='X'):
        chars = {'X':'0', '0':'X'}
        self.player_name = player_name
        machine_player_char = chars[x_or_o]
        self.board = TicTacToe()
        self.machine_player = MachinePlayer()
        self.players = {player_name : x_or_o, 'machine_player' : machine_player_char}
        self.player_switch = {player_name : 'machine_player', 'machine_player' : player_name}
        self.who_goes_first()

    def who_goes_first(self):
        self.whose_turn = random.choice(list(self.players.keys()))

    def choose_space(self, choice):
        return self.board.choose_space(str(choice), self.players[self.whose_turn])

    def take_turn(self, choice):
        if self.choose_space(choice):
            msg = 'Sorry that space is already taken'
        else:
            self.whose_turn = self.player_switch[self.whose_turn]
            msg = None
        return msg
