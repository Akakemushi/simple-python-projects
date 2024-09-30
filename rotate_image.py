import copy

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'X', 'O', '.', '.', '.'],
        ['X', 'O', 'X', 'O', '.', '.'],
        ['O', 'X', 'O', 'X', 'O', '.'],
        ['.', 'O', 'X', 'O', 'X', 'O'],
        ['O', 'X', 'O', 'X', 'O', '.'],
        ['X', 'O', 'X', 'O', '.', '.'],
        ['.', 'X', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def rotate_image(matrix):
    clone = []
    for col, char in enumerate(matrix[0]):
        new_row = []
        for row in matrix:
            new_row.insert(0, row[col])
        clone.append(new_row)
    return clone

rotaded_image = rotate_image(grid)
for x in rotaded_image:
    for y in x:
        print(y, end="")
    print("")
