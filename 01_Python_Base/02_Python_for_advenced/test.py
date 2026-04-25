n = int(input())
translate = {
    line.split(": ")[0].lower(): line.split(": ")[1] 
    for _ in range(n) 
    for line in [input()]
}
for _ in range(int(input())):
    word = input().lower
    if word not in translate:
        print("Не найдено")
    else:
        print(translate[word])