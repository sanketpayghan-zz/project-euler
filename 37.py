#!/usr/bin/python2


"""
Statement:

The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from unittest import TestCase, main
# from utils import check_prime, reverse
from utils import Utils


class Problem37(object):
    def __init__(self):
        self._primes = []

    def truncatable_prime(self, num):
        tmp = num / 10
        mf = 1
        while tmp:
            if not self._primes[tmp]:
                return False
            tmp /= 10
            mf *= 10
        tmp = num % mf
        while tmp:
            if not self._primes[tmp]:
                return False
            mf /= 10
            tmp %= mf
        return True

    def fn(self):
        total = 0
        self._primes = Utils.prime_sieve(1000000)
        for i, v in enumerate(self._primes):
            if i < 10:
                continue
            if v and self.truncatable_prime(i):
                total += i
        return total


class TestProblem37(TestCase):
    def setUp(self):
        self.answer = 748317

    def test_fn(self):
        self.assertEqual(Problem37().fn(), self.answer)


if __name__ == '__main__':
    main()
