# Actually a test of getEmptySpaces, which random moves depends on...

import sys
sys.path.append("..")
import mnk_game

def test():
    print("check valid random moves test")
    passed = False
    board = [['O','O','X'," "," "],['X','X'," ",'O','O'],[" ",'X','X','O','O'],['O','X'," ",'O'," "]]
    actual_result = [[0, 3], [0, 4], [1, 2], [2, 0], [3, 2], [3, 4]]
    try:
        # positive
        function_result = (mnk_game.getEmptySpaces(board, 4, 5))

        passed = actual_result == function_result
        
        if passed:
            print('pass')
        else:
            print('fail')

        return passed

    except:
        print('fail')
        return False


if __name__ == "__main__":
    if test():
        sys.exit(0)
    else:
        sys.exit(1)
