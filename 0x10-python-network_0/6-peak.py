#!/usr/bin/python3
# Python script to find peak

def find_peak(lst):
    """funtion that takes a list of integers and finds the peak"""
    if len(lst) == 0:
        return None
    return max(lst)