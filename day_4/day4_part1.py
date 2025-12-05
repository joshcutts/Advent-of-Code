def parse_input(filename):
    with open(filename, "r") as f:
        grid = [list(row) for row in f.read().splitlines()]

    return grid

def count_adjacent_rolls(grid, row_i, col_i):
    adjacent_rolls = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            adjacent_row = row_i + i
            adjacent_col = col_i + j
            
            if adjacent_row >= 0 and adjacent_col >= 0 and adjacent_row < len(grid) and adjacent_col < len(grid[0]):
                if grid[adjacent_row][adjacent_col] == '@':
                    
                    adjacent_rolls += 1
    
    return adjacent_rolls


# print(count_adjacent_rolls(grid, 0, 3)) # 3

def count_accessible_rolls(grid):
    accessible_rolls = 0

    for row_i in range(len(grid)):
        row = grid[row_i]
        for col_i in range(len(row)):
            if grid[row_i][col_i] == '@':
                adjacent_rolls = count_adjacent_rolls(grid, row_i, col_i)

                if adjacent_rolls < 4:
                    accessible_rolls += 1
                

    return accessible_rolls


# grid = parse_input('example.txt')
grid = parse_input('input.txt')
print(count_accessible_rolls(grid))



