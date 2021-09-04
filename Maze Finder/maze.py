#!/usr/bin/python3

def fill_matrix(matrix, rows):
    '''
    generate the matrix that is inputted via standard input
    '''
    for i in range(0,rows):
        c = input()
        matrix.append(list(c))

def print_matrix(matrix):
    '''
    simply print the matrix
    '''
    for i,j in enumerate(matrix):
        for k, l in enumerate(j):
            if k == len(matrix[0])-1:
                print(matrix[i][k],end='')
                print('\n',end='')
            else:
                print(matrix[i][k],end='')

def find_start(matrix, rows):
    '''
    used for determining where Niobe is at in the maze,
    return starting row, col
    '''
    matrix = tuple(matrix)
    for i, j in enumerate(matrix):
        for k, l in enumerate(j):
            if l == 'N':
                x, y = i, k
    row = x
    col = y
    return row, col


def valid_move(matrix, row, col, direction):
    '''
    used for determining if the current move is valid,
    Note: checks AHEAD in direction if move is ok
          (not row col itself, but the next move)
    return True if move is valid False otherwise
    '''
    if direction == 'NORTH':
        row = row-1
        if matrix[row][col] == ' ':
            return True
        else:
            return False
    elif direction == 'SOUTH':
        row = row+1
        if matrix[row][col] == ' ':
            return True
        else:
            return False
    elif direction == 'EAST':
        col = col+1
        if matrix[row][col] == ' ':
            return True
        else:
            return False
    elif direction == 'WEST':
        col = col - 1
        if matrix[row][col]==' ':
            return True
        else:
            return False

def at_end(matrix, row, col):
    '''
    used for determining if Noibe is at the exit,
    return True if at the exit False otherwise
    '''
    if matrix[row+1][col] == 'E':
        return True
    elif matrix[row-1][col] == 'E':
        return True
    elif matrix[row][col+1]=='E':
        return True
    elif matrix[row][col-1] == 'E':
        return True
    else:
        return False


def find_exit(matrix, row, col):
    '''
    used for finding the exit,
    this will be the recursive function
    returns True or False
    use solvesudoku as the basis of your code here.
    '''
    tempRow = row
    tempCol = col
    UNASSIGNED = " "
    NEWS = ['NORTH','SOUTH','EAST','WEST']
    a = at_end(matrix,row,col)
    if a == True:
        return True
    for directions in NEWS:
        row = tempRow
        col = tempCol
        if valid_move(matrix,row,col,directions):
            if directions == 'NORTH':
                matrix[row-1][col] = '@'
                row = row-1
            elif directions == 'SOUTH':
                matrix[row+1][col]='@'
                row = row+1
            elif directions == 'EAST':
                matrix[row][col+1] = '@'
                col = col+1
            elif directions == 'WEST':
                matrix[row][col-1]='@'
                col = col-1                 
            if find_exit(matrix,row,col):
                return True
            
            matrix[row][col]= UNASSIGNED
    return False
def main():
    '''
    Write your main here
    '''
    import sys
    i = 0
    while True:
        rows = int(input())
        if rows == 0:
            break
        else:
            matrix = []
            fill_matrix(matrix, rows)
            randomInput = input()
            row,col = find_start(matrix,rows)
            if find_exit(matrix,row,col):
                print('Map', i ,'-- Solution found:')
                print_matrix(matrix)
                print()
            else:
                print('Map',i,'-- No solution found:')
                print_matrix(matrix)
                print()
        i = i+1
    
    sys.exit()
# Do NOT edit below this line:
if __name__ == '__main__':
    main()

