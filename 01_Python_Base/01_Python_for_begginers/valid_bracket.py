"""
Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента
непустую строку text, состоящую из символов ( и ) и возвращает значение True,
если поступившая на вход строка является правильной скобочной последовательностью,
или False в противном случае.
"""

# объявление функции
def is_correct_bracket(text):
    cnt = 0
    for el in text:
        if el == "(":
            cnt += 1
        elif el == ")":
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
