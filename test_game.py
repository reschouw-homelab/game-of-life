import game
import pytest

def test_create_board():
    board = game.Board()
    assert(board.is_empty)

def test_get_board():
    board = game.Board()
    empty_state = [[False for x in range(10)] for y in range(10)]
    assert(board.get() == empty_state)

def test_print_board():
    board = game.Board(2,2)
    board.print()

