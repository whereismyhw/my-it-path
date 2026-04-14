s = input()
s_list = s.split()

result = [[s_list[0]]] 

for i in range(1, len(s_list)):
    
    current_item = s_list[i]
    last_sublist = result[-1]
    
    if current_item == last_sublist[-1]:
        last_sublist.append(current_item)
    else:
        result.append([current_item])

print(result)