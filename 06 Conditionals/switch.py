#!/usr/bin/python3
# switch.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    choice = dict(
        one = 'first',
        two = 'two',
        three = 'three'
    )
    v = 'five'
    print(choice.get(v, 'other'))
    v = 'this is true' if  a < b else 'false'

if __name__ == "__main__": main()
