package board

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestEmpty(t *testing.T) {
	board := CreateBoard(10, 10)
	fmt.Println(board)

	assert.Equal(t, IsEmpty(board), true, "Expecting board to be empty by default")
}
