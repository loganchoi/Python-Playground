#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
import game_functions
from game_utilites import Utilites


def test():
    print("\ngo inside cs building test")

    try:
        # get the current grid from the campus txt file
        utils = Utilites()
        grid_set = utils.get_campus_map('../maps/mst_campus.txt')
        original_curr_grid = grid_set[0][0].split('\n')

        # set inital variable values
        original_row = 1
        original_col = 1
        original_curr_grid[original_row] = original_curr_grid[original_row][0:original_col] + 'G' + original_curr_grid[original_row][original_col+1:len(original_curr_grid[original_row])]

        # for determining the floor we are on
        floor_map = {
            -1: '../maps/mst_campus.txt',
            1: '../maps/cs_first_floor.txt',
            2: '../maps/cs_second_floor.txt',
            3: '../maps/cs_third_floor.txt'
        }

        second_floor = ['                                                            ', '                                                            ', '                                                            ', '                                                            ', '                                                            ', '                                                            ', '                                                            ', '                                                            ', '                                                            ', '                                                        ', '▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀                   ', '                   ▌                  ▐                   ', '                   ▌                  ▐                   ', '                   ▌                  ▐                   ', '                   ▌                  ▐                   ', '        205        ▌        204       ▐                   ', '                   ▌                  ▐                   ', '                   ▌                  ▐                   ', '                   ▌                  ▐                   ', '                   ▌                  ▐                   ', '                   ▌                  ▌▀▀▀▀▀▀▀▀▀▀▀▀        ', '  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀        ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌▐        ', '                                                  ▐   ', '                                                  ▐   ', '                                                  ▐   ', '                                                  ▐        ', '▀▀▀▀▀▀▀▀▀▀▀▀▀▀    ▐▌   ▀▀▀▀▀▀▀▀▀▀▀▀▀^^^^          ▀▐        ', '▌                 ▐▌                  ▌▐-----▌++++▌▐        ', '▌                 ▐▌                  ▌▐-----▌++++▌▐        ', '▐                 ▐▌                  ▌▐-----▌++++▌▐        ', '▐                 ▐▌                  ▌▐-----▌++++▌▐        ', '▐                 ▐▌                  ▌▐-----▌++++▀▐        ', '▐       212       ▐▌        213       ▌▐-----▌++++▀▐        ', '▐                 ▐▌                  ▌▌          ▌▐        ', '▐                 ▐▌                  ▌▐ ▀▀▀▀▀▀▀▀▀▌▐        ', '▐                 ▐▌                  ▌▐                   ', '▐                 ▐▌                  ▌▐                   ', '▐                 ▐▌                  ▌▐                   ', '▐                 ▐▌                  ▌▐                   ', '▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▐                   ', '']
        first_floor = ['                                                                        ', '                                                                    ', '                                                           ', '                                                           ', '                                                           ', '                                                           ', '                                                           ', '                                                           ', '                                                          ', '                                                                        ', '▀▀▐▀▀▀▀▀▀▀▀▀▀▀▐▀▀▀▀▀▀▀▀▀▀▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▐▐               ', '  ▐           ▐          ▐              ▐▐               ', '  ▐           ▐          ▐              ▐▐               ', '  ▐    104C   ▐   104B   ▐     103A     ▐▐               ', '  ▐           ▐          ▐              ▐▐               ', '▀▀▀▀▀▀▀▀    ▀▀▀  ▐▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▐▐               ', '                                        ▐▐               ', '                 ▐                      ▐▐               ', '                 ▐         103          ▐▐               ', ' 104             ▐                      ▐▐               ', '                 ▐                      ▐▐               ', '       ▐         ▐                      ▐▐               ', '▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▐', '                                                     ▐', '                                              ▐      ▐', '                                              ▐      ▐', '▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▐▐   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀^^^   ▐ B1   ▐', '               ▐▐                     ▐▐++++  ▐      ▐', '               ▐▐                     ▐▐++++  ▐      ▐', '               ▐▐                     ▐▐++++  ▐      ▐', '               ▐▐                     ▐▐++++  ▐▀▀▀▀▀▀▐', '               ▐▐                     ▐▐             ▐', '               ▐▐                     ▐▐             ▐', '   101         ▐▐        102          ▐▐             ▐', '               ▐▐                     ▐▐▀▀▀▀^^^^▀▀▀▀▀▀', '               ▐▐                     ▐▐               ', '               ▐▐                     ▐▐               ', '               ▐▐                     ▐▐               ', '               ▐▐                     ▐▐               ', '▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀               ', '']
        third_floor = ['                                                                    ', '                                                                    ', '                                                                    ', '                                                                    ', '                                                                    ', '              ', '                                                                    ', '                                                                    ', '                                                                    ', '                                                                    ', '                                                                    ', '▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                     ', ' ▐           ▐          ▐          ▐          ▐                     ', ' ▐           ▐          ▐          ▐          ▐                     ', ' ▐           ▐          ▐          ▐          ▐                     ', ' ▐    319    ▐   318    ▐   315    ▐   314    ▐                     ', ' ▐           ▐          ▐          ▐          ▐                     ', ' ▐                      ▐                     ▐                     ', '▄▐▄▄▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄▄▄▐▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▐                     ', ' ▐        ▐    ▐        ▐        ▐   ▐        ▐                     ', ' ▐        ▐    ▐        ▐        ▐   ▐        ▐                     ', ' ▐  320   ▐    ▐  317   ▐  316   ▐   ▐   313  ▐                     ', ' ▐                      ▐                     ▐                     ', '▄▐▄▄▄▄▄▄▄▄▄     ▄▄▄▄▄▄▄▄▐▄▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▐▐     ', '                                                             ▐▐     ', '                                                             ▐▐     ', '  ▄▄▄▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▐▄▄▄▄▄▄▄▄▄▄▄▄▄     ▐▐     ', '  ▐                       ▐                    ▐-----▐▐▐-----▐▐     ', '  ▐        ▐                          ▐▐       ▐-----▐▐▐-----▐▐     ', '  ▐  304   ▐    ▐                 ▐   ▐▐  312  ▐-----▐▐▐-----▐▐     ', '  ▐        ▐    ▐                 ▐   ▐▐       ▐-----▐▐▐-----▐▐     ', '  ▐▄▄▄▄▄▄▄▄▐    ▐       308       ▐   ▐▄▄▄▄▄▄▄▄▐-----▐▐▐-----▐▐     ', '  ▐             ▐                 ▐            ▐             ▐▐     ', '  ▐   305  ▐    ▐                 ▐    ▐       ▐             ▐▐     ', '  ▐▄▄▄▄▄▄▄▄▐    ▐                 ▐    ▐  311  ▐▄▄▄▄▄▄▄▄▄▄▄▄▄▐▐     ', '  ▐        ▐    ▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▐    ▐▄▄▄▄▄▄▄▐▄▄▄▄▄▄▄▄▄▄▄▄▄▐▐     ', '  ▐                      ▐                     ▐                    ', '  ▐   306     ▐   307    ▐   309    ▐   310    ▐                    ', '  ▐           ▐          ▐          ▐          ▐                    ', '▄▄▐▄▄▄▄▄▄▄▄▄▄▄▐▄▄▄▄▄▄▄▄▄▄▐▄▄▄▄▄▄▄▄▄▄▐▄▄▄▄▄▄▄▄▄▄▐                    ', '']

        new_curr_grid_first_floor = []
        new_curr_grid_second_floor = []
        new_curr_grid_third_floor = []

        new_grid_row_first_floor = 0
        new_grid_row_second_floor = 0
        new_grid_row_third_floor = 0
        new_grid_col_first_floor = 0
        new_grid_col_second_floor = 0
        new_grid_col_third_floor = 0


        new_grid_set_first_floor = []
        new_grid_set_second_floor = []
        new_grid_set_third_floor = []


        new_grid_set_row_first_floor = 0
        new_grid_set_row_second_floor = 0
        new_grid_set_row_third_floor = 0
        new_grid_set_col_first_floor = 0
        new_grid_set_col_second_floor = 0
        new_grid_set_col_third_floor = 0

        outside_to_inside_new_floor_number = 0
        second_to_first_new_floor_number = 0
        second_to_third_new_floor_number = 0
            
        # starting from the outside going inside
        new_curr_grid_second_floor, new_grid_row_second_floor, new_grid_col_second_floor, new_grid_set_second_floor, new_grid_set_row_second_floor, new_grid_set_col_second_floor, outside_to_inside_new_floor_number = game_functions.go_inside_cs_building(floor_map[2], 2)

        # starting from second floor going to first floor
        new_curr_grid_first_floor, new_grid_row_first_floor, new_grid_col_first_floor, new_grid_set_first_floor, new_grid_set_row_first_floor, new_grid_set_col_first_floor, second_to_first_new_floor_number = game_functions.go_inside_cs_building(floor_map[1], 1)

        # starting from second floor going to third floor
        new_curr_grid_third_floor, new_grid_row_third_floor, new_grid_col_third_floor, new_grid_set_third_floor, new_grid_set_row_third_floor, new_grid_set_col_third_floor, second_to_third_new_floor_number = game_functions.go_inside_cs_building(floor_map[3], 3)

        # check to see if all the numerical values are correct
        if  second_to_third_new_floor_number != 3 or\
            second_to_first_new_floor_number != 1 or\
            outside_to_inside_new_floor_number != 2 or\
            ((new_grid_row_first_floor != new_grid_row_second_floor) or (new_grid_row_second_floor != new_grid_row_third_floor) or (new_grid_row_second_floor != 24)) or \
            ((new_grid_col_first_floor != new_grid_col_second_floor) or (new_grid_col_second_floor != new_grid_col_third_floor) or (new_grid_col_second_floor != 44)) or\
            ((new_grid_set_row_first_floor != new_grid_set_row_second_floor) or (new_grid_set_row_second_floor != new_grid_set_row_third_floor) or (new_grid_set_row_second_floor != 0))or \
            ((new_grid_set_col_first_floor != new_grid_set_col_second_floor) or (new_grid_set_col_second_floor != new_grid_set_col_third_floor) or (new_grid_set_col_second_floor != 2)) or \
            new_curr_grid_first_floor != first_floor or\
            new_curr_grid_second_floor != second_floor or\
            new_curr_grid_third_floor != third_floor:

            # # another way of letting students know what's wrong
            # print('go_inside_cs_building({},{}) returned: \n{}\n{}\n{}\n{}\n{}\n{}\n\nshould\'ve been\n{}\n{}\n{}\n{}\n{}\n{}\n\n'
            # .format(
            #         floor_map[2], 
            #         str(2), 
            #         '\n'.join(new_curr_grid_second_floor),
            #         str(new_grid_row_second_floor),
            #         str(new_grid_col_second_floor),
            #         str(new_grid_set_row_second_floor),
            #         str(new_grid_set_col_second_floor),
            #         str(outside_to_inside_new_floor_number),
            #         str(2),
            #         str(24),
            #         str(44),
            #         str(0),
            #         str(2),
            #         '\n'.join(second_floor)))
            
            # print('go_inside_cs_building({},{}) returned: \n{}\n{}\n{}\n{}\n{}\n{}\n\nshould\'ve been\n{}\n{}\n{}\n{}\n{}\n{}\n\n'
            # .format(
            #         floor_map[1], 
            #         str(1), 
            #         '\n'.join(new_curr_grid_first_floor),
            #         str(new_grid_row_first_floor),
            #         str(new_grid_col_first_floor),
            #         str(new_grid_set_row_first_floor),
            #         str(new_grid_set_col_first_floor),
            #         str(second_to_first_new_floor_number),
            #         str(1),
            #         str(24),
            #         str(44),
            #         str(0),
            #         str(2),
            #         '\n'.join(first_floor)))

            # print('go_inside_cs_building({},{}) returned: \n{}\n{}\n{}\n{}\n{}\n{}\n\nshould\'ve been\n{}\n{}\n{}\n{}\n{}\n{}\n\n'
            # .format(
            #         floor_map[3], 
            #         str(3), 
            #         '\n'.join(new_curr_grid_third_floor),
            #         str(new_grid_row_third_floor),
            #         str(new_grid_col_third_floor),
            #         str(new_grid_set_row_third_floor),
            #         str(new_grid_set_col_third_floor),
            #         str(second_to_third_new_floor_number),
            #         str(1),
            #         str(24),
            #         str(44),
            #         str(0),
            #         str(2),
            #         '\n'.join(third_floor)))
                    
            print('fail')
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

