n = int(input())
mtrx = [[int(el) for el in input().split()] for _ in range(n)]
minimum = mtrx[0][0]
for i in range(n):
    for j in range(n):
        if (i >= j and i <= n - j - 1 or i <= j and i >= (n - j - 1)) and mtrx[i][j] > minimum:
            minimum = mtrx[i][j]
print(minimum)
