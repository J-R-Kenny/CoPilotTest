import unittest
from tictactoe import calcWinState

class TestCalcWinState(unittest.TestCase):
    def test_calcWinState_row(self):
        board = [['X', 'X', 'X'],
                 ['O', 'O', ' '],
                 [' ', ' ', ' ']]
        self.assertEqual(calcWinState(board), 'X wins')

    def test_calcWinState_column(self):
        board = [['O', 'X', ' '],
                 ['O', 'X', ' '],
                 ['O', ' ', ' ']]
        self.assertEqual(calcWinState(board), 'O wins')

    def test_calcWinState_diagonal(self):
        board = [['X', 'O', ' '],
                 ['O', 'X', ' '],
                 [' ', ' ', 'X']]
        self.assertEqual(calcWinState(board), 'X wins')

    def test_calcWinState_draw(self):
        board = [['X', 'O', 'X'],
                 ['O', 'X', 'O'],
                 ['O', 'X', 'O']]
        self.assertEqual(calcWinState(board), 'Draw')

    def test_calcWinState_game_not_finished(self):
        board = [['X', 'O', ' '],
                 ['O', ' ', 'X'],
                 [' ', ' ', ' ']]
        self.assertEqual(calcWinState(board), 'Game not finished')

    def test_calcWinState_fail(self):
        board = [['X', 'O', 'X'],
                 ['O', 'X', 'O'],
                 ['O', 'O', 'O']]
        self.assertEqual(calcWinState(board), 'X wins') # This will fail because 'O' is the actual winner

if __name__ == '__main__':
    unittest.main()
