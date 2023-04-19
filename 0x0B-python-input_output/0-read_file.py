#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Function to read a utf-8 text file"""
    with open(filename, 'r', encoding='utf-8') as myFile:
        for line in myFile:
            print(line, end='')
