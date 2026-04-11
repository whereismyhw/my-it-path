import random
def is_valid(guess):
    if guess < 1 or guess > n:
        print("Число должно быть от 1 до", n)
        return False
    return True

n = int(input("Введите верхнюю границу: "))
print("Я загадал число от 1 до", n)
secret = random.randint(1, n)
guess = 0
cnt_tries = 0

while guess != secret:
    guess = int(input("Введите число: "))
    if is_valid(guess):
        cnt_tries += 1  
    if guess < secret:
        print("Моё число больше")
    elif guess > secret:
        print("Моё число меньше")

print("Вы угадали! Количество попыток:", cnt_tries)
