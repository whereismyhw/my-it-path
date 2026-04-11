# объявление функции
def is_password_good(password):
    cnt = 0
    if len(password) > 7:
        cnt += 1
    for el in password:
        if el.isupper():
            cnt += 1
            break
    for el in password:
        if el.islower():
            cnt += 1
            break
    for el in password:
        if el.isdigit():
            cnt += 1
            break
    return(cnt == 4)

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))