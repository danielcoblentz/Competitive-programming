OPERATORS = ['+', '-', '*', '/', '(', ')']


def tokenize(line: str):
    n = len(line)
    tokens = []
    current = ""
    i = 0

    # Turn string into list of tokens
    while i < n:
        # catch negative numbers
        if i < n - 1 and line[i] == '-' and line[i + 1].isnumeric():
            current += str(line[i])
            i += 1

        if line[i].isnumeric():
            # keep reading in digits until non-numeric character found
            while i < n and line[i].isnumeric():
                current += str(line[i])
                i += 1
        elif line[i].isalpha():
            # keep reading in alphabetical character until non-alphabetical
            # character found
            while i < n and line[i].isalpha():
                current += str(line[i])
                i += 1
        elif line[i] in OPERATORS:
            # read in an operator
            current = line[i]
            i += 1
        else:
            # character is whitespace, ignore
            i += 1
            continue

        tokens.append(current)
        current = ""

    return tokens


def is_num(lst: list[str]) -> bool:
    for c in lst:
        if c.isalpha() or c == '(' or c == ')':
            return False

    return True


def evaluate(tokens):
    if len(tokens) == 1:
        # Just 1 token means literal/variable
        return tokens[0]

    res = break_down(tokens)
    if res == ():
        return "Invalid expression"

    # operator is a string, op1 and op2 are lists
    operator, op1, op2 = res

    op1 = evaluate(op1)
    op2 = evaluate(op2)

    # By this point, `op1` and `op1` will both be strings -- not lists
    if is_num(op1) and is_num(op2):
        if operator == '+':
            return str(int(op1) + int(op2))
        elif operator == '-':
            return str(int(op1) - int(op2))
        elif operator == '*':
            return str(int(op1) * int(op2))
        elif operator == '/':
            return str(int(int(op1) / int(op2)))

    return f"({operator} {op1} {op2})"


def break_down(tokens: list) -> tuple:
    if tokens[0] != '(' or tokens[-1] != ')':
        # Illegal expression: application must begin with '('
        return ()

    n = len(tokens)

    operator = tokens[1]
    op1 = -1
    op2 = -1

    op2_index = 3

    if tokens[2] == '(':
        # op1 is an application
        nest_depth = 1
        while op2_index < n and nest_depth > 0:
            if tokens[op2_index] == '(':
                nest_depth += 1
            elif tokens[op2_index] == ')':
                nest_depth -= 1

            op2_index += 1

        if nest_depth != 0:
            # Invalid expression: unequal number of left/right parentheses
            return ()

        op1 = tokens[2:op2_index]
    else:
        # op1 is a literal/reference
        op1 = [tokens[2]]

    end_index = op2_index + 1

    if tokens[op2_index] == '(':
        # op2 is an application
        nest_depth = 1
        while end_index < n and nest_depth > 0:
            if tokens[end_index] == '(':
                nest_depth += 1
            elif tokens[end_index] == ')':
                nest_depth -= 1

            end_index += 1

        if nest_depth != 0:
            # Invalid expression: unequal number of left/right parentheses
            return ()

        op2 = tokens[op2_index:end_index]
    else:
        # op2 is a literal/reference
        op2 = [tokens[op2_index]]

    if end_index != n - 1:
        # end_index should be n - 1 by here
        return ()

    return operator, op1, op2


if __name__ == "__main__":
    while True:
        line = input()

        # First step: turn input into a list of tokens, where each token is
        # an integer literal, a variable, or an operator/parenthesis
        tokens = tokenize(line)

        # Second step: evaluate the list of tokens
        print(evaluate(tokens))
