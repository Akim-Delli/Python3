__author__ = 'adelli'


def main():
    d = {'one': 1, 'two':2, 'three': 3, 'four': 5, 'five': 5}
    e = dict(
        one = 1, two = 2, five = 'five'
    )
    print(d)
    for k in sorted(e.keys()):
        print(k, e[k])


if __name__ == "__main__": main()