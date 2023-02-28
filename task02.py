"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence

def check_fibonacci(data: Sequence[int]) -> bool:
    assert len(data) > 2
    i = 3
    while i <= len(data):
        if data[i-1] !=1 and data[i-1] != 2 and data[i-1] != 3 and data[i-1] != 5 and round(float(data[i-1]/data[i-2]),1) != float(1.6):
            return False
        if data[i-2] + data[i-3] != data[i-1]:
            return False
        i += 1
    return True

check_fibonacci([0,1,1])