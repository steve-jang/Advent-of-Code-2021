def multiply_positions(commands):
    horizontal = 0
    vertical = 0
    for command in commands:
        cmd, x = command.split(" ")
        x = int(x)
        if cmd == "forward":
            horizontal += x
        elif cmd == "down":
            vertical += x
        else:
            vertical -= x

    return horizontal * vertical


def mult_pos_2(commands):
    aim = 0
    horizontal = 0
    vertical = 0
    for command in commands:
        cmd, x = command.split(" ")
        x = int(x)
        if cmd == "down":
            aim += x
        elif cmd == "up":
            aim -= x
        else:
            horizontal += x
            vertical += aim * x

    return horizontal * vertical


if __name__ == "__main__":
    a = open("day2.txt", "r").readlines()
    print(multiply_positions(a))
    print(mult_pos_2(a))

