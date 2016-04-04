import scipy as sp
from matplotlib import pyplot as plt

n = 2000
A = sp.zeros((n, n))
p = 0.7
i, j = 0, 0
for i in range(0, n):
    for j in range(i + 1, n):
        A[i][j] = (sp.rand() < p)
        A[j][i] = A[i][j]
k = sp.sum(A, 1)
s = dict.fromkeys(k, 0)
for i in k:
    s[i] += 1
x = []
y = []
for i in s:
    x.append(i)
    y.append(s[i])
plt.plot(x, y)
plt.show()
