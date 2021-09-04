#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from characters import BrotherJedd
import unit_tests.check_base_test

def test():
    print('\nbrother_jedd_functions_test')

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
        if unit_tests.check_base_test.get_base(BrotherJedd()) not in failing_cases:
            brother_jedd = BrotherJedd()
            brother_jedd.set_col_coord(5)
            brother_jedd.set_row_coord(125)

            if  brother_jedd.get_col_coord() == 5 and\
                brother_jedd.get_row_coord() == 125 and\
                hasattr(BrotherJedd, 'print_position') and\
                callable(getattr(BrotherJedd, 'print_position')):
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

