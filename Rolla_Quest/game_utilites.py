# -*- coding: utf-8 -*-


class Utilites:
    def __init__(self):
        super().__init__()

    def get_cs_floor_map(self, file_path):
        grid = []
        with open(file_path, 'r') as fin:
            rows = fin.read().split('\n')
            grid_cols = []
            grid_rows = []

            size = int(len(rows[0])/3)
            num_cols = int(len(rows[0])/size)

            # iterate through the lines of a file and
            # add the first size characters to a list
            # the grid will be sizexsize
            for row in rows:
                for i in range(0, num_cols):
                    if len(row[i*size]) < len(row[i*size: (i+1)*size]):
                        segment = row[i*size: (i+1)*size]
                    else:
                        segment = row[i*size:]

                    grid_cols.append(segment)

                grid_rows.append(grid_cols)
                grid_cols = []  # clear list

            # # remove useless data
            if [] in grid_rows:
                grid_rows.remove([])

            for k in range(4):
                row = grid_rows[k*40: (k+1)*40]
                for i in range(num_cols):
                    sec = ''
                    for e in row:
                        sec += e[i] + '\n'
                    grid_cols.append(sec)

                if grid_cols != []:
                    grid.append(grid_cols)
                    grid_cols = []  # clear list

            return grid

    def get_campus_map(self, file_path):
        '''
        func:   get_campus_map()
        desc:   A function that parses a 40x800 text file and returns a 2D array
                that contains 40x80 chunks of the map. Rows are seperated by newline
                characters '\\n'. [0][0] is top left portion of map
                while [9][9] is the bottom right.
        param:  file_path -> str
        ret :   [][]
        '''
        grid = []
        with open(file_path, 'r') as fin:
            rows = fin.read().split('\n')
            grid_cols = []
            grid_rows = []

            num_cols = int(len(rows[0])/75)
            # iterate through the lines of a file and
            # add the first 80 characters to a list
            # the grid will be 40x80
            for row in rows:
                for i in range(num_cols):
                    segment = row[i*75:(i+1)*75]
                    grid_cols.append(segment)

                grid_rows.append(grid_cols)
                grid_cols = []  # clear list

            # # remove useless data
            if [] in grid_rows:
                grid_rows.remove([])

            for k in range(4):
                row = grid_rows[k*40: (k+1)*40]
                for i in range(num_cols):
                    sec = ''
                    for e in row:
                        sec += e[i] + '\n'
                    grid_cols.append(sec)

                if grid_cols != []:
                    grid.append(grid_cols)
                    grid_cols = [] # clear list

            return grid


def getch():
    try:
        import sys
        import tty
        import termios
    except ImportError:
        # but I think mscvrt implements getch
        raise ImportError('You\'re on Windows, aren\'t you?')
    stdin_fd = sys.stdin.fileno()  # We know this is a tty
    old_cfg = termios.tcgetattr(stdin_fd)  # save off the current config
    try:
        tty.setraw(stdin_fd)
        char = sys.stdin.read(1)
        if ord(char) == 3:  # Catch the Ctrl-C
            # Maybe a "goodbye" message here??
            sys.exit(0)
        return char
    finally:
        # Reset the terminal once we receive the Ctrl-C
        termios.tcsetattr(stdin_fd, termios.TCSADRAIN, old_cfg)


if __name__ == "__main__":
    utils = Utilites()
    campus = utils.get_cs_floor_map('maps/cs_second_floor.txt')

    for i in range(len(campus)):
        for j in range(len(campus[0])):
            print(campus[i][j])

