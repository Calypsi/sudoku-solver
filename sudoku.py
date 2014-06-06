import time


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

puzzle_values = '7...3.....6....97....9...565.......3.4......72..61....3.1..4.........56...7.2....'

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
    print(formatted_row)
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

def main():
    create_grid(puzzle_values)

main()

# test puzzle from www.puzzles.ca - easy puzzle #159 and solution
# '7...3.....6....97....9...565.......3.4......72..61....3.1..4.........56...7.2....'
# '795236148863451972412978356579842613146395287238617495381564729924783561657129834'
