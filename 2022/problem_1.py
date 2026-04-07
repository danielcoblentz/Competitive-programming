def transform_phrase(phrase, substitution):
    # case 1: input substitution string has an odd number of letters -> return "Wut"
    if len(substitution) % 2 != 0:
        return "Wut"

    # dictionary for substitutions 
    substitution_dict = {}
    for i in range(0, len(substitution), 2):
        original, replacement = substitution[i].lower(), substitution[i + 1]
        substitution_dict[original] = replacement


    # Process the phrase(keeping the origional case(upper or lower))
    transformed_phrase = []
    for char in phrase:
        lower_char = char.lower()
        if lower_char in substitution_dict:
            # replacement
            new_char = substitution_dict[lower_char]
            transformed_phrase.append(new_char.upper() if char.isupper() else new_char.lower())
        else:
            transformed_phrase.append(char)

    return ''.join(transformed_phrase) # join result



def main():
    #input for phrases / testing (inputoutput)
    num_phrases = int(input().strip())

    results = []
    for _ in range(num_phrases):
        phrase = input().strip()       # get phrase
        substitution = input().strip() # get substitution string
        results.append(transform_phrase(phrase, substitution))

    # show output to terminal 
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
