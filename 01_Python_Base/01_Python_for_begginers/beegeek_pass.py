"""
BEEGEEK наконец-то открыл свой банк, в котором используются специальные банкоматы с необычным паролем.

Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа.
Поскольку основатель BEEGEEK фанатеет от математики, то он решил:

число a – должно быть палиндромом;
число b – должно быть простым;
число c – должно быть чётным.

Напишите функцию is_valid_password(password), которая принимает в качестве аргумента
строковое значение пароля password и возвращает значение True, если пароль является
действительным паролем BEEGEEK банка, или False в противном случае.
"""


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def is_valid_password(password):
    is_palin = False
    is_prim = False
    is_even = False
    current_password = [int(el) for el in password.split(":")]
    if len(current_password) != 3:
        return False
    if str(current_password[0]) == str(current_password[0])[::-1]:
        is_palin = True
    if is_prime(current_password[1]):
        is_prim = True
    if current_password[2] % 2 == 0:
        is_even = True
    return is_palin and is_prim and is_even


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
