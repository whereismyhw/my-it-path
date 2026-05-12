'''
data.txt
name,address,age
George,4312 Abbey Road,22
John,54 Love Ave,21
'''

def read_csv(filename):
    with open(filename, encoding='utf-8') as f:
        keys = [k.strip() for k in f.readline().split(',')]
        
        return [dict(zip(keys, [v.strip() for v in line.split(',')])) for line in f]
    
print(read_csv("data.txt"))