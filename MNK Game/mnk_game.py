#!/usr/bin/env ipython3

# do NOT change the next two lines of code...
import sys
assert ('linux' in sys.platform), "This code should be run on Linux, just a reminder to follow instructions..."
import random

def drawBoard(board, numberOfRows, numberOfCols):
    print('  ',end='')
    for i in range(numberOfCols):
        if i == numberOfCols - 1:
            print(str(i),end='')
        else:
            print(str(i) + ' ',end='')

    print('\n',end='')

    for i,j in enumerate(board):
        print(str(i)+'|',end='')
        for k, l in enumerate(j):
            if k == len(board[0])-1:
                print(str(board[i][k])+'|',end='')
                print('\n',end='')
            else:
                print(str(board[i][k])+'|',end='')


def inputPlayerLetter():
    player = input("Do you want to be X or O?")
    if player == 'x':
        EmptyList = ['X','O']
    else:
        EmptyList = ['O','X']
    return EmptyList
    
    # Have test case - check_player_letter.py <input_player_letter.txt
    # Function inputPlayerLetter() lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.

    # the first element in the list is the player's letter, the second is the computer's letter.
    pass

def whoGoesFirst():
    # Function whoGoesFirst() randomly choose the player who goes first.
    random.seed(0)
    if random.randint(0, 1) == 0:
        return "computer"
    else:
        return "player"

def makeMove(board, letter, row, col):
    # Function makeMove(List, str, int) places player's letter or computer's letter at the specified
    # position i.e. move. Very simple function
    board[row][col] = letter
    pass


def checkAcross(board, letter, numberOfRows, numberOfCols, numberOfMatches, i, j):
    # Have test case - check_across_test.py
    # Function checkAcross(List, str, int, int, int, int, int) checks if player's letter is in all the
    # adjacent k (numberOfMatches) positions across the row from left to right.
    # Returns True if k-match pattern is found for player's letter across the row (corresponding to i,j)
    # Return False otherwise
    ActualString = numberOfMatches  * letter
    for i in range(numberOfRows):
        a = ''
        for m in board[i]:
            a = a + str(m)
            if ActualString in a:
                return True
    return False



def checkDown(board, letter, numberOfRows, numberOfCols, numberOfMatches, i, j):
    # Have test case - check_down_test.py
    # Function checkDown(List, str, int, int, int, int, int) checks if player's letter is in all
    # the k (numberOfMatches) positions down the column from top to bottom
    # Returns True if k-match pattern is found for player's letter down the column
    # returns False otherwise
    ActualString = numberOfMatches * letter
    for l in range(numberOfCols):
        a=''
        for i in range(numberOfRows):
            a = a +str(board[i][l])
        if ActualString in a:
           return True
    return False


def checkDiagonalRight(board, letter, numberOfRows, numberOfCols, numberOfMatches, i, j):
    # Have test case - check_diagonal_right_test.py
    # Function checkDiagonalRight(List, str, int, int, int, int, int) checks if player's letter is in
    # all the k (numberOfMatches) positions diagonally towards right
    # Returns True if k-match pattern is found for player's letter diagonally towards right
    # returns False otherwise
    
    while True:
        try:
            m=1
            while m  < numberOfMatches:
                if board[i+1][j+1] ==letter:
                    m= m +1
                    i = i + 1
                    j = j + 1
                else:
                    return False
                if m == numberOfMatches:
                    return True
        except IndexError:
            return False

def checkDiagonalLeft(board, letter, numberOfRows, numberOfCols, numberOfMatches, i, j):
    # Have test case - check_diagonal_left_test.py
    # Function checkDiagonalLeft(List, str, int, int, int, int, int) checks if player's letter is in
    # all the k (numberOfMatches) positions diagonally towards left
    # Returns True if k-match pattern is found for player's letter diagonally towards left
    # returns False otherwise
    while True:
        try:
            m=1
            while m  < numberOfMatches:
                if board[i+1][j-1] ==letter:
                    m= m +1
                    i = i + 1
                    j = j - 1
                else:
                    return False
                if m == numberOfMatches:
                    return True
        except IndexError:
            return False


def isWinner(board, letter, numberOfRows, numberOfCols, numberOfMatches):
    # Funtion isWinner(List, str, int, int, int) determines if the player has won or not, given a board,
    # a player's letter, number of rows in board,number of columns in board, and number of matches needed
    # for player's letter to win.

    # Returns True if k-matches for player's letter were found across the rows or down the columns or
    # diagonally towards right or diagonally towards left on the board
    for i in range(numberOfRows):
        for j in range(numberOfCols):
            if board[i][j] == letter:
                if checkAcross(board, letter, numberOfRows, numberOfCols, numberOfMatches, i, j):
                    return True
                if checkDown(board, letter, numberOfRows, numberOfCols, numberOfMatches, i, j):
                    return True
                if checkDiagonalRight(board, letter, numberOfRows, numberOfCols, numberOfMatches, i, j):
                    return True
                if checkDiagonalLeft(board, letter, numberOfRows, numberOfCols, numberOfMatches, i, j):
                    return True
    return False


