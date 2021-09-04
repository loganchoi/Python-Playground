#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
import rolla_quest
from characters import SweaterMerchant
import unit_tests.check_base_test

def test():
    print('\nsweater_merchant_functions_test')

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
        if unit_tests.check_base_test.get_base(SweaterMerchant()) not in failing_cases:
            sweater_merchant = SweaterMerchant()
            sweater_merchant.set_col_coord(5)
            sweater_merchant.set_row_coord(125)

            if  sweater_merchant.get_col_coord() == 5 and\
                sweater_merchant.get_row_coord() == 125 and\
                hasattr(SweaterMerchant, 'print_position') and\
                callable(getattr(SweaterMerchant, 'print_position')):
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

