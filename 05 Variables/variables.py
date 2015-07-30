#!/usr/bin/python3
# variables.py by Akim Delli

# Copyright 2010 The BearHeart Group, LLC

def main():
    n = 42
    print("This is the variables.py file.")
    s = r"this is \n {} string!".format(n)
    print(s)
    s2 = '''\
        this is a string
        line after line
        of text
        ...
        '''
    print(s2)

if __name__ == "__main__": main()
