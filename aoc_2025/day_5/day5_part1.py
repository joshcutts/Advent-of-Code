"""
Docstring for aoc_2025.day_5.day5_part1


"""

def parse_input(filename):
    with open(filename, "r") as f:
        ranges, ingredients = f.read().split('\n\n')

    # formatted_ranges = [[r.split('-')] for r in ranges.splitlines()]
    formatted_ranges = [
        [int(n) for n in range_line.split('-')]
        for range_line in ranges.splitlines()
    ]
    formatted_ingredients = [int(ingredient) for ingredient in ingredients.splitlines()]

    return formatted_ranges, formatted_ingredients

def count_fresh_ingredients(ranges, ingredients):
    fresh_ingredients = 0

    for ingredient in ingredients:
        if any(ingredient >= r[0] and ingredient <= r[1] for r in ranges):
            fresh_ingredients += 1
    
    return fresh_ingredients

# ranges, igredients = parse_input('example.txt')
ranges, igredients = parse_input('puzzle.txt')

print(count_fresh_ingredients(ranges, igredients))