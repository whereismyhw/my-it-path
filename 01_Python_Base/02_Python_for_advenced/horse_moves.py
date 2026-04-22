n = 8
mtrx = [['.' for _ in range(n)] for _ in range(n)]

ceils_c = "abcdefgh" 
input_data = input()
ceil_c = ceils_c.index(input_data[0])
row_c = n - int(input_data[1]) 

mtrx[row_c][ceil_c] = "N"

moves = [
    (-2, -1), (-2, 1), # Вверх на 2
    (2, -1), (2, 1),   # Вниз на 2
    (-1, -2), (1, -2), # Влево на 2
    (-1, 2), (1, 2)    # Вправо на 2
]

for dr, dc in moves:
    new_r = row_c + dr
    new_c = ceil_c + dc
    
    if 0 <= new_r < n and 0 <= new_c < n:
        mtrx[new_r][new_c] = "*"

for row in mtrx:
    print(*row)