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

func GetNumNeighbors(board Board, cellX int, cellY int) int {
	numNeighbors := 0
	for neighX := cellX - 1; neighX <= cellX+1; neighX++ {
		for neighY := cellY - 1; neighY <= cellY+1; neighY++ {
			switch {
			case (neighX < 0) || (neighX > len(board)-1):
				continue
			case (neighY < 0) || (neighY > len(board[neighX])-1):
				continue
			case (neighX == cellX) && (neighY == cellY):
				continue
			case board[neighX][neighY]:
				numNeighbors++
			}
		}
	}
	return numNeighbors
}

func Iterate(board Board) Board {
	nextBoard := make([][]bool, len(board))
	for x := 0; x < len(board); x++ {
		nextBoard[x] = make([]bool, len(board[x]))
	}
	for x := 0; x < len(board); x++ {
		for y := 0; y < len(board[x]); y++ {
			switch numNeighbors := GetNumNeighbors(board, x, y); {
			case numNeighbors < 2:
				nextBoard[x][y] = false
			case numNeighbors == 2:
				nextBoard[x][y] = board[x][y]
			case numNeighbors == 3:
				nextBoard[x][y] = true
			case numNeighbors > 3:
				nextBoard[x][y] = false
			}
		}
	}
	return nextBoard
}
