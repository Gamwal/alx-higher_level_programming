#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        mx = my_list[0]
        for i in my_list:
            if i > mx:
                mx = i
            else:
                mx = mx
        return mx
