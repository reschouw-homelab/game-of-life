import board as _board
import pytest

def test_create_board():
    board = _board.board()
    assert(board.is_empty)

def test_get_board():
    board = _board.board()
    empty_state = [[False for x in range(10)] for y in range(10)]
    assert(board.get() == empty_state)

def test_print_board():
    board = _board.board(2,2)
    board.print()

def test_is_empty():
    board = _board.board()
    assert(board.is_empty())
    board.set_cell(1,1, True)
    assert(not board.is_empty())

def test_cell():
    board = _board.board()
    board.set_cell(0,0,True)
    assert(board.get_cell(0,0) == True)
    assert(board.get_cell(1,0) == False)

def test_get_neighbors():
    board = _board.board()
    assert(board.get_num_neighbors(5,5) == 0)
    board.set_cell(5,6,True)
    board.set_cell(6,5,True)
    assert(board.get_num_neighbors(5,5) == 2)

def test_get_neighbors_edge_min():
    board = _board.board()
    assert(board.get_num_neighbors(0,0) == 0)
    board.set_cell(0,0,True)
    board.set_cell(0,1,True)
    board.set_cell(1,0,True)
    board.set_cell(1,1,True)
    assert(board.get_num_neighbors(0,0) == 3)

def test_get_neighbors_edge_max():
    board = _board.board()
    assert(board.get_num_neighbors(9,9) == 0)
    board.set_cell(9,9,True)
    board.set_cell(8,9,True)
    board.set_cell(9,8,True)
    board.set_cell(8,8,True)
    assert(board.get_num_neighbors(9,9) == 3)

def test_iterate_cell_dies():
    board = _board.board()
    board.set_cell(5,5, True)
    board.set_cell(5,6,True)
    board.iterate()
    assert(not board.get_cell(5,5))
    assert(not board.get_cell(5,6))

def test_iterate_cell_stays():
    board = _board.board()
    board.set_cell(5,5, True)
    board.set_cell(5,6,True)
    board.iterate()
    assert(not board.get_cell(5,5))
    assert(not board.get_cell(5,6))

def test_cell_comes_alive():
    board = _board.board()
    board.set_cell(5,6,True)
    board.set_cell(6,5,True)
    board.set_cell(6,6,True)
    board.iterate()
    assert(board.get_cell(5,5))

def test_cell_gets_overcrowded():
    board = _board.board()
    board.set_cell(5,6,True)
    board.set_cell(6,5,True)
    board.set_cell(6,6,True)
    board.set_cell(4,6,True)
    board.iterate()
    assert(not board.get_cell(5,5))