#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
import game_functions
from game_utilites import Utilites


def test():
    print("\ngo outside cs building test")

    try:
        # get the current grid from the campus txt file
        utils = Utilites()
        grid_set = utils.get_campus_map('../maps/mst_campus.txt')
        original_curr_grid = grid_set[0][0].split('\n')

        # set inital variable values
        original_row = 1
        original_col = 1
        original_curr_grid[original_row] = original_curr_grid[original_row][0:original_col] + 'G' + original_curr_grid[original_row][original_col+1:len(original_curr_grid[original_row])]

        correct_outside_grid = ['WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW', '                                                                           ', '                                                                           ', '                                                                           ', '                                                                           ', '                                                                           ', '                                                                           ', '                                                                           ', '                                                                           ', '                                                                           ', '                                                                           ', '                                                                           ', '                                                                           ', '                                                                           ', '                                                                           ', '▄▄▄▄▄▄▄▄▄▐▐                                                                ', 'aumanis  ▐▐                                                                ', 'James    ▐▐                                                                ', ' HALL    ▐▐                              ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄', '         ▐▐                              ▐                                 ', '▄▄▄▄▄▄▄▄▄▐▐                              ▐                EMERSON HALL     ', '                                         ▐                                 ', '                                       ▄▄▐                                 ', '                                       ▐                                   ', '                                       ▐                                   ', '                                       ▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄', '                                                                           ', '▄▄▄▄▄▄▄▐                                                                   ', 'DING   ▐                                                                   ', '       ▐                                                                   ', '       ▐                                                                   ', ' ENTER ▐          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                                  ', '▄^^^^^▄▐        ▄▄▐                      ▐▄▄▄                              ', '                ▐                           ▐                              ', '                ▐                           ▐                              ', '                ▐                           ▐                              ', '                ▐                           ▐                              ', '                ▐      CURTIS WILSON        ▐                              ', '                ▐        LIBRARY            ▐                              ', '                ▐                           ▐                              ', '']

        # for determining the floor we are on
        floor_map = {
            -1: '../maps/mst_campus.txt',
            1: '../maps/cs_first_floor.txt',
            2: '../maps/cs_second_floor.txt',
            3: '../maps/cs_third_floor.txt'
        }

        new_curr_grid_outside = []
        new_grid_row_outside = 0
        new_grid_col_outside = 0
        new_grid_set_outside = []
        new_grid_set_row_outside = 0
        new_grid_set_col_outside = 0
        inside_to_outside_new_floor_number = 0

        # starting from the outside going inside
        new_curr_grid_outside, new_grid_row_outside, new_grid_col_outside, new_grid_set_outside, new_grid_set_row_outside, new_grid_set_col_outside, inside_to_outside_new_floor_number = game_functions.go_outside_cs_building()

        # check to see if all the numerical values are correct
        # first check:  transistion from inside to outside of the cs building, the floor number 
        #               should be -1 as there are no floors outside
        # second check: default grid rows for exiting the building should be 35
        # third check:  all new grid cols for the floors should be 8
        # fouth check:  all new grid set row for exiting the building should be 0, the cs building
        #               is at the top of the map
        # fifth check:  all new grid set col for exiting the building should be 2, the cs building
        #               is at the top of the map and third grid spot
        # sixth check:  the new grid returned should be equivalent to the campus grid maps indexed
        #               at [0][2]
        if inside_to_outside_new_floor_number != -1 or\
            new_grid_row_outside != 35 or \
            new_grid_col_outside != 8 or \
            new_grid_set_row_outside != 0 or \
            new_grid_set_col_outside != 2 or \
            new_curr_grid_outside != correct_outside_grid:

            # another way of letting students know what's wrong
            # print('go_outside_cs_building() returned: \n{}\n{}\n{}\n{}\n{}\n{}\nshould\'ve been\n{}\n{}\n{}\n{}\n{}\n{}\n'
            # .format( str(inside_to_outside_new_floor_number),
            #         str(new_grid_row_outside),
            #         str(new_grid_col_outside),
            #         str(new_grid_set_row_outside),
            #         str(new_grid_set_col_outside),
            #         '\n'.join(new_curr_grid_outside),
            #         str(-1),
            #         str(35),
            #         str(8),
            #         str(0),
            #         str(2),
            #         '\n'.join(correct_outside_grid)))
            # print('fail')
            return False
        else:
            print('pass')
            return True
    except Exception as e:
        print("fail")
        print(e)
        return False


if __name__ == "__main__":
    if test():
        sys.exit(0)
    else:
        sys.exit(1)

