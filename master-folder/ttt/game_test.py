import unittest
from lib.game import Game

class GameTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_a_new_game_is_started_the_player_must_enter_a_name(self):
        self.game = Game('Michelle')
        self.assertEqual(self.game.player_name, 'Michelle')
    

if __name__ == '__main__':
    unittest.main()
