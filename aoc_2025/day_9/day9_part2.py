"""
Docstring for aoc_2025.day_9.day9_part2


..............
.......#XXX#.. 7,1 | 11, 1
.......XXXXX..
..#XXXX#XXXX.. 2, 3 | 7, 3
..XXXXXXXXXX..
..#XXXXXX#XX.. 2, 5 | 9, 5
.........XXX..
.........#X#.. 9, 7 | 11, 7
..............

7, 1 | 11, 1 => 5 * 1 => 5
7, 1 | 7, 3 =>  3 * 1 => 3
7, 1 | 9, 5 => 3 * 5 =>  15


[7, 1] [11, 1]
[7, 1] [7, 3]
[7, 1] [9, 5]
[11, 1] [11, 7]
[2, 3] [7, 3]
[2, 3] [2, 5]
[2, 3] [9, 5]
[7, 3] [9, 5]
[2, 5] [9, 5]
[9, 5] [9, 7]
[9, 5] [11, 7]
[9, 7] [11, 7]

[11, 1][7, 3]
[7, 3][11, 1]

"""


"""
referenced Dazbo's solution - learning ray casting technique
https://aoc.just2good.co.uk/2025/9
https://github.com/derailed-dash/advent-of-code/blob/master/src/AoC_2025/d09/d09.py
"""

import itertools

def parse_input(filename):
    with open(filename, "r") as f:
        data = f.read().splitlines()

    # int_tile_locs = [[int(coord) for coord in tile.split(',')] for tile in tile_locs]
    # int_tile_locs = map(int, tile_locs)

    return data


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
            
def generate_red_tile_point_list(locs):
    red_tiles = []

    for loc in locs:
        x, y = [int(coord) for coord in loc.split(',')]
        red_tiles.append(Point(x, y))
    
    return red_tiles

class PolygonSolver:
    def __init__(self, corners: list[Point]):
        self.corners = corners
        self.num_corners = len(corners)

        self.vertical_edges = [] # (x, y1, y2)
        self.horizontal_edges = [] # (x1, x2, y)

        for i in range(self.num_corners):
            p1 = corners[i]
            p2 = corners[(i + 1) % self.num_corners]

            if (p1.x == p2.x): # Vertical
                y_min, y_max = min(p1.y, p2.y), max(p1.y, p2.y)
                self.vertical_edges.append((p1.x, y_min, y_max))
            else:
                x_min, x_max = min(p1.x, p2.x), max(p1.x, p2.x)
                self.horizontal_edges.append((x_min, x_max, p1.y))
        
    def is_point_inside(self, px: float, py: float):
        intersections = 0

        for vx, vy_min, vy_max in self.vertical_edges:
            if vx > px:
                if vy_min <= py < vy_max:
                    intersections += 1

        return intersections % 2 == 1
    
    def intersects_rect(self, r_min_x, r_min_y, r_max_x, r_max_y):
        # check vertical edges
        for vx, vy_min, vy_max in self.vertical_edges:
            # does vertical edge X fall strictly inside rect X range
            if r_min_x < vx < r_max_x:
                overlap_min = max(vy_min, r_min_y)
                overlap_max = min(vy_max, r_max_y)
                if overlap_min < overlap_max:
                    return True
                
        for vx_min, vx_max, vy in self.horizontal_edges:
            # does horizontal egde Y fall strictly inside rect Y range
            if r_min_y < vy < r_max_y:
                overlap_min = max(vx_min, r_min_x)
                overlap_max = min(vx_max, r_max_y)
                if overlap_min < overlap_max:
                    return True
                
        return False

def calculate_area(p1, p2):
    area = (abs(p2.x - p1.x) + 1) * (abs(p2.y - p1.y) + 1)
    return area

def find_max_contained_area(polygon):
    max_area = 0

    for p1, p2 in itertools.combinations(red_tile_points, 2):
        area = calculate_area(p1, p2)
        if area <= max_area:
            continue

        r_min_x, r_max_x = min(p1.x, p2.x), max(p1.x, p2.x)
        r_min_y, r_max_y = min(p1.y, p2.y), max(p1.y, p2.y)

        if polygon.is_point_inside(r_min_x + 0.5, r_min_y + 0.5):
            if not polygon.intersects_rect(r_min_x, r_min_y, r_max_x, r_max_y):
                max_area = area
    
    return max_area


# red_tile_string_locs = parse_input('example.txt')
red_tile_string_locs = parse_input('puzzle.txt')
# print(locs)

# locs = parse_input('puzzle.txt')
red_tile_points = generate_red_tile_point_list(red_tile_string_locs)
polygon = PolygonSolver(red_tile_points)
print(find_max_contained_area(polygon))


"""
674960 - too low
2975958387 - too high
"""