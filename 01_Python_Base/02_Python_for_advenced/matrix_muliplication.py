n, m = [int(el) for el in input().split()]
mtrx1 = [[int(el) for el in input().split()] for _ in range(n)]
input()
m, k = [int(el) for el in input().split()]
mtrx2 = [[int(el) for el in input().split()] for _ in range(m)]

result = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for r in range(m):       
            result[i][j] += mtrx1[i][r] * mtrx2[r][j]

for row in result:
    print(*row)