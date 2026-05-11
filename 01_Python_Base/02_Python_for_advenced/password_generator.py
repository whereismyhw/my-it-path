import random
import string
def generate_password(length, letter):
    our = letter["EN"] + letter["en"] + letter["dig"]
    
    answer = []
    answer.append(random.choice(letter["EN"]))
    answer.append(random.choice(letter["en"]))
    answer.append(random.choice(letter["dig"]))
    for _ in range(3, length):
        answer.append(random.choice(our))
        
    random.shuffle(answer)
    return "".join(answer)
                      
def generate_passwords(count, length, letter):
    answer = []
    for _ in range(count):
        answer.append(generate_password(length, letter))
                      
    return answer
    
    
n, m = int(input()), int(input())
letter = {'EN': [x for x in string.ascii_uppercase if x not in 'OI'],
          'en': [x for x in string.ascii_lowercase if x not in 'ol'],
          'dig': [x for x in string.digits if x not in '01']}

print(*generate_passwords(n, m, letter), sep='\n')