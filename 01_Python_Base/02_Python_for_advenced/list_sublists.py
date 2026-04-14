'''

Все подсписки строки s

'''

s_list = input().split()

result = [[]]

for i in range(len(s_list)):
    for j in range(len(s_list) - i):
        result.append(s_list[j:i + 1 + j])
print(result)