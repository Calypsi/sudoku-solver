def create_sqr(rows, cols):
    return [row + col for row in rows for col in cols]

row_labels = 'ABCDEFGHI'
col_labels = '123456789'
digits = '123456789'
squares = create_sqr(row_labels, col_labels)

rows = [create_sqr(row_labels, col) for col in col_labels]
columns = [create_sqr(row, col_labels) for row in row_labels]
blocks = [create_sqr(row, col)
          for row in ('ABC', 'DEF', 'GHI')
          for col in ('123', '456', '789')]

# coordinates = ([create_sqr(rows, col) for col in cols] +
#     [create_sqr(row, cols) for row in rows] +
#     [create_sqr(r, c) for r in ('ABC', 'DEF', 'GHI') for c in ('123','456', '789')])

# units = dict((s, [c for c in coordinates if s in coordinates if s in u])
#               for s in squares)

print(columns)

