park = {}

for _ in range(int(input())):
    line = input().split()
    idd = line[0].strip(":")
    time1, time2 = line[1].strip().split(":")
    time = int(time1) * 60 + int(time2)
    park[idd] = time

out = {}

for _ in range(int(input())):
    line = input().split()
    idd = line[0].strip(":")
    time1, time2 = line[1].strip().split(":")
    time = int(time1) * 60 + int(time2)
    out[idd] = time

answer = {}

for idd in out:
    if out[idd] - park[idd] < 0:
        out[idd] = out[idd] + 24 * 60
        answer[idd] = out[idd] - park[idd]
    else:
        answer[idd] = out[idd] - park[idd]
    
    if answer[idd] <= 120:
        answer[idd] = "плата не взимается"
    else:
        answer[idd] = str((answer[idd] - 120) * 3) + "₽"
    print(f'{idd}: {answer[idd]}') 

