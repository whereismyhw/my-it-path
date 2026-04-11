def shift_word(text):
    shift = 0
    for char in text:
        if char.isalpha():
            shift += 1
    return shift            

            
text = input()
result = ""
text_list = [el for el in text.split()]
for word in text_list:
    shift = shift_word(word)
    for char in word:
        if char.isalpha():
            new_char = chr((ord(char) + shift))
            if new_char.lower() not in "abcdefghijklmnopqrstuvwxyz":
                new_char = chr((ord(new_char) - 26))
            result += new_char
        else:
            result += char
    result += " "
print(result.strip())