

class TicTacToe():

    def __init__(self):
        self.board = {}
        self.free_spaces = []
        self.create_board()


    def create_board(self):
        for i in range(1, 10):
            self.board[str(i)] = ' '
            self.free_spaces.append(i)

    def choose_space(self, space, character):
        space_taken = False
        if self.board[space] == ' ':
            self.board[space] = character
            self.free_spaces.remove(int(space))
        else:
            space_taken = True

        return space_taken
