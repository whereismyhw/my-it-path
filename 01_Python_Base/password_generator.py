import random
def generate_password(length, chars):
    password = ""
    for _ in range(length):
        password += random.choice(chars)
    return password

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"

chars = ""

n = int(input("Сколько паролей сгенерировать? "))
length = int(input("Какой длины должен быть пароль? "))
if input("Включать ли цифры? (да/нет) ").lower() == "да":
    chars += digits
if input("Включать ли строчные буквы? (да/нет) ").lower() == "да":
    chars += lowercase_letters
if input("Включать ли прописные буквы? (да/нет) ").lower() == "да":
    chars += uppercase_letters
if input("Включать ли специальные символы? (да/нет) ").lower() == "да":
    chars += punctuation
if input("Исключать ли неоднозначные символы? (да/нет) ").lower() == "да":
    for c in "il1Lo0O":
        chars = chars.replace(c, "")
print("Сгенерированные пароли:")
for _ in range(n):
    print(generate_password(length, chars))