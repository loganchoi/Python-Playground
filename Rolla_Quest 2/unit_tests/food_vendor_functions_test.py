#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from characters import  FoodVendor
import unit_tests.check_base_test

def test():
    print('\nfood_vendor_functions_test')

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
        if unit_tests.check_base_test.get_base(FoodVendor()) not in failing_cases:
            food_vendor = FoodVendor()
            food_vendor.set_col_coord(5)
            food_vendor.set_row_coord(125)

            if  food_vendor.get_col_coord() == 5 and\
                food_vendor.get_row_coord() == 125 and\
                hasattr(FoodVendor, 'print_position') and\
                callable(getattr(FoodVendor, 'print_position')):
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

