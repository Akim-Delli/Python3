#!/usr/bin/python3
# for.py by Akim Delli

# Copyright 2010 The BearHeart Group, LLC

def main():
    s = 'this is a string'
    for i, c in enumerate(s):
        if c == 's': print('index{} is an s'.format(i))

if __name__ == "__main__": main()
