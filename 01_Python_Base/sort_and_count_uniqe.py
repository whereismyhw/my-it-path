"""
Напишите функцию print_symbol_counts(s), которая принимает на вход слово s
и выводит для каждой буквы этого слова в лексикографическом порядке
в нижнем регистре на отдельной строке количество её вхождений в это слово
в следующем формате:

<L>: <N>

где <L> – некоторая буква слова s, <N> – количество вхождений этой буквы в слово s.
"""


def print_symbol_counts(s):
    res = [el for el in s.lower()]
    res.sort()
    unique = []
    for el in res:
        if el not in unique:
            print(f"{el}: {res.count(el)}")
        unique.append(el)


# считываем данные
s = input()

# вызываем функцию
print_symbol_counts(s)
