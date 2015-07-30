#!/usr/bin/python3
# break.py by Akim Delli

# Copyright 2010 The BearHeart Group, LLC

def main():
    s = 'this is a string'
    for c in s:
        if c == 's':
            print(c, end='')
    else:
        print('else')

if __name__ == "__main__": main()
