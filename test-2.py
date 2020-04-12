from tictactoe import result
from tictactoe import player
from tictactoe import winner


X = "X"
O = "O"
EMPTY = None

board = [[X, X, X],
         [O, O, EMPTY],
         [X, EMPTY, X]]


# newBoard = result(board, (0, 1))
# print(board)
# print(newBoard)

print(winner(board))