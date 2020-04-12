# def reassign(list):
#   #otherList = list # Copy list by reference
#   otherList = list[:] # Copy list by value
#   otherList = [10, 70]
#   return otherList
#   #list.append(6)

# def append(list):
#   list.append(1)


# list = [0]
# newList = reassign(list)

# print(list)
# print(newList)

# listA = [0]
# listB = listA
# listB.append(1)
# listA = [2, 4]
# print(listA)
# print(listB)
import copy

def result(board):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Create a new board, without modifying the original board received as input
    board[0][0] = 6
    result = copy.deepcopy(board)

    result[1][1] = 1

    return result




boardStart = [[0, 0, 0],
				[0, 0, 0],
				[0, 0, 0]]


newBoard = result(boardStart)
print(boardStart)
print(newBoard)