#!/usr/bin/env python3
# Problem 8 — Beesanese
# Translate words according to rules in the problem statement.
# consonants -> "Buzz!"; vowels -> two "Buzz!"; special handling for 'z' -> first bzz then later a Buzz!

import sys

VOWELS = set('aeiou')


def translate(word):
    # Implement rules inferred from EX:
    #  consonants -> one "Buzz!"
    #  vowels -> two "Buzz!" (concatenated)
    #  each 'z' emits an immediate "bzz" and also schedules one "Buzz!" to be appended after processing the whole word
    res_parts = []
    scheduled = []  
    for ch in word:
        if ch == 'z':
            res_parts.append('bzz')
            scheduled.append('Buzz!')
        elif ch in VOWELS:
            res_parts.append('Buzz!')
            res_parts.append('Buzz!')
        else:
            res_parts.append('Buzz!')
    # append scheduled Buzz! tokens (order matters here)
    res_parts.extend(scheduled)
    return ''.join(res_parts)


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    out = []
    idx = 1
    for _ in range(t):
        word = data[idx]; idx+=1
        out.append(translate(word))
    print('\n'.join(out))

if __name__=='__main__':
    main()
