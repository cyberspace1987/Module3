"""
Program: test_average_scores.py
Author: Cara Krug
Last date modified: 09/13/2020

Write the tests and program average_scores.py to read in one person's names, first and last, their age and three scores out of 100.
Take the three scores and find the average, storing into a variable.
"""
import unittest
import unittest.mock as mock
from formatoutput import average_scores


def test_average(self):
    with mock.patch('builtins.input', side_effect=[85, 90, 95]):
        assert average_scores.average() == 90


if __name__ == '__main__':
    unittest.main()
