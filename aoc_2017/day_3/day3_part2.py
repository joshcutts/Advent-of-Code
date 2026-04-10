class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def adjust_location(self, direction):
        if 'x' in direction.keys():
            self.x += direction['x']
        else:
            self.y += direction['y']

    def distance_to_center(self):
        return abs(self.x) + abs(self.y)

def adjust_matrix_size(add_x, current_row_length, current_column_length):
    if add_x:
        current_row_length += 1
    else:
        current_column_length += 1
    
    add_x = not add_x

    return [add_x, current_row_length, current_column_length]

def get_surrounding_coordinates(current_point):
    surrouding_coordinates = []

    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x == 0 and y == 0: continue
            surrouding_coordinates.append(f"{current_point.x + x}:{current_point.y + y}")
    
    return surrouding_coordinates


def calculate_current_sum(grid, current_point):
    sum = 0

    coordinates = get_surrounding_coordinates(current_point)
    for coordinate in coordinates:
        sum += grid.get(coordinate, 0)

    return sum


grid = {'0:0': 1}

def walk_spiral(input_number):
    current_point = Point(0, 0)
    n = 1
    current_row_length = 0
    current_column_length = 0
    direction = {
        0: {'x': -1},
        1: {'y': -1},
        2: {'x': 1},
        3: {'y': 1}
    }
    dir_counter = 0
    add_x = True

    while n < input_number:
        current_line = 0
        current_direction = direction[dir_counter % 4]
        print('current_dir', current_direction)
        max_line_length = current_row_length if add_x else current_column_length

        while current_line < max_line_length and n < input_number:
            current_point.adjust_location(current_direction)
            sum = calculate_current_sum(grid, current_point)
            grid[f"{current_point.x}:{current_point.y}"] = sum
            if sum >= input_number:
                return sum
            current_line += 1
            n += 1
            print('n: ', n, current_point.x, current_point.y, sum)
            print(grid)

        add_x, current_row_length, current_column_length = adjust_matrix_size(add_x, current_row_length, current_column_length)
        dir_counter += 1
        

    return current_point.distance_to_center()

# print(walk_spiral(12)) # 31
print(walk_spiral(368078)) # 371
