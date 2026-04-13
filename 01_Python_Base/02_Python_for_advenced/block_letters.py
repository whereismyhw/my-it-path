letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

word = input() + " запретил букву"

for j in letters:
    if j in word:
        print(*word.split(), j)
        word = word.replace(j, "")