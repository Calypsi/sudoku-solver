def create_sqr(rows, cols):
    return [row + col for row in rows for col in cols]

rows = 'ABCDEFGHI'
nums = '123456789'
cols = nums
squares = create_sqr(rows, cols)

coordinates = ([create_sqr(rows, col) for col in cols] +
    [create_sqr(row, cols) for row in rows] +
    [create_sqr(r, c) for r in ('ABC', 'DEF', 'GHI') for c in ('123','456', '789')])

units = dict((s, [c for c in coordinates if s in coordinates if s in u])
              for s in squares)

print(units)

