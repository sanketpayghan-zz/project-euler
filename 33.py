#!/usr/bin/python2


"""
Statement:

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
"""

from unittest import TestCase, main


class Problem33(object):
    def __init__(self, limit):
        self._limit = limit

    def fn(self):
        denominator = 1
        numerator = 1
        for num in xrange(11, self._limit):
            for den in xrange(num + 1, self._limit):
                if num % 10 == 0 or den % 10 == 0:
                    continue
                num_list = [s for s in str(num)]
                den_list = [s for s in str(den)]
                for s in num_list:
                    if s in den_list:
                        num_list.remove(s)
                        den_list.remove(s)
                        if (float(num_list[0]) / float(den_list[0]) == float(num) / float(den)):
                            denominator *= int(den_list[0])
                            numerator *= int(num_list[0])
        return denominator / numerator


class TestProblem33(TestCase):
    def setUp(self):
        self.bound = 100
        self.answer = 100

    def test_fn(self):
        self.assertEqual(Problem33(self.bound).fn(), self.answer)


if __name__ == '__main__':
    main()
