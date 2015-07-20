__author__ = 'adelli'

fh = open('lines.txt')
for line in fh.readlines():
    print(line, end='')