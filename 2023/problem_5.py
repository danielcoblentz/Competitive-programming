def max_card(row: list) -> int:
    ranking = [0 for _ in range(200)]

    for num in row:
        # For promo card n, we must add n cards of value n, n - 1 cards of
        # value n - 1, ..., 1 card of value 1
        for i in range(1, num + 1):
            ranking[i] += i

    max = row[0]
    max_index = 0

    # Traverse the rankings to find which card number has the most
    # in circulation
    for index, card_count in enumerate(ranking):
        if card_count >= max:
            max = card_count
            max_index = index

    return max_index


if __name__ == "__main__":
    # Get the number of rows to be input
    n = int(input())
    data = []

    for _ in range(n):
        row = input()
        row_list = list(map(int, row.split()))
        data.append(row_list)

    for row in data:
        print(max_card(row))
