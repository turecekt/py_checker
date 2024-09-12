"""Project: AK1VS - Final project."""

##########################################################################
# Description: This project should show how to work with versioning tool such
#              as git.
# Task: Character rate
#       - Input:    text file as parameter
#                   StdIn in case of no parameter (reading upon '#')
#       - Output:   character count
#                   most frequent character
#                   least frequent character
#                   average occurence of character
#                   frequency of each alphabetic character
#############################################################################
# UTB Zlin - FAI 2020
# Author: Adam Huspenina

import sys
import argparse
import statistics


class CharacterFrequency:
    """Class contains whole functionality for completing desired tasks."""

    def __init__(self, intput):
        """Initialize class properties."""
        self.input = intput
        self.char_dict = self._init_dictionary()

    def get_most_frequent(self):
        """Return touple of most frequent character list.

        *Returns list because of equalities.
        """
        max_value = max(self.char_dict.values())
        max_keys = []
        for k, v in self.char_dict.items():
            if v == max_value:
                max_keys.append(k)
        return (max_keys, max_value)

    def get_least_frequent(self):
        """Return touple of least frequent character list.

        *Returns list because of equalities.
        """
        min_value = min(self.char_dict.values())
        min_keys = []
        for k, v in self.char_dict.items():
            if v == min_value:
                min_keys.append(k)
        return (min_keys, min_value)

    def get_average(self):
        """Return touple of average occurence of character list.

        *Returns list because of equalities).
        """
        avg_value = statistics.mean(self.char_dict.values())
        rounded_value = round(avg_value)
        avg_keys = []
        for k, v in self.char_dict.items():
            if v == rounded_value:
                avg_keys.append(k)
        return (avg_value, avg_keys)

    def get_alpha_frequency(self):
        """Return alphabetic characters with their occurence rate."""
        alpha_dict = {}
        for k, v in self.char_dict.items():
            if k.isalpha():
                alpha_dict[k] = v
        return alpha_dict

    def output(self, output_list):
        """Print given touples with analyzed results."""
        print(str(output_list))

    def _init_dictionary(self):
        """Private method.

        Read input data and store them into dictionary.

        For stdin dictionary contains only characters until '#' is read.
        'DEBUG' option is for testing purposes, when tester can easily handle
        input. It can be only reached through code.

        Tester has to define self.char_dict by him self.
        """
        character_dict = {}
        if (self.input != 'DEBUG'):
            if (self.input == '<stdin>'):
                while True:
                    char = sys.stdin.read(1)
                    if (char == '#'):
                        break
                    dict_keys = character_dict.keys()
                    if (char in dict_keys):
                        character_dict[char] += 1
                    else:
                        character_dict[char] = 1
            else:
                file_input = open(self.input, 'r')
                while True:
                    char = file_input.read(1)
                    if (char == ''):
                        break
                    dict_keys = character_dict.keys()
                    if (char in dict_keys):
                        character_dict[char] += 1
                    else:
                        character_dict[char] = 1
            file_input.close()
        return character_dict


def parse_args():
    """Outter method for parsing input arguments from terminal."""
    parser = argparse.ArgumentParser(
        description="Get information about character frequency form input.")
    parser.add_argument("-i", nargs='?',
                        help="File containing characters to be analyzed.",
                        type=argparse.FileType('r'), default=sys.stdin)
    args = parser.parse_args()
    return args


def main(args):
    """Driving method for whole program."""
    characters = CharacterFrequency(args.i.name)
    # Print most frequent value with corresponding characters.
    characters.output(characters.get_most_frequent())
    # Print least frequent value with corresponding characters.
    characters.output(characters.get_least_frequent())
    # Print average rate value with characters having rounded average rate.
    characters.output(characters.get_average())
    # Print alphabetic characters rate.
    characters.output(characters.get_alpha_frequency())


if __name__ == "__main__":
    args = parse_args()
    main(args)
