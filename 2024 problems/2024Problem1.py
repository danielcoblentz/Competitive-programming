def upper(sen):
    print(sen.upper())


if __name__ == "__main__":
    sentences = []

    for _ in range(15):
        sen = input()
        sentences.append(sen)

    for sen in sentences:
        upper(sen)