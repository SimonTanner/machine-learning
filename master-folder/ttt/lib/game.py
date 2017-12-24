from lib.ttt_board import TicTacToe
from lib.machine_model import MachinePlayer

class Game():

    def __init__(self, player_name):
        self.player_name = player_name
        self.board = TicTacToe()
        self.machine_player = MachinePlayer()
