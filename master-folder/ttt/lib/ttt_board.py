

class TicTacToe():

    def __init__(self):
        self.board = {}
        self.create_board()


    def create_board(self):
        for i in range(1, 10):
            self.board[str(i)] = ' '
