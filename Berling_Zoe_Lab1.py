"""Zoe Berling Algorithms Lab 1 Matrix Multiply"""


def printMatrix(m):
    if m == False:
        print("Incorrect dimensions: Columns in A not equal to rows in B")
    else:
        for row in m:
            if sum(row) == 0:
                continue
            else:
                print(row)


def matrixMult(A, B):
    a_row = len(A) # number of rows A
    a_col = len(A[0])
    b_col = len(B[0]) # number of columns B
    b_row = len(B) # number of rows in B
    C = [[0 for i in range(3)] for j in range(3)]
    if a_col == b_row:
        for a in range(a_row):
            for b in range(b_col):
                for c in range(b_row):
                    C[a][b] += A[a][c] * B[c][b]
        return C
    else:
        return False


# Testing code
# Test1
A = [[ 2, -3, 3],
[-2, 6, 5],
[ 4, 7, 8]]

B = [[-1, 9, 1],
[ 0, 6, 5],
[ 3, 4, 7]]


C = matrixMult(A, B)
if not C == None:
    printMatrix(C)

# Test2
A = [[ 2, -3, 3, 0],
[-2, 6, 5, 1],
[ 4, 7, 8, 2]]
B = [[-1, 9, 1],
[ 0, 6, 5],
[ 3, 4, 7]]
C = matrixMult(A, B)
if not C == None:
    printMatrix(C)

# Test3
A = [[ 2, -3, 3, 5],
[-2, 6, 5, -2]]
B = [[-1, 9, 1],
[ 0, 6, 5],
[ 3, 4, 7],
[ 1, 2, 3]]
C = matrixMult(A, B)
if not C == None:
    printMatrix(C)
