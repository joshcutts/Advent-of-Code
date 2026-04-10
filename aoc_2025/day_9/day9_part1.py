import itertools

def parse_input(filename):
    with open(filename, "r") as f:
        tile_locs = f.read().splitlines()

    return [[int(coord) for coord in tile.split(',')] for tile in tile_locs]
    



def find_max_red_rectangle(locs):
    max_area = 0

    for tile_one, tile_two in itertools.combinations(locs, 2):
        area = (abs(tile_two[0] - tile_one[0]) + 1) * (abs(tile_two[1] - tile_one[1]) + 1)
        max_area = max(max_area, area)

    return max_area

# locs = parse_input('example.txt')
locs = parse_input('puzzle.txt')
print(find_max_red_rectangle(locs))