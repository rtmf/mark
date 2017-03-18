#!/usr/bin/env python3
import random
a = [1, 2, 3, 5, 10, 50, 100, 1000]
def bsearch(a, v, lo, hi):
    mid = (lo+hi)//2
    if a[mid] == v: return mid
    if lo == hi:
        return mid if a[mid] > v else None
    if hi - lo == 1:
        if a[mid] < v and a[hi] > v:
            return hi
    return bsearch(a, v, lo if v<a[mid] else mid+1, mid-1 if v<a[mid] else hi)

for v in a:
    answer = bsearch(a, v, 0, len(a)-1)
    print('search=', v, 'index=', answer, 'value=', a[answer], 'good' if a[answer] == v else 'bad')
    v -= 0.5
    print('search=', v, 'index=', answer, 'value=', a[answer], 'good' if a[answer] == v else 'bad')
