def make_triangle(n, triangle_p):
    for i in range(2, n + 1): 
        for j in range(1, i):
             triangle_p[i][j] = triangle_p[i-1][j-1] + triangle_p[i-1][j]

n = int(input())
triangle_p = [[1 for _ in range(i + 1)] for i in range(n + 1)]

make_triangle(n, triangle_p)

print(triangle_p[n])
