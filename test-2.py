from tictactoe import result
from tictactoe import player
from tictactoe import winner
from tictactoe import terminal
from tictactoe import utility


X = "X"
O = "O"
EMPTY = None

board = [[X, X, O],
         [O, O, X],
         [X, O, X]]


# newBoard = result(board, (0, 1))
# print(board)
# print(newBoard)

# print(f"Ganador?: {winner(board)}")
# print(f"Terminal: {terminal(board)}")

print(utility(board))
print(float('-inf'))