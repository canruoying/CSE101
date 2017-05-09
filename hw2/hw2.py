import numpy as np
import time

filename = 'results.csv'

def findIndependentSet(M):
    n = M.shape[1]
    maxReached = False
    S = []
    d = findNextMinDegree(M,0)
    nodes = findNodesWithDegree(M,d)
    while not maxReached:
        for i in nodes:
            S.append(i)
            notIndependent = False
            for j in S:
                if M[i][j] == 1 and i != j:
                    notIndependent = True
            if notIndependent:
                S.pop()
        d = findNextMinDegree(M,d)
        nodes = findNodesWithDegree(M,d)
        if len(nodes) == 0:
            maxReached = True
    return S

def findNextMinDegree(M,d):
    if d == -1:
        return []
    n = M.shape[1]
    minDegree = -1
    for i in range (0, n):
        s = M[i].sum()
        if (minDegree == -1 or s < minDegree) and s > d:
            minDegree = s
    return minDegree

def findNodesWithDegree(M,d):
    l = []
    for i in range (0, n):
        if M[i].sum() == d:
            l.append(i)
    return l


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

for i in range(2, 12):
    n = np.power(2, i)
    M = fillNormal(generateMatrix(n))
    start = time.time()
    runs = 50
    result = 0
    for j in range(0,runs):
        result = result + len(findIndependentSet(M))
    result = result / runs
    elapsed = time.time() - start
    line = [str(n), ',', str(result), ',', str(elapsed)]
    f.write(''.join(line))
    f.write('\n')
    print(i,n,result)