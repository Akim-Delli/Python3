#!/usr/bin/python3
# classes.py by Akim Delli

# Copyright 2010 The BearHeart Group, LLC

class Duck:
    def __init__(self, **kwargs):
        self.properties = kwargs

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def get_properties(self):
        return self.properties

    def get_property(self, key):
        return self.properties.get(key, None)

    @property
    def color(self):
        return self.properties.get('color', None)

    @color.setter
    def color(self, c):
        self.properties['color'] = c

    @color.deleter
    def color(self):
        del selfd.properties['color']

def main():
    donald = Duck()
    donald.color = 'blue'
    print(donald.get_property('color'))

if __name__ == "__main__": main()
