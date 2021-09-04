import sys
sys.path.append("..")
import mnk_game

def test():
    print("draw board test")
    board = [[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "]]
    try:
        # positive
        mnk_game.drawBoard(board, 4, 5)

    except:
        print('fail')
        return False


if __name__ == "__main__":
    test()
