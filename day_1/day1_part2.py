def parse_input(file):
    with open(file, "r") as f:
        lines = f.read().splitlines()
    
    return lines


def count_any_zero_position_during_rotations(instructions):
    zero_count = 0
    dial = 50

    for instruction in instructions:
        direction = instruction[0]
        num = int(instruction[1:])

        zero_count += num // 100
        num = num % 100

        num = num if direction == "R" else (num * -1)

        dial += num

        if dial > 100:
            zero_count += 1
            dial = dial % 100
        elif dial < 0:
            zero_count += 1 if num != dial else 0
            dial = 100 + dial
        
        dial = 0 if dial == 100 else dial
        zero_count += (dial == 0)
        print(instruction, num, dial, zero_count)
        
    
    return zero_count

instructions = parse_input("part1_input.txt")
# instructions = parse_input("example.txt")
print(count_any_zero_position_during_rotations(instructions))