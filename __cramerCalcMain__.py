"""This module is wrapper for running calculation of matrixes.

you should tun it with file specified
"""

# import file with methodss for matri operation
from __cramerLib__ import convertToMatrixAndVector
from __cramerLib__ import replaceWithRightSides
from __cramerLib__ import determinantCalculation
# import sys for handling of arguments
import sys


"""This method wraps all the code."""


def main(file=0):
    """Functon main calculates determinant of given matrix.

    >>> main("matrixTest.txt")
    0
    >>> main("KolalokaTest.csv")
    1
    >>> main()
    1

    This method is run automatically after script is opened
    Args:

    Returns:
        - 0 on scucess, 1 on failure
    """
    if(sys.argv[1] == 'help'):
        print("-Welcome to 3x3 matrix variables calculation script\n script re\
        turns value of variables x y z of matrix epanded by vector of right \
        sides containing results of equations")
        print("-Script is run by running python __cramerCalcMain__.py with spe\
        cification of file containing matrix to be solved with space used as d\
        elimiter between columns.")
        print("-Matrix must be of 3x3 with column with results of equations, \
        thus in format:")
        print("\t k1x l1y m1z R1")
        print("\t k2x l2y m2z R2")
        print("\t k3x l3y m3z R3")

        sys.exit(0)

    # open file
    if file == 0:
        try:
            FILE = open(sys.argv[1])
        except IOError:
            # print("File "+sys.argv[1]+' not found on this machine')
            return 1
    else:
        try:
            FILE = open(file)
        except IOError:
            # print("File "+file+' not found on this machine')
            return 1

    lines = []
    # convert file to array of strings where string is one line.
    for line in FILE:
        lines.append(line)

    # variables used in code to
    matrix = []
    vector = []

    # run conversion of file to matrix
    convertToMatrixAndVector(lines, matrix, vector)

    # determinant of matrix without altered columns
    determinantOfMatrix = determinantCalculation(matrix)

    if determinantOfMatrix == 0:
        print("determinant of matrix is ZERO! Can't calcualte value of \
        variables")
        # sys.exit(1)

    # array of results
    results = {}

    # calculation of
    deterX = determinantCalculation(replaceWithRightSides(matrix, vector, 0))
    deterY = determinantCalculation(replaceWithRightSides(matrix, vector, 1))
    deterZ = determinantCalculation(replaceWithRightSides(matrix, vector, 2))
    results["x"] = deterX / determinantOfMatrix
    results["y"] = deterY / determinantOfMatrix
    results["z"] = deterZ / determinantOfMatrix

    # print results of calculation
    # print("Results form matrix:")
    # print(str(matrix[0])+"\t"+str(matrix[1])+"\t"+str(matrix[2]))
    # print(str(matrix[3])+"\t"+str(matrix[4])+"\t"+str(matrix[5]))
    # print(str(matrix[6])+"\t"+str(matrix[7])+"\t"+str(matrix[8]))
    # print("And vector: "+str(vector[0])+" "+str(vector[1])+"\
    # "+str(vector[2]))
    # print("Are:")
    # print("x: "+str(results["x"]))
    # print("y: "+str(results["y"]))
    # print("z: "+str(results["z"]))
    return 0


# if __name__ == "__main__":
#    main()
