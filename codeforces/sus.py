'''



B. Impost or Sus
time limit per test1 second
memory limit per test256 megabytes
A string 𝑤 consisting of lowercase Latin letters is called suspicious if and only if all of the following conditions hold:

The letter 𝚜 appears at least twice, and
For every occurrence of the letter 𝚞, the two nearest occurrences of 𝚜 are the same number of characters away from the 𝚞.
After watching you finish a string task, your friend Aka has gifted you a string 𝑟 consisting only of letters 𝚜 and 𝚞. You can perform the following operation on 𝑟:

Choose an index 𝑖 (1≤𝑖≤|𝑟|), and set 𝑟𝑖 to 𝚜.
Determine the minimum number of operations needed to make 𝑟 suspicious. It can be shown that, under the given constraints, it is always possible to transform 𝑟 into a suspicious string.

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡 (1≤𝑡≤104). The description of the test cases follows.

The only line of each test case contains the string 𝑟 (3≤|𝑟|≤2⋅105). It is guaranteed that 𝑟𝑖=𝚜 or 𝚞.

It is guaranteed that the sum of |𝑟| over all test cases does not exceed 2⋅105.

Output
For each test case, output a single integer — the minimum number of operations needed to make 𝑟 suspicious.



'''





import sys
import io

TEST_INPUT = """9
sus
uuuu
sssss
uusuuu
suuuuuu
usssssss
sssuuusss
susuusuuus
uuuuuuuuuuu
"""

def solve():
    s = sys.stdin.readline().strip()
    if not s:
        return

    n = len(s)
    s_pos = [i for i, c in enumerate(s) if c == 's']

    if len(s_pos) == 0:
        print(2 + (n - 2) // 2)
        return

    prefix = s_pos[0]
    suffix = n - 1 - s_pos[-1]

    res = (prefix + 1) // 2 + (suffix + 1) // 2

    for i in range(len(s_pos) - 1):
        gap = s_pos[i + 1] - s_pos[i] - 1
        res += gap // 2

    print(res)

def main():
    sys.stdin = io.StringIO(TEST_INPUT)
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()
