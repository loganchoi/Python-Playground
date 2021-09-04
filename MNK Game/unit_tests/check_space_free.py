import sys
sys.path.append("..")
import mnk_game

def test():
    print("space free test")
    passed = False
    board = [[" ",'O','X','X','X'],[" "," "," "," "," "],[" "," "," ",'O'," "],[" "," "," "," "," "]]
    try:
        # positive
        has_space = mnk_game.isSpaceFree(board, 1, 3)

        if has_space:
            passed = True
        else:
            passed = False

        # negative
        has_space = mnk_game.isSpaceFree(board, 0, 3)

        if passed and has_space == False:
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
