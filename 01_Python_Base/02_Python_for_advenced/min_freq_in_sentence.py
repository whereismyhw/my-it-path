sentence = [el for el in input().strip(".?,:! ").split()]
words = {}

for word in sentence:
    words[word] = words.get(word, 0) + 1   

answer = None
min_freq = min(words.values())
answer = None

for word, freq in words.items():
    if freq == min_freq:
        if answer is None or answer > word:
            answer = word
        
print(answer)
