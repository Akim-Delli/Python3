#!/usr/bin/python3
# syntax.py by Akim Delli

# Copyright 2010 The BearHeart Group, LLC

def main():
    print("This is the syntax.py file.")
    func()

def func():
    for i in range(10):
        print(i, end= ' ')
    print()

if __name__ == "__main__": main()
