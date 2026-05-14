def times(hm):
    h, m = map(int, hm.split(":"))
    return int(h) * 60 + int(m)

def write_long_session_users(file):
    with open('output.txt', 'w', encoding='utf-8') as out, open(file, encoding='utf-8') as f:
        for line in f:
            name, log, olog = line.split(', ')
            time = times(olog) - times(log)
            if time < 0:
                time += 60 * 24
            if time >= 60:
                print(name, file=out)
            