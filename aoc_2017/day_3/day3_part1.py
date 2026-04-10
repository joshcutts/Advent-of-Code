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
            current_line += 1
            n += 1
            print('n: ', n, current_point.x, current_point.y, current_row_length, current_column_length)

        add_x, current_row_length, current_column_length = adjust_matrix_size(add_x, current_row_length, current_column_length)
        dir_counter += 1
        

    return current_point.distance_to_center()

print(walk_spiral(12)) # 31
# print(walk_spiral(368078)) # 371
