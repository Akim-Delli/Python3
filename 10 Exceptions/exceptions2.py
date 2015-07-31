#!/usr/bin/python3
# exceptions.py by Akim Delli



def main():
    try:
        for line in readfile('lines.doc'): print(line.strip())
    except IOError as e:
        print('Cannot read file :', e)
    except ValueError as e:
        print ('Bad Filename', e)

def readfile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines
    else: raise ValueError('Filename must end with .txt')

if __name__ == "__main__": main()
