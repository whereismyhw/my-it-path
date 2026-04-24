n = int(input())
students = [[el.strip() for el in input().split(":")] for _ in range(n)]
students_s = set([students[el][0] for el in range(len(students))])
cnt_correct = []

for i in range(n):
    if students[i][1] == "Correct":
        cnt_correct.append(students[i][0])
        
new_correct = set(cnt_correct)
 
if len(new_correct) == 0:
    print("Вы можете стать первым, кто решит эту задачу")
else:
    print(f'Верно решили {len(new_correct)} учащихся')
    print(f'Из всех попыток {int(len(cnt_correct) / n * 100 + 0.5)}% верных')