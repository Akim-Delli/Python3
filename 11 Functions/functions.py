#!/usr/bin/python3
# functions.py by Akim Delli

# Copyright 2010 The BearHeart Group, LLC

def main():
    testfunc(42, 2, three=3, four=4, five=5 )

def testfunc(number, another, **kwargs):
    print('This is a test function', number, another, kwargs)
    for element in kwargs: print(kwargs[element])

if __name__ == "__main__": main()
