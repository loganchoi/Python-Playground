import sys
import maze
import os
import importlib

def test():
    print("\nfill_matrix test")

    # remove old module from path
    # import new maze module from student repo
    sys.modules.pop('maze')
    maze = importlib.import_module('maze')

    rows = 14
    matrix = []

    orig_stdin = sys.stdin

    try:
        sys.stdin = open("unit_test_fstream_readin.txt", 'r')
        maze.fill_matrix(matrix, rows)

        sys.stdin = orig_stdin
        if matrix[5][12] == '|' and matrix[13][49] == 'E' and matrix[11][19] == 'N':
            print('pass')
            return True
        else:
            print('fail')
            return False
    except:
        sys.stdin = orig_stdin
        print('fail')
        return False


if __name__ == "__main__":
    test()
