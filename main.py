# SUDOKU SOLVER CARLOS AND MICHAL
import math
import random
import time
import subprocess, platform
import colorama
#count how many times validation was called
counter=[0]
def countBack(relase):
    counter[0]+=1
    if (relase):
        print("Number of backtracking tries:",counter[0])
        return counter[0]
    return
def solveSudoku(currentBoard,stepByStep):
    empty = findEmpty(currentBoard)
    if not empty:
        return True
    else:
        row = empty[0]
        cell = empty[1]
    possible_number = [*range(1, 10)]
    validSudoku(possible_number, row, cell, currentBoard)
    for i in range(1, 10):

        if validSudoku(i, row, cell, currentBoard):
            countBack(stepByStep)
            if (stepByStep):
                print_SudokuBoard(currentBoard)
                time.sleep(1.0)
                if platform.system() == "Windows":
                    subprocess.Popen("cls",
                                     shell=True).communicate()
                else:
                    print("\033c", end="")
                print("")

            currentBoard[row][cell] = i
            print("Current NR",i)
            if solveSudoku(currentBoard,stepByStep):
                return True
            currentBoard[row][cell] = 0
    return False


# Finding 0 in the grid
def findEmpty(currentBoard):
    for i in range(len(currentBoard)):
        for j in range(len(currentBoard[i])):
            if currentBoard[i][j] == 0:
                return [i, j]
    return None


def validSudoku(nr, row, cell, currentboard):
    for i in range(len(currentboard[row])):
        if currentboard[row].__contains__(nr):
            return False
        elif currentboard[i][cell] == (nr):
            return False
        elif  currentboard[row][cell] !=0:
            return False
    squareX = math.floor(row / 3)
    squareY = math.floor(cell / 3)
    for j in range(3):
        for z in range(3):

            if currentboard[j + 3 * squareX][z + 3 * squareY] == nr:
                return False
    return True

#Function which print grid
def print_SudokuBoard(currentboard):
    topOfSquare = "═══╤═══╤═══╦"
    topOfSquare = "╔" + topOfSquare * 2 + topOfSquare.replace("╦", "╗", 1)
    print(topOfSquare)
    # Creating board
    for i in range(len(currentboard)):
        print("║", end="")
        for j in range(len(currentboard[i])):
            if j % 3 == 2:
                formatting = " ║"
            else:
                formatting = " │"
            print("{}{}{}".format(" ", currentboard[i][j], formatting), end="")

        print("")
        if i == 2 or i==5:
            print("╠" + "═══╪═══╪═══╬" * 2 + "═══╪═══╪═══╣")
        elif i == 8:
            print("╚═"+"══╧═══╧═══╩═"* 2 +"══╧═══╩═══╝")
        else:
            print("╟" + "───┼───┼───╫" * 2 + "───┼───┼───╢")


def generateBoard():
    board0 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    boardCopy=board0
    #board0=randomRow(board0)
    board0[0][0]=random.randint(1, 9)
    for x in range(8):
        while True:

            randomNrRow = random.randint(1, 9)
            randomNrCol=random.randint(1, 9)
            if(x<3):
                if(randomNrRow==randomNrCol):
                    randomNrRow = random.randint(1, 9)
                    randomNrCol = random.randint(1, 9)
                    if (randomNrRow == randomNrCol):
                        randomNrRow = random.randint(1, 9)
                        randomNrCol = random.randint(1, 9)


            if (validSudoku(randomNrRow, 0, x+1, board0) and validSudoku(randomNrCol, x+1, 0, board0) ):
                board0[0][x+1] = randomNrRow
                board0[x+1][0] = randomNrCol
                break
    solveSudoku(board0,False)
    for x in range(64):

        randomNrRow = random.randint(0, 8)
        randomNrCol = random.randint(0, 8)
        if board0[randomNrRow][randomNrCol] != 0:
            board0[randomNrRow][randomNrCol]=0
        elif board0[randomNrRow][randomNrCol] == 0:
            randomNrRow = random.randint(0, 8)
            randomNrCol = random.randint(0, 8)
            board0[randomNrRow][randomNrCol] = 0
    #print_SudokuBoard(board0)
    return board0

def a():
    return 1+1
if __name__ == '__main__':
    print("Welcome To Sudoku Solver by Carlos and Michal")
    print("""We are happy to show you our sudoku solver
    """)
    colorama.init(autoreset=True)

    gridNr = input("Press any character and then enter to continue ")
    if (gridNr):

        board = generateBoard()
        boardCopy=board
        counter[0]=0
        howToSolveIt = input("""How would you like to solve it?""""""
(1) Qucik solving
(2) Step by step(Please use a terminal to make this function work properly. Do NOT use IDE terminal) 
        """)
        if howToSolveIt == "1":
            print("Generated Board:")
            print_SudokuBoard(board)
            solveSudoku(board,False)
            print("Solved Board:")
            print_SudokuBoard(board)
            countBack(True)

        elif howToSolveIt=="2":
            solveSudoku(board, True)
            print("Generated Board:")
            print_SudokuBoard(boardCopy)
            print("Solved Board:")
            print_SudokuBoard(board)
            countBack(True)
        exitProgram = input("Press anything to leave the program:")