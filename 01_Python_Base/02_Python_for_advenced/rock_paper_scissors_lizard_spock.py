answers = ['камень', 'ящерица', 'Спок', 'ножницы', 'бумага']

timur = answers.index(input())
ruslan = answers.index(input())

if timur - ruslan == 0:
    print("ничья")
elif (timur - ruslan) % 2 == 0:
    if max(timur, ruslan) == timur:
        print("Тимур")
    else:
        print("Руслан")
else:
    if min(timur, ruslan) == timur:
        print("Тимур")
    else:
        print("Руслан")