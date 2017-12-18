import unittest
from lib.ttt_board import TicTacToe

class TTTTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_TTT_contains_a_dict_with_keys_1_to_9(self):
        ttt = TicTacToe()
        ttt_test_board = {}
        for i in range(1, 10):
            ttt_test_board[str(i)] = ' '

        self.assertEqual(ttt.board, ttt_test_board)


if __name__ == '__main__':
    unittest.main()
