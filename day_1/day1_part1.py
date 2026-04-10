def parse_input(file):
    with open(file, "r") as f:
        lines = f.read().splitlines()
    
    return lines


def count_zero_position_during_rotations(instructions):
    zero_count = 0
    dial = 50

    for instruction in instructions:
        direction = instruction[0]
        num = int(instruction[1:]) % 100

        num = num if direction == "R" else (num * -1)
        dial += num
        
        if dial >= 100:
            dial = dial % 100
        elif dial < 0:
            dial = 100 + dial
        
        zero_count += (dial == 0)

    return zero_count

instructions = parse_input("part1_input.txt")
print(count_zero_position_during_rotations(instructions))

