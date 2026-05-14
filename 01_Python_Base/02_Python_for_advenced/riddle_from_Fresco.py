'''
# 1 ВАРИАНТ

from decimal import Decimal, getcontext 

def fresco_goats(text):
    all_g_d = {}
    
    with open(text) as f:
        for line in f:      
            if line.strip() == 'GOATS':
                break     
        for line in f:
            line = line.strip()
            all_g_d[line] = all_g_d.get(line, 0) + 1
            
    getcontext().prec = 12  
    all_g = sum(all_g_d.values())    
    answer = []
    
    for k, v in all_g_d.items():
        if Decimal(v / all_g) > 0.07:
            answer.append(str(k) + '\n')
            
    answer.sort()      
    
    with open('answer.txt', 'w') as out:
        out.writelines(answer)
'''

from decimal import Decimal, getcontext

def fresco_goats(text):
    all_g = {}
    total = 0

    with open(text, encoding='utf-8') as f:
        for line in f:      
            if line.strip() == 'GOATS':
                break     
        
        for line in f:
            line = line.strip()
            if line:
                all_g[line] = all_g.get(line, 0) + 1
                total += 1

    getcontext().prec = 12  
    answer = []
    
    threshold = Decimal('0.07')
    
    for k, v in all_g.items():
        if Decimal(v) / total > threshold:
            answer.append(k)
            
    answer.sort()      
    
    with open('answer.txt', 'w', encoding='utf-8') as out:
        out.write('\n'.join(answer))