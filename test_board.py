import board
import pytest

def test_create_board():
    board = board.board()
    assert(board.is_empty)

def test_get_board():
    board = board.board()
    empty_state = [[False for x in range(10)] for y in range(10)]
    assert(board.get() == empty_state)

def test_print_board():
    board = board.board(2,2)
    board.print()

def test_is_empty():
    board = board.board()
    assert(board.is_empty())
    board.set_cell(1,1, True)
    assert(not board.is_empty())

def test_cell():
    board = board.board()
    board.set_cell(0,0,True)
    assert(board.get_cell(0,0) == True)
    assert(board.get_cell(1,0) == False)