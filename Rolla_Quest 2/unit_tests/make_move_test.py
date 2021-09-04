#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
import game_functions
from game_utilites import Utilites


def test():
    print("\nmake_move test")

    try:
        # get the current grid from the campus txt file
        utils = Utilites()
        grid_set = utils.get_campus_map('../maps/mst_campus.txt')
        original_curr_grid = grid_set[0][0].split('\n')

        # set inital variable values
        original_row = 10
        original_col = 10
        original_curr_grid[original_row] = original_curr_grid[original_row][0:original_col] + 'G' + original_curr_grid[original_row][original_col+1:len(original_curr_grid[original_row])]
        character = 'G'
        unmodified_grid = []

        correct_grid_north = ['WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW', 'W                                                                          ', 'W                                                                          ', 'W                                                          ▄▄▄▄▄▄▄▄▄▄▄▄    ', 'W                                                                          ', 'W                                                     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄', 'W                                                     ▐                    ', 'W                                                     ▐                    ', 'W                                                     ▐                    ', 'W         G                                           ▐      SOME PARKING  ', 'W                                                     ▐         LOT        ', 'W                                                     ▐                    ', 'W                                                     ▐                    ', 'W                                                     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄', 'W                                                                          ', 'W                                                                          ', 'W                                                                          ', 'W                                                                          ', 'W                                                      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄', 'W                                                      ▐                   ', 'W                                                      ▐                   ', 'W                                                      ▐                   ', 'W                               ▐▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▐                   ', 'W                               ▐                                          ', 'W                               ▐                                          ', 'W                               ▐                                          ', 'W                               ▐                                          ', 'W                               ▐                                          ', 'W                               ▐                                          ', 'W                               ▐               MCNUTT HALL                ', 'W                               ▐                                          ', 'W                               ▐                                          ', 'W                               ▐                                          ', 'W                             ▄▄▐                                          ', 'W                             ▐                                            ', 'W                             ▐▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄             ▄▄▄▄▄▄▄▄', 'W                                                     ▐            ▐       ', 'W                                                     ▐            ▐       ', 'W                                                     ▐            ▐       ', 'W                                                     ▐            ▐       ', '']
        correct_grid_south = ['WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW', 'W                                                                          ', 'W                                                                          ', 'W                                                          ▄▄▄▄▄▄▄▄▄▄▄▄    ', 'W                                                                          ', 'W                                                     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄', 'W                                                     ▐                    ', 'W                                                     ▐                    ', 'W                                                     ▐                    ', 'W                                                     ▐      SOME PARKING  ', 'W         G                                           ▐         LOT        ', 'W                                                     ▐                    ', 'W                                                     ▐                    ', 'W                                                     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄', 'W                                                                          ', 'W                                                                          ', 'W                                                                          ', 'W                                                                          ', 'W                                                      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄', 'W                                                      ▐                   ', 'W                                                      ▐                   ', 'W                                                      ▐                   ', 'W                               ▐▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▐                   ', 'W                               ▐                                          ', 'W                               ▐                                          ', 'W                               ▐                                          ', 'W                               ▐                                          ', 'W                               ▐                                          ', 'W                               ▐                                          ', 'W                               ▐               MCNUTT HALL                ', 'W                               ▐                                          ', 'W                               ▐                                          ', 'W                               ▐                                          ', 'W                             ▄▄▐                                          ', 'W                             ▐                                            ', 'W                             ▐▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄             ▄▄▄▄▄▄▄▄', 'W                                                     ▐            ▐       ', 'W                                                     ▐            ▐       ', 'W                                                     ▐            ▐       ', 'W                                                     ▐            ▐       ', '']
        correct_grid_east  = ['WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW', 'W                                                                          ', 'W                                                                          ', 'W                                                          ▄▄▄▄▄▄▄▄▄▄▄▄    ', 'W                                                                          ', 'W                                                     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄', 'W                                                     ▐                    ', 'W                                                     ▐                    ', 'W                                                     ▐                    ', 'W                                                     ▐      SOME PARKING  ', 'W          G                                          ▐         LOT        ', 'W                                                     ▐                    ', 'W                                                     ▐                    ', 'W                                                     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄', 'W                                                                          ', 'W                                                                          ', 'W                                                                          ', 'W                                                                          ', 'W                                                      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄', 'W                                                      ▐                   ', 'W                                                      ▐                   ', 'W                                                      ▐                   ', 'W                               ▐▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▐                   ', 'W                               ▐                                          ', 'W                               ▐                                          ', 'W                               ▐                                          ', 'W                               ▐                                          ', 'W                               ▐                                          ', 'W                               ▐                                          ', 'W                               ▐               MCNUTT HALL                ', 'W                               ▐                                          ', 'W                               ▐                                          ', 'W                               ▐                                          ', 'W                             ▄▄▐                                          ', 'W                             ▐                                            ', 'W                             ▐▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄             ▄▄▄▄▄▄▄▄', 'W                                                     ▐            ▐       ', 'W                                                     ▐            ▐       ', 'W                                                     ▐            ▐       ', 'W                                                     ▐            ▐       ', '']
        correct_grid_west  = ['WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW', 'W                                                                          ', 'W                                                                          ', 'W                                                          ▄▄▄▄▄▄▄▄▄▄▄▄    ', 'W                                                                          ', 'W                                                     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄', 'W                                                     ▐                    ', 'W                                                     ▐                    ', 'W                                                     ▐                    ', 'W                                                     ▐      SOME PARKING  ', 'W         G                                           ▐         LOT        ', 'W                                                     ▐                    ', 'W                                                     ▐                    ', 'W                                                     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄', 'W                                                                          ', 'W                                                                          ', 'W                                                                          ', 'W                                                                          ', 'W                                                      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄', 'W                                                      ▐                   ', 'W                                                      ▐                   ', 'W                                                      ▐                   ', 'W                               ▐▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▐                   ', 'W                               ▐                                          ', 'W                               ▐                                          ', 'W                               ▐                                          ', 'W                               ▐                                          ', 'W                               ▐                                          ', 'W                               ▐                                          ', 'W                               ▐               MCNUTT HALL                ', 'W                               ▐                                          ', 'W                               ▐                                          ', 'W                               ▐                                          ', 'W                             ▄▄▐                                          ', 'W                             ▐                                            ', 'W                             ▐▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄             ▄▄▄▄▄▄▄▄', 'W                                                     ▐            ▐       ', 'W                                                     ▐            ▐       ', 'W                                                     ▐            ▐       ', 'W                                                     ▐            ▐       ', '']
        
        new_grid_north = []
        new_row_north = 0
        new_col_north = 0
        new_grid_south = []
        new_row_south = 0
        new_col_south = 0
        new_grid_east = []
        new_row_east = 0
        new_col_east = 0
        new_grid_west = []
        new_row_west = 0
        new_col_west = 0
        
        moved_north = False
        moved_south = False
        moved_east = False
        moved_west = False

        new_grid_north, new_row_north, new_col_north = game_functions.make_move(original_curr_grid, original_row, original_col, character,'w')
        if  new_grid_north[9][10] == character and \
            new_grid_north[original_row][original_col] != character and\
            new_grid_north == correct_grid_north:
            moved_north = True

        new_grid_south, new_row_south, new_col_south = game_functions.make_move(new_grid_north,  new_row_north, new_col_north, character,'s')            
        if  new_grid_south[10][10] == character and \
            new_grid_south[9][10] != character and \
            new_grid_south == correct_grid_south:
            moved_south = True

        new_grid_east, new_row_east, new_col_east = game_functions.make_move(new_grid_south,  new_row_south, new_col_south, character,'d')
        if  new_grid_east[10][11] == character and \
            new_grid_east[10][10] != character and \
            new_grid_east == correct_grid_east:
            moved_east = True

        new_grid_west, new_row_west, new_col_west = game_functions.make_move(new_grid_east,  new_row_east, new_col_east, character,'a')
        if  new_grid_west[10][10] == character and \
            new_grid_west[10][11] != character and \
            new_grid_west == correct_grid_west:
            moved_west = True

        if moved_north and moved_south and moved_east and moved_west:
            print("pass")
            return True
        else:
            # print('testing grid:')
            # print('make_move({},{},{},{},{}) \nreturned\n{}\n{}\n{}\n\nshould\'ve returned\n{}\n{}\n{}'
            # .format(
            #     'testing_grid', 
            #     str(original_row), 
            #     str(original_col), 
            #     character,
            #     'w',
            #     '\n'.join(new_grid_north),
            #     str(new_row_north),
            #     str(new_col_north),
            #     '\n'.join(correct_grid_north),
            #     str(9),
            #     str(10)                   
            #     ))

            # print('make_move({},{},{},{},{}) \nreturned\n{}\n{}\n{}\n\nshould\'ve returned\n{}\n{}\n{}'
            # .format(
            #     'testing_grid', 
            #     str(new_row_north), 
            #     str(new_col_north), 
            #     character,
            #     's',
            #     '\n'.join(new_grid_south),
            #     str(new_row_south),
            #     str(new_col_south),
            #     '\n'.join(correct_grid_south),
            #     str(10),
            #     str(10)                   
            #     ))



            # print('make_move({},{},{},{},{}) \nreturned\n{}\n{}\n{}\n\nshould\'ve returned\n{}\n{}\n{}'
            # .format(
            #     'testing_grid', 
            #     str(new_row_south), 
            #     str(new_col_south), 
            #     character,
            #     'a',
            #     '\n'.join(new_grid_east),
            #     str(new_row_east),
            #     str(new_col_east),
            #     '\n'.join(correct_grid_east),
            #     str(10),
            #     str(11)                   
            #     ))


            # print('make_move({},{},{},{},{}) \nreturned\n{}\n{}\n{}\n\nshould\'ve returned\n{}\n{}\n{}'
            # .format(
            #     'testing_grid', 
            #     str(new_row_east), 
            #     str(new_col_east), 
            #     character,
            #     'd',
            #     '\n'.join(new_grid_west),
            #     str(new_row_west),
            #     str(new_col_west),
            #     '\n'.join(correct_grid_west),
            #     str(10),
            #     str(10)                   
            #     ))
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

