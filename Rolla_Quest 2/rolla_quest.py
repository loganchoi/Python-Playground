#!/usr/bin/python3
# -*- coding: utf-8 -*-


import random
import time
import game_utilites
import game_functions
from characters import Hero, LostStudent, BrotherJedd, HuggingMom, SweaterMerchant, FoodVendor


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
        campus_grids = utils.get_campus_map('maps/mst_campus_with_characters.txt')
    except:
        campus_grids = utils.get_campus_map('../maps/mst_campus_with_characters.txt')

    # current set of grids we are working with
    grid_set = campus_grids

    # keep track of inside or outside
    inside = False

    # This is your character, literally
    character = 'G'
    main_character = Hero(character)
    lost_student = LostStudent()
    brother_jedd = BrotherJedd()
    hugging_mother = HuggingMom()
    st_pats_sweater_vendor = SweaterMerchant()
    food_vendor = FoodVendor()

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
        -1: 'maps/mst_campus_with_characters.txt',
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
    max_time = 300
    # keeps track of the number of moves we've made
    i = 0

    print('\033c', '\n'.join(current_grid))
    game_functions.print_time_left(max_time, i)

    while i < max_time:
        if i == 0:
            print('Welcome to Rolla Quest! It\'s time for you to get to class\nand you have 30 minutes, let\'s start your adventure.\n')

        print('Which direction would you like to go? w:north, a:west, s:south, d:east\n')

        move = game_utilites.getch()
        print(curr_grid_col)
        isValid = game_functions.is_valid_move(current_grid, curr_grid_row, curr_grid_col, move)

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
                    current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = game_functions.go_outside_cs_building()
                    isValid = True
                    inside = False

                # check to see if we are entering the cs building
                elif current_grid[curr_grid_row][curr_grid_col+1] == enter_exit_building_character and not inside:
                    current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = game_functions.go_inside_cs_building(floor_map[2], 2)
                    isValid = True
                    inside = True

                # if inside the cs building, go to the next floor downstairs
                elif current_grid[curr_grid_row][curr_grid_col+1] == upstairs_character:
                    if curr_floor == 1:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = game_functions.go_inside_cs_building(floor_map[2], 2)
                    elif curr_floor == 2:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = game_functions.go_inside_cs_building(floor_map[3], 3)
                    isValid = True
                    inside = True

                # if inside the cs building, go to the next floor upstairs
                elif current_grid[curr_grid_row][curr_grid_col+1] == downstairs_character:
                    if curr_floor == 3:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = game_functions.go_inside_cs_building(floor_map[2], 2)
                    elif curr_floor == 2:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = game_functions.go_inside_cs_building(floor_map[1], 1)
                    isValid = True
                    inside = True

                # just check if the new input was valid
                else:
                    isValid = game_functions.is_valid_move(current_grid, curr_grid_row, curr_grid_col, move)

            # same logic as above applies to each of the following cases, north, south, and west
            elif move == 'a':  # west
                if curr_grid_col <= 0:
                    curr_set_col -= 1
                    curr_grid_col = len(current_grid[0])-1
                    current_grid = grid_set[curr_set_row][curr_set_col].split('\n')
                    isValid = True

                elif current_grid[curr_grid_row][curr_grid_col-1] == enter_exit_building_character and inside:
                    current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = game_functions.go_outside_cs_building()
                    isValid = True
                    inside = False

                elif current_grid[curr_grid_row][curr_grid_col-1] == enter_exit_building_character and not inside:
                    current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = game_functions.go_inside_cs_building(floor_map[2], 2)
                    isValid = True
                    inside = True

                elif current_grid[curr_grid_row][curr_grid_col-1] == upstairs_character:
                    if curr_floor == 1:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = game_functions.go_inside_cs_building(floor_map[2], 2)
                    elif curr_floor == 2:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = game_functions.go_inside_cs_building(floor_map[3], 3)
                    isValid = True
                    inside = True

                elif current_grid[curr_grid_row][curr_grid_col-1] == downstairs_character:
                    if curr_floor == 3:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = game_functions.go_inside_cs_building(floor_map[2], 2)
                    elif curr_floor == 2:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = game_functions.go_inside_cs_building(floor_map[1], 1)
                    isValid = True
                    inside = True

                else:
                    isValid = game_functions.is_valid_move(current_grid, curr_grid_row, curr_grid_col, move)

            elif move == 'w':  # north
                if curr_grid_row <= 0:
                    curr_set_row -= 1
                    curr_grid_row = len(current_grid)-1
                    current_grid = grid_set[curr_set_row][curr_set_col].split('\n')
                    isValid = True

                elif current_grid[curr_grid_row-1][curr_grid_col] == enter_exit_building_character and inside:
                    current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = game_functions.go_outside_cs_building()
                    isValid = True
                    inside = False

                elif current_grid[curr_grid_row-1][curr_grid_col] == enter_exit_building_character and not inside:
                    current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = game_functions.go_inside_cs_building(floor_map[2], 2)
                    isValid = True
                    inside = True

                elif current_grid[curr_grid_row-1][curr_grid_col] == upstairs_character:
                    if curr_floor == 1:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = game_functions.go_inside_cs_building(floor_map[2], 2)
                    elif curr_floor == 2:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = game_functions.go_inside_cs_building(floor_map[3], 3)
                    isValid = True
                    inside = True

                elif current_grid[curr_grid_row-1][curr_grid_col] == downstairs_character:
                    if curr_floor == 3:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = game_functions.go_inside_cs_building(floor_map[2], 2)
                    elif curr_floor == 2:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = game_functions.go_inside_cs_building(floor_map[1], 1)
                    isValid = True
                    inside = True

                else:
                    isValid = game_functions.is_valid_move(current_grid, curr_grid_row, curr_grid_col, move)

            elif move == 's':  # south
                if curr_grid_row+1 >= len(current_grid)-1:
                    curr_set_row += 1
                    curr_grid_row = 0
                    current_grid = grid_set[curr_set_row][curr_set_col].split('\n')
                    isValid = True

                elif current_grid[curr_grid_row+1][curr_grid_col] == enter_exit_building_character and inside:
                    current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = game_functions.go_outside_cs_building()
                    isValid = True
                    inside = False

                elif current_grid[curr_grid_row+1][curr_grid_col] == enter_exit_building_character and not inside:
                    current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = game_functions.go_inside_cs_building(floor_map[2], 2)
                    isValid = True
                    inside = True

                elif current_grid[curr_grid_row+1][curr_grid_col] == upstairs_character:
                    if curr_floor == 1:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = game_functions.go_inside_cs_building(floor_map[2], 2)
                    elif curr_floor == 2:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = game_functions.go_inside_cs_building(floor_map[3], 3)
                    isValid = True
                    inside = True

                elif current_grid[curr_grid_row+1][curr_grid_col] == downstairs_character:
                    if curr_floor == 3:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = game_functions.go_inside_cs_building(floor_map[2], 2)

                    elif curr_floor == 2:
                        current_grid, curr_grid_row, curr_grid_col, grid_set, curr_set_row, curr_set_col, curr_floor = game_functions.go_inside_cs_building(floor_map[1], 1)
                    isValid = True
                    inside = True

                else:
                    isValid = game_functions.is_valid_move(current_grid, curr_grid_row, curr_grid_col, move)

            if not isValid:
                print('\033c', '\n'.join(current_grid), '\nInvalid move try again? w:north, a:west, s:south, d:east\n')
                move = game_utilites.getch()


        # move the character
        current_grid, curr_grid_row, curr_grid_col = game_functions.make_move(current_grid, curr_grid_row, curr_grid_col, character, move)

        # setting main characters coordinates
        main_character.set_col_coord(curr_grid_col)
        main_character.set_row_coord(curr_grid_row)

        print('\033c', '\n'.join(current_grid))
        print('time left til class starts: {} seconds'.format(max_time-i))

        # printing main characters coordinates
        main_character.print_position()

        time_lost = 0
        if game_functions.proximity_sensor(current_grid, curr_grid_row, curr_grid_col, lost_student.symbol, 1):
            time_lost = random.randint(2, 10)
            print('\033c', lost_student.__str__())
            random_selection = random.randint(0,2)
            print('Do you know where the {} is at?'.format(['Havener Center','CS Building','Library'][random_selection]))
            print('You\'ve lost {} seconds of time'.format(str(time_lost)))
            i += time_lost
            time.sleep(2)

        elif game_functions.proximity_sensor(current_grid, curr_grid_row, curr_grid_col, brother_jedd.symbol, 1):
            time_lost = random.randint(5, 20)
            print('\033c', brother_jedd.__str__())
            random_selection = random.randint(0,2)
            print('Lets talk about {}.'.format(['Jesus','your salvation','your eternal life'][random_selection]))
            print('You\'ve lost {} seconds of time'.format(str(time_lost)))
            i += time_lost
            time.sleep(2)

        elif game_functions.proximity_sensor(current_grid, curr_grid_row, curr_grid_col, hugging_mother.symbol, 1):
            time_lost = random.randint(2, 8)
            print('\033c', hugging_mother.__str__())
            random_selection = random.randint(0,2)
            print('You\'re {}!'.format(['AWESOME','able to do this','doing great'][random_selection]))
            print('You\'ve lost {} seconds of time'.format(str(time_lost)))
            i += time_lost
            time.sleep(2)

        elif game_functions.proximity_sensor(current_grid, curr_grid_row, curr_grid_col, st_pats_sweater_vendor.symbol, 2):
            time_lost = random.randint(8, 15)
            print('\033c', st_pats_sweater_vendor.__str__())
            random_selection = random.randint(0,2)
            print('Do you wanna buy a {} st pats sweater?'.format(['2017','2018','2019'][random_selection]))
            print('You\'ve lost {} seconds of time'.format(str(time_lost)))
            i += time_lost
            time.sleep(2)

        elif game_functions.proximity_sensor(current_grid, curr_grid_row, curr_grid_col, food_vendor.symbol, 2):
            gtime_lost = random.randint(4, 10)
            print('\033c', food_vendor.__str__())
            random_selection = random.randint(0,2)
            print('You bought a {}!'.format(food_vendor.food[random_selection]))
            print('You\'ve lost {} seconds of time but your energy is being restored!'.format(str(gtime_lost)))
            i += gtime_lost
            time.sleep(2)

        print('\033c', '\n'.join(current_grid))
        print('time left til class starts: {} seconds'.format(max_time-i))

        i += 1

