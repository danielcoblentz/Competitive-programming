#!/usr/bin/env python3
# Problem 9 — Zombiemon Go!
# Count number of ways to place zombies in N stalls with no adjacent occupied stalls.
# This is Fibonacci-like: ways[n] = ways[n-1] + ways[n-2], with base ways[0]=1 (empty), ways[1]=2 (empty or one)

import sys

def ways(n):
    # We need number of valid arrangements for n stalls, where each stall either empty or occupied, but no adjacent occupied.
    # Let f(n) be number of length-n binary strings with no consecutive ones. Known recurrence: f(0)=1, f(1)=2, f(n)=f(n-1)+f(n-2)
    if n==0:
        return 1
    a,b = 1,2
    for _ in range(2,n+1):
        a,b = b,a+b
    return b


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    out=[]
    idx=1
    for _ in range(t):
        n=int(data[idx]); idx+=1
        out.append(str(ways(n)))
    print('\n'.join(out))

if __name__=='__main__':
    main()
