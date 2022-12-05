#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    else:
        nlist=[]
        for i, j in enumerate(my_list):
            if i != idx:
                nlist.append(j)
        return nlist
