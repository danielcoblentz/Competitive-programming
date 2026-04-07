def solve(n: int, k: int, e: list) -> int:
    return solve_helper(n, k, e, 0)


def solve_helper(n: int, k: int, e: list, pos: int) -> int:
    if pos in e:
        return 0
    elif pos == n:
        return 1
    elif pos == n - 1:
        return solve_helper(n, k, e, pos + 1)
    else:
        return solve_helper(n, k, e, pos + 1) + solve_helper(n, k, e, pos + 2)


if __name__ == "__main__":
    num_staircases = int(input())

    num_stairs = []
    num_chambers = []
    positions = []

    for i in range(num_staircases):
        n = int(input())
        k = int(input())
        e = input()

        list_e = list(map(int, e.split()))

        num_stairs.append(n)
        num_chambers.append(k)
        positions.append(list_e)

    for i in range(num_staircases):
        print(solve(num_stairs[i], num_chambers[i], positions[i]))
