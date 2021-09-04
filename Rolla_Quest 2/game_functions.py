#!/usr/bin/python3
# -*- coding: utf-8 -*-


from game_utilites import Utilites
from typing import List, Tuple

GRIDS = List[str]
MAKE_MOVE = Tuple[List[str],int,int]
GO_INSIDE_OUTSIDE = Tuple[List[str],int,int,List[List[str]],int,int,int]
def make_move(grid: GRIDS, row: int, col:int, character: str, move:str)->MAKE_MOVE:
    '''
    function: make_move()

    def:    make_move() is a function that takes in the current
            grid, row, col, and move choice and replaces the
            old postion (given by row/col) with ' ' and new
            position with the characters tile.

    param1: map grid, [] of str's
    param2: row, in the grid this is the row pos, int
    param3: col, in the grid this is the col pos, int
    param4: the direction that a player wishes to move

    return values:
        grid:      [] of str's, the grid with the characters new position
        row:       int, the new row based off the move that was passed to
                   the function
        col:       int, the new col based off the move that was passed to
                   the function

    order of the return values is shown below
    return: grid, row, col
    '''
    if move == 'd':
        grid[row] = grid[row][0: col] + ' ' + grid[row][col+1:len(grid[row])]
        col = col+1
        grid[row] = grid[row][0: col] + character + grid[row][col+1:len(grid[row])]
    elif move == 'a':
        grid[row] = grid[row][0: col] + ' ' + grid[row][col+1:len(grid[row])]
        col = col-1
        grid[row] = grid[row][0: col] + character + grid[row][col+1:len(grid[row])]
    elif move == 'w':
        grid[row] = grid[row][0: col] + ' ' + grid[row][col+1:len(grid[row])]
        row = row-1
        grid[row] = grid[row][0: col] + character + grid[row][col+1:len(grid[row])]
    elif move == 's':
        grid[row] = grid[row][0: col] + ' ' + grid[row][col+1:len(grid[row])]
        row = row+1
        grid[row] = grid[row][0: col] + character + grid[row][col+1:len(grid[row])]

    return grid, row, col


def is_valid_move(grid: GRIDS, row: int, col: int, move: str)->bool:

    '''
    function: is_valid_move()

    def:    is_valid_move() is a function that takes in the current
            grid, row, col, and move choice and checks whether the
            next move is in an empty space (' '), if it is then the
            move is valid, else it's not.

    param1: map grid, [] of str's
    param2: row, in the grid this is the row pos, int
    param3: col, in the grid this is the col pos, int
    param4: the direction that a player wishes to move

    return values:
        isValid:   boolean, a variable based on the ability for to move
                   the character to next positon

    order of the return values is shown below
    return: isValid
    '''
    validMoveSet = ['d', 'w', 'a', 's']


    if move in validMoveSet:
        if move == 'd':  # east
            if col+1 < len(grid[0]):
                if grid[row][col+1] == ' ':
                    return True
        elif move == 'a':  # west
            if col-1 >= 0:
                if grid[row][col-1] == ' ':
                    return True
        elif move == 'w':  # north
            if row-1 >= 0:
                if grid[row-1][col] == ' ':
                    return True
        elif move == 's':  # south
            if row+1 < len(grid)-1:
                if grid[row+1][col] == ' ':
                    return True
    return False


def go_inside_cs_building(next_floor: str, next_floor_number:int)-> GO_INSIDE_OUTSIDE:
    '''
    function: go_inside_cs_building()

    def:    this function will load the map from './maps/mst_campus_with_characters.txt'
            and return variables with the new postion on the map and
            in terms of the row and col, the new grid set and set row/col,
            and set the next floor to.

    param1: next_floor, this just the file path of the next floor to be loaded
                        example: going to the second floor the value would be
                        './maps/cs_second_floor.txt'
    param2: next_floor_number,  this is just an integer representation of the
                                floor being loaded. example: going to the second
                                floor the value would be 2

    return values:
        next_grid:      [] of str's, this is the new grid that will be traversed
        next_row:       int, the row on the grid that you'll be at when outside, value will be 24
        next_col:       int, the column on the grid that you'll be at when outside, value will be 44 
        grid_set:       [[str's]]: this is a list of lists containing all the different grids of the
                        mst campus map. This is what's returned from utils.get_campus_map(file_path)
        next_set_row:   int, the row on the grid_set that you'll be at when outside, value will be 0
        next_set_col:   int, the column on the grid_set that you'll be at when outside, value will be 2

    order of the return values is shown below
    return: next_grid, next_row, next_col, grid_set,next_set_row, next_set_col, next_floor
    '''
    utils = Utilites()

    grid_set = utils.get_cs_floor_map(next_floor)
    next_grid = grid_set[0][2].split('\n')
    next_grid_row = 24
    next_grid_col = 44
    next_set_row = 0
    next_set_col = 2

    return next_grid, next_grid_row, next_grid_col, grid_set, next_set_row, next_set_col, next_floor_number


def go_outside_cs_building()->GO_INSIDE_OUTSIDE:
    '''
    function: go_outside_cs_building()

    description:    this function will load the map from './maps/mst_campus_with_characters.txt'
                    and return variables with the new postion on the map and
                    in terms of the row and col, the new grid set and set row/col,
                    and set the next floor to.

    return values:
        next_grid:      [] of str's, this is the new grid that will be traversed
        next_row:       int, the row on the grid that you'll be at when outside, value will be 35
        next_col:       int, the column on the grid that you'll be at when outside, value will be 8
        grid_set:       [[str's]]: this is a list of lists containing all the different grids of the
                        mst campus map. This is what's returned from utils.get_campus_map(file_path)
        next_set_row:   int, the row on the grid_set that you'll be at when outside, value will be 0
        next_set_col:   int, the column on the grid_set that you'll be at when outside, value will be 2
        next_floor:     int, there is no floors outside, value will be -1

    order of the return values is shown below
    return: next_grid, next_row, next_col, grid_set,next_set_row, next_set_col, next_floor
    '''
    from game_utilites import Utilites
    utils = Utilites()

    try:
        grid_set = utils.get_campus_map('maps/mst_campus_with_characters.txt')
    except:
        grid_set = utils.get_campus_map('../maps/mst_campus_with_characters.txt')

    next_grid = grid_set[0][2].split('\n')
    next_row = 35
    next_col = 8
    next_set_row = 0
    next_set_col = 2
    next_floor = -1

    return next_grid, next_row, next_col, grid_set, next_set_row, next_set_col, next_floor


'''
grid is the grid you wish to search
row is the row of the location you wish to search
col is the column of the location you wish to search
character is the character you are searching for (i.e. "X", "Y")
distance is the number of rows/cols from grid[row, col] you wish to search.
if the distance is 1, it searches
---
-G-
---
if distance is 2, it searches
-----
-----
--G--
-----
-----
'''

# TODO you need to write this one
# proximity_sensor function should take in grid, row, col, character, distance, and then return a bool,
# indicating True for being within proximity of an on-map character.
def proximity_sensor(grid: GRIDS,row: int,col: int,character: str,distance:int)->bool:
    try:
       for x in range(0,len(grid)):
           a = 0
           for i in grid[x] :
               if i == character:
                   newRow = x
                   newCol = a
                   break
               a = a + 1

       if abs(row - newRow) <= distance and abs(col-newCol)<=distance:
           return True
       else:
           return False
    except:
        return False



def print_time_left(max_time: int, current_time_played:int)->None:
    print('time left til class starts: {} seconds'.format(max_time-current_time_played))

