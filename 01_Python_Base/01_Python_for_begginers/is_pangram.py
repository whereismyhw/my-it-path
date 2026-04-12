# объявление функции
def is_pangram(text):
    for i in range(26):
        if chr(ord("a") + i) not in text.lower():
            return False
    else:
        return True
        

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))