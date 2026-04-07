def count_partitions(nums):
    total = sum(nums)
    if total % 3 != 0:
        return 0

    target = total // 3
    count = 0
    prefix = 0
    found_first = 0

    for i in range(len(nums) - 1):
        prefix += nums[i]
        if prefix == 2 * target:
            count += found_first
        if prefix == target:
            found_first += 1

    return count


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    print(count_partitions(nums))
