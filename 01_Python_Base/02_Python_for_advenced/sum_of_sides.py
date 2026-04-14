n = int(input())
mtrx = [[int(el) for el in input().split()] for _ in range(n)]
up, down, left, right = 0, 0, 0, 0

for i in range(n):
    for j in range(n):
        if i < j and i < n - j - 1:
            up += mtrx[i][j]
        elif i < j and i > n - j - 1:
            rigt += mtrx[i][j]
        elif i > j and i > n - j - 1:
            down += mtrx[i][j]
        else:
            left += mtrx[i][j]
print(f'Верхняя четверть: {up}', end=" ")
print(f'Правая четверть: {right}', end=" ")
print(f'Нижняя четверть: {down}', end=" ")  
print(f'Левая четверть: {left}', end=" ")