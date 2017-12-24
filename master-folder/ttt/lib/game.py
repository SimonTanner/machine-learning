from lib.ttt_board import TicTacToe
from lib.machine_model import MachinePlayer
import random

class Game():

    def __init__(self, player_name):
        self.player_name = player_name
        self.board = TicTacToe()
        self.machine_player = MachinePlayer()
        self.players = [player_name, 'machine_player']
        self.who_goes_first()

    def who_goes_first(self):
        self.whose_turn = random.choice(self.players)
