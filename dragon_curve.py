"""DragonCurve1.1.py.

This code is used for printing dragon curve in 2 ways
in L-system and in system of iterated functions.
"""

import turtle

r = 'r'  # make variables for the right and left containg 'r' and 'l'
L = 'l'


def functioncycle(iteration):
    """Print iterations."""
    old = r  # assign first iteration a right so we can build off of it
    new = old
    cycle = 1
    while cycle < iteration:
        # keep on generating next iteration until desired iteration is reached
        new = old + r  # add a right to the end of the old iteration
        old = old[::-1]     # flip the old iteration around
        #  cycling through each character in the flipped old iteration:
        for char in range(0, len(old)):

            if old[char] == r:
                # if the character is a right:

                old = old[:char] + L + old[char+1:]  # change it to a left

            elif old[char] == L:  # otherwise, if it's a left:

                old = old[:char] + r + old[char+1:]    # change it to a right
        new = new + old  # add the modified old to the new iteration

        old = new  # save the new iteration to old as well for use next cycle
        cycle = cycle+1
    return new


def functionprinttantsrlrl(printans, new):
    """Print rl form of dragon curve."""
    if printans == 'y':
        return new
    else:
        return ""


if __name__ == '__main__':
    iteration, length, pencolor, backgroundcolor, printans = (
        int(input('Zadajte pocet iterácii:') or 9),  # input of pen color
        int(input('Zadajte dĺžku každého segmentu:') or 10),
        str(input('Zadajte farbu pera:') or 'red'),
        str(input('Zadajte farbu pozadia:') or 'black'),  # and bg color
        input('Display r/l form?(y/n):')
    )

    new = functioncycle(iteration)
    print(functionprinttantsrlrl(printans, new))

    turtle.ht()  # do not show the turtle icon when drawing
    turtle.speed(22)  # set drawing speed to fastest(no animation)
    turtle.pencolor(pencolor)  # set pen color as requested
    turtle.bgcolor(backgroundcolor)  # set background color as requested

    # turtle.forward(length)
    # display segment of desired length to build off of

    for char in range(0, len(new)):

        if new[char] == r:  # if the character is a right:

            turtle.right(90)  # turn right at a right angle

            turtle.forward(length)  # go forward desired length

        elif new[char] == L:  # otherwise, if the character is a left:

            turtle.left(90)  # turn left at a right angle

            turtle.forward(length)  # go forward desired length

    turtle.done()
