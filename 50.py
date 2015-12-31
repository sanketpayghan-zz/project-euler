#!/usr/bin/python2

"""
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

from unittest import TestCase, main
from utils import Utils


class Problem50(object):
    def __init__(self, bound):
        self._bound = bound

    def run(self):
        p_list = []
        c_sum = 0
        p_num = 1
        while c_sum + p_num < self._bound:
            if Utils.check_prime(p_num):
                c_sum += p_num
                p_list.append(p_num)
            p_num += 1
        while not Utils.check_prime(c_sum):
            c_sum -= p_list.pop(0)
        return c_sum


class TestProblem50(TestCase):
    def setUp(self):
        self.bound = 1000000
        self.answer = 997651

    def test_run(self):
        self.assertEqual(Problem50(self.bound).run(), self.answer)


if __name__ == '__main__':
    main()
