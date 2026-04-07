#!/usr/bin/env python3
"""
Problem 7 — Pokémon Island Survival
Simulate three flood steps (decrease land cells by 1 per step, floor at 0),
then count 4-connected components of cells > 0.
Input format described in the contest PDF.
"""

import sys
from collections import deque


def count_islands(grid, m, n):
    visited = [[False] * n for _ in range(m)]
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    islands = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] > 0 and not visited[i][j]:
                islands += 1
                # BFS
                dq = deque()
                dq.append((i, j))
                visited[i][j] = True
                while dq:
                    x, y = dq.popleft()
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] > 0:
                            visited[nx][ny] = True
                            dq.append((nx, ny))
    return islands


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    try:
        t = int(next(it))
    except StopIteration:
        return

    out_lines = []
    for _ in range(t):
        m = int(next(it))
        n = int(next(it))
        grid = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                grid[i][j] = int(next(it))
        # simulate three flood steps
        for i in range(m):
            for j in range(n):
                grid[i][j] = max(0, grid[i][j] - 3)
        islands = count_islands(grid, m, n)
        out_lines.append(str(islands))

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main()
