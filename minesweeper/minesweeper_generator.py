import numpy

# global constant for empty field in the playground
EMPTY = " "
# global constant for mine in the playground
MINE = "*"


# class which represents minesweeper structure
class Minesweeper:
    def __init__(self, rows, cols, count_of_mines):
        # count of rows of the playground, +2 means # for each side of the playground
        self.rows = rows + 2
        # count of cols of the playground, +2 means # for each side of the playground
        self.cols = cols + 2
        # count of mines which should be in the playground
        self.count_of_mines = count_of_mines
        # playground which is full of #
        self.playground = [["#"] * self.cols for row in range(self.rows)]
        # full playground with EMPTY constant, from 1 to rows/cols - 1, which means borders of the playground
        for i in range(1, self.rows - 1):
            for j in range(1, self.cols - 1):
                self.playground[i][j] = EMPTY


def create_array_with_mines(rows, cols, count_of_mines):
    """
        input:  rows
                cols
                count of mines
        output: array with bombs on random indices
        * represents mine
    """
    array = []
    array_len = rows * cols
    for i in range(0, array_len):
        if count_of_mines == 0:
            array.append(EMPTY)
        else:
            array.append(MINE)
            count_of_mines -= 1
    numpy.random.shuffle(array)
    bombs_array = numpy.reshape(array, (rows, cols))
    return bombs_array
