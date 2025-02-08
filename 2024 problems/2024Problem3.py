def cms_order(order: list):
    o = order.copy()
    total = 0

    while o[2] > 0 and o[5] > 0:
        # Add up combo #1s
        total += 11
        o[2] -= 1
        o[5] -= 1

    while o[0] > 0 and o[3] > 0:
        total += 4
        o[0] -= 1
        o[3] -= 1

    total += ((o[0] * 3) + (o[1] * 6) + (o[2] * 10)
              + (o[3] * 3) + (o[4] * 2) + (o[5] * 4))
    return total


def wck_order(order: list):
    o = order.copy()
    total = 0

    while o[1] > 0 and o[3] > 0 and o[4] > 0:
        total += 9
        o[1] -= 1
        o[3] -= 1
        o[4] -= 1

    total += ((o[0] * 2) + (o[1] * 7) + (o[2] * 9)
              + (o[3] * 3) + (o[4] * 3) + (o[5] * 3))

    return total


def cheapest(order: list):
    cms = cms_order(order)
    wck = wck_order(order)

    if cms < wck:
        print(f"CMS {cms}")
    else:
        print(f"WCK {wck}")


if __name__ == "__main__":
    n = int(input())  # number of orders
    orders = []

    for _ in range(n):
        order = input()
        order_list = list(map(int, order.split()))

        orders.append(order_list)

    for order in orders:
        cheapest(order)