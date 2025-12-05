import pytest
import pygame
from tictactoe.TicTacToe import TicTacToe
#from tictactoe.main import run

@pytest.fixture
def board():
    return TicTacToe()


class TestTicTacToe:

    def test_init(self, board):
        assert board.player == 1
        assert board.board == [["__" for _ in range(3)] for _ in range(3)]
        assert isinstance(board.win, pygame.surface.Surface)
    