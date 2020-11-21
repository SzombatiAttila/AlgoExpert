import unittest
from ValidateSubsequence import isValidSubsequence

from parameterized import parameterized


class TestSequence(unittest.TestCase):
    @parameterized.expand([
        [[5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]],
        [[5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10]],
        [[5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 6, -1, 8, 10]],
        [[5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 10]],
        [[5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 6, -1, 8, 10]],
    ])
    def test_sequence(self, array, sequence):
        try:
            self.assertTrue(isValidSubsequence(array, sequence))
        except AssertionError:
            print(array, sequence)
