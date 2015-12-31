#!/usr/bin/python2

"""
he prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from unittest import TestCase, main
from utils import Utils


class Problem3(object):
    def __init__(self, bound):
        self._bonud = bound

    def run(self):
        for i in xrange(int(self._bound / 2), 0, -1):
            if self._bound % i == 0 and Utils.check_prime(i):
                return i

