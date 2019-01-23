
#!/bin/python3
import re

def matrix_Script(matrix):
    matrix = [list(i) for i in matrix]
    col_wise = []
    for ind in range(len(matrix[0])):
        col_wise.append([row[ind] for row in matrix])
    final_string = ''
    for ind in range(len(matrix[0])):
        final_string = final_string + ''.join(col_wise[ind])
    final_string = re.sub(r"(?<=\w)([^\w]+)(?=\w)"," ",final_string)
    return (final_string)

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    matrix = []

    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)
    print (matrix_Script(matrix))