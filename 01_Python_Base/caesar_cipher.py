way = input("Шифровать или дешифровать? (шифровать/дешифровать) ").lower()
language = input("Выберите язык (русский/английский) ").lower()
shift = int(input("Введите сдвиг: "))

if language == "русский":
    alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
elif language == "английский":
    alphabet = "abcdefghijklmnopqrstuvwxyz"
else:
    print("Неправильный выбор языка.")
    exit()

result = ""
text = input("Введите текст: ")

for char in text:
    if char.lower() in alphabet:
        index = alphabet.index(char.lower())
        if way == "шифровать":
            new_index = (index + shift) % len(alphabet)
        elif way == "дешифровать":
            new_index = (index - shift) % len(alphabet)
        else:
            print("Неправильный выбор действия.")
            break
        new_char = alphabet[new_index]
        if char.isupper():
            new_char = new_char.upper()
        result += new_char
    else:
        result += char

print("Результат:", result)