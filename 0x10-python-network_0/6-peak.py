#!/usr/bin/python3
"""Python script to find peak"""


def find_peak(lst):
    """funtion that takes a list of integers and finds the peak"""
    n = len(lst)
    if n == 0:
        return None
    mid = n // 2
    left = mid
    right = mid
    while ((left - 1) >= 0) and ((right + 1) < n):
        left = mid - 1
        right = mid + 1
        if (lst[mid] > lst[left]) and (lst[mid] > lst[right]):
            return lst[mid]
        elif (lst[left] == lst[right]) and ((left - 2) >= 0):
            mid = left - 1
        elif (lst[left] >= lst[mid]):
            mid = left  
        elif (lst[right] > lst[mid]):
            mid = right
    if right == (n - 2):
        return lst[right]
    else:
        return lst[left]
