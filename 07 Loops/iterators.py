#!/usr/bin/python3
# iterators.py by Akim Delli

# Copyright 2010 The BearHeart Group, LLC

def main():
    fh = open('lines.txt')
    for line in fh.readlines():
        print(line)

if __name__ == "__main__": main()
