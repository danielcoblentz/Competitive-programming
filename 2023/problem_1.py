def print_template(sentence, token, sequences):
    # Split `sequences` into an array of strings
    split_seqs = sequences.split()

    # Iterate for each sequence
    for seq in split_seqs:
        print(sentence.replace(token, seq))


if __name__ == "__main__":
    # get number of templates
    num_templates = int(input())
    sentences = []
    tokens = []
    word_sequences = []

    # get info for each template
    for i in range(num_templates):
        sen = input()
        token = input()
        sequences = input()

        sentences.append(sen)
        tokens.append(token)
        word_sequences.append(sequences)

    # print each template
    for i in range(num_templates):
        print_template(sentences[i], tokens[i], word_sequences[i])
