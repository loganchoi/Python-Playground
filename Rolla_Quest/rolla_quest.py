#!/usr/bin/python3
# -*- coding: utf-8 -*-

import game_utilites
import random


def make_move(grid, row, col, character, move):
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
    emptySpace = ' '
    if move == 'w':
        grid[row] = grid[row][:col] + ' '+ grid[row][col+1:]
        grid[row-1] = grid[row-1][:col]+character + grid[row-1][col+1:]
        row = row - 1
    elif move == 'a':
        grid[row] = grid[row][:col]+' '+grid[row][col+1:]
        col = col - 1
        grid[row] = grid[row][:col]+character +grid[row][col+1:]
    elif move == 's':
        grid[row] = grid[row][:col] + ' '+ grid[row][col+1:]
        grid[row+1] = grid[row+1][:col]+character + grid[row+1][col+1:]
        row = row + 1
    elif move == 'd':
        grid[row] = grid[row][:col]+' '+grid[row][col+1:]
        col = col + 1
        grid[row] = grid[row][:col]+character +grid[row][col+1:]

    return grid, row, col


def is_valid_move(grid, row, col, move):

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

    isValid = False
    if move =='w':
        row = row-1
        if grid[row][col] == ' ':
            isValid = True
    elif move == 'a':
        col = col-1
        if grid[row][col] == ' ':
            isValid = True
    elif move == 's':
        row = row + 1
        if grid[row][col]==' ':
            isValid = True
    elif move == 'd':
        col = col + 1
        if grid[row][col] == ' ':
            isValid = True
    else:
        isValid = False


    return isValid


def go_inside_cs_building(next_floor, next_floor_number):
    '''
    function: go_inside_cs_building()

    def:    this function will load the map from './maps/mst_campus.txt'
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
        next_row:       int, the row on the grid that you'll be at when outside, value will be 35
        next_col:       int, the column on the grid that you'll be at when outside, value will be 8
        grid_set:       [[str's]]: this is a list of lists containing all the different grids of the
                        mst campus map. This is what's returned from utils.get_campus_map(file_path)
        next_set_row:   int, the row on the grid_set that you'll be at when outside, value will be 0
        next_set_col:   int, the column on the grid_set that you'll be at when outside, value will be 2
        next_floor:     int, there is no floors outside, value will be just the parameter next_floor_number

    order of the return values is shown below
    return: next_grid, next_row, next_col, grid_set,next_set_row, next_set_col, next_floor
    '''
    from game_utilites import Utilites
    utils = Utilites()
    NewFloor = open(next_floor)
    NewFloor = NewFloor.readlines()
    # note: you may need to change these values
    grid_set = utils.get_cs_floor_map(next_floor)
    next_grid = grid_set[0][2].split('\n')
    next_row = 24
    next_col = 44
    next_set_row = 0
    next_set_col = 2
    next_floor = next_floor_number

    return next_grid, next_row, next_col, grid_set, next_set_row, next_set_col, next_floor


