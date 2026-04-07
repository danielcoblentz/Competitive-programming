'''
A. Yes or Yes
time limit per test1 second
memory limit per test256 megabytes
Last Christmas, your friend Fernando gifted you a string 𝑠 consisting only of the characters 𝚈 and 𝙽, representing "Yes" and "No", respectively.

You can repeatedly apply the following operation on 𝑠:

Choose any two adjacent characters and replace them with their logical OR.
Formally, in each operation, you can choose an index 𝑖 (1≤𝑖≤|𝑠|−1), remove the characters 𝑠𝑖 and 𝑠𝑖+1, then insert:

A single 𝚈 if at least one of 𝑠𝑖 or 𝑠𝑖+1 is 𝚈;
A single 𝙽 if both 𝑠𝑖 and 𝑠𝑖+1 are 𝙽.
Note that after each operation, the length of 𝑠 decreases by 1.

Unfortunately, Fernando does not want you to combine "Yes OR Yes", as he has experienced trauma relating to a certain song.

Determine whether it is possible to reduce 𝑠 to a single character by repeatedly applying the operation above, without ever combining two 𝚈's.

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡 (1≤𝑡≤500). The description of the test cases follows.

The only line of each test case contains the string 𝑠 (2≤|𝑠|≤100). It is guaranteed that 𝑠𝑖=𝚈 or 𝙽.

Output
For each test case, print "YES" if the string can be reduced to a single character by repeatedly applying the described operation, and "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

Input:
7
YY
NN
NNY
YYYNY
NNNNN
YYYYYY
YNNNNN

output:
NO
YES
YES
NO
YES
NO
YES

Note
In the first test case, you cannot combine 𝑠1 and 𝑠2 since they are both 𝚈. Thus, the answer is NO.

In the third test case, the following is a valid sequence of operations: 𝙽𝙽⎯⎯⎯⎯𝚈→𝙽𝚈⎯⎯⎯⎯→𝚈. Thus, the answer is YES.

In the fourth test case, there are two possibilities for the first operation: 𝚈𝚈𝚈𝙽⎯⎯⎯⎯𝚈→𝚈𝚈𝚈𝚈 or 𝚈𝚈𝚈𝙽𝚈⎯⎯⎯⎯→𝚈𝚈𝚈𝚈. However, in either case, it is not possible to perform any more operations without combining two 𝚈's. Thus, the answer is NO.

In the fifth test case, the following is a valid sequence of operations: 𝙽𝙽𝙽⎯⎯⎯⎯𝙽𝙽→𝙽𝙽⎯⎯⎯⎯𝙽𝙽→𝙽𝙽𝙽⎯⎯⎯⎯→𝙽𝙽⎯⎯⎯⎯→𝙽. Thus, the answer is YES.


'''

def solve(s:str):
    y_count = s.count('Y')
    if y_count > 1:
        return "NO"
    else:
        return "YES"


# --- Running the examples from the problem ---
examples = [
    "YY",       # Case 1
    "NN",       # Case 2
    "NNY",      # Case 3
    "YYYNY",    # Case 4
    "NNNNN",    # Case 5
    "YYYYYY",   # Case 6
    "YNNNNN"    # Case 7
]

print(f"{'Input':<10} | {'Output':<10}")
print("-" * 22)

for test_case in examples:
    result = solve(test_case)
    print(f"{test_case:<10} | {result:<10}")