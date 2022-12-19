#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        y = 1
        for i in my_list:
            if y <= x:
                print(i, end="")
                y += 1
        print("\n", end="")
    except Exception:
        pass
    finally:
        return y-1
