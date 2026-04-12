
n = int(input())
k = int(input())

all_people = [el for el in range(1, n + 1)]
index = 0

while len(all_people) > 1:
    index = (index + k - 1) % len(all_people)
    del all_people[index]
print(*all_people)