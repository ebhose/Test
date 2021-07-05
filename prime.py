#!/usr/bin/env python3

import math


def is_prime(num):

    for divisor in range(2, int(math.sqrt(num) + 1)):
        if num % divisor == 0:
            return False
    return True


