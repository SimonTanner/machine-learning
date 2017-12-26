

class TicTacToe():

    def __init__(self):
        self.board = {}
        self.free_spaces = []
        self.win = False
        self.create_board()


    def create_board(self):
        for i in range(1, 10):
            self.board[str(i)] = ' '
            self.free_spaces.append(i)

    def check_board(self):
        board = self.board
        for i in range(1, 9, 3):
            j = int((i + 2) / 3)
            if board[str(i)] == board[str(i + 1)] == board[str(i + 2)] != ' ':
                self.win = True
            elif board[str(j)] == board[str(j + 3)] == board[str(j + 6)] != ' ':
                self.win = True

    def choose_space(self, space, character):
        space_taken = False
        if self.board[space] == ' ':
            self.board[space] = character
            self.free_spaces.remove(int(space))
            self.check_board()
        else:
            space_taken = True

        return space_taken
