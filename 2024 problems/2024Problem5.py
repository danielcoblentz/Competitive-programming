data = {}
scores = {}


def calculate_score(id):
    n = data[id]["num_plays"]
    d = len(data[id]["days"])
    s = data[id]["last_day"] - data[id]["first_day"]

    scores[id] = (n * d) + s


def find_maxes():
    maxes = []

    for _ in range(10):
        current_max = -1
        current_max_id = -1

        for k, v in scores.items():
            if v > current_max:
                current_max = v
                current_max_id = k

        maxes.append(current_max_id)
        scores.pop(current_max_id)

    for i, m in enumerate(maxes):
        if i == 9:
            print(m, end="")
        else:
            print(m, end=" ")


if __name__ == "__main__":
    lines = []

    for i in range(14):
        line = list(map(int, input().split()))

        if line[0] == -1:
            continue

        for id in line:
            if id not in data:
                new_data = {
                    "num_plays": 1,
                    "days": [i],
                    "first_day": i,
                    "last_day": i
                }
                data[id] = new_data
            else:
                data[id]["num_plays"] += 1
                if i not in data[id]["days"]:
                    data[id]["days"].append(i)
                data[id]["last_day"] = i

    for id in data:
        calculate_score(id)

    find_maxes()