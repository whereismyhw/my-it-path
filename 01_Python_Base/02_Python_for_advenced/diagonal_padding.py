n, m = [int(el) for el in input().split()]

mtrx = [[None for _ in range(m)] for _ in range(n)]
nm = 0
for q in range(n + m - 1):
    for i in range(n):
        if 0 <= q - i < m:
            nm += 1
            mtrx[i][q - i] = nm
for row in mtrx:
    print(*row)