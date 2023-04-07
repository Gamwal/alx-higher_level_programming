#!/usr/bin/python3
"""Python script to find peak"""


def find_peak(lst):
    """funtion that takes a list of integers and finds the peak"""
    n = len(lst)
    if n == 0:
        return None
    elif n == 1:
        return lst[0]
    elif n == 2:
        return max(lst)

    m = len(lst) // 2
    r = m + 1
    left = m - 1

    if (lst[m] > lst[left]) and (lst[m] > lst[r]):
        return lst[m]
    elif lst[left] >= lst[r]:
        return find_peak(lst[:r])
    elif lst[r] > lst[left]:
        return find_peak(lst[m:])
