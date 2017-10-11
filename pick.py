#!/usr/bin/env python

import random


def load(fileName):
    with open(fileName, 'r') as f:
        for line in f:
            yield line.strip()

if __name__ == '__main__':
    words = [l for l in load('brutethink.txt')]
    print(random.choice(words))
