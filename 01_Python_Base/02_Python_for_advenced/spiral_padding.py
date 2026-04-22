n, m = [int(el) for el in input().split()]
mtrx = [[0 for _ in range(m)] for _ in range(n)]

r = 0
c = 0
move_idx = 0

moves = [
    (0, 1), (1, 0),
    (0, -1), (-1, 0)
]

for i in range(1, n * m + 1):
    mtrx[r][c] = i

    if i == n * m:
        break

    dr, dc = moves[move_idx]

    if not (0 <= r + dr < n and 0 <= c + dc < m and mtrx[r + dr][c + dc] == 0):
        move_idx = (move_idx + 1) % 4
        dr, dc = moves[move_idx]

    r += dr
    c += dc

for row in mtrx:
    print(*(str(el).ljust(3) for el in row))