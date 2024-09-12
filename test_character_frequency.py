"""Project: AK1VS - Final project (testing part)."""

#############################################################################
# Project: AK1VS - Final project
# Description: This project should show how to work with versioning tool such
#              as git.
# Task: Create unittests for chosen project.
#############################################################################
# UTB Zlin - FAI 2020
# Author: Adam Huspenina

from character_frequency import CharacterFrequency
import unittest


class TestCharacterFrequency(unittest.TestCase):
    """Testcase class for character frequency analyzer."""

    @classmethod
    def setUpClass(cls):
        """Execute only once at the begining of testcase."""
        cls.chars = CharacterFrequency("DEBUG")
        cls.test_dict = {'a': 42, 'b': 18, 'c': 6, '&': 1}

    @classmethod
    def tearDownClass(cls):
        """Execute at the end."""
        pass

    def setUp(self):
        """Execute before every test-case."""
        self.chars.char_dict = self.test_dict
        pass

    def tearDown(self):
        """Execute after every test-case."""
        pass

    # @unittest.skip('Intentionally skipped for development purposes.')
    def test_most_frequency(self):
        """Tests if most frequent character could be found."""
        self.chars.char_dict['X'] = 100
        result = self.chars.get_most_frequent()
        self.assertEqual(result[1], 100)

    # @unittest.skip('Intentionally skipped for development purposes.')
    def test_least_frequency(self):
        """Tests if least frequent character could be found."""
        self.chars.char_dict['X'] = 1
        result = self.chars.get_least_frequent()
        self.assertEqual(result[1], 1)

    # @unittest.skip('Intentionally skipped for development purposes.')
    def test_average_frequency(self):
        """Tests if character with average rate could be found."""
        self.chars.char_dict['X'] = 13
        result = self.chars.get_average()
        self.assertEqual(result[0], 15.5)

    # @unittest.skip('Intentionally skipped for development purposes.')
    def test_alphabetic_frequency(self):
        """Tests if alphabetic characters with rate could be filtered."""
        self.chars.char_dict['!'] = 13
        result = self.chars.get_alpha_frequency()
        for key in list(result.keys()):
            self.assertTrue(key.isalpha())


if __name__ == '__main__':
    unittest.main()
