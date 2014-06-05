def create_coordinates(rows, columns):
    return [rows + columns for row in rows for column in columns]

rows = 'ABCDEFGHI'
columns = '123456789'
coordinates = create_coordinates(rows, columns)

print(coordinates)
