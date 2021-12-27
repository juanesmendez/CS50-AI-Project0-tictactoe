"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCounter = 0
    oCounter = 0

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == X:
                xCounter += 1
            elif board[i][j] == O:
                oCounter += 1

    if xCounter > oCounter:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set()

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == EMPTY:
                possibleActions.add((i, j))

    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Create new board, without modifying the original board received as input
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = player(board)
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    if(board[0][0] is not None and board[0][0] == board[0][1] and board[0][1] == board[0][2]):
        # print('1')
        return board[0][0]
    elif(board[1][0] is not None and board[1][0] == board[1][1] and board[1][1] == board[1][2]):
        # print('2')
        return board[1][0]
    elif(board[2][0] is not None and board[2][0] == board[2][1] and board[2][1] == board[2][2]):
        # print('3')
        return board[2][0]
    elif(board[0][0] is not None and board[0][0] == board[1][0] and board[1][0] == board[2][0]):
        # print('4')
        return board[0][0]
    elif(board[0][1] is not None and board[0][1] == board[1][1] and board[1][1] == board[2][1]):
        # print('5', 'Board ', board[0][2])
        return board[0][1]
    elif(board[0][2] is not None and board[0][2] == board[1][2] and board[1][2] == board[2][2]):
        # print("6")
        return board[0][2]
    elif(board[0][0] is not None and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        # print('7')
        return board[0][0]
    elif(board[0][2] is not None and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        # print('8')
        return board[0][2]    
    else:
        # print('9')
        return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None):
        return True
    else:
        return False
    #return True if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None) else False # noqa E501


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0
    # Check how to handle exception when a non terminal board is received.


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = min_value(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move

    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = max_value(result(board, action))
        if aux < v:
            v = aux
            move = action
            if v == -1:
                return v, move

    return v, move
    