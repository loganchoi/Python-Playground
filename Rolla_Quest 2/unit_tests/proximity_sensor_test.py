#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
import game_functions
from game_utilites import Utilites

def test():
    print("\nProximity Sensor Test")

    try:
        test_grid = ["---",
                     "---",
                     "K--",
                     "-G-"]
        if game_functions.proximity_sensor(test_grid, 1, 1, "K", 10):
            test1 = True
        else:
            print("Test 1 failed")
            test1 = False
        if game_functions.proximity_sensor(test_grid, 1, 1, "G", 2):
           test2 = True
        else:
            print("Test 2 Failed")
            test2 = False
        test_grid = ["LLLLL",
                     "KLLLL",
                     "LLLLL",
                     "LLLLL",
                     "JLLLL"]
        if game_functions.proximity_sensor(test_grid, 1, 1, "K", 1):
            test3 = True
        else:
            print("Test 3 Failed")
            test3 = False
        if game_functions.proximity_sensor(test_grid, 0, 0, "J", 5):
            test4 = True
        else:
            print("Test 4 Failed")
            test4 = False
        if not game_functions.proximity_sensor(test_grid, 0, 0, "J", 1):
            test5 = True
        else:
            print("Test 5 Failed")
            test5 = False
        if test1 and test2 and test3 and test4 and test5:
            print("pass")
            return True
        else:
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

