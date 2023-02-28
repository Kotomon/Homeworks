"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List
from random import *


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    assert len(a) >= 0 and len(a) <= 1000
    assert len(a)==len(b) and len(a)==len(c) and len(a)==len(d)
    i,j,k,l,res=0,0,0,0,0
    res=int(0)
    while i < len(a):
        while j < len(a):
            while k<len(a):
                while l<len(a):
                    if a[i]+b[j]+c[k]+d[l]==0:
                        res += 1
                    l+=1
                k+=1
            j+=1
        i+=1
    return res


N = randrange(1, 1000)
a, b, c, d = [0] * N, [0] * N, [0] * N, [0] * N
for x in range(len(a)):
    a[x]= randrange(-100, 100)
    b[x]= randrange(-100, 100)
    c[x]= randrange(-100, 100)
    d[x]= randrange(-100, 100)
check_sum_of_four(a,b,c,d)