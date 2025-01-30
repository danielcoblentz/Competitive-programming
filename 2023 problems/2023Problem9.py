def validate(s: str) -> str:
    stack = []  # stack of uppercase chars

    i = 0  # index
    n = len(s)

    while i < n:
        ch = s[i]

        if ch.isupper():
            # `ch` is uppercase
            if ch == 'X':
                if i == n:
                    # X cannot be the last character
                    return "Trick!"
                # If we're nested and the character following X is uppercase, this
                # is invalid - nested characters cannot follow a nested X
                elif s[i + 1].isupper() and stack:
                    # Nested characters cannot follow a nested X
                    return "Trick!"

                # X is valid, continue
                i += 1
            else:
                # If we're nested and most recently nested character is
                # "behind" `ch` in the alphabet, this is invalid
                if stack and stack[0] >= ch:
                    return "Trick!"

                stack.insert(0, ch)  # Push `ch` to stack
                i += 1
        else:
            # `ch` is lowercase
            for _ in range(2):
                # Check that all 3 characters are the same
                i += 1
                if s[i] != ch:
                    return "Trick!"

            # If top of stack doesn't correspond to `ch`, this is invalid
            if stack[0] != ch.upper():
                return "Trick!"
            else:
                # Spine-chilling pair complete, pop from stack
                stack.pop(0)

            i += 1

    return "Treat!"


if __name__ == "__main__":
    n = int(input())  # number of inputs
    strs = []

    for _ in range(n):
        s = input()
        strs.append(s)

    for s in strs:
        print(validate(s))
