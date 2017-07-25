from django.db import models

# Create your models here.


class TicTacToe():

    def __init__(self):

        self.board = []
        self.create_board()
        self.free_spaces = []

    def create_board(self):
        board = self.board
        for row in range(3):
            board.append([])
            for column in range(3):
                board[row].append('.')

    def print_board(self):
        for row in self.board:
            print(" ".join(row))

    def input_marker(row, column, input_type):
        self.board[row][column] = input_type
        self.print_board(board)

    def win_check_row(self, letter):
        for r in self.board:
          if r[0] == r[1] == r[2] == letter:
            return('win')


    def win_check_column(self, letter):
        board = self.board
        for c in range(0, len(board[0])):
          if board[0][c] == board[1][c] == board[2][c] == letter:
            return('win')


    def win_check_diag(self, letter):
        board = self.board
        if board[0][0] == board[1][1] == board[2][2] == letter:
            return("win")
        elif board[0][2] == board[1][1] == board[2][0] == letter:
            return("win")
        else:
            return False

    def win_check(self, letter):
        if self.win_check_row(letter) == "win" or self.win_check_column(letter) == "win" or self.win_check_diag(letter) =="win":
            return "win"

    def receive_input(self, position, letter):
        r, c = position
        self.board[r][c] = letter
        self.free_board_space()
        print(self.free_spaces)

    def free_board_space(self):
        self.free_spaces = []
        for row in range(0, len(self.board)):
            for column in range(0, len(self.board)):
                if self.board[row][column] != '.':
                    free_int = row * 3 + column + 1
                    self.free_spaces.append(free_int)



def main():
    new_board = TicTacToe()
    new_board.print_board()
    while True:

        position = input("Enter a position: ").split(" ")
        position = list(map(lambda a: int(a), position))
        new_board.receive_input(position, "X")
        new_board.print_board()
        if new_board.win_check("X") == "win":
            print("You've won!!!")
            if input("Play again? Enter y for yes: ") == "y":
                main()
            else:
                break

    quit()


main()
