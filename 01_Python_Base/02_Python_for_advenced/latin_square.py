def is_latin(matrix, ideal):
    for i in range(n):
        ceil = []
        for j in range(n):
            ceil.append(matrix[j][i])
        ceil.sort()
        if ceil != ideal:
            return "NO"
    for row in matrix:
        row.sort()
        if row != ideal:
            return "NO"
    return "YES"
        

n = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(n)]

ideal = list(range(1, n + 1))
print(is_latin(matrix, ideal))
