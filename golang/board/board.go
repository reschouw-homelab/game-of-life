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
	for x := 0; x < len(board); x++ {
		for y := 0; y < len(board[x]); y++ {
			if board[x][y] {
				return false
			}
		}
	}
	return true
}

func SetCell(board Board, x int, y int, state bool) Board {
	board[x][y] = state
	return board
}

func GetCell(board Board, x int, y int) bool {
	return board[x][y]
}
