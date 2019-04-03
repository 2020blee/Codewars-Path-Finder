def matrix_addition(a, b):
    final_matrix = []
    for x in range(len(a)):
        row=[]
        for y in range(len(b)):
            row.append(0)
        final_matrix.append(row)
    for i in range(len(a)):
        for j in range(len(a)):
            final_matrix[i][j] = a[i][j] + b[i][j]
    return final_matrix

a = [ [1, 2],[1, 2] ]
b = [ [2, 3],[2, 3] ]

matrix_addition(a,b)
