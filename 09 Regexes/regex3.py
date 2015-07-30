#!/usr/bin/python3
# regex.py by Akim Delli



import re

def main():
    fh = open('raven.txt')
    pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
    for line in fh:
        match = re.search(pattern, line)
        if match:
            print(pattern.sub('###', line), end='')

if __name__ == "__main__": main()
