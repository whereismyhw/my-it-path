'''
Начальный вариант

def concatenate_files(*filenames):
    data = ''
    for filename in filenames:
        with open(filename) as f:
            data += f.read()
    
    with open('output.txt', 'w') as f:
        f.write(data)
'''

def concatenate_files(*files):
    with open('output.txt', 'w', encoding='utf-8') as out:
        for file in files:
            with open(file, 'r', encoding='utf-8') as f:
                for line in f:
                    out.write(line)