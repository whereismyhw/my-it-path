with open(input(), encoding='utf-8') as f, open(input(), encoding='utf-8') as bad:
    bad_words = bad.read().split()

    for line in f:
        for b_word in bad_words:
            while b_word.lower() in line.lower():
                start = line.lower().find(b_word.lower())
                end = start + len(b_word)
                
                line = line[:start] + '*' * len(b_word) + line[end:]
        
        print(line, end='')