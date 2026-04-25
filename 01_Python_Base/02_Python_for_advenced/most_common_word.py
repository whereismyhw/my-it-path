text = input()
result = {}

for word in text.split():
    result[word] = result.get(word, 0) + 1

answer = None
max_v = max(result.values())

for key, value in result.items():
    if value == max_v:
        if answer is None or answer > key :
            answer = key
            
print(answer)
