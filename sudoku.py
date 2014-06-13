import time
from pprint import pprint


row_labels = 'ABCDEFGHI'
col_labels = '123456789'
digits = '123456789'

def create_sqr(rows, cols):
    return [row + col for row in rows for col in cols]

square_keys = create_sqr(row_labels, col_labels)
rows = [create_sqr(row_labels, col) for col in col_labels]
columns = [create_sqr(row, col_labels) for row in row_labels]
blocks = [create_sqr(row, col)
          for row in ('ABC', 'DEF', 'GHI')
          for col in ('123', '456', '789')]

check_list = rows + columns + blocks
squares = dict((square, [item for item in check_list if square in item])
               for square in square_keys)

check_group = dict((square, set(sum(squares[square], []))-set([square]))
                   for square in square_keys)

puzzle_values = ('7...3.....6....97....9...56'
                 '5.......3.4......72..61....'
                 '3.1..4.........56...7.2....'
                 )

def create_puzzle_row(row_slice):
    row_1 = ''
    row_2 = ''
    row_3 = ''

    for char in row_slice[0:3]:
        row_1 = row_1 + (char + ' ')

    for char in row_slice[3:6]:
        row_2 = row_2 + (char + ' ')

    for char in row_slice[6:9]:
        row_3 = row_3 + (char + ' ')

    formatted_row = row_1 + '| ' + row_2 + '| ' + row_3
    return formatted_row

def create_block_row(block_slice):
    block = (create_puzzle_row(block_slice[0:9]) + '\n'
           + create_puzzle_row(block_slice[9:18]) + '\n'
           + create_puzzle_row(block_slice[18:27]) + '\n')

    return block

def create_horizontal_ln():
    horizontal_line = '+ '.join(['- '*(3)]*3) + '\n'

    return horizontal_line

def create_grid(puzzle_values):
    grid = (create_block_row(puzzle_values[0:27]) + create_horizontal_ln()
          + create_block_row(puzzle_values[27:54]) + create_horizontal_ln()
          + create_block_row(puzzle_values[54:81]))

    return grid

def set_known_values(square_keys, puzzle_values):

    square_val = dict((square, list(digits)) for square in square_keys)
    known_val = dict((k, v) for k, v in zip(square_keys, puzzle_values) if v != '.')
    for k, v in known_val.items():
        square_val[k] = v

    return square_val

def remove_knowns(grid_values):
    for k, v in list(grid_values.items()):
        if len(v) == 1:
            for square in check_group[k]:
                if len(grid_values[square]) != 1:
                    try:
                        grid_values[square].remove(v)
                    except ValueError:
                        pass
    return grid_values

# def compare_unknowns(grid_values):
#     for k, v in list(grid_values.items()):
#         if len(v) > 1:
#             for square in check_group[k]:
#                 for digit in grid_values[square]:
#                     for square2 in check_group[k]:
#                         if digit not in grid_values[square2]:
#                             if len(grid_values[square2]) > 1:
#                                 grid_values[square2] = digit
#     return grid_values


def find_single_options_left(group):
    pass

def group_flip(group):
    digit_group = {digit: set() for digit in digits}
    for k, v in group.items():
        for val in v:
            digit_group[val].add(k)
    return digit_group





def main():
    # assert compare_values(compare_values(set_known_values(square_keys, puzzle_values))) == \
    pprint(group_flip(remove_knowns(set_known_values(square_keys, puzzle_values))))


if __name__ == "__main__":
    main()

# test puzzle from http://www.puzzles.ca/sudoku.html - easy puzzle #159 and solution
# '7...3.....6....97....9...565.......3.4......72..61....3.1..4.........56...7.2....'
# '795236148863451972412978356579842613146395287238617495381564729924783561657129834'
