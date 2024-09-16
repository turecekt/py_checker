"""Project for AK1VS.

Author: Matúš Juhasz.
"""

import re
import sys
from argparse import ArgumentParser
from operator import itemgetter


def arguments():
    """
    Parse argument from std-in or as parameters.

    Use argparse library.
    Args:
        - input - Input file
    Without parameter it read from std-in else from input files
    Returns:
        all parsed arguments.
    """
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest="filename", action="store",
                        help="Type input FILE", metavar="FILE")

    arg_len = len(sys.argv)
    if arg_len == 1:
        result = sys.stdin.read()
        return read_file(result, arg_len)
    else:
        args = parser.parse_args().filename
        return read_file(args, arg_len)


def read_file(input_file, arg_len):
    """
    Read all characters to specific char.

    Returns:
         data = string which will be working next.
    """
    if arg_len != 1:
        with open(input_file, "rt") as f:
            text = f.read()
            data = text.split('#', 1)[0]
    else:
        data = input_file.split('#', 1)[0]

    return data


def number_char(file_data):
    """Return length of given string.

    Returns:
        number_char = number of characters in string
    """
    num_char = len(file_data)

    return num_char


def number_occurence(file_data):
    """Create list of occurrence without unwanted chars.

    Returns:
        my_list = list of all characters
    """
    my_list = []
    file_data = file_data.lower()
    for char in file_data:
        if re.match('^[a-z]+$', char):
            count = len(re.findall(char, file_data))
            if not tuple((char, count)) in my_list:
                my_list.append(tuple((char, count)))

    return my_list


def all_occurence(list):
    """Find frequency of each char in string.

    Returns:
        return all occurence of char
    """
    string = "Znak \" {} \" sa v texte nachadza : \" {} \"krat\n"
    final_string = ""
    for x in list:
        final_string += string.format(x[0], x[1])

    return final_string


def max_occurence(list):
    """Find max occurence.

    Returns:
        max occurence of char
    """
    string = "Najcastejsie sa vyskutuje znak: \"{}\" a pocet vyskytov je: {}"\
        .format(max(list, key=itemgetter(1))[0],
                max(list, key=itemgetter(1))[1])

    return string


def min_occurence(list):
    """Find min occurence.

    Returns:
        min occurence of char
    """
    string = "Najmenej sa vyskutuje znak: \"{}\" a pocet vyskytov je: {}"\
        .format(min(list, key=itemgetter(1))[0],
                min(list, key=itemgetter(1))[1])

    return string


def art_freq(list):
    """Count frequency of characters.

    Returns:
        frequency of characters
    """
    number = 0
    for x in list:
        number += x[1]

    return number/len(list)


def main():
    """Execute all."""
    file_data = arguments()
    number_char(file_data)
    print("Celkovy pocet znakov je: ", number_char(file_data))
    print(max_occurence(number_occurence(file_data.replace(" ", ""))))
    print(min_occurence(number_occurence(file_data.replace(" ", ""))))
    print(all_occurence(number_occurence(file_data.replace(" ", ""))))
    print("Cetnost znakov je: ", art_freq(number_occurence(file_data)))


if __name__ == '__main__':
    main()
