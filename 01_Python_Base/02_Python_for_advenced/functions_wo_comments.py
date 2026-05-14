with open(input(), encoding='utf-8') as f:
    w_com = []
    com = []
    for line in f:
        if '#' in line:
            w_com.append(f.readline())
    f.seek(0)
    for line in f:
        if 'def ' in line:
            com.append(line[4:line.find('(')])
            
    w_com1 = [name[4:name.find('(')] for name in w_com if 'def ' in name]

if w_com1 == com:
    print('Best Programming Team')
else:
    for d in com:
        if d not in w_com1:
            print(d)