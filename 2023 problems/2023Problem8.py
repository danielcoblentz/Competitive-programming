VOWELS = ['a', 'e', 'i', 'o', 'u']
VOWELS_UPPER = ['A', 'E', 'I', 'O', 'U']

CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
              'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
CONSONANTS_UPPER = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',
                    'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']


def encypher(s):
    new_s = ""

    for c in s:
        if c in VOWELS:
            index = VOWELS.index(c)
            new_s += VOWELS[(index + 1) % len(VOWELS)]
        elif c in VOWELS_UPPER:
            index = VOWELS_UPPER.index(c)
            new_s += VOWELS_UPPER[(index + 1) % len(VOWELS_UPPER)]
        elif c in CONSONANTS:
            index = CONSONANTS.index(c)
            new_s += CONSONANTS[(index + 1) % len(CONSONANTS)]
        elif c in CONSONANTS_UPPER:
            index = CONSONANTS_UPPER.index(c)
            new_s += CONSONANTS_UPPER[(index + 1) % len(CONSONANTS_UPPER)]
        else:
            new_s += c

    return new_s


if __name__ == "__main__":
    n = int(input())  # number of strings
    inputs = []

    for _ in range(n):
        # get each string from input
        s = input()
        inputs.append(s)

    for s in inputs:
        # encypher each string
        print(encypher(s))
