import unittest
import sys

# the array is sorted already
def chop_rec(n, array):
    def chop_rec_inter(n, array, start, end):
        if end < start:
            return -1
        mid = start + ((end - start) / 2)
        val = array[mid]
        if val > n:
            return chop_rec_inter(n, array, start, end-1)
        elif val < n:
            return chop_rec_inter(n, array, start+1, end)
        else:
            return mid

    return chop_rec_inter(n, array, 0, len(array) - 1)

def chop_iterative(n, array):
    
    start, end = 0, (len(array) - 1)
    while True:
        if start > end:
            return -1

        mid = start + ((end - start) / 2)
        el = array[mid]
        if n == el:
            return mid
        elif n < el:
            end -= 1
        else:
            start += 1


