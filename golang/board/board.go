package board

type Board [][]bool

func CreateBoard(width int, height int) Board {
	board := make([][]bool, width)
	for x := 0; x < width; x++ {
		board[x] = make([]bool, height)
	}
	return board
}

func IsEmpty(board Board) bool {
	return true
}
