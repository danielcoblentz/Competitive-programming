def check_heights(heights):
    if len(heights) == 1:
        print("yes")
        return

    reversed = False

    if heights[1] < heights[0]:
        reversed = True

    if reversed:
        for i in range(len(heights)-1, 0, -1):
            if heights[i] > heights[i-1]:
                print("no")
                return
    else:
        for i in range(2, len(heights)):
            if heights[i] < heights[i-1]:
                print("no")
                return

    print("yes")


if __name__ == "__main__":
    heights_list = []

    while True:
        heights = input()

        if heights == "-1":
            break

        heights_ints = list(map(int, heights.split()))
        heights_list.append(heights_ints)

    for heights in heights_list:
        check_heights(heights)