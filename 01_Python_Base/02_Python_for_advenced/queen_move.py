s = input()
c = ord("a") - ord(s[0])
r = 8 - int(s[1])

table = [["."] * 8 for _ in range(8)]

moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


for dr, dc in moves:

    new_dr = r + dr
    new_dc = c + dc

    while 0 <= new_dr <= 7 and 0 <= new_dc <= 7:
        table[new_dr][new_dc] = "*"
        new_dr += dr
        new_dc += dc
        
table[r][c] = "Q"

for row in table:
    print(*row)