def go_outside_cs_building():
    '''
    function: go_outside_cs_building()

    description:    this function will load the map from './maps/mst_campus.txt'
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
    campus = '../maps/mst_campus.txt'

    # note: you may need to change these values
    grid_set = utils.get_campus_map(campus)
    next_grid = grid_set[0][2].split('\n')
    next_row = 35
    next_col = 8
    next_set_row = 0
    next_set_col = 2
    next_floor = -1



    return next_grid, next_row, next_col, grid_set, next_set_row, next_set_col, next_floor


if __name__ == "__main__":
    # 3 starting postions, list of tuples of tuples
    # first tuple: starting grid
    # second tuple: starting positon inside grid
    starting_positions = [
        ([1, 0], (1, 73)),
        ([0, 2], (38, 1)),
        ([1, 3], (1, 73))
    ]

    # Begin Quest to Get to Class
    utils = game_utilites.Utilites()
    try:
        campus_grids = utils.get_campus_map('maps/mst_campus.txt')
    except:
        campus_grids = utils.get_campus_map('../maps/mst_campus.txt')

    # current set of grids we are working with
    grid_set = campus_grids

    # keep track of inside or outside
    inside = False

    # This is your character, literally
    character = 'G'

    # Signs for going in/outside, up/downstairs
    enter_exit_building_character = '^'
    upstairs_character = '+'
    downstairs_character = '-'

    # starting position
    random_start_num = random.randint(0, 2)
    starting_grid_pos = starting_positions[1]

    # current_map is just a string containing new lines
    curr_set_col = starting_grid_pos[0][1]
    curr_set_row = starting_grid_pos[0][0]
    current_map = grid_set[curr_set_row][curr_set_col]

    # Current Floor, relative to CS Building
    # outside: -1 not on a floor
    # first floor: 1
    # second floor: 2
    # third floor: 3
    curr_floor = -1

    floor_map = {
        -1: 'maps/mst_campus.txt',
        1: 'maps/cs_first_floor.txt',
        2: 'maps/cs_second_floor.txt',
        3: 'maps/cs_third_floor.txt'
    }

    # get the row and position in the string
    curr_grid_row = starting_grid_pos[1][0]  # also row position
    curr_grid_col = starting_grid_pos[1][1]  # also col position

    # split on the newlines and now we have  list to work with
    current_grid = current_map.split('\n')

    # intial placement of character
    current_grid[curr_grid_row] = current_grid[curr_grid_row][0: curr_grid_col] + character + current_grid[curr_grid_row][curr_grid_col+1:len(current_grid[curr_grid_row])]

    # keeps track of the number of moves we've made
    i = 0

    print('\033c', '\n'.join(current_grid))

    while i < 1000:
        if i == 0:
            print('Welcome to Rolla Quest! It\'s time for you to get to class\nand you have 30 minutes, let\'s start your adventure.\n')

        print('Which direction would you like to go? w:north, a:west, s:south, d:east\n')
        move = game_utilites.getch()
        print(curr_grid_col)
        isValid = is_valid_move(current_grid, curr_grid_row, curr_grid_col, move)

        # while the user input is not valid continue getting user input
        # of if the input is not valid because there's not a ' ' check to see
        # if it's an entrace to a building
        while not isValid:
            # grid transition logic
            # transition between buildings and the outside
            if move == 'd':  # east

                # check to see if we're within the bounds of the map
                if curr_grid_col+1 >= len(current_grid[0]):
                    curr_set_col += 1
                    curr_grid_col = 0
                    current_grid = grid_set[curr_set_row][curr_set_col].split('\n')
                    isValid = True

                # check to see if we are exiting the cs building
                elif current_grid[curr_grid_row][curr_grid_col+1] == enter_exit_building_character and inside:
                    current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = go_outside_cs_building()
                    isValid = True
                    inside = False

                # check to see if we are entering the cs building
                elif current_grid[curr_grid_row][curr_grid_col+1] == enter_exit_building_character and not inside:
                    current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = go_inside_cs_building(floor_map[2], 2)
                    isValid = True
                    inside = True

                # if inside the cs building, go to the next floor downstairs
                elif current_grid[curr_grid_row][curr_grid_col+1] == upstairs_character:
                    if curr_floor == 1:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = go_inside_cs_building(floor_map[2], 2)
                    elif curr_floor == 2:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = go_inside_cs_building(floor_map[3], 3)
                    isValid = True
                    inside = True

                # if inside the cs building, go to the next floor upstairs
                elif current_grid[curr_grid_row][curr_grid_col+1] == downstairs_character:
                    if curr_floor == 3:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = go_inside_cs_building(floor_map[2], 2)
                    elif curr_floor == 2:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = go_inside_cs_building(floor_map[1], 1)
                    isValid = True
                    inside = True

                # just check if the new input was valid
                else:
                    isValid = is_valid_move(current_grid, curr_grid_row, curr_grid_col, move)

            # same logic as above applies to each of the following cases, north, south, and west
            elif move == 'a':  # west
                if curr_grid_col <= 0:
                    curr_set_col -= 1
                    curr_grid_col = len(current_grid[0])-1
                    current_grid = grid_set[curr_set_row][curr_set_col].split('\n')
                    isValid = True

                elif current_grid[curr_grid_row][curr_grid_col-1] == enter_exit_building_character and inside:
                    current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = go_outside_cs_building()
                    isValid = True
                    inside = False

                elif current_grid[curr_grid_row][curr_grid_col-1] == enter_exit_building_character and not inside:
                    current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = go_inside_cs_building(floor_map[2], 2)
                    isValid = True
                    inside = True

                elif current_grid[curr_grid_row][curr_grid_col-1] == upstairs_character:
                    if curr_floor == 1:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = go_inside_cs_building(floor_map[2], 2)
                    elif curr_floor == 2:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = go_inside_cs_building(floor_map[3], 3)
                    isValid = True
                    inside = True

                elif current_grid[curr_grid_row][curr_grid_col-1] == downstairs_character:
                    if curr_floor == 3:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = go_inside_cs_building(floor_map[2], 2)
                    elif curr_floor == 2:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = go_inside_cs_building(floor_map[1], 1)
                    isValid = True
                    inside = True

                else:
                    isValid = is_valid_move(move, current_grid, curr_grid_row, curr_grid_col)

            elif move == 'w':  # north
                if curr_grid_row <= 0:
                    curr_set_row -= 1
                    curr_grid_row = len(current_grid)-1
                    current_grid = grid_set[curr_set_row][curr_set_col].split('\n')
                    isValid = True

                elif current_grid[curr_grid_row-1][curr_grid_col] == enter_exit_building_character and inside:
                    current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = go_outside_cs_building()
                    isValid = True
                    inside = False

                elif current_grid[curr_grid_row-1][curr_grid_col] == enter_exit_building_character and not inside:
                    current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = go_inside_cs_building(floor_map[2], 2)
                    isValid = True
                    inside = True

                elif current_grid[curr_grid_row-1][curr_grid_col] == upstairs_character:
                    if curr_floor == 1:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = go_inside_cs_building(floor_map[2], 2)
                    elif curr_floor == 2:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = go_inside_cs_building(floor_map[3], 3)
                    isValid = True
                    inside = True

                elif current_grid[curr_grid_row-1][curr_grid_col] == downstairs_character:
                    if curr_floor == 3:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = go_inside_cs_building(floor_map[2], 2)
                    elif curr_floor == 2:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = go_inside_cs_building(floor_map[1], 1)
                    isValid = True
                    inside = True

                else:
                    isValid = is_valid_move(current_grid, curr_grid_row, curr_grid_col, move)

            elif move == 's':  # south
                if curr_grid_row+1 >= len(current_grid)-1:
                    curr_set_row += 1
                    curr_grid_row = 0
                    current_grid = grid_set[curr_set_row][curr_set_col].split('\n')
                    isValid = True

                elif current_grid[curr_grid_row+1][curr_grid_col] == enter_exit_building_character and inside:
                    current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = go_outside_cs_building()
                    isValid = True
                    inside = False

                elif current_grid[curr_grid_row+1][curr_grid_col] == enter_exit_building_character and not inside:
                    current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = go_inside_cs_building(floor_map[2], 2)
                    isValid = True
                    inside = True

                elif current_grid[curr_grid_row+1][curr_grid_col] == upstairs_character:
                    if curr_floor == 1:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = go_inside_cs_building(floor_map[2], 2)
                    elif curr_floor == 2:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = go_inside_cs_building(floor_map[3], 3)
                    isValid = True
                    inside = True

                elif current_grid[curr_grid_row+1][curr_grid_col] == downstairs_character:
                    if curr_floor == 3:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = go_inside_cs_building(floor_map[2], 2)

                    elif curr_floor == 2:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = go_inside_cs_building(floor_map[1], 1)
                    isValid = True
                    inside = True

                else:
                    isValid = is_valid_move(current_grid, curr_grid_row, curr_grid_col, move)

            if not isValid:
                print('\033c', '\n'.join(current_grid), '\nInvalid move try again? w:north, a:west, s:south, d:east\n')
                move = game_utilites.getch()

        # move the character
        current_grid, curr_grid_row, curr_grid_col = make_move(current_grid, curr_grid_row, curr_grid_col, character, move)

        print('\033c', '\n'.join(current_grid))
        i += 1

