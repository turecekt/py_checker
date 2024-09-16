"""Project for AK1VS.

Author: Matúš Juhasz.
"""

import unittest

import main


class Test(unittest.TestCase):
    """Testing class for methods."""

    def setUp(self):
        """Set variables for testing."""
        self.s = "Lorem Ipsum is simply dummy text of " \
                 "the printing and typesetting industry"
        self.mylist = [('l', 1), ('o', 1), ('r', 1)]

    def test_read_file(self):
        """Test for read_file method."""
        self.assertEqual(main.read_file(arg_len=1,
                                        input_file="Lorem Ipsum is simply "
                                                   "dummy text of"
                                                   " the printing "
                                                   "and typesetting "
                                                   "industry"),
                         self.s)
        self.assertNotEqual(main.read_file(arg_len=1,
                                           input_file="AHoj"), self.s)

    def test_number_char(self):
        """Test if method return correct lenght of word."""
        self.assertEqual(73, main.number_char(self.s))

    def test_number_occurence(self):
        """Testing method for correct number of occurrence.

        #1 Test if method create correct List.
        #2 Test if all word are lower case.
        #3 Test for ignoring characters with accents.
        #4 Test for ignoring characters with accents.
        """
        self.assertNotEqual(self.mylist, main.number_occurence("Example"))
        self.assertEqual(self.mylist, main.number_occurence("Lor"))
        self.assertEqual([('l', 1)], main.number_occurence("L"))
        self.assertEqual([], main.number_occurence("žáš"))
        self.assertEqual([], main.number_occurence("9_+"))

    def test_all_occurence(self):
        """Test for final output."""
        a = main.all_occurence([('l', 1)])
        b = "Znak \" l \" sa v texte nachadza : \" 1 \"krat\n"
        self.assertEqual(a, b)

    def test_max_occurence(self):
        """Test for max occurence."""
        self.assertEqual("Najcastejsie sa vyskutuje znak: \"""l" "\""
                         " a pocet vyskytov je: 1",
                         main.max_occurence([('l', 1)]))

    def test_min_occurence(self):
        """Test for min."""
        self.assertEqual("Najmenej sa vyskutuje znak: \"""l" "\""
                         " a pocet vyskytov je: 1",
                         main.min_occurence([('l', 1)]))

    def test_art_freq(self):
        """Test for frequency."""
        self.assertEqual(1.0, main.art_freq(self.mylist))
        self.assertNotEqual(4.0, main.art_freq(self.mylist))


if __name__ == "__main__":
    unittest.main()
