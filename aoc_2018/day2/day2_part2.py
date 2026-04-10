def parse_input(file):
    with open(file, "r") as f:
        lines = f.read().splitlines()

    return lines

# ids = parse_input('example.txt')
ids = parse_input('puzzle.txt')

def find_common_letters(ids):
    length = len(ids[0])

    for id_one in ids:
        for id_two in ids:
            difference_i = None

            if id_one is id_two:
                continue

            for i in range(length):
                if difference_i == None and id_one[i] != id_two[i]:
                    difference_i = i
                elif id_one[i] != id_two[i]:
                    break

            if i == length - 1:
                return id_one[:difference_i] + id_one[difference_i + 1:]
        

print(find_common_letters(ids))

# oeylbtcxjqnzhgyyylfapvius - not correct
# oeylbtcxjqnzhgyylfapviusr