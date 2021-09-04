#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
import rolla_quest
from characters import Hero, LostStudent, BrotherJedd, HuggingMom, SweaterMerchant, FoodVendor, Character


def get_base(character):
    # print(str(character.__class__.__bases__).split('.')[1].split('\'')[0])
    return str(character.__class__.__bases__).split('.')[1].split('\'')[0]

def test():
    print('\ncheck_base_test')

    try:
        # check if there are base classes for
        # Hero()
        # LostStudent()
        # BrotherJedd()
        # HuggingMom()
        # SweaterMerchant()
        # FoodVendor()
        
        failing_cases = [
            'Hero',
            'LostStudent',
            'BrotherJedd',
            'HuggingMom',
            'SweaterMerchant',
            'FoodVendor'
        ]
        
        hero = get_base(Hero())
        lost_student = get_base(LostStudent())
        brother_jedd = get_base(BrotherJedd())
        hugging_mom = get_base(HuggingMom())
        sweater_merchant = get_base(SweaterMerchant())
        food_vendor = get_base(FoodVendor())

        if  hero not in failing_cases and\
            lost_student not in failing_cases and\
            brother_jedd not in failing_cases and\
            hugging_mom not in failing_cases and\
            sweater_merchant not in failing_cases and\
            food_vendor not in failing_cases:
            print('pass')
            return True
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

