"""This is the "main" module.

Draws Koch's snowflake according to user input
"""

import sys


def koch(a, order, instr=None):
    """Generate instructions for drawing one side of Koch's snowflake.

    :param a: Size of the side.
    :param order: Number of iterations for Koch's snowflake.
    :param instr: List of turtle instructions.
    :return: List of turtle instructions for drawing of Koch's snowflake.

    >>> koch(400, 0)
    [('forward', 400)]
    """
    if instr is None:
        instr = []

    if order > 0:
        for t in [60, -120, 60, 0]:
            koch(a / 3, order - 1, instr)
            instr.append(('left', t))
    else:
        instr.append(('forward', a))

    return instr


def getColor(num):
    """Return the name of a color based on the provided number.

    :param num: Number assigned to a specific color.
    :return: Name of the color.

    >>> getColor(5)
    'black'
    """
    match num:
        case 1:
            return "blue"
        case 2:
            return "red"
        case 3:
            return "green"
        case 4:
            return "yellow"
        case 5:
            return "black"
        case 6:
            return "white"


def drawSnowflake(iteration, line, background):
    """Set up snowflake parameters and draws Koch's snowflake.

    :param iteration: Number of iterations for Koch's snowflake.
    :param line: Color of the snowflake.
    :param background: Color of the background.
    """
    import turtle
    turtle.pencolor(getColor(line))
    turtle.bgcolor(getColor(background))
    turtle.fillcolor('white')
    turtle.width(2)
    size = 400

    # Centers snowflake
    turtle.penup()
    turtle.backward(size / 1.732)
    turtle.left(30)
    turtle.pendown()

    # Makes turtle run faster
    turtle.tracer(100)
    turtle.hideturtle()
    turtle.speed(0)
    turtle.begin_fill()

    # Three Koch curves
    for i in range(3):
        instructions = koch(size, iteration)
        for instr in instructions:
            if instr[0] == 'left':
                turtle.left(instr[1])  # Execute left turn
            elif instr[0] == 'forward':
                turtle.forward(instr[1])  # Execute forward movement
        turtle.right(120)

    turtle.end_fill()

    turtle.update()

    turtle.exitonclick()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        iteration = int(sys.argv[1])
        if iteration > 9:
            iteration = 9
        if iteration < 0:
            iteration = 0

        print("Choose line color:")
        print("Blue = 1")
        print("Red = 2")
        print("Green = 3")
        print("Yellow = 4")
        print("Black = 5")
        print("White = 6")
        line = int(input("Enter your choice: "))

        print("Choose background color:")
        print("Blue = 1")
        print("Red = 2")
        print("Green = 3")
        print("Yellow = 4")
        print("Black = 5")
        print("White = 6")
        background = int(input("Enter your choice: "))
    else:
        # Defalut configuration
        iteration = 4
        line = 6
        background = 1

    drawSnowflake(iteration, line, background)
