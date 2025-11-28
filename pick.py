#!/usr/bin/env python

import argparse
import random


def to_absolute(fileName):
    import os.path
    # where is this module?
    thisDir = os.path.dirname(__file__)
    return os.path.join(thisDir, fileName)


def load(fileName):
    with open(fileName, 'r') as f:
        for line in f:
            yield line.strip()


#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------

table = {
    'brute': 'brutethink.txt',
    'easy': 'easy-names.txt',
    'name': 'names.txt',
    'star': 'stars.txt',
    'noun': 'nouns.txt',
    'verb': 'verbs.txt'
}


def main():
    parser = buildArgParser()
    args = parser.parse_args()

    fileName = table[args.source]

    words = [l for l in load(to_absolute(fileName))]

    for i in range(0, args.count):
        print(random.choice(words))


def buildArgParser():
    p = argparse.ArgumentParser(description='randomly choose words')
    p.add_argument('source', choices=sorted(table.keys()),
                   nargs='?',
                   default='easy',
                   help='which source to use')
    p.add_argument('count', type=int,
                   nargs='?',
                   default='1',
                   help='number of words to choose')
    return p

if __name__ == '__main__':
    main()
