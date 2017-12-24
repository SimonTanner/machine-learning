import unittest
from lib.game import Game
from lib.ttt_board import TicTacToe
from lib.machine_model import MachinePlayer

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

    def test_a_machine_player_instance_is_created_when_a_game_starts(self):
        self.game = Game('Helen')
        player_2 = self.game.machine_player
        self.assertIsInstance(player_2, MachinePlayer)

    def test_a_game_chooses_a_player_at_random_to_go_first(self):
        first_turns = []
        test_count = 10
        for i in range(test_count):
            self.game = Game('Helen')
            first_turns.append(self.game.whose_turn)
        self.assertLess(first_turns.count('Helen'), test_count)

    def test_a_player_can_choose_a_space(self):
        self.game = Game('Helen', 'X')
        self.game.whose_turn = 'Helen'
        self.game.choose_space('1')
        self.assertEqual(self.game.board.board['1'], 'X')

    def test_once_a_player_has_taken_thier_turn_the_other_player_goes_next(self):
        self.game = Game('Helen', 'X')
        previous_turn = self.game.whose_turn
        self.game.take_turn('4')
        current_turn = self.game.whose_turn
        self.assertNotEqual(previous_turn,current_turn)



if __name__ == '__main__':
    unittest.main()