def getBoardCopy(board):
    # Function getBoardCopy(List) makes a copy of the board list and returns it.
    boardCopy = [[board[i][j] for j in range(len(board[i])) ] for i in range(len(board))]
    return boardCopy


def isSpaceFree(board, row, col):
    # Have test case - space_free_test.py
    # Function isSpaceFree(List, int, int) returns True if the passed move is free on the passed board.
    # Very simple function
    if board[row][col] == ' ':
        return True
    else:
        return False


def getPlayerMove(board, numberOfRows, numberOfCols):
    # Function getPlayerMove(List, int, int) prompts for a valid player's move
    # Print "What is your next move? (0-rows, 0-cols)" where rows and cols are the size of your game.
    # See test for formatting
    # Take integer input with spaces, eg., 1 2
    while True:
        print("What is your next move? (0-",end='')
        print(str(numberOfRows-1),end='')
        print(", 0-" +str(numberOfCols-1)+')')
        row,col = input().split(' ')
        row = int(row)
        col = int(col)
        if 0<=row<=numberOfRows-1 and 0<=col<=numberOfCols-1:
            return row, col


def chooseRandomMoveFromList(board, movesList):
    # Function chooseRandomMoveFromList(List, List) randomly returns a computer move from the available moves
    random.seed(0)
    if len(movesList) != 0:
        move = random.choice(movesList)
        return move[0], move[1]
    else:
        return None


def getEmptySpaces(board, numberOfRows, numberOfCols):
    # Have test case - check_valid_random_moves.py
    # Function getEmptySpaces(List, int, int) returns a list of possible moves where the cell holds a space
    # Spaces should be in order of reading them out, e.g.,: [[0, 0], [1, 1], [1, 2]]
    ValidSpaces = []
    for i,j in enumerate(board):
        for k,l in enumerate(j):
            if l == ' ':
                a = [i,k]
                ValidSpaces.append(a)
    return ValidSpaces

def getComputerMove(board, computerLetter, numberOfRows, numberOfCols, numberOfMatches):
    # Function getComputerMove(List, str, int, int, int) determines computer's move, given a board,
    # the computer's letter, number of rows of the board, the number of columns of the board, and
    # number of matches.
    # Returns a computer's move.
    if computerLetter == "X":
        playerLetter = "O"
    else:
        playerLetter = "X"

    # Here is our algorithm for our m-n-k AI:
    # First, check if we can win in the next move
    Empty = getEmptySpaces(board,numberOfRows,numberOfCols)
    for position in Empty:
        boardCopy = getBoardCopy(board)
        a,b = position
        if isSpaceFree(boardCopy, a,b):
            makeMove(boardCopy, computerLetter,a,b)
            if isWinner(boardCopy, computerLetter,numberOfRows,numberOfCols,numberOfMatches):
                return a,b
    # Check if the player could win on next move, and block them.
    for position in Empty:
        boardCopy = getBoardCopy(board)
        a,b = position
        if isSpaceFree(boardCopy,a,b):
            makeMove(boardCopy, playerLetter, a,b)
            if isWinner(boardCopy, playerLetter,numberOfRows,numberOfCols,numberOfMatches):
                return a,b


    # Check for empty spaces on the board
    emptySpaces = getEmptySpaces(board, numberOfRows, numberOfCols)

    # Try to place a random move in the empty cell.
    return chooseRandomMoveFromList(board, emptySpaces)


def isBoardFull(board, numberOfRows, numberOfCols):
    for i,j in enumerate(board):
        for k,l in enumerate(j):
            if board[i][k] == ' ':
                return False
    return True
    # Have test case - board_full_test.py
    # Function isBoardFull(List, int, int) checks if every space on the board has been taken.
    # Returns True if the board is full, Otherwise returns False.


def main():
    print("Welcome to m-n-k game!")

    while True:
        m = int(input("Enter number of rows, m : "))
        n = int(input("Enter number of columns, n : "))
        k = 0
        print("k should be greater than 2 and should not be greater than m or n")
        while k <= 2 or k > m or k > n:
            k = int(input("Enter valid number of matches, k : "))
        # Reset the board
        theBoard = [[" "] * n for i in range(m)]
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        print("\nThe " + turn + " will go first.")
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == "player":
                # Player's turn.
                drawBoard(theBoard, m, n)
                row, col = getPlayerMove(theBoard, m, n)
                makeMove(theBoard, playerLetter,  row, col)
                
                if isWinner(theBoard, playerLetter, m, n, k):
                    drawBoard(theBoard, m, n)
                    print("Hooray! You have won the game!")
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard, m, n):
                        drawBoard(theBoard, m, n)
                        print("The game is a tie!")
                        break
                    else:
                        turn = "computer"
            else:
                # Computer's turn.
                row, col = getComputerMove(theBoard, computerLetter, m, n, k)
                makeMove(theBoard, computerLetter, row, col)

                if isWinner(theBoard, computerLetter, m, n, k):
                    drawBoard(theBoard, m, n)
                    print("The computer has beaten you! You lose.")
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard, m, n):
                        drawBoard(theBoard, m, n)
                        print("The game is a tie!")
                        break
                    else:
                        turn = "player"

        print("Do you want to play again? (y or n)")
        if not input().lower().startswith("y"):
            break

if __name__ == '__main__':
    main()

