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
