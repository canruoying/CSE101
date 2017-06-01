import numpy as np
import time

filename = 'results.csv'

def findIndependentSet(M,deletedVertices):
    n = M.shape[1]
    for i in range(0, n):
        if not i in deletedVertices:
            d1 = deletedVertices
            d1.append(i)
            N = neighbors(M,i)
            d2 = list(set(d1 + neighbors(M,i)))
            s1 = findIndependentSet(M,d1)
            s2 = 1 + findIndependentSet(M,d2)
            if s1 > s2:
                return s1
            return s2
    return 0

def neighbors(M,v):
    n = M.shape[1]
    N = []
    for i in range(0, n):
        if M[v,i] == 1:
            N.append(i)
    return N

def generateMatrix(n):
    M = np.zeros((n, n))
    for x in range(0, n):
        M[x][x] = 1
    return M

def fillNormal(M):
    n = M.shape[1]
    for i in range(0, n):
        for j in range(i+1, n):
            M[i][j] = np.around(np.random.uniform(0, 1))
            M[j][i] = M[i][j]
    return M

f = open(filename, 'w')
f.write("Normal\n")

for i in range(2, 65):
    M = fillNormal(generateMatrix(i))
    start = time.time()
    runs = 30
    result = 0
    for j in range(0,runs):
        d = []
        result = result + findIndependentSet(M,d)
        print(j)
    result = result / runs
    elapsed = time.time() - start
    line = [str(i), ',', str(result), ',', str(elapsed)]
    f.write(''.join(line))
    f.write('\n')
    print(i,result)