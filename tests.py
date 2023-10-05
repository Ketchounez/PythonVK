import unittest
from main import TicTacGame

class TestTicTacGame(unittest.TestCase):

    def setUp(self):
        self.game = TicTacGame()

    def test_validate_input(self):
        self.assertTrue(self.game.validate_input(0, 0))  # Правильный ход
        self.assertTrue(self.game.validate_input(1, 2))  # Правильный ход
        self.assertTrue(self.game.validate_input(2, 2))  # Правильный ход
        self.assertFalse(self.game.validate_input(-1, 0))  # Ошибка: отрицательная координата
        self.assertFalse(self.game.validate_input(0, 3))  # Ошибка: слишком большая координата
        self.assertTrue(self.game.validate_input(2, 2))  # Правильный ход (повторный ход)

    def test_check_winner(self):
        self.game.board = [['X', 'O', 'X'],
                           ['O', 'X', 'O'],
                           ['O', 'X', 'X']]
        self.assertTrue(self.game.check_winner())  # Победа для 'X'

        self.game.board = [['X', 'O', 'X'],
                           ['O', 'X', 'O'],
                           ['O', 'O', 'X']]
        self.assertTrue(self.game.check_winner())  # Победа для 'O'

        self.game.board = [['X', 'O', 'X'],
                           ['O', 'X', 'O'],
                           ['O', 'X', 'O']]
        self.assertFalse(self.game.check_winner())  # Ничья

        self.game.board = [['X', 'O', ' '],
                           ['O', 'X', 'O'],
                           ['O', 'X', 'O']]
        self.assertFalse(self.game.check_winner())  # Игра продолжается

if __name__ == '__main__':
    unittest.main()