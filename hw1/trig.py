import numpy as np
import time

filename = 'results.csv'

def findTriangle(M):
	for i in range(0, n):
		for j in range(i+1, n-1):
			if M[i][j] == 1:
				for k in range(j+1, n):
					if (M[i][k] == 1 and M[j][k] == 1):
						return True
	return False

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

def fillBipartite(M):
	n = M.shape[1]
	for i in range(0, n//2):
		for j in range(n//2, n):
			M[i][j] = np.around(np.random.uniform(0, 1))
			M[j][i] = M[i][j]
	return M

f = open(filename, 'w')
f.write("Normal\n")

for i in range(2, 12):
	n = np.power(2, i)
	M = fillNormal(generateMatrix(n))
	start = time.time()
	result = findTriangle(M)
	elapsed = time.time() - start
	line = [str(n), ',', str(elapsed), ',', str(result)]
	f.write(''.join(line))
	f.write('\n')
	print(n)

f.write("Bipartite\n")

for i in range(2, 12):
	n = np.power(2, i)
	M = fillBipartite(generateMatrix(n))
	start = time.time()
	result = findTriangle(M)
	elapsed = time.time() - start
	line = [str(n), ',', str(elapsed), ',', str(result)]
	f.write(''.join(line))
	f.write('\n')
	print(n)

f.close()