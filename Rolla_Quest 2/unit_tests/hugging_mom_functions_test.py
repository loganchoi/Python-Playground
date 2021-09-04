#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from characters import  HuggingMom
import unit_tests.check_base_test

def test():
    print('\nhugging_mom_functions_test')

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
        if unit_tests.check_base_test.get_base(HuggingMom()) not in failing_cases:
            hugging_mom = HuggingMom()
            hugging_mom.set_col_coord(5)
            hugging_mom.set_row_coord(125)

            if  hugging_mom.get_col_coord() == 5 and\
                hugging_mom.get_row_coord() == 125 and\
                hasattr(HuggingMom, 'print_position') and\
                callable(getattr(HuggingMom, 'print_position')):
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

