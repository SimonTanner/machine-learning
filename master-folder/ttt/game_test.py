import unittest
from lib.game import Game
from lib.ttt_board import TicTacToe

class GameTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_a_new_game_is_started_the_player_must_enter_a_name(self):
        self.game = Game('Michelle')
        self.assertEqual(self.game.player_name, 'Michelle')

    def test_a_board_is_created_when_a_new_game_starts(self):
        self.game = Game('Michelle')
        board = self.game.board
        self.assertIsInstance(board, TicTacToe)


if __name__ == '__main__':
    unittest.main()
