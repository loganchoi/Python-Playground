#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from characters import Hero
import unit_tests.check_base_test

def test():
    print('\nhero_functions_test')

    failing_cases = [
        'Hero',
        'LostStudent',
        'BrotherJedd',
        'HuggingMom',
        'SweaterMerchant',
        'FoodVendor'
    ]
    # make sure test fails if base class is not defined
    try:
        if unit_tests.check_base_test.get_base(Hero()) not in failing_cases:
            hero = Hero()
            hero.set_col_coord(5)
            hero.set_row_coord(125)

            if  hero.get_col_coord() == 5 and\
                hero.get_row_coord() == 125 and\
                hasattr(Hero, 'print_position') and\
                callable(getattr(Hero, 'print_position')):
                print('pass')
                return True
            else:
                print('fail')
        else:
            print('fail')   

    except Exception as e:
        print('fail')
        print(e) 

    return False

        
if __name__ == '__main__':
    if test():
        sys.exit(0)
    else:
        sys.exit(1)

