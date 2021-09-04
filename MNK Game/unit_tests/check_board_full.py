import sys
sys.path.append("..")
import mnk_game

def test():
    print("board full test")
    passed = False
    board_positive = [['O','O','X','X','X'],['O','O','X','X','X'],['O','O','X','X','X'],['O','O','X','X','X']]
    board_negative = [['O','O','X'," ",'X'],['O','O','X','X','X'],['O','O','X','X','X'],['O','O','X','X','X']]
    try:
        # positive
        is_board_full = mnk_game.isBoardFull(board_positive, 4, 5)

        if is_board_full:
            passed = True
        else:
            passed = False

        # negative
        is_board_full = mnk_game.isBoardFull(board_negative, 4, 5)

        if passed and is_board_full == False:
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
