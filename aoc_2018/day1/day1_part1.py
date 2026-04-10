def parse_input(file):
    with open(file, "r") as f:
        # lines = f.read().splitlines()
        lines = f.read().splitlines()
    
    return lines

nums = parse_input('example.txt')
# print(nums)

def calculate_total(str_nums):
    total = 0

    totals = set()
    i = 0
    
    while True:
        str_num = str_nums[i % len(str_nums)]
        total += int(str_num)

        # print(total, total in totals)
        if total in totals:
            return total

        totals.add(total)
        i += 1

    return None

print(calculate_total(nums))

