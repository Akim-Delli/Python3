#!/usr/bin/python3
# switch.py by Akim Delli

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
