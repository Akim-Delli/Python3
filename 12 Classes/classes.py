#!/usr/bin/python3
# classes.py by Akim Delli

# Copyright 2010 The BearHeart Group, LLC

class Duck:

    private_variable ={};
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == "__main__": main()
