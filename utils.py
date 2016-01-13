#!/usr/bin/python2

"""
Contains the functions defination which are commonly used
"""
from math import sqrt


class Utils(object):
    @classmethod
    def check_prime(cls, num):
        for i in xrange(2, int(sqrt(num)) + 1, 1):
            if num % i == 0:
                return False
        return True

    @classmethod
    def reverse(cls, num):
        rev_num = 0
        while num:
            rev_num = 10 * rev_num + num % 10
            num /= 10
        return rev_num

    @classmethod
    def check_palindrom(cls, num):
        if num == Utils.reverse(num):
            return True
        return False

    @classmethod
    def prime_sieve(cls, limit):
        sieve = [True] * int(limit)
        sieve[0], sieve[1] = [None] * 2
        counter = 0
        for i, v in enumerate(sieve):
            if not v:
                continue
            sieve[i ** 2::i] = ([False] *
                                ((limit - 1) / i - (i - 1)))
            counter += 1
        # 1 is neither prime nor composite, 2 is prime
        sieve[0], sieve[1] = (False, False)
        return sieve
