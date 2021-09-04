import sys
sys.path.append("..")
import mnk_game

def test():
    print("check player letter test")
    passed = False
    try:
        letters_match = ["X", "O"] == mnk_game.inputPlayerLetter()

        if letters_match:
            passed = True
        else:
            passed = False
        
        letters_match = ["O", "X"] == mnk_game.inputPlayerLetter()

        if passed and letters_match:
            passed = True
        else:
            passed = False
        
        if passed:
            print('pass')
        else:
            print('fail')

        return passed

    except:
        return False


if __name__ == "__main__":
    if test():
        sys.exit(0)
    else:
        sys.exit(1)
