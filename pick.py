#!/usr/bin/env python

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

if __name__ == '__main__':
    words = [l for l in load(to_absolute('brutethink.txt'))]
    print(random.choice(words))
