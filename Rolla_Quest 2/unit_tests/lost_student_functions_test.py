#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from characters import LostStudent
import unit_tests.check_base_test

def test():
    print('\nlost_student_functions_test')

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
        if unit_tests.check_base_test.get_base(LostStudent()) not in failing_cases:
            lost_student = LostStudent()
            lost_student.set_col_coord(5)
            lost_student.set_row_coord(125)

            if  lost_student.get_col_coord() == 5 and\
                lost_student.get_row_coord() == 125 and\
                hasattr(LostStudent, 'print_position') and\
                callable(getattr(LostStudent, 'print_position')):
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

