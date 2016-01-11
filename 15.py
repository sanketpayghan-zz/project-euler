#!/usr/bin/python2


"""
Statement:

Starting in the top left corner of a 2x2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""


from unittest import TestCase, main


class Problem15(object):
    def __init__(self, limit):
        self._limit = limit

    def fn(self):
        matrix = [[1 for j in xrange(self._limit + 1)] for i in xrange(self._limit + 1)]
        for i in xrange(1, self._limit + 1, 1):
            for j in xrange(1, self._limit + 1, 1):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        return matrix[self._limit][self._limit]


class TestProblem15(TestCase):
    def setUp(self):
        self.limit = 20
        self.answer = 137846528820
        # self.limit = 2
        # self.answer = 6

    def test_fn(self):
        self.assertEqual(Problem15(self.limit).fn(), self.answer)


if __name__ == '__main__':
    main()
