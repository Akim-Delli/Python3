#!/usr/bin/python3
# generator.py by Akim Delli


def main():
    print("This is the functions.py file.")
    for i in inclusive_range(1,27,3):
        print(i, end = ' ')

def inclusive_range(*args):
    numargs = len(args)
    if numargs <1 : raise TypeError('error at leat one argument')
    elif numargs == 1:
        start = 1
        stop = args[0]
        step = 1
    elif numargs == 2:
        start = args[0]
        stop = args[1]
        step = 1
    elif numargs == 3:
        start, stop, step = args
    else: raise ValueError('error too many arguments got {}'.format(numargs))
    i = start
    while i <= stop:
        yield i
        i += step

if __name__ == "__main__": main()
