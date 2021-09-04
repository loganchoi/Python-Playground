import sys
sys.path.append("..")
import mnk_game

def test():
    print("check across test")
    passed = False
    board_positive = [[" ",'O','X','X','X'],[" "," "," "," "," "],[" "," "," ",'O'," "],[" "," "," "," "," "]]
    board_negative = [[" "," ",'O','X','X'],[" "," "," "," "," "],[" "," "," ",'O'," "],[" "," "," "," "," "]]
    try:
        # positive
        match_found = mnk_game.checkAcross(board_positive, 'X', 4, 5, 3, 0, 2)

        if match_found:
            passed = True
        else:
            passed = False

        # negative
        match_found = mnk_game.checkAcross(board_negative, 'X', 4, 5, 3, 0, 3)

        if passed and match_found == False:
            passed = True
        else:
            passed = False

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
