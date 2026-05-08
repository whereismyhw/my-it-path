'''
Напишите программу для подсчета количества единиц каждого вида товара
из приобретенных каждым покупателем интернет-магазина.
'''
result = {}
for _ in range(int(input())):
    name, gros, cnt = input().split()
    result.setdefault(name, {})
    result[name][gros] = result[name].get(gros, 0) + int(cnt)
    
name_s = sorted(result)

for name in name_s:
    print(f'{name}:')
    gros_s = sorted(result[name])
    for gros in gros_s:
        print(f'{gros} {result[name][gros]}')
        