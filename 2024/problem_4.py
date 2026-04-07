def is_anagram(wd1, wd2) -> bool:
    wd1_list = [0 for _ in range(26)]
    wd2_list = [0 for _ in range(26)]

    for ch in wd1:
        index = ord(ch) - ord('A')
        wd1_list[index] += 1

    for ch in wd2:
        index = ord(ch) - ord('A')
        wd2_list[index] += 1

    return wd1_list == wd2_list


def results(wds):
    n = len(wds)
    dupes = [False for _ in range(n)]

    for i in range(n-1):
        wd1 = wds[i]
        for j in range(i+1, n):
            if i == j:
                # skip same index
                continue

            wd2 = wds[j]

            if is_anagram(wd1, wd2):
                dupes[i] = True
                dupes[j] = True

    valid = []
    for i, wd in enumerate(wds):
        if not dupes[i]:
            valid.append(wd)

    valid.sort()
    print("Results:")
    for wd in valid:
        print(wd)


if __name__ == "__main__":
    seqs = []

    while True:
        n = int(input())

        if n == 0:
            break

        wds = input()
        seqs.append(wds.split())

    for wds in seqs:
        results(wds)