#!/usr/bin/python3
# exceptions.py by Akim Delli



def main():
    try:
        fh = open('xlines.txt')
    except IOError as e:
        print('Couldnt open the file: ', e)

    for line in fh: print(line.strip())


if __name__ == "__main__": main()
