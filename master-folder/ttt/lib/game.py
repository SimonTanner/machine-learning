from lib.ttt_board import TicTacToe

class Game():

    def __init__(self, player_name):
        self.player_name = player_name
        self.board = TicTacToe()
