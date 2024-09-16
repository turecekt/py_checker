"""Module (file) docstring."""
import turtle  # Importing the turtle module to use graphics.


def turn_line(a):
    """Drawing Dragon curve."""
    for j in range(len(a)):
        if a[j] == 'r':
            turtle.right(90)
            turtle.forward(10)
        if a[j] == 'l':
            turtle.left(90)
            turtle.forward(10)


def input_data(value, default):
    """Input bg and pen cl."""
    if value == '':
        return default
    else:
        return value


def sides(itr_):
    """Miscalculation of turns."""
    old = 'r'
    new = old

    for i in range(1, itr_, 1):
        new = old + 'r'
        old = old[::-1]
        for j in range(0, len(old)):
            if old[j] == 'r':
                old = old[:j] + 'l' + old[j + 1:]
            else:
                old = (old[:j]) + 'r' + (old[j + 1:])
        new += old
        old = new
    return new


if __name__ == '__main__':
    turtle.bgcolor(input_data(input('Enter background color:'), 'black'))
    turtle.color(input_data(input('Enter pen color:'), 'red'))
    itr = int(input_data(input('Enter the number of iterations:'), 9))
    q = sides(itr)
    turtle.ht()
    turtle.speed(0)
    turn_line(q)
    turtle.done()
