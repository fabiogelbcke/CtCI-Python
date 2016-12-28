def zero_matrix(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return matrix
    cols = set()
    lines = set()
    width, height = len(matrix), len(matrix[0])
    for i in range(width):
        for j in range(height):
            if matrix[i][j] == 0:
                cols.add(j)
                lines.add(i)
    for i in range(width):
        for j in range(height):
            if i in lines or j in cols:
                matrix[i][j] = 0
    return matrix

matrix = [[0,1,2,3],[4,5,0,6],[7,8,9,10]]

zero = zero_matrix(matrix)

for i in range(len(zero)):
    print zero[i]
