#!/usr/bin/python3
"""Python script to find peak"""


def find_peak(lst):
    """funtion that takes a list of integers and finds the peak"""
    n = len(lst)
    if n == 0:
        return None
    while (n > 2):
        m = len(lst) // 2
        r = m + 1
        left = m - 1

        if (lst[m] > lst[left]) and (lst[m] > lst[r]):
            return lst[m]
        elif lst[left] >= lst[r]:
            lst = lst[:r]
        elif lst[r] > lst[left]:
            lst = lst[m:]
        n = len(lst)
    return max(lst)
