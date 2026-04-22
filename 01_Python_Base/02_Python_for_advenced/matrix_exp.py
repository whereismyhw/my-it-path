n = int(input())
mtrx = [[int(el) for el in input().split()] for _ in range(n)]
m = int(input())

new_mtrx = mtrx.copy()

for _ in range(m - 1):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += mtrx[i][k] * new_mtrx[k][j]
    new_mtrx = result.copy()        
    
for row in result:
    print(*row)