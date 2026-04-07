def execute(instructions: list[str]) -> tuple[int, int]:
    # initialize position to (0, 0)
    x = 0
    y = 0
    facing = 90

    # initialize stack
    stack = []
    i = 0

    while i < len(instructions):
        inst = instructions[i]

        if "push" in inst:
            num = int(inst[5:])
            stack.insert(0, num)

            i += 1
        elif "add" in inst:
            num1 = stack.pop(0)
            num2 = stack.pop(0)
            stack.insert(0, num1 + num2)

            i += 1
        elif "move" in inst:
            val = stack.pop(0)
            if facing == 90:  # up
                y += val
            elif facing == 0:  # right
                x += val
            elif facing == 270:  # down
                y -= val
            elif facing == 180:  # left
                x -= val

            i += 1
        elif "turn" in inst:
            val = stack.pop(0)
            facing += val
            facing %= 360

            i += 1
        elif "branch" in inst:
            if stack[-1] != 0:
                i = int(inst[7:])
            else:
                i += 1
        elif "halt" in inst:
            break

    return x, y


if __name__ == "__main__":
    programs = []

    while True:
        n = int(input())

        if n == 0:
            break

        instructions = []

        for _ in range(n):
            inst = input()
            instructions.append(inst)

        programs.append(instructions)

    for prog in programs:
        print(f"Mower halts at {execute(prog)}")
