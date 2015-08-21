#!/usr/bin/python3
# files.py by Akim Delli

# Copyright 2010 The BearHeart Group, LLC

def main():
    bufferSize = 50000
    infile = open('bigfile.txt', 'r')
    outfile = open('new.txt', 'w')
    buffer = infile.read(bufferSize)
    while len(buffer):
        outfile.write(buffer)
        print('.', end = '')
        buffer = infile.read(bufferSize)

    print('Done.')


if __name__ == "__main__": main()
