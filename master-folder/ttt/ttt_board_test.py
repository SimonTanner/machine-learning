import unittest
from lib.ttt_board import TicTacToe

class TTTTest(unittest.TestCase):

    def setUp(self):
        self.ttt = TicTacToe()
        pass

    def test_TTT_contains_a_dict_with_keys_1_to_9(self):

        ttt_test_board = {}
        for i in range(1, 10):
            ttt_test_board[str(i)] = ' '

        self.assertEqual(self.ttt.board, ttt_test_board)

    def test_TTT_allows_player_to_choose_a_space(self):
        self.ttt.choose_space('6', 'X')
        self.assertLessEqual({'6':'X'}.items(), self.ttt.board.items())

    def test_TTT_cannot_enter_the_same_space_more_than_once(self):
        self.ttt.choose_space('6', 'X')
        self.assertEqual(self.ttt.choose_space('6', 'X'), True)

    def test_when_a_player_chooses_a_space_it_is_dropped_from_free_spaces(self):
        self.ttt.choose_space('6', 'X')
        self.assertNotIn(6, self.ttt.free_spaces)


if __name__ == '__main__':
    unittest.main()
