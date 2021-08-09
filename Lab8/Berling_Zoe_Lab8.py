"""Berling Zoe Lab 8 Chained Matrix Multiplication DP"""
# dynamic programing to solve chained matrix multiplication problem

def printMatrix(m):
    for row in m:
        print(row)

def chainMatrix(dims):
    # Create the empty 2-D table
    n = len(dims)-1
    m = [[None for i in range(n)] for j in range(n)]  # optimal vlaue matrix
    t = [[None for i in range(n)] for j in range(n)]  # traceback matrix
    # Fill in the base case values
    for i in range(n):
        m[i][i] = 0
    # Fill in the rest of the table diagonal by diagonal
    for chainLength in range(2,n+1):
        for i in range(n+1-chainLength):
            j = i + chainLength - 1
            # Fill in m[i][j] with the best of the recursive options
            m[i][j] = float("inf")
            for k in range(i,j):
            # Two previous table values plus
            # what it cost to mult the resulting matrices
                q = m[i][k]+m[k+1][j]+dims[i]*dims[k+1]*dims[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    t[i][j] = k  # create traceback and add to chainMatrixfunction

    # printMatrix(m)
    printMatrix(t)
    return m[0][n-1], t


# define a new function called parenStr that will return a str repreentation of the matrices with parenthases
def parenStr(t,i,j):
    """run through traceback matrix """
    if i == j:
        print(f'(A{i})', end='')
    else:
        print("(",end="")
        parenStr(t, i, t[i][j])
        parenStr(t, t[i][j]+1, j)
        print(")",end="")


dims = [30,35,15,5,10,20,25]
o, t = chainMatrix(dims) # optimal cost of the matrix, traceback matrix

names = [i for i in range(len(t[0]))]
parenStr(t, 0, len(t[0])-1)

