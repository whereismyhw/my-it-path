n = int(input())

correct_students = set()
correct_attempts = 0

for _ in range(n):
    name, result = input().split(": ") 
    
    if result == "Correct":
        correct_attempts += 1
        correct_students.add(name)

if not correct_students:
    print("Вы можете стать первым, кто решит эту задачу")
else:
    print(f"Верно решили {len(correct_students)} учащихся")
    percent = int((correct_attempts / n) * 100 + 0.5)
    print(f"Из всех попыток {percent}% верных")