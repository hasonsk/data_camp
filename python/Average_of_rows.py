import numpy as np
# input number of rows, columns
n, p = ([int(x) for x in input().split()])

# add new elements
matrix = []
for x in range(n):
    matrix.append([float(i) for i in input().split()])
matrix_np = np.array(matrix)

# calculate mean rows
row_means = np.round(np.mean(matrix_np, axis=1), decimals=2)

# print the row means
print(row_means)
