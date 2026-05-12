def f_weight(file):
    with open(file, encoding='utf-8') as f:
        content = f.read()
        return len(content) + content.count('\n')
    
answer = []
for _ in range(int(input())):
    name = input()
    answer.append((f_weight(name), name))
    
answer.sort(key=lambda x: x[1])
answer.sort(key=lambda x: x[0], reverse=True)

for b, name in answer:
    print(f'{name} {b}B')




