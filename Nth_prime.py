#!/bin/bash/python
# encoding: utf-8

import sys
import math

def find_Nth_prime(n):
    if isinstance(n, str):
        n = int(n)
    # n >= 1
    primes = [2]
    curt = 2
    while len(primes) < n:
        # todo
        curt += 1
        prime = True
        for i in xrange(2, int(math.sqrt(curt)) + 1):
            if curt % i == 0:
                prime = False
                break
        if prime:
            primes.append(curt)
        #print primes
    return primes[-1]

print "the {0}th prime is: {1}".format(sys.argv[1], find_Nth_prime(sys.argv[1]))
