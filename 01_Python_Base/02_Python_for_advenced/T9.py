sentence = input().upper()

numbers = {
    "1": (".", ",", "?", "!", ":"),
    "2": ("A", "B", "C"),
    "3": ("D", "E", "F"),
    "4": ("G", "H", "I"),
    "5": ("J", "K", "L"),
    "6": ("M", "N", "O"),
    "7": ("P", "Q", "R", "S"),
    "8": ("T", "U", "V"),
    "9": ("W", "X", "Y", "Z"),
    "0": (" ",)
}

for letter in sentence:
    for key, value in numbers.items():
        if letter in value:
            print(key * (value.index(letter) + 1), end="")
            break