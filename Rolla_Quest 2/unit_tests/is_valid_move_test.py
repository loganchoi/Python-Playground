#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
import game_functions
from game_utilites import Utilites


def test():
    print("\nis valid move test")

    try:
        # get the current grid from the campus txt file
        utils = Utilites()
        grid_set = utils.get_campus_map('../maps/mst_campus.txt')
        original_curr_grid = grid_set[0][0].split('\n')

        # set inital variable values
        original_row = 1
        original_col = 1
        original_curr_grid[original_row] = original_curr_grid[original_row][0:original_col] + 'G' + original_curr_grid[original_row][original_col+1:len(original_curr_grid[original_row])]

        move_north = game_functions.is_valid_move(original_curr_grid, original_row, original_col, 'w')
        move_west  = game_functions.is_valid_move(original_curr_grid, original_row, original_col, 'a')
        move_south = game_functions.is_valid_move(original_curr_grid, original_row, original_col, 's')
        move_east  = game_functions.is_valid_move(original_curr_grid, original_row, original_col, 'd')

        if not move_north and not move_west and move_south and move_east:
            print("pass")
            return True
        else:
            # print('testing grid:\n{}'.format('\n'.join(original_curr_grid)))
            # print('is_valid_move({},{},{},{}) returned {}, expected {}'.format('testing grid',str(original_row),str(original_col),'w',str(move_north), str(False)))
            # print('is_valid_move({},{},{},{}) returned {}, expected {}'.format('testing grid', str(original_row), str(original_col),'a',move_west, False))
            # print('is_valid_move({},{},{},{}) returned {}, expected {}'.format('testing grid', str(original_row), str(original_col),'s',move_south, True))
            # print('is_valid_move({},{},{},{}) returned {}, expected {}'.format('testing grid', str(original_row), str(original_col),'d',move_east, True))
            print("fail")
            return False
    except Exception as e:
        print("fail")
        print(e)
        return False


if __name__ == "__main__":
    if test():
        sys.exit(0)
    else:
        sys.exit(1)

