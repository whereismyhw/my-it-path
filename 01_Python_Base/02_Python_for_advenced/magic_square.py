n = int(input())

mtrx = [[int(el) for el in input().split()] for _ in range(n)]
flag = True
main_d = 0
sub_d = 0
first_row = 0
unique = []
for i in range(n):
    first_row += mtrx[0][i]

for i in range(n):
    current_ceil, current_row = 0, 0
    for j in range(n):
        current_row += mtrx[i][j]
        current_ceil += mtrx[j][i]
        unique.append(mtrx[i][j])
    if current_row != first_row or current_row != current_ceil or current_ceil != first_row:
        flag = False
        break
else:
    for i in range(n):
        main_d += mtrx[i][i]
        sub_d += mtrx[i][n-i-1]

if sorted(unique) != list(range(1, n * n + 1)):
    flag = False
    
if flag and main_d == sub_d == first_row:
    print("YES")
else:
    print("NO")