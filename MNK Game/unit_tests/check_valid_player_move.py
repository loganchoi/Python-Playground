import sys
sys.path.append("..")
import mnk_game

def test():
    print("valid player move test")
    board = [[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "]]
    try:
        mnk_game.getPlayerMove(board, 4, 5)

    except:
        return False

if __name__ == "__main__":
    test()
