#Оптимальное расставление скобок при перемножении матриц

import numpy as np


def matrixChain(p, n=1, memo=None, seq=None):
    size = len(p) - n
    if n == 1:
        memo = np.zeros([size, size], dtype=int)
        seq = np.zeros([size, size], dtype=int)
    else:
        for i in range(size):
            j = i + n - 1
            for k in range(i, j):
                t = memo[i, k] + memo[k + 1, j] + p[i] * p[k + 1] * p[j + 1]
                if t < memo[i, j] or memo[i, j] == 0:
                    memo[i, j] = t
                    seq[i, j] = k
    if n < len(p) - 1:
        matrixChain(p, n + 1, memo, seq)
    return memo, seq


def prtSeq(seq, i, j):
    size = j - i + 1
    if size == 1:
        return 'A%d' % i
    else:
        k = seq[i, j]
    res = ''
    res += '(' + prtSeq(seq, i, k)
    res += prtSeq(seq, k + 1, j) + ')'
    return res


n = 12
p = [9, 5, 2, 8, 5, 6, 9, 8, 3, 4, 7, 9, 2]
m, seq = matrixChain(p)
res = prtSeq(seq, 0, n - 1)
print('Наилучший порядок умножения:% s, трудоёмкость:% d' % (res[1: -1], m[0, -1]))
