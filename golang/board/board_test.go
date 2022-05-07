package board

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestEmpty(t *testing.T) {
	board := CreateBoard(10, 10)
	assert.Equal(t, IsEmpty(board), true, "Expecting board to be empty by default")
	board = SetCell(board, 5, 5, true)
	assert.Equal(t, IsEmpty(board), false, "Expecting board to not be empty")
}

func TestGetSet(t *testing.T) {
	board := CreateBoard(10, 10)
	board = SetCell(board, 5, 5, true)
	board = SetCell(board, 0, 0, true)
	board = SetCell(board, 9, 9, true)
	assert.Equal(t, GetCell(board, 3, 3), false, "Expecting 3,3 to be empty")
	assert.Equal(t, GetCell(board, 0, 0), true, "Expecting 0,0 to be alive")
	assert.Equal(t, GetCell(board, 9, 9), true, "Expecting 9,9 to be alive")
}

func TestNumNeighbors(t *testing.T) {
	board := CreateBoard(10, 10)
	board = SetCell(board, 5, 5, true)
	assert.Equal(t, GetNumNeighbors(board, 5, 5), 0, "Cell is expected to be by itself")
	board = SetCell(board, 5, 6, true)
	board = SetCell(board, 6, 6, true)
	assert.Equal(t, GetNumNeighbors(board, 5, 5), 2, "Cell is expected to have two neighbors")
}

func TestNumNeighborsEdges(t *testing.T) {
	board := CreateBoard(10, 10)
	board = SetCell(board, 0, 0, true)
	assert.Equal(t, GetNumNeighbors(board, 0, 0), 0, "Cell is expected to be by itself")
	board = SetCell(board, 1, 1, true)
	board = SetCell(board, 1, 0, true)
	assert.Equal(t, GetNumNeighbors(board, 0, 0), 2, "Cell is expected to have two neighbors")
	board = SetCell(board, 9, 9, true)
	board = SetCell(board, 9, 8, true)
	board = SetCell(board, 8, 9, true)
	board = SetCell(board, 8, 8, true)
	assert.Equal(t, GetNumNeighbors(board, 9, 9), 3, "Cell is expected to have three neighbors")
}

func TestCellStarves(t *testing.T) {
	board := CreateBoard(10, 10)
	board = SetCell(board, 5, 5, true)
	board = Iterate(board)
	assert.Equal(t, GetCell(board, 5, 5), false, "Cell is expected to starve")
	board = SetCell(board, 5, 5, true)
	board = SetCell(board, 5, 6, true)
	board = Iterate(board)
	assert.Equal(t, GetCell(board, 5, 5), false, "Cell is expected to starve")
}

func TestCellNoChange(t *testing.T) {
	board := CreateBoard(10, 10)
	board = SetCell(board, 5, 5, true)
	board = SetCell(board, 6, 5, true)
	board = SetCell(board, 5, 6, true)
	board = Iterate(board)
	assert.Equal(t, GetCell(board, 5, 5), true, "Cell is expected to stay alive")
	board = CreateBoard(10, 10)
	board = SetCell(board, 6, 5, true)
	board = SetCell(board, 5, 6, true)
	board = Iterate(board)
	assert.Equal(t, GetCell(board, 5, 5), false, "Cell is expected to stay dead")
}

func TestCellComesAlive(t *testing.T) {
	board := CreateBoard(10, 10)
	board = SetCell(board, 5, 6, true)
	board = SetCell(board, 6, 5, true)
	board = SetCell(board, 4, 4, true)
	board = Iterate(board)
	assert.Equal(t, GetCell(board, 5, 5), true, "Cell is expected to come alive")
}

func TestCellIsOvercrowded(t *testing.T) {
	board := CreateBoard(10, 10)
	board = SetCell(board, 5, 5, true)
	board = SetCell(board, 4, 5, true)
	board = SetCell(board, 5, 4, true)
	board = SetCell(board, 4, 4, true)
	board = SetCell(board, 5, 6, true)
	board = Iterate(board)
	assert.Equal(t, GetCell(board, 5, 5), false, "Cell is expected to starve")
}
