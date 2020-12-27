import math


def solveSudoku():
    empty = findEmpty()
    row = empty[0]
    cell = empty[1]
    possible_number = [*range(1, 10)]
    validSudoku()


# Finding 0 in the grid
def findEmpty():
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return [i, j]


def validSudoku(nr,row,cell):


    for i in range(len(board[row])):

        if board[row].__contains__(nr):  # or board[1][0]==(i+1)  :
            return False
        # possible_number.remove(i+1)
        elif board[i][cell] == (nr):
            return False

    # print(squareY)
    # print("niedziala")
    squareX = math.floor(row / 3)
    squareY = math.floor(cell / 3)
    for j in range(3):
        for z in range(3):
            print(board[j + 3 * squareX][z + 3 * squareY])
            if board[j + 3 * squareX][z + 3 * squareY] == nr:
                return False

    return True


# Test board
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

copyBoard = board


def print_SudokuBoard():
    topOfSquare = "═══╤═══╤═══╦"
    middleOfSquare = " 0 │"

    print("╚═══╧═══╩═══╝")
    topOfSquare = "╔" + topOfSquare * 2 + topOfSquare.replace("╦", "╗", 1)

    middleOfSquare = "║" + middleOfSquare

    print(topOfSquare)
    # Creating board
    for i in range(len(board)):
        print("║", end="")
        for j in range(len(board[i])):
            if j % 3 == 2:
                formating = " ║"
            else:
                formating = " │"
            print("{}{}{}".format(" ", board[i][j], formating), end="")

        print("")
        if i % 3 == 2:
            print("╠" + "═══╪═══╪═══╬" * 2 + "═══╪═══╪═══╣")
        else:
            print("╟" + "───┼───┼───╫" * 2 + "───┼───┼───╢")

        # if i % 3 == 2 and i != 0:


if __name__ == '__main__':
    print_SudokuBoard()
    solveSudoku()
